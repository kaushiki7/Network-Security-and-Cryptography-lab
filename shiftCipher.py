plain="qyfwigy"
key=6
cipher=""
print("Roll No. 161210025")
print("Key :",key)
print("Plain Text :",plain)
#Encryption
print("\nUsing Shift Cipher Method\n")

for i in range(len(plain)):
    j=ord(plain[i])%96
    if (j+key)%26!=0:
        j=((j+key)%26)+96
    else:
        j=26+96
    cipher+=chr(j)
print("Encrypted Text :",cipher)

#Decryption
plain=""
for i in range(len(cipher)):
    j=ord(cipher[i])%96
    if j<key:
        j=j-key+26+96
    else:
        j=j-key+96
    plain+=chr(j)
print("Decrypted Text :",plain)
