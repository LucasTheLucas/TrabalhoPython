nome = input("Digite seu nome: ")
anoDeNascimento = int(input("Digite seu ano de nascimento: "))
mesDeNascimento = int(input("Digite o seu mes de nascimento: "))
diaDeNascimento = int(input("Digite o dia do seu nascimento: "))
anoAtual: int = 2024
diaAtual: int = 14
mesAtual: int = 3

if (mesAtual == mesDeNascimento):
    if (diaAtual >= diaDeNascimento):
        print(nome," você tem ", anoAtual-anoDeNascimento, " anos!")
    
    else:
        print(nome," você vai fazer ", anoAtual-anoDeNascimento, " anos!")

else:
    if (mesAtual > mesDeNascimento):
        print(nome," tem ", anoAtual-anoDeNascimento, " anos!")

    else:
            print(nome," você vai fazer ",anoAtual-anoDeNascimento," anos!")
