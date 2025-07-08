Security-Constrained Optimal Power Flow (SC-OPF) is an advanced extension of the traditional OPF formulation that incorporates system security considerations into the optimization process. In addition to minimizing operational costs or losses, SC-OPF ensures that the power system remains within safe operating limits even under predefined contingency scenarios, such as line outages or generator failures (commonly referred to as N-1 security).

This approach is essential for maintaining system reliability and stability, especially in large-scale or critical infrastructure networks. By accounting for contingencies during the optimization, SC-OPF helps operators make decisions that are both economically efficient and resilient to unexpected disruptions.

In this section, you will learn how to set up and execute SC-OPF analyses, define contingency cases, interpret the results, and understand the trade-offs between cost optimization and system security.


````py title="main.py" linenums="10" hl_lines="4 11"
if __name__ == "__main__":

    case_study = CaseStudy()
    case_study.read_data('CS2')


    # mpopf - multiple period OPF
    #case_study.run_mpopf()

    # scopf - security constraint OPF
    #case_study.run_scopf()
````

As shown in the code block above, you need to modify the scenario file on line 13 to match the specific case you want to analyze in this example, it’s ``CS2.json``. This is the execution file referenced [here](directory.md).

Next, enable the type of OPF you want to solve by uncommenting the corresponding line. For solving the Security-Constrained OPF (SC-OPF), uncomment line 20.


!!! warning 

    **Do not** uncomment both line 17 and line 20 simultaneously. Attempting to solve both OPF types at the same time may result in inaccurate or inconsistent results.
