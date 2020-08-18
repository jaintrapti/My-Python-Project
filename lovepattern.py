str1 = "LOVE"
print__L = [[" " for i in range(5)] for j in range(5)]
print__O = [[" " for i in range(5)] for j in range(5)]
print__V = [[" " for i in range(5)] for j in range(5)]
print__E = [[" " for i in range(5)] for j in range(5)]


#code for L
for i in range(5):
    for j in range(5):
        if j==0 or (i==4 and j>0):
            print__L[i][j]= "*"

#code for O          
for i in range(5):
    for j in range(5):
        if(j==0 or j==4) and (i!=0 and i!=4) or (i==0 or i==4) and (j>0 or j<4):
            print__O[i][j]= "*"


#code for V           
for i in range(5):
    for j in range(5):
        if ((i==0 and j==0) or (i==2 and j==1) or (i==4 and j==2) or (i==2 and j==3) or (i==0 and j==4)):
            print__V[i][j]= "*"

#code for E           
for i in range(5):
    for j in range(5):
        if j==0 or ((i==0 or i==2 or i==4) and (j>0)):
            print__E[i][j]= "*"
              
for i in range(5):
    for j in range(5):
        print(print__L[i][j],end=" ")
    print(end="  ")
    for j in range(5):
        print(print__O[i][j],end=" ")
    print(end="  ")
    for j in range(5):
        print(print__V[i][j],end=" ")
    print(end="  ")
    for j in range(5):
        print(print__E[i][j],end=" ")
    print()   
