+++
title = 'R<span style="font-variant: small-caps">elia</span>: Accelerating the Analysis of Cloud Access Control Policies'
date = 2025-11-16
type = 'paper'
layout = 'paper'
draft = false

research_label = []
bibtex = """
"""
abstract = [
    "With the diversification of cloud services, cloud providers offer flexible access control by letting users apply fine-grained cloud access control policies to secure their cloud resources. However, flexibility comes with the cost that configuring cloud access control policies is error-prone. Therefore, cloud providers have developed SMT-based tools to formally analyze the user-defined policies. Unfortunately, we find these analyzers slow, due to the complex regular expression matching conditions in policies. To this end, this paper introduces R<span style=\"font-variant: small-caps\">elia</span>, a general method to speed up the analysis of cloud access control policies. The key idea of R<span style=\"font-variant: small-caps\">elia</span> is to pre-compute a set of <i>String Equivalence Classes (SECs)</i> based on the regular expressions in a policy, assign a unique integer to each SEC, and rewrite the regular constraints into equivalent integer constraints, which are easier to solve. We implement R<span style=\"font-variant: small-caps\">elia</span> as a transparent layer between our in-house access analyzer and off-the-shelf SMT solvers. Based on real policies from a large public cloud provider, we show that: when enabling R<span style=\"font-variant: small-caps\">elia</span>, our in-house portfolio solver (consisting of Z3, CVC4, and CVC5) can speed up the analysis process for nearly 95% of all cases, with an average speedup of 8.21×."
]
doi = ""
publisher = "Proceedings of IEEE/ACM ASE'25"
top = true
[[paper.author]]
    name = 'Dan Wang'
    id = 'dwang'
[[paper.author]]
    name = 'Peng Zhang'
    id = 'pzhang'
[[paper.author]]
    name = 'Zhenrong Gu'
    id = 'zrgu'
[[paper.author]]
    name = 'Weibo Lin'
[[paper.author]]
    name = 'Shibiao Jiang'
[[paper.author]]
    name = 'Zhu He'
[[paper.author]]
    name = 'Xu Du'
[[paper.author]]
    name = 'Longfei Chen'
[[paper.author]]
    name = 'Jun Li'
[[paper.author]]
    name = 'Xiaohong Guan'
+++