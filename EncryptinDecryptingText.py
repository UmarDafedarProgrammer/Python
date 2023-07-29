alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ','!','@','#','$','%','^','&','*','(',')','0','1','2','3','4','5','6','7','8','9']

Encrypted = []

def encrypt():
  print("Encryption is in Progress...")
  encryptedtext = ""
  for i in range(0,len(text)):
    tmp = ""
    index1 = alphabet.index(text[i])
    tmp = encryptedtext + Encrypted[index1]
    encryptedtext = tmp
  print(f"Encrypted Text is :{encryptedtext}")
    
def decrypt():
  print("Decrypton is in Progress...")
  decryptedtext = ""
  for i in range(0,len(text)):
    tmp = ""
    index1 = Encrypted.index(text[i])
    tmp = decryptedtext + alphabet[index1]
    decryptedtext = tmp
  print(f"Decrypted Text is :{decryptedtext}")
  
def GenerateEncryptionKey():
  for i in range(0,len(alphabet)):
    if i+EncryptionKey > len(alphabet)-1:
      Encrypted.append(alphabet[i+EncryptionKey-len(alphabet)])
    else:
      Encrypted.append(alphabet[i+EncryptionKey])
  
EnDecode = input("Do you want to encode or decode?: ").lower()
text = input("Provide the input text: ").lower()
EncryptionKey = int(input("Provide the encryption Key: "))

GenerateEncryptionKey()

if EnDecode == "encrypt":
  encrypt()
else:
  decrypt()
