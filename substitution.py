import string
plain_text=input("Enter plain text : ")
key=int(input("Enter key : "))
d1={}
alpha=string.ascii_letters
n=len(alpha)
for i in range(n):
    d1[alpha[i]]=alpha[(i+key)%n]
encrypt=""
for i in plain_text:
    encrypt+=d1.get(i,i)
d2={}
for i in range(n):
    d2[alpha[i]]=alpha[(i-key)%n]
decrypt=""
for i in encrypt:
    decrypt+=d2.get(i,i)
print("Encrypted text : ",encrypt)
print("Decrypted text : ",decrypt)