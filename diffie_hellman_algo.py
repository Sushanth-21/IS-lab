p,g=map(int,input("Enter values for public keys : ").split())
a,b=map(int,input("Enter values for private keys : ").split())
x=(g**a)%p
y=(g**b)%p
ka=(y**a)%p
kb=(x**b)%p
print("{} {} are the secret keys.".format(ka,kb))