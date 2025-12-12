+++
title = 'APKeep: Realtime Verification for Real Networks'
date = 2020
type = 'paper'
layout = 'paper'

research_label = ["Verification"]
bibtex = """@inproceedings {246370,
    author = {Peng Zhang and Xu Liu and Hongkun Yang and Ning Kang and Zhengchang Gu and Hao Li},
    title = {{APKeep}: Realtime Verification for Real Networks },
    booktitle = {17th USENIX Symposium on Networked Systems Design and Implementation (NSDI 20)},
    year = {2020},
    isbn = {978-1-939133-13-7},
    address = {Santa Clara, CA},
    pages = {241--255},
    url = {https://www.usenix.org/conference/nsdi20/presentation/zhang-peng},
    publisher = {USENIX Association},
ccf = "A"
publish = "conference"
    month = feb
}"""
abstract = [
    "Realtime network verification ensures the correctness of network by incrementally checking data plane updates in real time (e.g., < 1ms per rule update). Even state-of-the-art methods can already achieve sub-millisecond verification time, such speed is achieved mostly for pure IP forwarding devices, and is unrealistic for real-world networks, due to two reasons. (1) Their network models cannot express the forwarding behavior of real devices, which have various functions including IP forwarding, ACL, NAT, policy-based routing, etc. (2) Their update algorithms do not scale in space and/or time: multifield rules (e.g., ACL rules) can make these tools run out of memory and/or incur long verification time. To scale realtime verification to real networks, we propose APKeep based on a new modular network model that is expressive for real devices, and propose new algorithms that can achieve low memory cost and fast update speed at the same time. Our experiments show that for real-world update traces consisting of IP forwarding rules and ACL rules, existing methods either run out of memory or incur a prohibitively long verification time, while APKeep still achieves a sub-millisecond verification time. We also show that APKeep can verify an update of NAT rule mostly in less than 1 millisecond."
]
publisher = "Proceedings of USENIX NSDI'20"
top = true
pdf = 'https://www.usenix.org/system/files/nsdi20-paper-zhang-peng.pdf'
slide = 'https://www.usenix.org/sites/default/files/conference/protected-files/nsdi20_slides_zhang_1.pdf'
video = 'https://www.youtube.com/embed/SHDVeGM4h8E?si=PREHXlJwmek1ji2B'
web = 'https://www.usenix.org/conference/nsdi20/presentation/zhang-peng'
code = "https://github.com/XJTU-NetVerify/apkeep"
[[paper.author]]
    name = 'Peng Zhang'
    id = 'pzhang'
[[paper.author]]
    name = 'Xu Liu'
    id = 'xliu'
[[paper.author]]
    name = 'Hongkun Yang'
[[paper.author]]
    name = 'Ning Kang'
    id = "nkang"
[[paper.author]]
    name = 'Zhengchang Gu'
[[paper.author]]
    name = 'Hao Li'
    url = "https://gr.xjtu.edu.cn/en/web/hao.li"
+++
