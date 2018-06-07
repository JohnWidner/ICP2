"""
John Widner
06-07-18
"""
"""Problem 1"""
L1 = ["a", "list", "of", "strings"]
L2 = []
print("The longest in the list is " + str(len(max(L1))) + " which is " + str(max(L1)))

listlen = len(L1)
i = 0
while i < listlen:

    L2.append(str(len(L1[i])) + ", " + L1[i])
    i += 1

print(L2)

"""Problem 2"""

infile = open('inpt.txt')
outfile = open('outpt.txt', "w")
line = infile.readline()

while line != "":
    outfile.write(str(len(line)) + " " + str(line))
    line = infile.readline()

infile.close()
outfile.close()

"""Problem 3"""

infile2 = open('inpt2.txt')
line = infile2.readline()
list2 = []
while line != "":
    list2.append(list(line.split()))
    line = infile2.readline()
for lst in list2:
    s = ""
    for l in lst:
        s = s + " " + l
    print(s + " " + str(len(lst)))
print(list2)
infile2.close()

"""Problem 4"""

top = "---"
side = "|   |"

x = int(input("what length?"))
y = int(input("what height?"))
top_b = ""
side_b = ""
for i in range(x):
    top_b = top + "   " + top_b
    side_b = side + side_b
for j in range(y):
    print(top_b)
    print(side_b)
    print(top_b)
