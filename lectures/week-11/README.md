# Coding Architecture II: FS26
## Week 10 – Structural Analysis

![Course Banner](../../_static/caii-banner_fs26.jpg)

> Visualize our designs in using extended reality (XR) technologies to explore immersive .

## Table of Contents

- [Extended Reality](#extended-reality)
- [Why XR for Architecture?](#why-xr-for-architecture)
- [What is WebXR?](#what-is-webxr)
- [Why do we need a local server?](#why-do-we-need-a-local-server)
- [What is a GLB file?](#what-is-a-glb-file)
- [Workflow Overview](#workflow-overview)
- [Slides](#slides)

## Extended Reality

**XR (Extended Reality)** is an umbrella term for technologies that blend the physical and digital worlds.

It includes:

- **VR (Virtual Reality)**
  Fully immersive environments. You are inside a completely virtual world.

- **AR (Augmented Reality)**
  Digital objects are placed in your real environment.

- **MR (Mixed Reality)**
  Digital and physical elements interact more deeply (e.g. occlusion, physics).

In this course, we focus on **AR** to place our architectural models in real space at real scale.

### Why XR for Architecture?

XR allows us to:

- View models at **1:1 scale**
- Understand **spatial qualities** better than on screen
- Share projects in a very **friction-less way**
- Move from abstract geometry to an **immersive experience**

### What is WebXR?

**WebXR** is a web standard that allows XR directly in the browser:

- No app required
- Works from a **URL**
- Uses your device’s **camera and sensors**
- Runs on modern mobile browsers

### Why do we need a local server?

Browsers have security restrictions:

- You cannot reliably load 3D assets (like `.glb`) from `file://`
- XR features often require a **secure or local server context**

So we:

- Run a simple Python server
- Access the page via `http://<local-ip>:8000`
- Open it on our phone

### What is a GLB file?

**GLB (binary glTF)** is a compact 3D file format:

- Contains **geometry, materials, textures**
- Optimized for **real-time rendering**
- Ideal for web and XR

👉 It’s the format we export from Rhino and load in the browser.

### Workflow Overview

1. **Model in Rhino / Grasshopper**
2. **Bake geometry**
3. **Export as `.glb`**
4. **Serve files with Python**
5. **Open on your phone**
6. **View in 3D → switch to AR**

##  Slides

[![Slides](../../_static/slides.png)](https://docs.google.com/presentation/d/19bnSOJctAEXt9uK4EZOB70AEP3rbCfIzLmJ3dNJb_xU)

<div style="display: flex; justify-content: center; align-items: center; height: 1vh;">
    <p style="font-size: 75%;">
        ↑ click to open ↑
    </p>
</div>


