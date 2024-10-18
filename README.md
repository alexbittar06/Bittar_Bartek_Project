# Bittar_Bartek_Project
Project for Theory of Computing 
Team name: 
    KeoughKitch

Names of all team members: 
    Evan Bartek, Alex Bittar

Link to github repository: 
    https://github.com/alexbittar06/Bittar_Bartek_Project

Which project options were attempted: 
    The K-partite Matching Problem number 3

Approximately total time spent on project: 

The language you used, and a list of libraries you invoked.
    python
    time, networkX

How would a TA run your program (did you provide a script to run a test case?)
    just running the code (python3 ______.py) will automatically run the tests on the data files in the folder

A brief description of the key data structures you used, and how the program functioned.
    arrays,dictionaries,pairs

A discussion as to what test cases you added and why you decided to add them (what did they tell you about the correctness of your code). Where did the data come from? (course website, handcrafted, a data generator, other)
    Our test data came mainly jjjeeefrom networkX. It created many differnt cases in which there were and there were not perfect matches and they were placed in two differnt CSV files and those files were then read in by our program in order to get the output. They are called not_perfect_partite_graph.csv and perfect_partite_graph.csv.

An analysis of the results, siuch as if timings were called for, which plots showed what? What was the approximate complexity of your program?

Average compleicty is O(kn^2)
    
A description of how you managed the code development and testing.

We managed the code devlopment by each craeting seperate functions that did differnt tasks. Alex handled the unit rules and Evan managed the creation of the test Files and the graphs. Both worked on the actaul matching part of the code. For testing we ran two diffent times, one without the unit rules implemented and one with. We then got data from both of them and graphed.

Did you do any extra programs, or attempted any extra test cases

We did a program that just tested the unit rule until that worked and then implmented it into our main code where the matching actually happnes. There were certain test cases that we manually wrote into the code testing the unit rule but that was simply just to test that out.

