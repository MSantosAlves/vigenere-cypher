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
      if message[i].isalpha():
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
            col = self.__table[row].index(self.__handle_especial_chars(cipher[i]))
        else:
            col = self.__table[row].index(cipher[i].upper())
        message += self.__alphabet[col] if cipher[i].isupper() else self.__alphabet[col].lower()
        key_iterator += 1
      else:
        message += cipher[i]
    return message

  def __ascii_to_table_index(self, letter):
    return ord(letter.upper()) - ord('A')

  def __handle_especial_chars(self, esp_char):
    map_accents = {
      'á': 'a',
      'à': 'a',
      'ã': 'a',
      'â': 'a',
      'é': 'e',
      'ê': 'e',
      'í': 'i',
      'ó': 'o',
      'ô': 'o',
      'õ': 'o',
      'ú': 'u',
      'ü': 'u',
      'ç': 'c'
    }

    return map_accents[esp_char.lower()].upper()

  
