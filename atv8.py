aluno = input("Nome do aluno: ")
notaQuantitativa = float(input(f"Informe qual foi a nota que {aluno} tirou na nota quantitativa: "))
notaDaProva = float(input(f"Informe qual foi a nota que {aluno} tirou na nota da prova: "))
print(f"A media do aluno {aluno} foi de: ",(notaQuantitativa + (notaDaProva*2)) /3)