import math
a1=input("Type a\n")
b1=input("Type b\n")
c1=input("Type c\n")
a= float(a1)
b= float(b1)
c= float(c1)
i=0
while i!=10:
    print("\n")
    i+=1

D=0
D=b**2-4*a*c
print(f"D={round(D,2)}")
if D<0:
    print('Немає коренів\n')
if D==0:
    x=0
    x=(-b/(2*a))
    print(f"x={x}\n")
if D>0:
    x1=0
    x2=0
    D1=math.sqrt(D)
    x1=((-b+D1)/(2*a))
    x2=((-b-D1)/(2*a))
    print(f"x1={round(x1,2)}\nx2={round(x2,2)}")
    print(f"a={a}")
    print(f"b={b}")
    print(f"c={c}")

    