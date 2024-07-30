a=[1, 2, 3, 4] 
b=[5, 6, 7, 8]
result1=0
lastresult=0
for i in range(len(a)):
    result1=a[i]*b[i]
    lastresult=result1+lastresult
print(lastresult)
    