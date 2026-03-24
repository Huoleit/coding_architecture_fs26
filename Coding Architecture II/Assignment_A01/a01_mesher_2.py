import Rhino.Geometry as rg  # type: ignore
from compas.datastructures import Mesh
from compas.geometry import NurbsSurface
from compas.geometry import Point
from compas.geometry import Polyline
from compas.itertools import linspace
from compas_rhino.conversions import polyline_to_compas


class BaseMesher:
    """Small shared base class for Brep-based meshers."""

    def __init__(self, u_count: int, v_count: int, brep: rg.Brep, closed: bool):
        self.u_count = u_count
        self.v_count = v_count
        self.brep = brep
        self.closed = closed    
        self.mesh = Mesh()

    @property
    def face(self) -> rg.BrepFace:
        return self.brep.Faces[0]

    @property
    def surface(self) -> NurbsSurface:
        return NurbsSurface.from_native(self.face.UnderlyingSurface())

    def is_vertex_on_face(self, vertex_key) -> bool:
        # CHALLENGE 01:
        # Get the point of the vertex and check if it's on the face using Rhino's `IsPointOnFace` method.
        # Remember to convert between COMPAS and Rhino geometry when needed.
        point = self.mesh.vertex_point(vertex_key)
        rhino_point = rg.Point3d(point.x, point.y, point.z)
        result, u, v = self.face.ClosestPoint(rhino_point)
        if not result:
            return False
        relation = self.face.IsPointOnFace(u,v)
        return relation != rg.PointFaceRelation.Exterior

    def _vertex_key(self, u_index: int, v_index: int) -> int:
        return next(self.mesh.vertices_where({"u": u_index, "v": v_index}))

    def _filtered_face_vertices(self, vertex_keys: list[int]) -> list[int]:
        # CHALLENGE 02:
        # A useful helper method would be to filter a list of vertex keys, keeping only those that are on the face.
        return [key for key in vertex_keys if self.is_vertex_on_face(key)]
    
    def generate_vertices(self) -> None:
        """Sample the surface on a regular UV grid and store mesh vertices."""
        # Create evenly spaced sample values in the U domain of the surface
        # Use `self.u_count + 1` values so you get the grid vertices (not just cells)
        u_domain = self.surface.domain_u
        u_values = list(linspace(u_domain[0], u_domain[1], self.u_count + 1))

        # Create evenly spaced sample values in the V domain of the surface
        # Use `self.v_count + 1` values for the same reason
        v_domain = self.surface.domain_v
        v_values = list(linspace(v_domain[0], v_domain[1], self.v_count + 1))

        # Loop over all U samples (keep both the index `ui` and the parameter value `u`)
        for ui, u in enumerate(u_values):
            # Loop over all V samples (keep both `vi` and `v`)
            for vi, v in enumerate(v_values):
                # Evaluate the surface at (u, v) to get a 3D point
                point = self.surface.point_at(u, v)
                # Add a mesh vertex at that point
                # Also store the grid indices as attributes: `u=ui`, `v=vi`
                self.mesh.add_vertex(x=point.x, y=point.y, z=point.z, u=ui, v=vi)

        # Explicitly return None (optional, but kept for clarity)
        return None
    
    def get_edges(self) -> list:
        """Return edges based on the closed toggle.
        
        closed=True  → all edges (boundary + interior)
        closed=False → interior edges only (boundary edges hidden)
        """
        if self.closed:
            return list(self.mesh.edges())
        else:
            return [edge for edge in self.mesh.edges() if not self.mesh.is_edge_on_boundary(edge)]

