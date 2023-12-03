# Spatial Fiber Printing - [project page](https://guoxinfang.github.io/SpatialFiberPrinting)

## Abstract
This is the data set for technical paper "Exceptional Mechanical Performance by Spatial Printing with Continuous Fiber" by Guoxin Fang, Tianyu Zhang, Yuming Huang, Zhizhou Zhang, Kunal Masania, Charlie C.L. Wang.

We explore a spatial printing method to fabricate continuous fiber-reinforced thermoplastic composites (CFRTPCs), which can achieve exceptional mechanical performance. We propose a computational approach to generate 3D toolpaths that satisfy two major reinforcement objectives: 1) following the maximal stress directions in critical regions and 2) connecting multiple load-bearing regions by continuous fibers.

## Usage of the dataset

Each folder (with model name) contains waypoint sets (fiber toolpath) and mesh sets (matrix material layer). The format of the toolpath waypoint is [x, y, z, nx, ny, nz] + [user defined parameters].

You could visualize the toolpath and curved layer using MeshLab software.

The hardware implementation and communication between robots can be found at [link](https://github.com/yuminghuang1995/Hardware_support_for_Curved_RoboFDM).
