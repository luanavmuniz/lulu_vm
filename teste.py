print("A senha deve conter letras e números, deve ter pelo menos ujma letra maiúscula e uma minúscula e conter ao menos um caractere especial.")

senha = input("Digite a senha: ")

if len(senha) < 8:
  print(senha)
  if senha.isalnum():
    print("A senha deve conter pelo menos um caractere especial.")
    if senha.isupper():
      print("A senha deve conter pelo menos uma letra maiúscula.")
      if senha.isolwer():
        print("A senha deve conter pelo menos uma letra minúscula.")
        if senha.isdigit():
          print("A senha deve conter pelo menos um número.")
        else:
          print("A senha está correta.") 
          senha=input("Digite a senha novamente: ")
      else:
        print("A senha deve conter letras e numeros")
        senha=input("Digite a senha novamente: ")
    else:
      print("A senha deve conter letras e números")
      senha=input("Digite a senha novamente: ")
  else:
    print("A senha deve conter apenas letras e números")
    senha=input("Digite a senha novamente: ")
else:
  print("A senha deve conter pelo menos 8 caracteres")
  senha=input("Digite a senha novamente: ")
  
  
   