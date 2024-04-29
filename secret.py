def encryption():
    a=input("Enter the message you want to encrypt")
    words=a.split(" ")
    joined=[]
    print(words)
    
    for word in words:
        if len(word)==1:
           word=word[0]
           joined.append(word)

         
        elif len(word)==2:
            word=word[1]+word[0]
            joined.append(word)
            
        


        else:
            random1="sdx"
            random2="trj"
            word=random1+word[1:]+word[0]+random2
            
            joined.append(word)
    print(" ".join(joined))

def decryption():
    dec=[]
    a=input("Enter encrypted message here:")
    words=a.split(" ")
    for word in words:

        if len(word)>=3:
            anew=word[3:-3]
            decoded=anew[-1]+anew[:-1]
            dec.append(decoded)
            
        else:
            dec.append(word[::-1])
    print(" ".join(dec))
            
          
            

            


print("Hi there! this is a secret message encryption and decryption service.")
service=int(input("Press 1 for a secret message encryption or press 2 for secret message decryption"))
if service==1:
    encryption()
elif service==2:
    decryption()
else:
    print("Invalid input! Please enter either 1 or 2")


