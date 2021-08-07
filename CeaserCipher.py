def ceaserEncrypt(plainText, shiftKey) : 

    cipherText = plainText.upper() # convert plaintext to uppercase. It will make it easier to use unicode numbers afterwards.
    encryptedText = ""

    for c in cipherText :
        
        if c.isupper() :
            #get unicode and index for each letter in text.
            c_unicode = ord(c) # get the unicode for each of the charachters in the ciphertext
            c_index = c_unicode - ord("A") # get the index of each charachter in the alphabet for each of the charachters in the ciphertext

            e_newIndex = (c_index + shiftKey) % 26  #perform the shift using the shiftKey and mod 26 to stay within range of alphabet.
            e_newUnicode = e_newIndex + ord("A") #get unicode for new charachter
            
            e_charachter = chr(e_newUnicode)
            encryptedText += e_charachter
        
        else : 
            encryptedText += c # if character is not upper case, just return the character unchanged.
        
    print(encryptedText)


def ceasarDecrypt(codedText, shiftKey) :
    
    encrypt_text = codedText.upper() # convert coded text to uppercase. It will make it easier to use unicode numbers afterwards.

    decryptedText = ""

    for c in encrypt_text :

        if c.isupper() :
            c_unicode = ord(c) # get the unicode for each of the charachters in the encrypted text
            c_index = c_unicode - ord("A") # get the index of each charachter in the alphabet for each of the charachters in the ciphertext

            d_newIndex = (c_index - shiftKey) % 26
            d_newUnicode = d_newIndex + ord("A")

            d_charachter = chr(d_newUnicode)
            decryptedText += d_charachter

        else : 
            decryptedText += c # if character is not upper case, just return the character unchanged.

    print(decryptedText)


def hackCeasarDecrypt(codedText) : #function to be used when shiftkey is not known
    
    encrypt_text = codedText.upper() # convert coded text to uppercase. It will make it easier to use unicode numbers afterwards.
    shiftKey = 0
    decryptedText = ""
    my_dict = {}
    
    while shiftKey <= 26 : # iterate through total numbers in alphabet.
        for c in encrypt_text :

            if c.isupper() :
                c_unicode = ord(c) # get the unicode for each of the charachters in the encrypted text
                c_index = c_unicode - ord("A") # get the index of each charachter in the alphabet for each of the charachters in the ciphertext

                d_newIndex = (c_index - shiftKey) % 26
                d_newUnicode = d_newIndex + ord("A")

                d_charachter = chr(d_newUnicode)
                decryptedText += d_charachter

            else : 
                decryptedText += c # if character is not upper case, just return the character unchanged.

            my_dict[shiftKey] = decryptedText
        
        shiftKey +=1 #add 1 to the shiftkey
        decryptedText ="" # clear the string after use

    print(my_dict)



