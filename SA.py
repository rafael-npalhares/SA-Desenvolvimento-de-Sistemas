pessoas = []
senhas = []

salas = ["Sala do menino mal", "Sala de Reuniao 2", "Auditorio"]
reservas = []
salas_reservadas = []


def selecionar_p():
    global reservas
    a = int(input(f"\nDigite o numero da pessoa que deseja conversar com o menino mal  {len(pessoas)} ):  "))

    mostrar_dicionario(pessoas[a-1])
    return pessoas[a-1]

def selecionar_sala():
    while True:
        sala_selecionada = input(f"\nselecione uma sala.\nsalas: {salas}")
        for i in salas:
            if sala_selecionada.lower() == i.lower():
                return i
    
def selecionar_data():
    data_valida = False
    while not data_valida:
        data = input("\ndigite a data desejada para a reserva (dd/mm/aaaa): ")
        data_valida = validar_data(data)
    return data

def selecionar_horario():
    horario_valido = False
    while not horario_valido:
        hora = input("\ndigite o horario que deseja reservar (formato => hh:mn ex: 13:30)")
        horario_valido = validar_horario(hora)
    return hora

def validar_horario(horario):
    horario.strip()
    horario = horario.split(":")
    if len(horario) > 2:
        return False
    for i in horario:
        if not i.isnumeric():
            return False 
    if int(horario[0]) > 24:
        return False 
    if int(horario[1]) > 59:
        return False 
    return True

def validar_data(data):
    data.strip()
    data = data.split("/")
    dia = int(data[0])
    mes = int(data[1])
    if mes in  [1, 3, 5, 7, 8, 10, 12]:
        return dia <= 31
    if mes in [4, 6, 9, 11]:
        return dia <= 30
    if mes == 2:
        return dia <= 28
    else:
        print("digite uma data válida!")
        return False

def agenda(sala_s = None):
    global reservas
    while True:
        pessoa = selecionar_p()
        reserva = dict()
        reserva["Nome"] = pessoa["Nome"]
        if sala_s == None:
            sala_s = selecionar_sala()           

        if sala_s != salas[0]:
            print("Vc não selecionou a sala certa")
            return 
            
        reserva["Sala"] = sala_s
        data = selecionar_data()
        reserva["Data"] = data
        hora = selecionar_horario()
        reserva["Horario"] = hora

        deuBoa = True
        for sala_reservada in reservas:
            if sala_reservada["Sala"] == reserva["Sala"] and sala_reservada["Data"] == reserva["Data"] and sala_reservada["Horario"] == reserva["Horario"]:
                print("essa sala ja esta reservada nesta data e nesse horario!")
                deuBoa = False
                break                
        
        if deuBoa:
            reservas.append(reserva)
            print(reservas)
            return


def validar_cpf(cpf):
    cpf = cpf.replace(".", "").replace("-", "")
    if len(cpf) != 11 or not cpf.isdigit():
        return False
    
    if cpf == cpf[0] * 11:
        return False

    soma1 = 0
    for i in range(9):
        soma1 += int(cpf[i]) * (10 - i)
    resto1 = (soma1 * 10) % 11
    digito1 = 0 if resto1 == 10 else resto1

    soma2 = 0
    for i in range(10):
        soma2 += int(cpf[i]) * (11 - i)
    resto2 = (soma2 * 10) % 11
    digito2 = 0 if resto2 == 10 else resto2

    return int(cpf[9]) == digito1 and int(cpf[10]) == digito2

def validar_email(email):
    valido = 0
    for i in email:
        if i == "@":
            valido += 1
    if "@" in email:
        testando = email.split("@")
    else: return False
    for i in testando[1]:
        if i == ".":
            valido += 1 
        if valido == 2:
            print("\nemail cadastrado com sucesso!")
            return True
    else:
        print("\no email nao é valido!")
        return False

def validar_idade():
    while True:
        idade = input("\nqual é sua idade? ")
        if idade.strip():
            valido = 0
            for i in idade:
                if i.isnumeric():
                    valido += 1
            if valido == len(idade):
                idade = int(idade)
                if idade > 0 and idade >= 18:
                    return idade
        else: print("\na idade não é valida!")
  
def nome(): 
    while True:
        nome = input("\ndigite o seu nome por favor: ")
        if nome.strip():
            aprovado = True
            nome2 = nome.split(" ")
            for i in nome2:
                for x in i:
                    if x.isnumeric():
                        aprovado = False 
            if aprovado == True:
                return nome
        else : print("\no nome é invalido, digite-o novamente!: ")    

