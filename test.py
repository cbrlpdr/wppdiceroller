from random import randint

entrada = input(">")
entrada = entrada.strip()
mod=0
posD=entrada.find('d')
#print(posD)
q=int(entrada[0:posD])
t=entrada[posD+1:(len(entrada))]

for c in t:
    if((not c.isnumeric()) and c!='+' and c!='-'):
        t=t.replace(c,'')
        
    

if("+" in t):
    posSinal=t.find("+")
    mod=int(t[posSinal+1:len(t)])
    print(mod)
    t=int(t[0:posSinal])
elif ("-" in t):
    posSinal=t.find("-")
    mod=int(t[posSinal+1:len(t)])*(-1)
    print(mod)
    t=int(t[0:posSinal])


print(q)
t=int(t)
print(t)

mensagem = "Resultado: ("
res=0
for i in range(q):
    roll=randint(1,t)
    mensagem+=str(roll) + " "
    res+=roll
mensagem+=")"
mensagem=mensagem.replace(" )",")")
if(mod!=0):
    if(mod>0):
        mensagem+=" + " + str(mod)
    else:
        mensagem+=" - " + str(abs(mod))
    
    res+=mod

mensagem+=" = " + str(res)
print(mensagem)

