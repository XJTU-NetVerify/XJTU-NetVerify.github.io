+++

title = 'S2: A Distributed Configuration Verifier for Hyper-Scale Networks'
date = 2025
type = 'paper'
layout = 'paper'
draft = false

research_label = ["Verification", "Simulation"]
bibtex = """
"""
abstract = [
    "Network configuration verifiers can proactively reason about a network’s correctness to prevent network outages. However, even recent efforts have proposed algorithms to “scale up” the verification to several thousand switches, these algorithms still cannot be used for networks with more than 10K switches or 1000M routes, which is common for large service providers. In this paper, instead of further scaling up the verification limited to a single server, we study how to “scale out” the verification using the resources of multiple servers. To achieve this, we propose S2, a distributed verif ier for network configurations. S2 partitions the network model and distributes the verification tasks, i.e., control plane simulation and data plane verification, to run on multiple servers in parallel. Additionally, S2 uses prefix sharding during control plane simulation to further reduce the memory footprint on each server. We implement a prototype of S2 based on Batfish, the state-of-the-art network verifier. Based on real datacenter topologies of a large service provider and synthetic FatTree topologies, we show that S2 can verify networks with 10K routers and 1000M routes within 2 hours."
]
doi = ""
publisher = "Proceedings of ACM SIGCOMM'25"
top = true
[[paper.author]]
    name = 'Dan Wang'
    id = 'dwang'
[[paper.author]]
    name = 'Peng Zhang'
    id = 'pzhang'
[[paper.author]]
    name = 'Wenbing Sun'
    id = 'wbsun'
[[paper.author]]
    name = 'Wenkai Li'
    id = 'wkli'
[[paper.author]]
    name = 'Xing Feng'
    id = 'xfeng'
[[paper.author]]
    name = 'Hao Li'
[[paper.author]]
    name = 'Jiawei Chen'
[[paper.author]]
    name = 'Weirong Jiang'
[[paper.author]]
    name = 'Yongping Tang'

+++