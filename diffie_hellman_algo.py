from random import getrandbits
from random import randint
import sys


def is_prime_calc(num):
    return all(num % i for i in range(2, num))


def is_prime(num):
    return is_prime_calc(num)


def get_random_prime():
    while True:
        n = getrandbits(12) + 3
        if is_prime(n):
            return n


def gcd(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a


def primitive_root(modulo):
    required_set = set(num for num in range(
        1, modulo) if gcd(num, modulo) == 1)
    for g in range(1, modulo):
        actual_set = set(pow(g, powers) %
                         modulo for powers in range(1, modulo))
        if required_set == actual_set:
            return g


alice_private = int(input("enter alice private key"))
print('Alice private key is {}'.format(alice_private))
bob_private = int(input("enter bob private key"))
print('Bob private key is {}'.format(bob_private))
p = int(input("enter prime number"))
print('primitive root is {}'.format(primitive_root(p)))
g = primitive_root(p)
print('p parameter is {}, g parameter is {}'.format(p, g))
alice_public = pow(g, alice_private) % p
bob_public = pow(g, bob_private) % p
print('Alice public key is {}'.format(alice_public))
print('Bob public key is {}'.format(bob_public))
alice_key = (pow(bob_public, alice_private)) % p
bob_key = (pow(alice_public, bob_private)) % p
print('Common secret: {} == {}'.format(alice_key, bob_key))
