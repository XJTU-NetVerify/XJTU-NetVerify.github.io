+++
title = 'NDD: A Decision Diagram for Network Verification'
date = 2025-04-28
type = 'paper'
layout = 'paper'
draft = false

research_label = ["Verification"]
bibtex = """
"""
award = "Outstanding Paper Award"
abstract = [
  "State-of-the-art network verifiers extensively use Binary Decision Diagram (BDD) as the underlying data structure to represent the network state and equivalence classes. Despite its wide usage, we find BDD is not ideal for network verification: verifiers need to handle the low-level computation of equivalence classes, and still face scalability issues when the network state has a lot of bits.",
  "To this end, this paper introduces Network Decision Diagram (NDD), a new decision diagram customized for network verification. In a nutshell, NDD wraps BDD with another layers of decision diagram, such that each NDD node represents a field of the network, and each edge is labeled with a BDD encoding the values of that field. We designed and implemented an library for NDD, which features a native support for equivalence classes, and higher efficiency in memory and computation. Using the NDD library, we re-implemented five BDD-based verifiers with minor modifications to their original codes, and observed a 100x reduction in memory cost and 100x speedup. This indicates that NDD provides a drop-in replacement of BDD for network verifiers."
]
doi = ""
publisher = "Proceedings of USENIX NSDI'25"
pdf = '/papers/NDD/NDD-final-version.pdf'
code = 'https://github.com/XJTU-NetVerify/NDD'
slide = '/papers/NDD/NDD-A-Decision-Diagram-for-Network-Verification.pdf'
video = ''
top = true
[[paper.author]]
    name = 'Zechun Li'
    id = 'zcli'
[[paper.author]]
    name = 'Peng Zhang'
    id = 'pzhang'
[[paper.author]]
    name = 'Yichi Zhang'
    id = 'yczhang'
[[paper.author]]
    name = 'Hongkun Yang'
+++
