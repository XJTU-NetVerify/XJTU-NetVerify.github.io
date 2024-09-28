+++
title = 'Expresso: Comprehensively Reasoning About External Routes Using Symbolic Simulation'
date = 2024
type = 'paper'
layout = 'paper'
draft = false

research_label = ["", ""]
bibtex = """@inproceedings{wang2024expresso,
  title={Expresso: Comprehensively Reasoning About External Routes Using Symbolic Simulation},
  author={Wang, Dan and Zhang, Peng and Gember-Jacobson, Aaron},
  booktitle={Proceedings of the ACM SIGCOMM 2024 Conference},
  pages={197--212},
  year={2024}
}"""
abstract = [
    "Existing network verifiers can efficiently identify failure-induced bugs. However, an equally-important concern is identification of external-routes-induced bugs, which has not been well addressed. Comprehensively reasoning about external routes is challenging, since each external neighbor can advertise an arbitrary set of routes, which is quite a huge space. This paper introduces a new network verifier, Expresso, which uses symbolic simulation to explore the equivalences in the space of external routes. We evaluate the effectiveness and scalability of Expresso on the WAN of a large cloud service provider and Internet2. Expresso found various property violations, some of which have already been confirmed by the operators. To the best of our knowledge, Expresso is the only verifier that can check the correctness of WANs amidst arbitrary external routes in a tractable amount of time, while other verifiers time-out after 1 day."
]
doi = "10.1145/3651890.3672220"
publisher = "Proceedings of ACM SIGCOMM'24"
pdf = 'https://dl.acm.org/doi/pdf/10.1145/3651890.3672220'
slide = '/slides/expresso/expresso-slides.pdf'
video = 'https://www.youtube.com/embed/cafm5zeSf68?si=trl416sgzCI0u0Ke'
top = true
[[paper.author]]
    name = 'Dan Wang'
    id = 'dwang'
[[paper.author]]
    name = 'Peng Zhang'
    id = 'pzhang'
[[paper.author]]
    name = 'Aaron Gember-Jacobson'
    url = 'https://aaron.gember-jacobson.com'

+++
