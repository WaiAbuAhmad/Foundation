if __name__ == '__main__':
    s = input()

alphanumeric =False
alphabetical= False
digits = False
lowercase = False
uppercase= False

for letter in s :
   alphanumeric =alphanumeric or letter.isalnum()
   alphabetical= alphabetical or letter.isalpha()
   digits = digits or letter.isdigit()
   lowercase = lowercase or letter.islower() 
   uppercase= uppercase or letter.isupper() 
print(alphanumeric)
print(alphabetical)
print(digits)
print(lowercase)
print(uppercase)
    