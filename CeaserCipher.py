def ceaserEncrypt(plainText, shiftKey) : 
    alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    cipherText = ""
   
    for letter in alpha[:shiftKey] : #start from shift key and iterate over charachter
        alpha.remove(letter) #remove characters from list
        alpha.append(letter) #append leftover characters to get new alphabet

    for char in plainText :
        letterPos = ord(char)-97
        if letterPos < 0 : # spaces will return negative unicode numbers. If negative, print a space.
            cipherText += " "
            #print(" ")
        else :
            cipherText += alpha[letterPos]
            #print (alpha[letterPos])

    return (cipherText)

