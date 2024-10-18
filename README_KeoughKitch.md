# Bittar_Bartek_Project

Project for Theory of Computing 

Team name: 
    KeoughKitch


Names of all team members: 
    Evan Bartek, Alex Bittar


Link to github repository: 
    https://github.com/alexbittar06/Bittar_Bartek_Project


Which project options were attempted: 
    Sat Porblem part 4


Approximately total time spent on project: 
around a total of 30 hours

The language you used, and a list of libraries you invoked.
    Python - language used 
    Time- used to keep track of time 
    Random - to build wffs
    DumbSat.py - Was used as a starting point, modified to give better output to a file and       then later modified to be smartSat 



How would a TA run your program (did you provide a script to run a test case?)

    just running the code (python3 ______.py) will run both of the codes as both of them already have test cases implemnted in the code. 




A brief description of the key data structures you used, and how the program functioned.

     Arrays - used to be able to solve and process Sat problems
   csv files - were used to save output data and have it in an organized format that can be graphed




A discussion as to what test cases you added and why you decided to add them (what did they tell you about the correctness of your code). Where did the data come from? (course website, handcrafted, a data generator, other)

Test cases provided in files. dumbsat is reduced for sake of time. Since the dumbSat solver takes a long time(40 minutes), we just used the provided test cases to the point where the program took exponentially more time to execute and took those results and placed them on a graph as control data. 

In smartSat, we were able to use ALL of the cases provided in the dumbSat code. These ran significantly more efficiently with our new and improved check() function at work. These test cases can all be found in the smartSat file. This again was coded to be output in an organized matter into a file which would later serve as the data for our second graph






An analysis of the results, siuch as if timings were called for, which plots showed what? What was the approximate complexity of your program?

As seen in the data, Smartsat has a linear time complexity while dumbsat has an exponential complexity.

The first graph seen is our implementation of the check() function that creates a “smartSat” solver. As seen from analysis of the graph, it seems to be a linear amount of time spent solving satProblems. This is SIGNIFICANTLY better than the second graph shown which is the control data from the dumbSat solver. The second graph shows an exponential time increase at around 32 clauses to last for a total of 125,000 milliseconds just about. In the smartSat Graph, the same amount of clauses is solved in just a few milliseconds which is a very good difference. dumbSat runs at O(n)^2 or worse while smartSat runs at O(n).
    




A description of how you managed the code development and testing.

As one person set up testing cases along with reading the output into a graph, the other spent time working on the actual SmartSat solution.

  
We both debugged and switched roles every once in a while.

Additionally, we used ChatGPT to brainstorm unit rules for the smartsat solution, and we then wrote code based on the concepts it gave us (binary increment to generate next, unit literals). From there, one of us wrote the code for the new check() function based on the ideas of increment and unit literals as the other started to work on changing dumbSat code to provide output in the form of CSV files. This was for dumbSat.


FOR OUR FAILED attempt at k-partite

We split the work similarly, one looked at the code that was on canvas and got it to read the data that came from it and output it to a CSV file and the other tried to create rules to make the matching process faster. One of us also made a code to generate test cases for perfect and non-perfect matches. Our problem came in that our smartSolver was slower than the dumbSolver and after much debugging and consideration, we decided to unfortunately drop this project. 





Did you do any extra programs, or attempted any extra test cases

We did all the extra programs under the k-partite dropped folder. This was dropped due to the fact that our "smart" solver was slower than out "dumb" solver. We did not know if it was the test cases that were being generated or the code that was not functioning properly, so we sadly decided to drop it after much consideration.

