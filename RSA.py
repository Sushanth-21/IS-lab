def gcd(a, b):
    while(True):
        t = a % b
        if t == 0:
            return b
        a = b
        b = t


p, q = map(int, input("Enter 2 prime numbers : ").split())
plain = int(input("Enter plain text : "))
n = p*q
e = 2
phi = (p-1)*(q-1)
while(e < phi):
    if gcd(e, phi) == 1:
        break
    e += 1

for k in range(2, phi):
    if gcd(k, phi) == 1:
        break

for i in range(1, 10):
    x = 1 + i*phi
    if x % k == 0:
        d = int(x/k)
        break
c = (plain**e) % n
print("d-{} e-{} phi-{} c-{} n-{}".format(d, e, phi, n))
print("Encrypted message is : ", c)
m = (c**d) % n
print("Decrypted message is : ", m)
