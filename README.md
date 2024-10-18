# Bittar_Bartek_Project
Project for Theory of Computing 
Team name: 
    KeoughKitch

Names of all team members: 
    Evan Bartek, Alex Bittar

Link to github repository: 
    https://github.com/alexbittar06/Bittar_Bartek_Project
    *contents are in sat folder NOT bipartite_dropped.

Which project options were attempted: 
    Sat problem 4

Approximately total time spent on project: 
    30hrs - mainly because we wasted alot of time on bipartitie.

The language you used, and a list of libraries you invoked.
    python
    time, random, DumbSat.py

How would a TA run your program (did you provide a script to run a test case?)
    just running the code (python3 SmartSat.py) will automatically run the tests on the data files in the folder
    python3 SmartSat.py to compare if needed
    - Test data was provided within the DumbSat.py file on canvas

A brief description of the key data structures you used, and how the program functioned.
    arrays, csv files

A discussion as to what test cases you added and why you decided to add them (what did they tell you about the correctness of your code). Where did the data come from? (course website, handcrafted, a data generator, other)
    for Dumbsat, our test cases are multiple variations of low clause problems from the provided DumbSat file. This was to keep the test cases for the DumbSat graph reasonable to run.
    for Smartsat, our test cases were all of the provided dumsat test cases.

    this tells us that smart sat is exponentially faster than dumbsat as what would take 40minutes instead takes seconds.

An analysis of the results, siuch as if timings were called for, which plots showed what? What was the approximate complexity of your program?
    the smartSat graph shows a linear time complexity as the number of clauses and/or variables grew
    the dumbsat graph shows an exponential time complexity as the number of clauses grew.

    
A description of how you managed the code development and testing.
    As one set up testing cases and reading the output into a graph, the other spent time working on the actual SmartSat solution.
    we both debugged and switched roles every once an a while.


Did you do any extra programs, or attempted any extra test cases
    yes. all of the files and programs in the bipartite_dropped folder in the github repo was done unsuccessfully 


