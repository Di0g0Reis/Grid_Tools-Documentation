Multi-Period Optimal Power Flow (MP-OPF) extends the traditional optimal power flow analysis by considering a sequence of time steps, enabling the modeling of time-coupled constraints such as energy storage behavior and varying load or generation profiles. This approach is essential for studying the dynamic operation of power systems over time and for optimizing decisions that depend on both current and future system states.

In this section, you will learn how to set up and run MP-OPF simulations and understand the specific challenges involved (such as data consistency and intertemporal constraints).

After having the correct files in the [Execution file](directory.md), all you need to do is make the proper changes to the ``main.py`` file.

````py title="main.py" linenums="10" hl_lines="4 8"
if __name__ == "__main__":

    case_study = CaseStudy()
    case_study.read_data('CS2')


    # mpopf - multiple period OPF
    #case_study.run_mpopf()

    # scopf - security constraint OPF
    #case_study.run_scopf()
````

As shown in the code block above, you need to modify the scenario file on line 13 to match the specific case you want to analyze in this example, it’s ``CS2.json``. This is the execution file referenced [here](directory.md).

Next, enable the type of OPF you want to solve by uncommenting the corresponding line. For solving the Multi-Period OPF (MP-OPF), uncomment line 17.


!!! warning 

    **Do not** uncomment both line 17 and line 20 simultaneously. Attempting to solve both OPF types at the same time may result in inaccurate or inconsistent results.
