+++
title = 'Mitigating CPU Frontend for Complex Data Plane Applications'
date = 2025-12-23
type = 'paper'
layout = 'paper'
draft = false

research_label = []
bibtex = """
"""
abstract = [
 "The functionality and requirement of modern networks are becoming increasingly complex, giving rise to Complex Data Plane Applications (CDPA) with rich semantics but often limited performance. However, most existing optimizations fail to improve the performance of CDPAs. This is because CDPAs usually come with excessively large code size, which is often two order of magnitude larger than today’s L1 instruction cache (I-cache) size, causing the CPU to frequently stall on accessing instructions, thus presenting a distinct performance profile that bounds on CPU frontend. This paper proposes NanoPL, an i-cache friendly new execution model that shuffles the packet processing order to efficiently mitigate CPU frontend for CDPAs. Stemming from the common execution pattern of CDPAs, NanoPL analyzes its code to ensure semantic consistency after shuffling. By collecting performance profile of CDPAs over underlying traffic, NanoPL partitions CDPAs into execution stages and conducts i-cache friendly shuffing policy. Experiments show that NanoPL can achieve 17.2%~30.2% higher throughput over real world CDPAs due to the reduction of i-cache misses by up to 86.4%."
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
    name = 'Yihan Dang'
[[paper.author]]
    name = 'Hao Li'
    url = "https://gr.xjtu.edu.cn/en/web/hao.li"
[[paper.author]]
    name = 'Ze Xia'
    id = 'zxia'
[[paper.author]]
    name = 'Jiajun Luan'
[[paper.author]]
    name = 'Peng Zhang'
    id = 'pzhang'
+++
