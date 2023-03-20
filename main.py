def DFA(cuvant,stare):
    global ok
    ok=0
    if cuvant=="" and stare in final:
        ok=1
    elif cuvant!="" and ok==0:
        for x in M[:len(M)-1]:
            if x[1]==cuvant[:1] and x[0]==stare:
                S.append(x[2])
                DFA(cuvant[1:],x[2]);

f=open("tastatura.txt")
M=[line.split() for line in f.readlines()]
final=M[len(M)-1]
cuvant=input("Cuvantul citit este ")
initial=M[0][0]
S=[initial]
ok=0
for x in M[:len(M)-1]:
    if x[0]==initial and x[1]==cuvant[:1]:
        S.append(x[2])
        DFA(cuvant[1:],x[2])
    elif cuvant=="" and final.count(initial)==1:
        ok=1
if ok==1:
    print("acceptat")
    print("Drumul este ",end="")
    for x in S[:len(S)-1]:
        print(x,"->",end=" ")
    print(S[len(S)-1])
else:
    print("neacceptat")
