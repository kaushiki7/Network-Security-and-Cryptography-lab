all=['a','b','c','d','e','f','g','h','i','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
key="monarchy"
text="instruments"
list=[]
mat=[]
print("Roll No. 161210025")
#append key elements
for i in range(len(key)):
    if key[i]=='j':
        list.append('i')
    if key[i] not in list:
        list.append(key[i])
    if key[i] in all:
        all.remove(key[i])
#append rest alphabets
for i in range(len(all)):
    list.append(all[i])
#print(list)
#converting list into matrix
j=0
k=5
for i in range(5):
    mat.append(list[j:k])
    j=k
    k=k+5
print("Given key :",key)
print("\nUsing Playfair Cipher Method:\n")
print("Matrix formed is ")
for i in range(5):
    for j in range(5):
        print(" ",mat[i][j],end=" ")
    print("\n")

print("Plain Text :",text)
#function to find positions of both letters
pos1,pos2=[],[]
def position(mat,first,sec,cipher):
    pos1,pos2=[],[]
    for i in range(5):
        for j in range(5):
            if mat[i][j]==first:
                pos1.append(i)
                pos1.append(j)
            if mat[i][j]==sec:
                pos2.append(i)
                pos2.append(j)
    #print(first,sec)
    cipher=rules(mat,pos1,pos2,cipher)
    return cipher
#rules
def rules(mat,pos1,pos2,cipher):
    new_pos1,new_pos2=[],[]
    if pos1==pos2:  #same element
        new_pos1=pos1
        new_pos2=pos2
    elif pos1[0]==pos2[0]: #same row
        new_pos1.append(pos1[0])
        new_pos2.append(pos2[0])
        if pos1[1]==4:
            new_pos1.append(0)
        else:
            new_pos1.append(pos1[1]+1)
        if pos2[1]==4:
            new_pos2.append(0)
        else:
            new_pos2.append(pos2[1]+1)
    elif pos1[1]==pos2[1]:  #same
        if pos1[0]==4:
            new_pos1.append(0)
        else:
            new_pos1.append(pos1[0]+1)
        if pos2[0]==4:
            new_pos2.append(0)
        else:
            new_pos2.append(pos2[0]+1)
        new_pos1.append(pos1[1])
        new_pos2.append(pos2[1])
    elif pos1[0]!=pos2[0] and pos1[1]!=pos2[1]:#different row, different column
        new_pos1.append(pos1[0])
        new_pos1.append(pos2[1])
        new_pos2.append(pos2[0])
        new_pos2.append(pos1[1])
    a=mat[new_pos1[0]][new_pos1[1]]
    b=mat[new_pos2[0]][new_pos2[1]]
    cipher+=a+b
    return cipher

def encrypt(text):
    if len(text)%2!=0:
        text+='x'               #append X
    cipher=""
    for i in range(0,len(text),2):
        cipher=position(mat,text[i],text[i+1],cipher)       #passing pairs
    print("Encrypted text :",cipher)


encrypt(text)
