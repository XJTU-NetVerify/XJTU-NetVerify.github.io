+++
title = 'Network Simulation'
date = 2024-05-17T15:25:56+08:00
draft = false
type = 'research'
layout = 'research'
label = "Simulation"

intro = """Network simulation aims to help operators try out new designs on their network withoutreally touching the network. It achieves this by creating a twin of the network with some level of abstraction. Depending on the abstraction level, it can either be pure simulation using customized codes to mimic the behaviors of real networks, or emulation, which uses the images or libraries of real devices."""

detailedIntro = [
"对于大规模数据中心网络，特别面向大模型训练的万卡数据中心网络，其承载真实流量和业务，且构建的成本很高，对其变更风险极大，且性能难以评估和优化。为解决这一问题，网络仿真通过抽象真实网络，在孪生的数字网络上，评估变更影响、预测训练完成时间，评估部署方案等。网络仿真既可以是基于一定抽象来高效建模网络的行为，也可以基于真实镜像来精确模拟网络的行为。目前，我们着重研究如何利用分布式计算和并行加速的更加高效、高精度的仿真大规模数据中心网络。"
]
img = "/research/Simulation.png"
imgDark = "/research/Simulation_dark.png"
+++
