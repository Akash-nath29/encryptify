def encrypt(userInput):
        """
        This function takes in a string and returns an encrypted version. First it iterets over all the items in the user input, then for each String Character it returns a binary digit. Then it converts those binary digits based on the logic defined below and returns '.' for each '1' and ' ' for each '0'
        """
        binary = ''.join(format(ord(c), '08b') for c in userInput)
        text = ""
        for bit in binary:
            if bit == '1':
                text += "."
            elif bit=='0':
                text += " "
            else:
                return TypeError
        print(text)
        
userQuery = input("Enter the words: ")
encrypt(userQuery)