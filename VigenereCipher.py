plain="DONT BUNK LAB CLASS"
key="NITDELHI"
cipher=""
c=len(plain)-len(key)
n_key=key
decrypt=""
j=0

for i in range(len(plain)):
    j=0
    if plain[i]==" ":
        n_key+=plain[i]
    else:
        n_key+=key[j]
        j=j+1

#for i in range(c):
#    n_key+=key[i]

print("Plain Text: ",plain)
print("Extended key: ",n_key)  #Extended key

for i in range(len(plain)):
    n=0
    if plain[i]==" ":
        cipher+=" "
    else:
        n=((ord(plain[i])+ord(n_key[i]))%26)+65
        cipher+=chr(n)

print("Encrypted Text: ",cipher)

for i in range(len(cipher)):
    n=0
    if cipher[i]==" ":
        decrypt+=" "
    else:
        n=(((ord(cipher[i])-ord(n_key[i]))+26)%26)+65
        decrypt+=chr(n)
print("Decrypted Text: ",decrypt)
print()
