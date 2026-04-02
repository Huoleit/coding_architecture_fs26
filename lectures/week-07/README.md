# Coding Architecture II: FS26
## Week 07 – Design to Fabrication

![Course Banner](../../_static/caii-banner_fs26.jpg)

> Geometry is not the final output, it's the starting point of a pipeline that ends at the machine.

`design` → `semantic model` → `fabrication data` → `machine`

## Table of Contents

- [Introduction](#introduction)
- [Assignment A03](#assignment-a03)
- [From Geometry to Semantic Models](#from-geometry-to-semantic-models)
- [Model Structure](#model-structure)
- [BTLx & Fabrication Data](#btlx--fabrication-data)
- [CNC Workflow](#cnc-workflow)
- [Robotic Fabrication](#robotic-fabrication)
- [Site Visit](#site-visit)
- [Slides](#slides)

## Introduction

We're moving from shape to system, from generating geometry to making it fabricable. The goal is a continuous pipeline where design intent survives all the way to the machine without loss of meaning.

> **Key takeaway:** geometry is now an intermediate representation, it's the output of a parametric semantic model.

## Assignment A03

The final project brings together everything from the course. You'll design a fabricable timber structure with real beams, real joints, and real fabrication logic, not just geometry that looks structural.

**Integrates:**
- Reciprocal frame systems
- Brep-based design intent + modifier-based relaxation
- Timber modeling (`compas_timber`)

> Link to full description: [Assignment 03: Design Project](../../assignments/A03-design-project/README.md)


## From Geometry to Semantic Models

Geometry describes *where* things are. Semantics describe *what* they are and *how* they behave. A line can represent almost anything. A beam with cross-section, grain direction, and a joint history is unambiguous.

In a semantic model, elements carry meaning beyond shape. A beam is not a curve with a profile swept along it, it's an object with dimensions, an orientation frame, material properties, and connections to other objects. Joints are logical relationships, not coincidental intersections of geometry.

This shift is what allows fabrication data to be derived automatically rather than drawn by hand.

## Model Structure

A well-structured timber model separates concerns cleanly. Think of it as three stacked layers, each answering a different question:

| Layer | What it contains | Question it answers |
|---|---|---|
| **Parts** | Individual timber beams - geometry, cross-section, material | What are the physical elements? |
| **Connections** | Topological relationships between parts | How do they meet, and with what structural intent? |
| **Processings** | Fabrication operations: cuts, holes, slots | What needs to happen to fabricate each joint? |

Design intent lives in *Parts* and *Connections*. Fabrication specifics live in *Processings*. Changing a joint type doesn't require redrawing geometry, it should just update the rule set.

## BTLx & Fabrication Data

**BTLx** is the bridge between our digital model and the CNC machine. It's an XML-based industry standard for timber machining, not a 3D file format, but a *process description*.

A BTLx file describes each element's geometry alongside the processings to be applied: lap joints, drillings, tenons, notches. Some CNC machines reads this directly, others require conversion to an intermediate format.

## CNC Workflow

The full pipeline from design to cut follows a structured sequence. Each step transforms the data while preserving the original design intent.

1. **Semantic timber model**: beams and joints created in `compas_timber`
2. **Joint processings**: joints resolved into specific fabrication operations on each part
3. **BTLx export**: model serialized to machine-readable XML format
4. **Machine-code conversion**: BTLx interpreted into machine-specific toolpaths
5. **CNC fabrication**: physical components cut on a joinery machine; digital logic becomes timber

## Robotic Fabrication

CNC machines operate in fixed configurations, the workpiece comes to the tool. Industrial robots invert this: the tool comes to the workpiece, in any configuration space allows.

In a robotic workflow, our geometry defines target frames and orientations in space. Inverse kinematics then compute the joint rotations required to reach each frame, translating design toolpaths into precise robot trajectories.

This opens up tasks that linear machining can't handle: complex assembly sequences, curved toolpaths, multi-face processing, and working in-situ. The trade-off is added complexity in programming and collision checking.

## Site Visit

Before finalizing our session, we go to the Quartiergarten site.

**Location:** Quartiergarten

- Observe the context, what surrounds the site, what it's embedded in
- Understand real scale and spatial constraints firsthand
- Relate your design logic to actual conditions on the ground

Bring your ideas and sketchpads. What looks right on screen often needs adjustment when you're standing in the space.

##  Slides

[![Slides](../../_static/slides.png)](https://docs.google.com/presentation/d/1c19PQM1UrqFrzq21Y9ziEUBlbrv0kQHVqbxQzTLppUY/)

<div style="display: flex; justify-content: center; align-items: center; height: 1vh;">
    <p style="font-size: 75%;">
        ↑ click to open ↑
    </p>
</div>
