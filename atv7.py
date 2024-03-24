vendedor = input("Digite o nome do vendedor: ")
quantidadeDeCarrosVendidos = int(input(f"Quantos carros {vendedor} vendeu? "))
valorTotalDeCarrosVendidos = float(input(f"Qual foi o valor total das vendas do vendedor {vendedor}: "))
print(f"O salário de {vendedor} foi de: ",((quantidadeDeCarrosVendidos*50)+(valorTotalDeCarrosVendidos*0.05)+500))