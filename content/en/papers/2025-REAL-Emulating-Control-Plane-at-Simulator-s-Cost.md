+++
title = 'REAL: Emulating Control Plane at Simulator’s Cost'
date = 2025-12-21
type = 'paper'
layout = 'paper'
draft = false

research_label = ["Simulation"]
bibtex = """
"""
abstract = [
 "Validating control plane behavior and ensuring policy compliance in modern, large-scale networks is a critical challenge. Simulation-based approaches offer low computational and memory costs, but their level of abstraction fails to capture vendor-specific device behaviors, limiting their accuracy for real-world validation. In contrast, control plane emulation provides high fidelity by using unmodified router containers that preserve these vendor-specific details, but its excessive computational and memory requirements make it impractical for large networks. In this paper, we present REAL, a lightweight runtime that emulates control planes using unmodified router containers but at the cost of simulation-based approaches. REAL achieves this by simulating a lightweight data plane to accelerate boot-up, employing a two-phase scheduling policy to minimize cache inefficiencies during convergence, and enabling iterative convergence to reduce peak memory usage by partitioning the network. Our evaluation shows that REAL emulates a 1,000-node network 4× faster than state-of-the-art simulation while preserving vendor-specific behaviors, and can scale to 4,500 nodes on four commodity servers by shaving 8.3× memory."
]
doi = ""
publisher = "Proceedings of USENIX NSDI'26"
ccf = "A"
publish = "conference"
pdf = ''
code = ''
slide = ''
video = ''
top = true
[[paper.author]]
    name = 'Ze Xia'
    id = 'zxia'
[[paper.author]]
    name = 'Hao Li'
[[paper.author]]
    name = 'Jinyu Fu'
[[paper.author]]
    name = 'Xin Wan'
[[paper.author]]
    name = 'Yihan Dang'
[[paper.author]]
    name = 'Danfeng Shan'
[[paper.author]]
    name = 'Li Chen'
[[paper.author]]
    name = 'Peng Zhang'
    id = 'pzhang'
+++
