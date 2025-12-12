+++
title = 'Modular Data Plane Verification for Compositional Networks'
date = 2023-12-01
type = 'paper'
layout = 'paper'

research_label = ["Verification"]
bibtex = """@article{liu2023modular,
  title={Modular Data Plane Verification for Compositional Networks},
  author={Liu, Xu and Zhang, Peng and Li, Hao and Sun, Wenbing},
  journal={Proceedings of the ACM on Networking},
  volume={1},
  number={CoNEXT3},
  pages={1--22},
  year={2023},
  publisher={ACM New York, NY, USA}
}"""
abstract = [
    "Modern networks are increasingly using layering and bridging to form a compositional architecture. Layering protocols like VXLAN create multiple overlay networks on top of a single underlay network infrastructure. This makes network configurations even more complex, and error-prone.To check the correctness of such compositional networks, one needs to model the dependency across multiple layers (underlay and overlay) and multiple domains (different VPNs/VPCs). Existing verifiers, which are optimized to scale in single-layer single-domain networks, exhibit scalability limitations when applied to compositional networks.This paper proposes MNV a modular network verifier that scales to large compositional networks. At its core is a new verification method termed decompose-merge reasoning, which decomposes the network into self-contained modules, verifies each module independently, and merges the verification results. Our experiments show that for a typical data center network virtualized with VXLAN, to check reachability for more than 100 million pairs of subnets, MNV is at least 100x faster than state-of-the-art tools."
]
doi = "10.1145/3629145"
publisher = "Proceedings of ACM CoNEXT'23"
ccf = "B"
publish = "conference"
web = 'https://dl.acm.org/doi/abs/10.1145/3629145'
video = 'https://www.youtube.com/embed/SXem7FXMUZo?si=uVPMH7226YmTEO03'
[[paper.author]]
    name = 'Xu Liu'
    id = 'xliu'
[[paper.author]]
    name = 'Peng Zhang'
    id = 'pzhang'
[[paper.author]]
    name = 'Hao Li'
    url = "https://gr.xjtu.edu.cn/en/web/hao.li"
[[paper.author]]
    name = 'Wenbing Sun'
    id = "wbsun"
+++
