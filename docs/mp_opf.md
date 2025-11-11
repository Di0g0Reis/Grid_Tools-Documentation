Multi-Period Optimal Power Flow (MP-OPF) extends the traditional optimal power flow analysis by considering a sequence of time steps, enabling the modeling of time-coupled constraints such as energy storage behavior and varying load or generation profiles. This approach is essential for studying the dynamic operation of power systems over time and for optimizing decisions that depend on both current and future system states.

In this section, you will learn how to set up and run MP-OPF simulations and understand the specific challenges involved (such as data consistency and intertemporal constraints).

After having the correct files in the [Execution file](directory.md), all you need to do is make the proper changes to the ``main.py`` file.

````py title="main.py"
from SCOPF_Package import run_case_study

if __name__ == "__main__":

    run_case_study("CS2", "MP")
````

As shown in the code block above, you need to modify the scenario file to match the specific case you want to analyze in this example, it’s ``CS2.json``. This is the execution file referenced [here](directory.md).

Next, enable the type of OPF you want to solve by writing "MP" in the operation spot for solving the Multi-Period OPF (MP-OPF).