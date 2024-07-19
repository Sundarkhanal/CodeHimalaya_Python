S1 = int(input("Enter the marks of English"))
S2 = int(input("Enter the marks of Physics"))
S4 = int(input("Enter the marks of Mathematics"))
S5 = int(input("Enter the marks of Computer Science"))

sum = S1 +S2 +S4+S5
print(sum)
per = (sum/4)
gpa = per/25
print(per)
print(gpa)
if per>89:
    print("Grade A")
elif per>79:
    print("Grade B")
elif per>69:
    print("Grade C")
elif per>59:
    print("Grade D")
elif per>49:
    print("Grade E")
else:
    print("Fail")
