+++
title = 'Incremental Network Configuration Verification'
date = 2020
type = 'paper'
layout = 'paper'
draft = false

research_label = ["Verification", "Simulation"]
bibtex = """@inproceedings{zhang2020incremental,
  title={Incremental network configuration verification},
  author={Zhang, Peng and Huang, Yuhao and Gember-Jacobson, Aaron and Shi, Wenbo and Liu, Xu and Yang, Hongkun and Zuo, Zhiqiang},
  booktitle={Proceedings of the 19th ACM Workshop on Hot Topics in Networks},
  pages={81--87},
  year={2020}
}"""
abstract = [
    "Network configurations are constantly changing, and each change poses a risk of catastrophic network outages. Consequently, the networking community has put significant effort into developing and optimizing configuration verifiers. However, we observe existing configuration verifiers still have a significant drawback: they are not optimized for configuration *changes*. That is, they always check a snapshot of network configuration from scratch, even though the configuration often changes slightly since the last verification. In this paper, we demonstrate the benefits, opportunities, and challenges of *incremental network configuration verification (INCV)*. We also demonstrate the feasibility of INCV by introducing RealConfig, an incremental configuration verifier that can check configuration changes within one second."
]
publisher = "Proceedings of ACM HotNets'20"
pdf = 'http://nskeylab.xjtu.edu.cn/people/pzhang/files/2020/10/hotnets20.pdf'
[[paper.author]]
    name = 'Peng Zhang'
    id = 'pzhang'
[[paper.author]]
    name = 'Yuhao Huang'
[[paper.author]]
    name = 'Aaron Gember-Jacobson'
    url = 'https://aaron.gember-jacobson.com'
[[paper.author]]
    name = 'Wenbo Shi'
[[paper.author]]
    name = 'Xu Liu'
    id = 'xliu'
[[paper.author]]
    name = 'Hongkun Yang'
[[paper.author]]
    name = 'Zhiqiang Zuo'
+++
