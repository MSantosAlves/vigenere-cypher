import string

class Vigenere:
  
  def __init__(self):
    self.__alphabet = string.ascii_uppercase
    self.__table = []

    for i in range(len(self.__alphabet)):
      row = self.__alphabet[i:] + self.__alphabet[:i]
      self.__table.append(row)

  def cipher_message(self, message, key):

    cipher = ""
    key = (key * (len(message)//len(key) + 1))[:len(message)]
    key_iterator = 0
    
    for i in range(len(message)):
      row = self.__ascii_to_table_index(key[key_iterator])
      col = self.__ascii_to_table_index(message[i])
      accents = ['á', 'à', 'ã', 'â', 'é', 'ê', 'í', 'ó', 'ô', 'õ', 'ú', 'ü', 'ç']
      if message[i].isalpha():
        if message[i].lower() in accents:
            cipher += message[i].lower()
        else:
          cipher += self.__table[row][col] if message[i].isupper() else self.__table[row][col].lower()
          key_iterator += 1
      else:
        cipher += message[i]
    return cipher

  def decipher_message(self, cipher, key):
    message = ""
    key = (key * (len(cipher)//len(key) + 1))[:len(cipher)]
    key_iterator = 0
    accents = ['á', 'à', 'ã', 'â', 'é', 'ê', 'í', 'ó', 'ô', 'õ', 'ú', 'ü', 'ç']
    
    for i in range(len(cipher)):
      row = self.__ascii_to_table_index(key[key_iterator])
      if cipher[i].isalpha():
        if cipher[i].lower() in accents:
            message += cipher[i].lower()
        else:
            col = self.__table[row].index(cipher[i].upper())
            key_iterator += 1
            message += self.__alphabet[col] if cipher[i].isupper() else self.__alphabet[col].lower()
      else:
        message += cipher[i]
    return message

  def __ascii_to_table_index(self, letter):
    return ord(letter.upper()) - ord('A')