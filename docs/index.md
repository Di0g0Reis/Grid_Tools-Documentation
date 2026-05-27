# Power Flow Optimization Tools

Welcome to the **Grid Operation Tools Documentation**, a suite of tools for advanced power system optimization. These models are designed to help engineers, researchers, and system operators simulate and solve power flow problems under realistic system and operational constraints.

---

## ⚡ Overview
- **Probabilistic Optimal Power Flow (P-OPF)**: P-OPF is primarily analytical. It takes uncertain inputs, such as, weather-dependent renewable output or shifting load patterns, 
and maps them as probability distributions to determine the likelihood of various system outcomes. Its primary purpose is to provide a "risk profile" for a given operation, 
showing planners how often voltage or thermal limits might be breached under current market conditions without necessarily changing the dispatch to fix them.

- **Stochastic Optimal Power Flow (S-OPF)**: S-OPF is primarily prescriptive. It explicitly integrates uncertainty into the optimization engine by solving for a dispatch 
schedule that performs well across a set of diverse, probable scenarios. By minimizing the expected cost while ensuring that operational constraints are respected across 
all modeled scenarios (often using multi-stage or scenario-based programming), it creates a robust, "future-proof" dispatch plan that remains optimal even when 
market conditions or supply availability fluctuate.

- **Chance-Constrained Optimal Power Flow (CC-OPF)**: CC-OPF incorporates uncertainty by enforcing operational limits (such as voltage or thermal constraints)
to be satisfied with a **predefined level of confidence** (e.g., 95%). It allows system operators to manage risks by quantifying how much "buffer" is
required in dispatch schedules to accommodate fluctuations in wind, solar, or market price volatility without violating safety thresholds.

- **Security-Constrained Optimal Power Flow (SC-OPF)**: SC-OPF ensures the power system remains stable and within limits even 
after the sudden loss of a critical component (N-1 security). It models system behavior under specific contingency scenarios, such as, a transmission line or generator failure, 
ensuring that the market-cleared dispatch remains robust and that the grid can withstand a primary equipment failure without cascading outages.

- **Chance-Constrained Security-Constrained Optimal Power Flow (CC-SC-OPF)**: CC-SC-OPF is the most advanced framework, combining risk-based handling of stochastic uncertainty with 
rigorous reliability standards. It optimizes grid dispatch by simultaneously ensuring that system constraints are met under probabilistic variations (like forecast errors) and discrete
contingency events (like component failure). It provides a high-reliability operational strategy that balances cost-efficiency with a robust, risk-aware approach to both 
market volatility and physical grid security.

These tools can be used independently or combined for security-aware, time-coupled, stochastic optimization in power systems.

---

## 🚀 Key Features

- Support for **single or multi-period, and stochastic and probabilistic optimization**
- Built-in **N-1 contingency analysis**
- **Ramp rate modeling** for generators
- Integration with industry-standard solvers (e.g., Pyomo)

---

## 📘 Documentation Sections

This website is broken down into the following sections:
=== "Sections"

    * [About this project](about.md)
    * [Getting Started](getting_started.md)
    * [Datastructure and Elements](elements.md)
    * [Optimal Power Flow](opf.md)
    * [Security-Constrained Optimal Power Flow](sc_opf.md)

---
