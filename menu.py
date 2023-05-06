from vigenere import Vigenere
from decrypter import Decrypter

vigenere = Vigenere()
decrypter = Decrypter()

def Menu():
  print("Bem-vindo(a) ao aplicativo de criptografia!")

  option = -1
  while option != "5":
    print("\nSelecione uma das opções abaixo:")
    print("1 - Cifrar mensagem")
    print("2 - Decifrar mensagem")
    print("3 - Ataque de frequência na cifra de Vigenere para mensagem em português")
    print("4 - Ataque de frequência na cifra de Vigenere para mensagem em inglês")
    print("5 - Sair")

    option = input("Opção selecionada: ")
    if option == "1":
      message = input("Digite a mensagem a ser cifrada: ")
      key = input("Digite a chave para cifragem: ")
      result = vigenere.cipher_message(message, key)
      print("Mensagem cifrada: ", result)
    elif option == "2":
      message = input("Digite a mensagem a ser decifrada: ")
      key = input("Digite a chave para decifragem: ")
      result = vigenere.decipher_message(message, key)
      print("Mensagem decifrada: ", result)
    elif option == "3":
      message = input("Digite a mensagem cifrada: ")
      result = decrypter.get_key(message, "pt-BR")
      print("Chave encontrada para mensagem: ", result)
    elif option == 4:
      message = input("Digite a mensagem cifrada: ")
      result = decrypter.get_key(message, "en-US")
      print("Chave encontrada para mensagem: ", result)

    elif option != "5":
      print("Opção inválida.")