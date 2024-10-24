+++
title = 'Network Simulation'
date = 2024-05-17T15:25:56+08:00
draft = false
type = 'research'
layout = 'research'
label = "Simulation"

intro = """Network simulation aims to help operators try out new designs on their network withoutreally touching the network. It achieves this by creating a twin of the network with some level of abstraction. Depending on the abstraction level, it can either be pure simulation using customized codes to mimic the behaviors of real networks, or emulation, which uses the images or libraries of real devices."""

detailedIntro = [
  "Networks like WANs and DCNs carry production traffic, and it is risky to make a change to real networks. It is hard to evaluate and optimized the performance of traing task, due to the high cost of building a large DCNs with 10K GPUs. A preferrable way is to create a twin of the network with some level of abstraction, and try out new ideas on top of it to anticipate the effects on real networks. That is what network simulation is going to do. It can either pure simulation, which use customized codes to mimic the behaviors of real networks, or emulation, which uses vendor images or libraries which have exactly the same behaviors with real devices. We study both simulation and emulation for large-scale networks with distributed and parallel computing techniques."
]

img = "/research/Simulation.png"
imgDark = "/research/Simulation_dark.png"
+++
