#                    Brute Force SAT
# This file generates a set of random wffs and tests each for satisfiability.
#   The test returns "Satisfiable" or not, and the time it took to determine that.
# A wff is expressed as a list of lists where each internal list is a clause.
#    and each integer within a clause list is a literal
#    A positive integer such as "3" means that clause is true if variable 3 is true
#    A negative integer such as "-3" means that clause is true if variable 3 is false
#  A clause is satisfiable if at least one literal is true
#  A wff is satisfiable if all clauses are satisfiable
# An assignment to n variables is a list of n 0s or 1s (0=>False, 1=>True)
#    where assignment[i] is value for variable i+1 (there is no variable 0)
#
# build_wff builds a random wff with specified # of clauses, variables,
#   and literals/clause
# check takes a wff, generates all possible assignments,
#   and determines if any assignment satisfies it.
#   If so it stops and returns the time ans assignment
# test_wff builds a random wff with certain structure
#
# run_cases takes a list of 4-tuples and for each one generates a number of wffs
#    with the same specified characteristices, and test each one.
#    It outputs to a file (in current directory) each wff in cnf format,
#    and also for each case it dumps a row to a .csv file that contains
#       the test conditions and the satisfying assignment if it exists

import time
import random
import string


def check(Wff, Nvars, Nclauses, Assignment):
    Satisfiable = False
    while (Assignment[Nvars + 1] == 0):
        # Iterate thru clauses, quit if not satisfiable
        for i in range(0, Nclauses):  # Check i'th clause
            Clause = Wff[i]
            Satisfiable = False
            for j in range(0, len(Clause)):  # check each literal
                Literal = Clause[j]
                if Literal > 0:
                    Lit = 1
                else:
                    Lit = 0
                VarValue = Assignment[abs(Literal)]  # look up literal's value
                if Lit == VarValue:
                    Satisfiable = True
                    break
            if not Satisfiable:
                break
        if Satisfiable:
            break  # exit if found a satisfying assignment
        # Last try did not satisfy; generate next assignment
        for i in range(1, Nvars + 2):
            if Assignment[i] == 0:
                Assignment[i] = 1
                break
            else:
                Assignment[i] = 0
    return Satisfiable


def build_wff(Nvars, Nclauses, LitsPerClause):
    wff = []
    for _ in range(1, Nclauses + 1):
        clause = []
        for _ in range(1, LitsPerClause + 1):
            var = random.randint(1, Nvars)
            if random.randint(0, 1) == 0:
                var = -var
            clause.append(var)
        wff.append(clause)
    return wff


def test_wff(wff, Nvars, Nclauses):
    Assignment = list((0 for _ in range(Nvars + 2)))
    start = time.time()  # Start timer
    SatFlag = check(wff, Nvars, Nclauses, Assignment)
    end = time.time()  # End timer
    exec_time = int((end - start) * 1e6)
    return [wff, Assignment, SatFlag, exec_time]


def run_cases(TestCases, ProbNum, tablefile):
    # Open table file to write results
    with open(tablefile + ".csv", 'w') as tablef:
        tablef.write("Clauses, SAT Time Taken (us), UNSAT Time Taken (us)\n")  # Table header

        for i in range(len(TestCases)):
            TestCase = TestCases[i]
            Nvars = TestCase[0]
            NClauses = TestCase[1]
            LitsPerClause = TestCase[2]
            Ntrials = TestCase[3]

            for j in range(Ntrials):
                random.seed(ProbNum)
                wff = build_wff(Nvars, NClauses, LitsPerClause)
                results = test_wff(wff, Nvars, NClauses)
                Exec_Time = results[3]

                if results[2]:  # Satisfiable
                    # Write SAT time
                    tablef.write(f"{NClauses*Nvars},{Exec_Time},\n")
                else:  # Unsatisfiable
                    # Write UNSAT time
                    tablef.write(f"{NClauses*Nvars},,{Exec_Time}\n")

                # Increment problem number
                ProbNum += 1


# Example TestCases and running the function
TestCases = [
    [4,10,2,10],
    [8,16,2,10],
    [12,24,2,10],
    [16,32,2,10],
    [18,36,2,10],
    [20,40,2,10],
    [22,44,2,10],
    [24,48,2,10],
]

ProbNum = 3
resultsfile = r'resultsfile'
tracefile = r'tracefile'
cnffile = r'cnffile'
summaryfile = 'summary_results'  # Name of the summary output file

# Run the function with the test cases
run_cases(TestCases, ProbNum, summaryfile)
