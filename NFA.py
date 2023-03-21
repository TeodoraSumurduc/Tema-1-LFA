def NFA(cuvant,stare):
    global D,Drumuri,k
    if cuvant=="" and stare in final:
        Drumuri.append(D)
        Drumuri[len(Drumuri)-1].append("acceptat")
    elif cuvant=="":
        Drumuri.append(D)
    elif cuvant!="":
        for x in N:
            if x[1]==cuvant[:1] and x[0]==stare:
                for j in x[2]:
                    D.append(j)
                    k+=1
                    NFA(cuvant[1:],j)
                    D=D[:-1]
                    k-=1
                    if k!=0:
                        D=D[:-k]
f=open("input.txt")
M=[line.split() for line in f.readlines()]
N=[[M[0][0],M[0][1],[M[0][2]]]]
final=M[len(M)-1]
initial=M[0][0]
s=M[0][0]
a=M[0][1]
j=0
for i in range(1,len(M)-1):
    if M[i][0]==s and M[i][1]==a:
        N[j][2].append(M[i][2])
    elif M[i][0]==s:
        N.append([M[i][0],M[i][1],[M[i][2]]])
        a=M[i][1]
        j+=1
    else:
        s=M[i][0]
        a=M[i][1]
        N.append([M[i][0],M[i][1],[M[i][2]]])
        j+=1
cuvant=input("Cuvantul citit este ")
Drumuri=[]
D=[]
for x in N:
    if x[0]==initial and x[1]==cuvant[:1]:
        D=[x[0]]
        for j in x[2]:
            D.append(j)
            k=0
            NFA(cuvant[1:],j)
            D=[x[0]]
for d in Drumuri:
        for x in d[:-1]:
            print(x,"->",end="")
        print(d[-1])
