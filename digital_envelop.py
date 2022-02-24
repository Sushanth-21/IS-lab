from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii
from cryptography.fernet import Fernet

message = input("enter plain text:")
key = Fernet.generate_key()
print("key is:", end=" ")
print(key)
fernet = Fernet(key)
encMessage = fernet.encrypt(message.encode())
print("original string: ", message)
print("CipherText: ", encMessage)


keyPair = RSA.generate(1024)
pubKeyB = keyPair.publickey()
pubKeyPEMB = pubKeyB.exportKey()

print("")

print(pubKeyPEMB.decode('ascii'))
privKeyPEMB = keyPair.exportKey()

print("")

print(privKeyPEMB.decode('ascii'))

msg = bytes(str(key), 'utf-8')

encryptor = PKCS1_OAEP.new(pubKeyB)

encrypted = encryptor.encrypt(msg)

EncryptedKey = binascii.hexlify(encrypted)
print(" Encrypted  key with public key B:", binascii.hexlify(encrypted))

digitalenvelope = encMessage+EncryptedKey
print(digitalenvelope)
decryptor = PKCS1_OAEP.new(keyPair)

decrypted = decryptor.decrypt(encrypted)

print('Decrypted key is:', decrypted.decode('utf-8'))
decryptedkey = decrypted.decode('utf-8')

if(str(key) == str(decryptedkey)):
    print("both keys matched")
else:
    print("both keys not matched")

decMessage = fernet.decrypt(encMessage).decode()

print("decrypted string: ", decMessage)
