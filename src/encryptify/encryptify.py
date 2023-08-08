"""
This module implements the main functionality of encryption of data.

Author: Akash Nath
Website: https://tinyurl.com/akash-nath

"""

__author__ = "Akash Nath"
__email__ = "anath5440@gmail.com"

class Encryptify:
    """
    This class has the main functionality for the encryption and decryption.
    
    Requirements: user input (data-type independent)
    """
    def __init__(self, userInput):
        self.userInput = userInput
        
    def encrypt(self):
        """
        This function takes in a string and returns an encrypted version. First it iterets over all the items in the user input, then for each String Character it returns a binary digit. Then it converts those binary digits based on the logic defined below and returns '.' for each '1' and ' ' for each '0'
        """
        binary = ''.join(format(ord(c), '08b') for c in self.userInput)
        for bit in binary:
            if bit == '1':
                return "."
            elif bit=='0':
                return " "
            else:
                return TypeError
            
    def decrypt(self):
        """
        This function takes in a string and returns its decrypted form. It takes the encrypted text from user (with '.' and ' ' only, other inputs will raise TypeError) and converts them based on the logic defined below and returns the actual text. 
        """
        # ensures user given data is binary ↓↓
        userData = []
        for x in self.userInput:
            if x=='.' or x==' ':
                userData.append(x)
            else:
                return TypeError
        
        #converts all the dots and spaces into binary ↓↓
        decrypted_binary = ""
        for i in userData:
            if i=='.':
                decrypted_binary += '1'
            else:
                decrypted_binary += '0'
                
        #binary to string convertion
        binary_data = list(decrypted_binary)
        decrypted_text = ""
        while binary_data:
            byte = "".join(binary_data[:8])
            binary_data = binary_data[8:]
            decrypted_text += chr(int(byte, 2))
        
        return decrypted_text
        
        