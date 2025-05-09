+++

title = 'Nüwa: Efficient Generative Control Plane for AI Network Simulation'
date = 2025-08-01
type = 'paper'
layout = 'paper'
draft = false

research_label = ["Simulation"]
bibtex = """
"""
abstract = [ "Network simulation plays a critical role in improving AI supercomputer efficiency for new design validation, parameter tuning, and network protocol development. However, high fidelity network simulation is very slow at scale. We observe that the significantly inefficient network control plane initialization is the key reasons of slow simulation speed. Existing network simulation searching for the available routing at simulation initialization which takes hours or even days. Moreover, the large routing table involves redundant information which occupy high memory volume and makes routing look-up very slow. In this paper, we present Nüwa, an efficient generative control plane for AI network simulation. Nüwa leverages the layered network architecture of AI network to generate routing tables of each layer directly from the topology description. Thus, the simulator only needs to store several items for whole network routing. Evaluations show that Nüwa can reduce the routing table generation from hours to only 1 second for 64K nodes. For data plane execution, Nüwa can reduce the overall simulation time over 100x by almost eliminating the forwarding calculation." ]
doi = ""
publisher = "Proceedings of APNet'25"
top = true

[[paper.author]]
name = 'Wenkai Li'
id = 'wkli'

[[paper.author]]
name = 'Ran Shu'

[[paper.author]] 
name = 'Peng Zhang'
id = 'pzhang'

[[paper.author]]
name = 'Yongqiang Xiong'

+++
