# Assignment 03 - Final Design Project

> **Goal:** Design a unique reciprocal frame (RF) timber structure for the **Quartiergarten Hard** in Zurich by synthesizing the computational workflows developed throughout the semester (`RFSystem`, `BrepMesher`, `MeshRelaxer`).

## Project Overview

For your final project, you will deploy your Python-based computational tools to author a reciprocal frame timber pavilion. The design must be materialized as a comprehensive, fabricable timber model complete with beams and joints. 

This project is an open-ended opportunity to combine all the skills acquired in previous assignments into a single, cohesive architectural proposal. We encourage you to explore expressive forms and spatial configurations, provided they respect the structural logic of reciprocal frames and the site constraints.

### Site & Constraints
* **Location:** Quartiergarten Hard, Zurich.
* **Max Surface Area:** 40 m² (projected footprint).
* **Max Height:** 3.0 m.
* **Foundations:** The structure must integrate with **screw foundations**.

*(A base Grasshopper file with context, [A03_design-project.ghx](A03_design-project.ghx), is provided).*

---

## Evaluation Criteria

Projects will be evaluated out of **6.0 points** total. 
> **NOTE: You must achieve a minimum grade of 4.0 on this final design project to pass the course.**

* **Coding Process (2.5 pts):** The process by which you produce the design.
    * Main Task Integration (0.5 pt)
    * Extra Challenges (up to 2.0 pts)
* **Project Quality (2.5 pts):** The resulting design.
    * Concept & Design Intent (1.0 pt)
    * Spatial Organization (0.5 pt)
    * Construction / Assembly / Materialization Logic (0.5 pt)
    * Formal & Atmospheric Quality (0.5 pt)
* **Presentation (1.0 pt):** How well you present the work.
    * Argumentation & Clarity (0.5 pt)
    * Quality of Poster & Visual Media (0.5 pt)

---

## Tasks

### 1. Main Task: Core Design & Integration (0.5 pt)
The primary requirement is to integrate the code you wrote in previous assignments into the A03 template to produce a cohesive, functional design. You will need to bring together your mesher (A01), your relaxer and modifiers (A02), and any joint generation rules you have developed. 

* **Originality:** Your base geometry must be uniquely authored for this assignment. Submitting a design based on the provided sample BREPs is considered an invalid submission.
* **Focus:** You do not need to write extensive new core algorithms. Instead, focus on how these existing components interact to generate a beautiful, fabricable architectural proposition.

### 2. Extra Challenges (up to 2.0 pts)
To achieve a higher grade, you may complete any combination of the following advanced challenges. **For any challenge you choose, you must document the process and include evidence of it in your final presentation poster.**

* **3D Printing your model (0.5 pt):** Produce a scaled, physical model of your design. The A03 template largely sets up this pipeline. You will be responsible for preparing the geometry, running the print, and assembling the parts.
* **Static Analysis (0.5 pt):** Use **Karamba3D** to validate the stability of your design under self-weight. A basic Karamba3D setup is included in the template (lab licenses are available). 
* **Simulated milling toolpath (0.25 pt):** Generate and visualize the robotic milling toolpaths for your structure’s joints to prove fabricability.
* **XR Visualization (0.25 pt):** Bake and texture your model, export it to the `.glb` format, and set up an immersive AR/VR viewing experience. You can use a hosted viewer (e.g., [modelviewer.dev](https://modelviewer.dev/editor)) or run the provided local python web server and HTML viewer (`a03_extra_webxr.py` and `a03_extra_webxr.html`). *(Note: On iPhone, Safari is required for AR mode).*
* **Assembly Sequence Planning (0.25 pt):** Leverage graph traversal algorithms to determine and animate a logical, step-by-step manual assembly sequence for your beams. *(Video tutorial provided in upcoming weeks).*
* **Graph Traversal & Load Paths (0.25 pt):** Use graph algorithms to visualize the shortest path for force transmission or to simulate load distribution through the network of timber members. *(Video tutorial provided in upcoming weeks).*

## Presentation

### Project Poster (PDF)

You must prepare a single-page, landscape poster that communicates your design effectively. It should include:
- A brief description of your concept and design intent.
- Technical diagrams explaining the underlying mesh generation and reciprocal frame logic.
- High-quality renders, screenshots, or photos of the final timber model.
- Key snippets of interesting code.
- Documentation/proof of any extra challenges you completed.

There is an available template for the poster, [a03_layout_template.zip](./poster/a03_layout_template.zip), but you are free to design your own layout if you prefer.

---

## Deliverables

Submit the following files:

- Grasshopper File: `mustermann_max_A-03.ghx`
- Rhino File (with site model): `mustermann_max_A-03.3dm`
- Python files: All relevant `.py` files used in the project, including any new scripts for extra challenges.
- HTML files: Any HTML files used for XR visualization if applicable.
- Poster: `mustermann_max_A-03.pdf`
- Screenshots (`.png`)
  - File Name: `mustermann_max_A-03_xx.png`
  - Dimensions: `3200 x 2400 px`
  - View: `Parallel`, `Shaded`

If you complete the 3D printing, include photos of the physical model in your poster and submit them as part of your screenshots as well as showcasing the physical model in your presentation.

## Submission

Upload the assignment via POLY.GRADE