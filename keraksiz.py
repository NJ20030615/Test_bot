def new_test(file_name):
    
    file = open(file_name, "r")
    
    savol= []
    A=[]
    B=[]
    C=[]
    D=[]
    E=[]
    # write to console
    for line in file:
        if line.startswith(" "):
            savol.append(line)
        elif line.startswith("A"):
            A.append(line)
        elif line.startswith("B"):
            B.append(line)
        elif line.startswith("C"):
            C.append(line)
        elif line.startswith("D"):
            D.append(line)
        elif line.startswith("E"):
            E.append(line)
    file.close()
    
    questions = []
    
    for i in range(len(savol)):
        question = []
        question.append(savol[i])
        question.append([A[i][:-2], A[i][-2]])
        question.append([B[i][:-2], B[i][-2]])
        question.append([C[i][:-2], C[i][-2]])
        question.append([D[i][:-2], D[i][-2]])
        question.append([E[i][:-2], E[i][-2]])
        questions.append(question)
    
    return questions

def length():
    return len(new_test("baza.txt"))-1

print((new_test("baza2.txt")))
print(length())
# tests = new_test("baza.txt")
#
# for i in range(len(tests)):
#     print(tests[i][0])
#     print(tests[i][1])
#     print(tests[i][2])
#     print(tests[i][3])
#     print(tests[i][4])
#     print(tests[i][5])
#     print("\n")

# x=0
# for i in tests:
#     x += 1
#     print(x,i)
#
# print(len(tests))
# while len(tests) < 5:
#     if randint(0, 11) not in tests:
#         tests.append(test_number)

