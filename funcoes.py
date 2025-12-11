"""def nomes_deles(nome):

    return  f"Olá {nome}"
print(nomes_deles("Jorge"))"""

"""def soma(a,b):
    return a+b
result = soma(3,4)
print(f"A soma é :{result}")"""


"""def saudacao():
    print("Jorge você é muito bom")
saudacao()"""

users =[
  {
    "id": 1,
    "name": "Aureliano Nunes",
    "funcao": "TI",
    "idade": "22",
    "password": "Nunes"
  },
   {
  "id": 2,
  "name": "Jorge C. Nunes",
  "funcao": "TI",
  "idade": "19",
  "password": "Todos"
}
]

qualquer_nome = input("Digite seu nome: ")
qualquer_senha = input("Digite sua senha: ")

def nome_aluno(nome):
    return nome
for nome in users:
  if qualquer_nome == users[0]["name"]:  
        if qualquer_senha == users[0]["password"]: 
         print("Você pode acessar")
        break        
  else:
    print("Você não pode acessar")
    break
#print("Seu nome é:", qualquer_nome)
nome_aluno(qualquer_nome)

"""name_user= ["Jorge", "Ana", "Maria", "João"]
password_user= ["1234", "5678", "abcd", "efgh"]

qualquer_nome = input("Digite seu nome: ")
qualquer_senha = input("Digite sua senha: ")

def nome_aluno(nome):
    return nome
for nome in name_user:
  if qualquer_nome == nome:
    for senha in password_user:
      if qualquer_senha == senha:
        print("Você pode acessar")
        break
  else:
    print("Você não pode acessar")
    break
#print("Seu nome é:", qualquer_nome)
nome_aluno(qualquer_nome)"""

"""def mensagem():
    return "Olá jorge C. Nunes"
print(mensagem())"""