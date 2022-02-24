import math


def encrypt(plain, key):
    cipher = ""
    ind = 0
    lst = list(plain)
    n = len(lst)
    k_lst = sorted(list(key))
    col = len(key)
    row = int(math.ceil(n/col))
    null_val = int((row*col)-n)
    lst.extend("_"*null_val)
    arr = [lst[i:i+col] for i in range(0, n, col)]
    for _ in range(col):
        curr = key.index(k_lst[ind])
        cipher += ''.join([row[curr] for row in arr])
        ind += 1
    return cipher


def decrypt(cipher, key):
    plain = ""
    ind = 0
    m_ind = 0
    lst = list(cipher)
    n = len(lst)
    k_lst = sorted(list(key))
    col = len(key)
    row = int(math.ceil(n/col))
    tmp = []
    for _ in range(row):
        tmp += [[None]*col]
    for _ in range(col):
        curr = key.index(k_lst[ind])
        for j in range(row):
            tmp[j][curr] = lst[m_ind]
            m_ind += 1
        ind += 1
    plain += "".join(sum(tmp, []))
    null_c = plain.count("_")
    if null_c > 0:
        return plain[:-null_c]
    return plain


plain = input("Enter plain text : ")
key = input("Enter key : ")
cipher = encrypt(plain, key)
print("Encrypted message - ", cipher)
print("Encrypted message - ", decrypt(cipher, key))