def cep():
    while True:
        cep = input("\ndigite o seu cep por favor: ")
        if cep.strip():
            cep = cep.replace(".", "")
            cep = cep.replace("-", "")
            valido = 0
            for i in cep:
                if i.isnumeric():
                    i = int(i)
                    valido += 1
        if len(cep) == 8:
            if valido == len(cep):
                return cep

def cadastrar_p():
    global pessoas
    nome_individuo = nome()
    idade_individuo = validar_idade()
    cpf = pedir_cpf()
    email_individuo = pedir_email()
    cep_individuo = cep()
    senha = input("\ndigite uma senha de acesso: ")
    pessoa = {
        "Nome" : nome_individuo,
        "Idade" : idade_individuo,
        "CPF" : cpf,
        "Email" : email_individuo,
        "Cep" : cep_individuo
    }
    senhas.append(senha)
    pessoas.append(pessoa)
    return pessoa

def mostrar_dicionario(d):
    for chave, valor in d.items():
        print(f"{chave:<10}: {valor}")

def listar():
    for i, pessoa in enumerate(pessoas, 1):
        print(f"\n--- Usuário {i} ---")
        mostrar_dicionario(pessoa)

def alterar_usuario():
    global pessoas
    listar()
    alteracao = input("\ninforme o usuario que deseja alterar(ex: digite 1 para 'usuario 1'): ")
    if alteracao.isnumeric():
        alteracao = int(alteracao)
    else: 
        print("\nusuario inválido!")
        return
    alteracao = alteracao - 1
    if alteracao > len(senhas) -1:
        print("\nusuário inválido!")
        return
    senha_digitada = input("\ndigite a senha: ")
    if senhas[alteracao] == senha_digitada:
        campo = input("\nqual campo deseja mudar as informaçoes: ")
        if campo.lower() == "nome":
            pessoas[alteracao]["Nome"] = nome()
        if campo.lower() == "idade":
            pessoas[alteracao]["Idade"] = validar_idade()
        if campo.lower() == "email":
            pessoas[alteracao]["Email"] = pedir_email()
        if campo.lower() == "cpf":
            pessoas[alteracao]["CPF"] = pedir_cpf()
        if campo.lower() == "cep":
            pessoas[alteracao]["Cep"] = cep()
        else: print("\ncampo inválido!")
    else: print("\nsenha incorreta!")

def pedir_cpf():
    cpf_valido = False 
    while not cpf_valido:
        cpf = input("\ndigite seu cpf: ")
        cpf_valido = validar_cpf(cpf)
    return cpf   

def pedir_email():
    email_valido = False 
    while not email_valido:
        email = input("\ndigite seu email: ")
        email_valido = validar_email(email)
    return email

def deletar_usuario():
    usuario_desejado = input("\ninforme o usuario que deseja deletar(ex: para 'usuario 1' digite 1): ")
    if usuario_desejado.isnumeric():
        usuario_desejado = int(usuario_desejado)
    else: 
        print("\nusuário inválido!")
        return
    usuario_desejado -= 1
    if usuario_desejado > len(senhas) -1:
        print("\nusuário inválido!")
        return
    senha = input("\ndigite a senha: ")
    if senhas[usuario_desejado] == senha:
        pessoas.pop(usuario_desejado)
        senhas.pop(usuario_desejado)
    else: print("\nsenha incorreta!")

def menu():
    while True:
        print("\n--------ESCOLHA SUA OPÇAO--------")
        print("\n1- CADASTRAR PROFESSOR(A)")
        print("\n2- LISTAR PROFESSORES")
        print("\n3- ALTERAR INFORMAÇÕES 🔒️")
        print("\n4- DELETAR UM USUARIO 🔒️")
        print("\n5- marcar conversinha com o menino mal")
        print("\n6- SAIR DO SISTEMA")
        opcao = input("\nDigite a opçao que voce deseja: ")
        
        if opcao == "1":
            cadastrar_p()   
        if opcao == "2":
            listar()
        if opcao == "3":
            alterar_usuario()
        if opcao == "4":
            deletar_usuario()
        if opcao == "5":
            agenda()
        if opcao == "6":
          print("\nsaindo sistema...")
          break
menu()

