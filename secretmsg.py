print("ENCRYPTION & DECRYPTION")

input("Press \'y\' to start : ")
#ENCRYPTION

alphabets = 'abcdefghijklmnopqrstuvwxyz'

key = int(input("enter a key for encryption(number only) : "))

msg = input("enter the message you want to encrypt : ")

emsg = ''

character = ' '

newCharacter = ''

for character in msg:
    
	if character in alphabets:
            
		position = alphabets.find(character)
		newPosition = (position + key) % 26
		newCharacter = alphabets[newPosition]
		emsg += newCharacter
	else :
            
		emsg += character
		
print("encrypted message is :", emsg)


#DECRYPT

alphabets = 'abcdefghijklmnopqrstuvwxyz'

key = int(input("enter a key for decryption(number only) : "))

msg = input("enter the message you want to decrypt : ")

emsg = ''

character = ' '

newCharacter = ''

for character in msg:
    
	if character in alphabets:
            
		position = alphabets.find(character)
		newPosition = (position - key) % 26
		newCharacter = alphabets[newPosition]
		emsg += newCharacter
	else :
            
		emsg += character
		
print("decrytpted message is :", emsg)

input("Press \'x\' to exit : ")

