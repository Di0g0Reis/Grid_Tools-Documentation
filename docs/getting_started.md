# Getting Started

## Installation
You can begin using SC-OPF in just a few easy steps. First you need to install an IDE, in our case we used Pycharm, which can be installed through [Anaconda](https://www.anaconda.com/download) or through their official [website](https://www.jetbrains.com/pycharm/).
After installing the IDE you will need to install the following necessary libraries:

### Pyomo
[Pyomo](https://www.pyomo.org) is a powerful open-source Python library used for defining and solving mathematical optimization problems. It supports a wide range of optimization types, including linear programming (LP), mixed-integer programming (MIP), nonlinear programming (NLP), and more. Pyomo allows users to build complex optimization models in a flexible and readable way using Python code. It can interface with various solvers like GLPK, CBC, CPLEX, and Gurobi. Pyomo is widely used in academia and industry for operations research, supply chain optimization, energy systems, and engineering applications. Its strength lies in its modeling flexibility and integration with the Python ecosystem.

If you are using Anaconda, install Pyomo through the anaconda prompt:
```
conda install conda-forge::pyomo
```
You can also install it with pip:
```
pip install pyomo
```
### IPOPT
[IPOPT](https://coin-or.github.io/Ipopt/) (Interior Point Optimizer) is an open-source software package for large-scale nonlinear optimization. It is designed to solve problems with continuous variables, including **NonLinear Programming (NLP)**
problems that may have thousands or millions of variables and constraints. IPOPT uses an interior-point algorithm and supports sparse matrix techniques for efficient computation. 
It is particularly effective for smooth, constrained optimization problems in engineering, economics, and scientific computing. IPOPT can be used with modeling languages like Pyomo and AMPL, 
and integrates with various linear algebra libraries for improved performance.

If you are using Anaconda, install IPOPT through the anaconda prompt:
```
conda install conda-forge::ipopt
```
or
```
conda install -c conda-forge ipopt
```
You can also install it with pip:
```
pip install cyipopt
```
To use IPOPT you will also need to create a `.env` file with the `ipopt.exe` file location.
To find the corresponding location, run the following code in the anaconda prompt:
```commandline
where ipopt
```
If this command doesn't work try:
```commandline
which ipopt
```
It will return the location of IPOPT execution file, copy that location as it is essential to create the `.env` file. 
Simply create a new file on your IDE at the same level of the main code that you are going to run with the name `.env`. It should look something like this:
````title=".env"
SOLVER_PATH='\Path_to_ipopt_exe_file\ipopt'
````

!!! tip "Recommendation"

    We recommend using the [HSL solvers](https://licences.stfc.ac.uk/product/coin-hsl) from UK Research and Innovation, because they are much faster. However, to access them, you need to submit a request with a justification. After approval, you’ll receive a set of packages to download, along with a README file that guides you through the installation process.

If you want to use our Mixed Integer Quadratic Programing (MIQP), CC-SC-OPF framework solution, you will need to install a solver of said type. We recommend the [Gurobi](https://www.gurobi.com/misc/lp/all/gurobi-vs-other-solvers-how-to-benchmark-optimization-solutions-the-right-way?utm_source=google&utm_medium=cpc&utm_campaign=2026+emea+googleads+search+non+brand&utm_content=benchmarking-guide&gad_source=1&gad_campaignid=193469376&gclid=CjwKCAjwrNrQBhBjEiwAoR4VO58ieIxiY5z3Qh6BciM2YGWYX2p0PHq0flQWKjlGopi0QOVQTJiO0hoCeOAQAvD_BwE) solver. 

After this, you will need the entry files (grid files) for the package to read. For this step you should read the [Datastructures and Elements](elements.md) section.


### Download the SCOPF Package
You can download the package from GitLab. There, you’ll find all the auxiliary code and data sources for the various test cases. Remember to read the [Datastructures and Elements](elements.md) section, before you start simulating.

For details on how each function works, refer to the [Optimal Power Flow](opf.md) and [Security-Constrained Optimal Power Flow](sc_opf.md) modules.