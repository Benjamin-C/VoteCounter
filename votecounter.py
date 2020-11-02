# ----------------------------
# ╔═╗┌─┐┌┬┐┬ ┬┌─┐
# ╚═╗├┤  │ │ │├─┘
# ╚═╝└─┘ ┴ └─┘┴
# ----------------------------
import sys
true = True
false = False
# Class candidate
class candidate:
    def __init__(self, name, votes):
        self.name = name
        self.votes = votes
        self.rank = -1
    def __repr__(self):
        return self.name + "[" + str(self.votes) + "]{" + str(self.rank) + "}"

# Sort the candidates by rank
def sort(candidates):
    loc = 0
    while loc+1 < len(candidates):
        if candidates[loc].rank > candidates[loc+1].rank:
            temp = candidates[loc]# Need to switch
            candidates[loc] = candidates[loc+1]
            candidates[loc+1] = temp
            loc = 0
        else:
            loc += 1

# ----------------------------
# ╔╦╗┌─┐┬┌┐┌
# ║║║├─┤││││
# ╩ ╩┴ ┴┴┘└┘
# ----------------------------
if len(sys.argv) < 1:
    print("Please specify an action gen, count, or help")
    exit();
if sys.argv[1] == "help":
    print("Vote Counter v1.0 by Benjamin Crall")
    print("Simple script to count ranked votes")
    print("Usage:")
    print("\tpython votecounter.py <count|gen|help>")
    print("\tpython votecounter.py count <source> [dest]")
    print("\tpython votecounter.py gen <count> <dest>")
    print("Function:")
    print("\tThis script counts ranked votes by eliminating the lease favorite candidate.")
    print("\tEach round, each voters' first choices are counted, and the candidate with")
    print("\tthe least votes is eliminated from the pool. Any vote for them is removed from")
    print("\tthe vote pool, sliding subsequent votes up. This is repeated until there are")
    print("\tno candidates left, and the reults are then printed and optionally saved to")
    print("\ta file.")
    print("File Format:")
    print("\tThe script expects and saves votes in a comma seperated value (.csv) file format,")
    print("\twhere each line represents one voter, with their ordered list of candidates")
    print("\tin orderof 1st,2nd,3rd... choices. Candidates are seperated by commas only,")
    print("\t not spaces. The list of candidates is generated automatically by gathering")
    print("\tany name that was voted for. The output of the counter is in a human-readable")
    print("\ttext format listing the places one per line with any candidates in that place")
    print("\tincluding ties on that line")
    print("Author")
    print("\tThis script was written by Benjamin Crall with the help of the kind people of")
    print("\tthe internet. Contact me at bencrall@gmail.com")
elif sys.argv[1] == "gen":
    # ----------------------------
    # ╔═╗┌─┐┌┐┌┌─┐┬─┐┌─┐┌┬┐┌─┐
    # ║ ╦├┤ │││├┤ ├┬┘├─┤ │ ├┤
    # ╚═╝└─┘┘└┘└─┘┴└─┴ ┴ ┴ └─┘
    # ----------------------------
    # Stop the program if there are not enough args
    if len(sys.argv) < 4:
        print("Please specify a count and a file")
        exit()
    import random
    import copy
    opts = ['Rose', 'Bob', 'Jane', 'Joe', 'Samantha', 'Bill', 'Sally', 'Fred']
    res = ""
    for x in range(int(sys.argv[2])):
        if x > 0:
            res += "\n"
        tmp = copy.deepcopy(opts)
        first = true
        while len(tmp) > 0:
            if first:
                first = False
            else:
                res += ","
            ran = random.randrange(len(tmp))
            res += tmp[ran]
            tmp.remove(tmp[ran])
    with open(sys.argv[3], 'w') as file:
        file.write(res)
    print("Generated " + sys.argv[2] + " votes to " + sys.argv[3])
    exit()
elif sys.argv[1] == "count":
    # ----------------------------
    # ╔═╗┌─┐┬ ┬┌┐┌┌┬┐
    # ║  │ ││ ││││ │
    # ╚═╝└─┘└─┘┘└┘ ┴
    # ----------------------------
    if len(sys.argv) < 3:
        print("Please specify a file with votes")
        exit();
    # Only continue if a vote file has been selected
    # Import the list of votes
    import csv
    votes = list(csv.reader(open(sys.argv[2])))
    # Generate the list of candidates
    candidates = []
    for reccord in votes:
        for element in reccord:
            if not (any(x.name == element for x in candidates)):
                candidates.append(candidate(element, 0))
    # Add up all votes
    rank = 0
    while any(x.rank < 0 for x in candidates):
        # Count votes per candidate
        for reccord in votes:
            for can in candidates:
                if len(reccord) > 0 and can.name == reccord[0] and can.rank < 0:
                    can.votes += 1
        # Find what the least votes is
        min = len(votes)+1
        for can in candidates:
            if can.rank < 0 and can.votes < min:
                min = can.votes
        # Find who has the least votes
        for can in candidates:
            if can.votes == min:
                can.rank = rank
        # Remove them from the votes
        for can in candidates:
            if can.rank == rank:
                for reccord in votes:
                    try:
                        reccord.remove(can.name)
                    except ValueError:
                        null = 0;
        # Reset votes on remaining candidates
        for can in candidates:
            if can.rank < 0:
                can.votes = 0
        # Go to the next rank
        rank += 1
    # Show the results
    print("Winning order:")
    # Switch rank values from first eliminated to first winner
    for can in candidates:
        can.rank = rank - can.rank
    # Generate nice output string
    sort(candidates)
    sout = "\t"
    for i in range(len(candidates)):
        can = candidates[i]
        if i-1 >= 0 and can.rank == candidates[i-1].rank:
            sout += ", " + can.name
        else:
            if i != 0:
                sout += "\n\t"
            sout += str(can.rank)
            if can.rank == 1:
                sout += "st"
            elif can.rank == 2:
                sout += "nd"
            elif can.rank == 3:
                sout += "rd"
            else:
                sout += "th"
            sout += ": " + can.name
    # Show the nice output string
    print(sout)
    if len(sys.argv) >= 4:
        with open(sys.argv[3], 'w') as file:
            file.write(sout.replace("\t", ""))
        print("Results saved to " + sys.argv[3])
    exit()
else:
    print("Please specify an action gen, count, or help")
