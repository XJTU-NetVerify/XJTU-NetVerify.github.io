+++
title = 'Differential Network Analysis'
date = 2022
type = 'paper'
layout = 'paper'
draft = false

research_label = ["Verification", "Simulation"]
bibtex = """@inproceedings{zhang2022differential,
  title={Differential network analysis},
  author={Zhang, Peng and Gember-Jacobson, Aaron and Zuo, Yueshang and Huang, Yuhao and Liu, Xu and Li, Hao},
  booktitle={19th USENIX Symposium on Networked Systems Design and Implementation (NSDI 22)},
  pages={601--615},
  year={2022}
}"""
abstract = [
    "Networks are constantly changing. To avoid outages, operators need to know whether prospective changes in a network’s control plane will cause undesired changes in end-to-end forwarding behavior. For example, which pairs of end hosts are reachable before a configuration change but unreachable after the change? Control plane verifiers are ill-suited for answering such questions because they operate on a single snapshot to check its “compliance” with “explicitly specified” properties, instead of quantifying the “differences” in “affected” end-toend forwarding behaviors. We argue for a new control plane analysis paradigm that makes differences first class citizens. Differential Network Analysis (DNA) takes control plane changes, incrementally computes control and data plane state, and outputs consequent differences in end-to-end behavior. We break the computation into three stages—control plane simulation, data plane modeling, and property checking—and leverage differential dataflow programming frameworks, incremental data plane verification, and customized graph algorithms, respectively, to make each stage incremental. Evaluations using both real and synthetic control plane changes demonstrate that DNA can compute the resulting differences in reachability in a few seconds—up to 3 orders of magnitude faster than state-of-the-art control plane verifiers."
]
publisher = "Proceedings of USENIX NSDI'22"
top = true
pdf = 'https://gr.xjtu.edu.cn/documents/1748990/0/dna_nsdi22.pdf/bc7e8943-85e4-ffa2-d00e-86fc09ea5313?t=1632275920827'
code = "https://github.com/XJTU-NetVerify/dna"
web = "https://www.usenix.org/conference/nsdi22/presentation/zhang-peng"
slide = "https://www.usenix.org/system/files/nsdi22_slides_zhang-peng.pdf"
video = "https://www.youtube.com/embed/DnGxG_Qe2pY?si=IXVsM372Mqydawjn"
[[paper.author]]
    name = 'Peng Zhang'
    id = "pzhang"
[[paper.author]]
    name = 'Aaron Gember-Jacobson'
    url = 'https://aaron.gember-jacobson.com'
[[paper.author]]
    name = 'Yueshang Zuo'
[[paper.author]]
    name = 'Yuhao Huang'
[[paper.author]]
    name = 'Xu Liu'
    id = 'xliu'
[[paper.author]]
    name = 'Hao Li'
    url = "https://gr.xjtu.edu.cn/en/web/hao.li"
+++
