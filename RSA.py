import math
p, q = map(int, input("enter two prime numbers").split())
print('p == {} , q == {}'.format(p, q))
n = p*q
print('n == {}'.format(n))


def phi(p, q):
    return (p-1)*(q-1)


print('phi == {}'.format(phi(p, q)))
e = 2
while e < phi(p, q):
    if math.gcd(e, phi(p, q)) == 1:
        break
    else:
        e += 1
print('e == {}'.format(e))


def compute_d(e, phi):
    d = 1
    while True:
        if (d*e) % phi == 1:
            return d
        else:
            d += 1


print('d == {}'.format(compute_d(e, phi(p, q))))
d = compute_d(e, phi(p, q))
plain_text = int(input("enter plain_text"))
cipher_text = (plain_text**e) % n
print('plain_text == {}'.format(plain_text))
print('cipher_text == {}'.format(cipher_text))
plain_text = (cipher_text ** d) % n
print('plain_text == {}'.format(plain_text))
