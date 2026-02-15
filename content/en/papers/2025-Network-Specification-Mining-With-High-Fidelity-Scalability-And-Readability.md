+++
title = 'Network Specification Mining With High Fidelity, Scalability, and Readability'
date = 2025-09-24
type = 'paper'
layout = 'paper'
draft = false

research_label = ["Synthesis"]
bibtex = """
@ARTICLE{11178104,
  author={Kang, Ning and Zhang, Peng and Li, Hao and Wen, Sisi and Ji, Chaoyang and Yang, Yongqiang},
  journal={IEEE Transactions on Networking}, 
  title={Network Specification Mining With High Fidelity, Scalability, and Readability}, 
  year={2025},
  volume={},
  number={},
  pages={1-16},
  keywords={Topology;Network topology;Scalability;Routing;Costs;Computational modeling;Data mining;Analytical models;Data models;Complexity theory;Specification;scalability;fidelity;readability},
  doi={10.1109/TON.2025.3607440}}
"""
abstract = [
  "Network specification, which describes what an existing network is designed for, can help operators better understand and manage their networks, and is a critical pre-condition for network verification and synthesis tools to work. Existing tools for specification mining either cannot scale to large networks, or scale by sacrificing fidelity. Moreover, the specification contains a huge number of low-level intents (e.g., tens of thousands of pairwise reachability), making it hard for operators to read. To this end, this paper presents NetMiner, which can mine specification from network configurations, with high scalability, fidelity, and easier to read. The key idea of NetMiner is to faithfully simulate the network routing and forwarding behaviors with control plane simulators and data plane verifiers, so as to achieve high fidelity. Meanwhile, NetMiner improves the scalability by identifying relevant failure scenarios, and aggregating them to significantly reduce the number of needed simulations. Moreover, NetMiner clusters similar low-level intents into a high-level intent, to make the specification more concise and easier to read. Experiments using real configurations from a large cloud service provider and synthetic configurations show that NetMiner can mine specification 10× faster, and reduce the number of intents by 100×, compared to state-of-the-art tools."
]
doi = "10.1109/TON.2025.3607440"
publisher = "Proceedings of IEEE TON'25 IEEE"
ccf = "A"
publish = "journal"
pdf = '/papers/NetMiner/NetMiner_TON.pdf'
code = ''
slide = ''
video = ''
top = true
[[paper.author]]
    name = 'Ning Kang'
    id = 'nkang'
[[paper.author]]
    name = 'Peng Zhang'
    id = 'pzhang'
[[paper.author]]
    name = 'Hao Li'
[[paper.author]]
    name = 'Sisi Wen'
[[paper.author]]
    name = 'Chaoyang Ji'
[[paper.author]]
    name = 'Yongqiang Yang'
+++
