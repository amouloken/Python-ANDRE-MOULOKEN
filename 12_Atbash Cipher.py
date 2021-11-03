import string
checklist = string.ascii_lowercase
 
 
def cipher(sentence):
    result = ""
    for i in sentence:
        if i == " ":
            continue
        n = len(checklist) - checklist.index(i) - 1
        result += checklist[n]
    print (result)
 
#cipher("gsvjf rxpyi ldmul cqfnk hlevi gsvoz abwlt")
#cipher("the quick brown fox jumps over the lazy dog")
x = (input("Enter letters:" ))
print(cipher(x))
