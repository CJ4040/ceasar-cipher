def ceaserEncrypt(plainText, shiftKey) : 

    cipherText = plainText.upper() # convert plaintext to uppercase. It will make it easier to use unicode numbers afterwards.
    encryptedText = ""

    for c in cipherText :
        
        if c.isupper() :
            #get unicode and index for each letter in text.
            c_unicode = ord(c) # get the unicode for each of the charachters in the ciphertext
            c_index = ord(c) - ord("A") # get the index of each charachter in the alphabet for each of the charachters in the ciphertext

            e_newIndex = (c_index + shiftKey) % 26  #perform the shift using the shiftKey and mod 26 to stay within range of alphabet.
            e_newUnicode = e_newIndex + ord("A") #get unicode for new charachter
            
            e_charachter = chr(e_newUnicode)
            encryptedText += e_charachter
        
        else : 
            encryptedText += c # if character is not upper case, just return the character unchanged.
        
    print(encryptedText)



