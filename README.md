# Spatial Fiber Printing - [project page](https://guoxinfang.github.io/SpatialFiberPrinting)

## Abstract
This work explores a spatial printing method to fabricate continuous fiber-reinforced thermoplastic composites (CFRTPCs), which can achieve exceptional mechanical performance. For models giving complex 3D stress distribution under loads, typical planar-layer-based fiber placement usually fails to provide sufficient reinforcement due to their orientations being constrained to planes. The effectiveness of fiber reinforcement could be maximized by using multi-axis additive manufacturing (MAAM) to better control the orientation of continuous fibers in 3D-printed composites.

## Usage of the dataset

Each folder (with model name) contains waypoint sets (fiber toolpath) and mesh sets (matrix material layer). The format of the toolpath waypoint is [x, y, z, nx, ny, nz] + [user defined parameters].

You could visualize the toolpath and curved layer using MeshLab software.

The hardware implementation and communication between robots can be found at [link](https://github.com/yuminghuang1995/Hardware_support_for_Curved_RoboFDM).
