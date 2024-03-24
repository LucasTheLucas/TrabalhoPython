aluno = input("Nome do aluno: ")
media = 7
segundaNota = float(input(f"Informe qual foi a segunda nota do aluno {aluno}: "))
print(f"para ser aprovado na media o aluno {aluno} deve tirar no minimo: ",(media * 3)-(segundaNota*2))