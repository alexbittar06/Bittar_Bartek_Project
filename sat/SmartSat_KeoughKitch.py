
import time
import random
import string

# Following is an example of a wff with 3 variables, 3 literals/clause, and 4 clauses
Num_Vars=3
Num_Clauses=4
wff=[[1,-2,-2],[2,3,3],[-1,-3,-3],[-1,-2,3],[1,2,-3]]


# Following is an example of a wff with 3 variables, 3 literals/clause, and 8 clauses
Num_Clauses=8
wff=[[-1,-2,-3],[-1,-2,3],[-1,2,-3],[-1,2,3],[1,-2,-3],[1,-2,3],[1,2,-3],[1,2,3]]

def check(Wff, Nvars, Nclauses, Assignment):
    # Create a count of the number of clauses and literal occurrences
    literal_count = {}
    unit_clauses = []

    # First pass: Initialize the counts for literals and identify unit clauses
    for clause in Wff:
        if len(clause) == 1:
            unit_clauses.append(clause[0])
        for literal in clause:
            abs_literal = abs(literal)
            if abs_literal not in literal_count:
                literal_count[abs_literal] = [0, 0]  # [positive_count, negative_count]
            if literal > 0:
                literal_count[abs_literal][0] += 1
            else:
                literal_count[abs_literal][1] += 1

    # Apply Pure Literal Elimination
    for literal, counts in literal_count.items():
        if counts[0] > 0 and counts[1] == 0:  # Only positive literals
            Assignment[literal] = 1
        elif counts[1] > 0 and counts[0] == 0:  # Only negative literals
            Assignment[literal] = 0

    # Second pass: Assign values for unit clauses
    for unit_literal in unit_clauses:
        var = abs(unit_literal)
        if unit_literal > 0:
            Assignment[var] = 1  # Assign true
        else:
            Assignment[var] = 0  # Assign false

    # Check if current assignment satisfies the WFF
    Satisfiable = True
    for clause in Wff:  # Check i'th clause
        ClauseSatisfied = False
        for literal in clause:  # Check each literal in the clause
            VarValue = Assignment[abs(literal)]
            if (literal > 0 and VarValue == 1) or (literal < 0 and VarValue == 0):
                ClauseSatisfied = True
                break
        if not ClauseSatisfied:  # If any clause is not satisfied
            Satisfiable = False
            break

    if Satisfiable:  # Found a satisfying assignment
        return True

    # Generate the next assignment using binary increment
    for i in range(1, Nvars + 1):
        if Assignment[i] == 0:
            Assignment[i] = 1  # Increment the current variable
            break
        else:
            Assignment[i] = 0  # Reset to 0 and move to the next variable
    else:
        # If we exit the loop normally (no break), it means we've tried all assignments
        return False

    return False  # No satisfying assignment was found
    
def build_wff(Nvars,Nclauses,LitsPerClause):
    wff=[]
    for i in range(1,Nclauses+1):
        clause=[]
        for j in range(1,LitsPerClause+1):
            var=random.randint(1,Nvars)
            if random.randint(0,1)==0: var=-var
            clause.append(var)
        wff.append(clause)
    return wff

def test_wff(wff,Nvars,Nclauses):
    Assignment=list((0 for x in range(Nvars+2)))
    start = time.time() # Start timer
    SatFlag=check(wff,Nvars,Nclauses,Assignment)
    end = time.time() # End timer
    exec_time=int((end-start)*1e6)
    return [wff,Assignment,SatFlag,exec_time]

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
                    tablef.write(f"{NClauses},{Exec_Time},\n")
                else:  # Unsatisfiable
                    # Write UNSAT time
                    tablef.write(f"{NClauses},,{Exec_Time}\n")

                # Increment problem number
                ProbNum += 1

# Following generates several hundred test cases of 10 different wffs at each size
# and from 4 to 22 variables, 10 to 240 clauses, and 2 to 10 literals per clause 
TestCases=[
    [4,10,2,10],
    [8,16,2,10],
    [12,24,2,10],
    [16,32,2,10],
    [18,36,2,10],
    [20,40,2,10],
    [22,44,2,10],
    [24,48,2,10],
    [4,20,3,10],
    [8,40,3,10],
    [12,60,3,10],
    [16,80,3,10],
    [18,90,3,10],
    [20,100,3,10],
    [22,110,3,10],
    [24,120,3,10],
    [4,40,4,10],
    [8,80,4,10],
    [12,120,4,10],
    [16,160,4,10],
    [18,180,4,10],
    [20,200,4,10],
    [22,220,4,10],
    [24,240,4,10],
    [4,40,5,10],
    [8,80,5,10],
    [12,120,5,10],
    [16,160,5,10],
    [18,180,5,10],
    [20,200,5,10],
    [22,220,5,10],
    [24,240,5,10],
    [4,40,6,10],
    [8,80,6,10],
    [12,120,6,10],
    [16,160,6,10],
    [18,180,6,10],
    [20,200,6,10],
    [22,220,6,10],
    [24,240,6,10]]

TC2=[
    [4,10,2,10],
    [8,16,2,10],
    [12,24,2,10],
    [16,32,2,10],
    [18,36,2,10],
    [4,10,3,10],
    [8,16,3,10],
    [12,24,3,10],
    [16,32,3,10],
    [18,36,3,10],
    [4,10,4,10],
    [8,16,4,10],
    [12,24,4,10],
    [16,32,4,10],
    [18,36,4,10],
]
# Following generates a bunch of 2 literal wffs
SAT2=[
    [4,9,2,10],
    [8,18,2,10],
    [12,20,2,10],
    [16,30,2,10],
    [18,32,2,10],
    [20,33,2,10],
    [22,38,2,10],
    [24,43,2,10],
    [26,45,2,10],
    [28,47,2,10]
    ]

trace=True
ShowAnswer=True # If true, record evaluation result in header of each wff in cnffile
ProbNum = 3
resultsfile = r'resultsfile'
tracefile = r'tracefile'
cnffile = r'cnffile'# Each of these list entries describes a series of random wffs to generate
summaryfile = 'smartOutput_KeoughKitch'  # Name of the summary output file


#run_cases(TC2,ProbNum,resultsfile,tracefile,cnffile)
#run_cases(SAT2,ProbNum,resultsfile,tracefile,cnffile)
run_cases(TestCases,ProbNum,summaryfile) # This takes a Looong Time!! 40  minutes



                    


    


        
                
            
            
                

            
