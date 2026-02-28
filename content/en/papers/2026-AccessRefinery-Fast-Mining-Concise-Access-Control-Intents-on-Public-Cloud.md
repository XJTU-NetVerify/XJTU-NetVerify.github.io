+++
title = 'AccessRefinery: Fast Mining Concise Access Control Intents on Public Cloud'
date = 2026-07-05
type = 'paper'
layout = 'paper'
draft = false

research_label = []
bibtex = """
"""
abstract = [
    "Modern cloud applications heavily rely on Identity and Access Management (IAM) services to enforce flexible access control over their data. However, the flexibility comes at a cost: IAM policies are often complex and prone to misconfigurations, leading to risks of data exposure. There is an increasing need to mine a compact set of intents that describe what the policies collectively try to achieve, thereby enabling operators to better understand their policies. However, existing tools on mining access control intent have two major limitations: (1) the mining process is slow and even times out on some complex policies; (2) the mined intents are excessive in number and thus still hard to understand. To overcome these limitations, this paper presents <i>AccessRefinery</i>, which can speed up the mining process while reducing the number of intents. The key idea for the speedup is to reduce the redundancy of the multi-round SMT solving, by preprocessing the constraints into bit-vector constraints. For intent reduction, <i>AccessRefinery</i> computes a compact set of intents that can cover the mined intents, by solving a min-set-cover problem. Experiments based on real and synthetic datasets show that <i>AccessRefinery</i> achieves a ~10–100× speedup in intent mining, and reduces the number of intents by up to ~10×."
]
publisher = "Proceedings of ACM FSE'26"
ccf = "A"
publish = "conference"
pdf='/papers/VeriBoost/accessrefinery_final_version.pdf'
top = true
[[paper.author]]
    name = 'Ning Kang'
    id = 'nkang'
[[paper.author]]
    name = 'Peng Zhang'
    id = 'pzhang'
[[paper.author]]
    name = 'Jianyuan Zhang'
    id = 'jyzhang'
[[paper.author]]
    name = 'Hao Li'
    url = "https://gr.xjtu.edu.cn/en/web/hao.li"
[[paper.author]]
    name = 'Dan Wang'
    id = 'dwang'
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
