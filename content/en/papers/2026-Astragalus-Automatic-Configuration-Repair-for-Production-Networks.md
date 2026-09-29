+++
title = 'Astragalus: Automatic Configuration Repair for Production Networks'
date = 2026-11-15
type = 'paper'
layout = 'paper'
draft = false

research_label = ["Verification", "Synthesis"]
bibtex = """@misc{gu2026astragalus,
      title={Astragalus: Automatic Configuration Repair for Production Networks}, 
      author={Zhenrong Gu and Peng Zhang and Xing Feng and Xu Liu},
      year={2026},
      eprint={2605.22092},
      archivePrefix={arXiv},
      primaryClass={cs.NI},
      url={https://arxiv.org/abs/2605.22092}, 
}"""
abstract = [
 "Network configurations are prone to errors, which can lead to catastrophic service outages. A tool that can achieve automatic configuration repair (ACR) is highly desired by operators. Existing tools for ACR follow a <i>semantics-driven</i> approach: they model network semantics as a set of SMT constraints, and solve them for a location or fix of the error. Due to the complex semantics of networks, constructing and solving these constraints can be prohibitively expensive, making these tools neither general nor scalable. Inspired by automatic program repair (APR), we explore another direction, i.e., a <i>syntax-driven</i> approach, which generates and validates syntactically-valid candidate updates without modeling program semantics, often drawing on existing code in the same repository. Following this direction, we propose Astragalus, a syntax-driven method for ACR. It uses multiple iterations of a \"localize-fix-validate\" pipeline to search for repairs, and proves quite effective on configurations of our production network. Specifically, we show that Astragalus can repair every incident in multiple sizes of a synthesized network, and 97.5% of the incidents on a real network, both with 15 types of errors injected, within an average time of 6.93 seconds. It has also provided valid repair suggestions in under 6 minutes for 7 recent network incidents or undesired changes, in a real production network with O(1,000)∼O(10,000) devices."
]
doi = ""
publisher = "Proceedings of ACM SIGOPS ATC '26"
ccf = "A"
publish = "conference"
preprint = "https://arxiv.org/abs/2605.22092"
slide = ''
video = ''
top = true
[[paper.author]]
    name = 'Zhenrong Gu'
    id = 'zrgu'
[[paper.author]]
    name = 'Peng Zhang'
    id = 'pzhang'
[[paper.author]]
    name = 'Xing Feng'
    id = 'xfeng'
[[paper.author]]
    name = 'Xu Liu'
    id = 'xliu'
+++
