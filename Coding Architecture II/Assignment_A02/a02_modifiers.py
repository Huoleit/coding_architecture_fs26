# ========================================================================
# CHALLENGE 02: Custom Modifiers
# To complete this challenge:
# 1. Define a new class for each mesh modifier you want to create.
# 2. Ensure each class implements an `apply(self, relaxer, mesh)` method.
#    The mesh relaxer will call this method to apply your custom logic.
# 3. Use this week's provided examples as inspiration for your code.
# 4. Use your new modifiers adding them to the Grasshopper canvas,
#    into the `Modifiers` section.
# Example:
#
# class SomeCustomModifier:
#     def __init__(self, whatever_param):
#         pass
#
#     def apply(self, relaxer, mesh):
#         # Do something with the mesh
#         # ...
#         # return the modified mesh
#         return mesh
# ========================================================================

from compas.geometry import Point
from compas.geometry import Vector


class AttractorPointModifier:
    def __init__(self, point: Point, force: float):
        self.point = point
        self.attraction_force = force
        self.type = "force_modifier"

    def apply(self, relaxer, mesh):
        for vertex in mesh.vertices():
            neighbors = mesh.vertex_neighbors(vertex)

            if len(neighbors) <= 2:
                continue

            vertex_point = mesh.vertex_point(vertex)
            direction = Vector.from_start_end(vertex_point, self.point)
            attraction_force = direction * (1 / direction.length) * self.attraction_force
            force = mesh.vertex_attribute(vertex, "force")
            force += attraction_force
            mesh.vertex_attribute(vertex, "force", force)

