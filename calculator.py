a,b = input("enter two element\n").split(",")
c = input("choose the opretor press\n1 for plus\n2 for subtation\n")
if c == '1':
    print("sum of element is:",int(a)+int(b))
elif c == '2':  
    print("substation of element is:",int(a)-int(b) )
else:
    print("wront input")