class QuadMesher(BaseMesher):
    """Generate a quad mesh from a single-face Brep.

    Parameters
    ----------
    u_count : int
        Number of cells in the U direction.
    v_count : int
        Number of cells in the V direction.
    brep : rg.Brep
        Input Brep. Only the first face is used.
    full_quads : bool, optional
        If ``True``, keep only complete quads.
        If ``False``, allow clipped boundary polygons.

    Attributes
    ----------
    mesh : compas.datastructures.Mesh
        Output mesh.
    """

    def __init__(self, u_count: int, v_count: int, brep: rg.Brep, full_quads: bool = False, closed: bool = True):
        super().__init__(u_count, v_count, brep, closed)
        self.full_quads = full_quads

    def generate_mesh(self) -> Mesh:
        # First, generate the grid vertices on the surface
        self.generate_vertices()

        # Loop over each grid cell in U (there are `self.u_count` cells)
        for ui in range(self.u_count):
            # Loop over each grid cell in V (there are `self.v_count` cells)
            for vi in range(self.v_count):

                # Get the four corner vertex keys of the current cell
                # Follow a consistent order around the face (v1, v2, v3, v4)
                v1 = self._vertex_key(ui, vi)
                v2 = self._vertex_key(ui + 1, vi)
                v3 = self._vertex_key(ui + 1, vi + 1)
                v4 = self._vertex_key(ui, vi + 1)
                

                # Filter out corners that are not actually on the Brep face
                # (important near trimmed boundaries)
                vertex_keys = self._filtered_face_vertices([v1, v2, v3, v4])

                # If fewer than 3 vertices remain, we cannot make a face
                # Skip this cell
                if len(vertex_keys) < 3:
                    continue

                # If `self.full_quads` is True, only keep complete 4-sided faces
                # Skip clipped boundary polygons
                if self.full_quads and len(vertex_keys) != 4:
                    continue

                # Add the face to the mesh
                self.mesh.add_face(vertex_keys)

        # Clean up any vertices that were generated but never used by a face
        self.mesh.cull_vertices()

        # Return the completed mesh
        return self.mesh

class TriMesher(BaseMesher):
    """Generate a triangle mesh by splitting each quad cell along the diagonal."""
    def __init__(self, u_count: int, v_count: int, brep: rg.Brep, closed: bool = True):
        super().__init__(u_count, v_count, brep, closed)
    def generate_mesh(self) -> Mesh:
        self.generate_vertices()

        for ui in range(self.u_count):
            for vi in range(self.v_count):
                v1 = self._vertex_key(ui,     vi)
                v2 = self._vertex_key(ui + 1, vi)
                v3 = self._vertex_key(ui + 1, vi + 1)
                v4 = self._vertex_key(ui,     vi + 1)

                # Each triangle filtered independently so trimmed edges
                # still contribute one triangle instead of losing the whole cell
                for tri in ([v1, v2, v3], [v1, v3, v4]):
                    filtered = self._filtered_face_vertices(tri)
                    if len(filtered) == 3:
                        self.mesh.add_face(filtered)

        self.mesh.cull_vertices()
        return self.mesh
    
class HexaMesher(BaseMesher):
    """Generate a hex-dominant mesh via the dual of a triangle mesh.

    How it works:
      1. Build an internal TriMesh at 2x resolution.
      2. Place one new vertex at the centroid of every triangle face.
      3. For each vertex of the tri-mesh, collect the centroids of its
         neighbouring faces in cyclic order and connect them into a polygon.
         - Interior vertices (valency 6) → hexagons
         - Boundary vertices             → pentagons / quads (trimmed, expected)
    The 2x resolution makes the hex cells roughly the same size as quads
    at the user-requested resolution.
    """
    def __init__(self, u_count: int, v_count: int, brep: rg.Brep, closed: bool = True):
        super().__init__(u_count, v_count, brep, closed)
        
    def generate_mesh(self) -> Mesh:
        # Step 1: build internal tri-mesh at double resolution
        tri_mesher = TriMesher(self.u_count * 2, self.v_count * 2, self.brep, self.closed)
        tri_mesh = tri_mesher.generate_mesh()

        # Step 2: one centroid vertex per triangle → added to self.mesh
        face_to_centroid = {}
        for fk in tri_mesh.faces():
            coords = [tri_mesh.vertex_coordinates(v) for v in tri_mesh.face_vertices(fk)]
            cx = sum(c[0] for c in coords) / len(coords)
            cy = sum(c[1] for c in coords) / len(coords)
            cz = sum(c[2] for c in coords) / len(coords)
            face_to_centroid[fk] = self.mesh.add_vertex(x=cx, y=cy, z=cz)

        # Step 3: for each tri-mesh vertex, the ring of adjacent face centroids
        # forms one polygon in the hex mesh
        for vk in tri_mesh.vertices():
            adj_faces = tri_mesh.vertex_faces(vk, ordered=True)
            # Drop any None entries that appear on boundary vertices
            adj_faces = [fk for fk in adj_faces if fk is not None and fk in face_to_centroid]
            if len(adj_faces) < 3:
                continue
            polygon = [face_to_centroid[fk] for fk in adj_faces]
            self.mesh.add_face(polygon)

        self.mesh.cull_vertices()
        return self.mesh


