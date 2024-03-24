hamburger = int(input("Digite a quantidade de hamburger: "))
cheeseburger = int(input("Digite a quantidade de cheesehamburger: "))
fritas = int(input("Digite a quantidade de fritas: "))
refrigerante = int(input("Digite a quantidade de refrigerante: "))
milkshake = int(input("Digite a quantidade de milkshake: "))

valorHamburger = 3
valorCheeseburger = 2.5
valorFritas = 2.5
valorRefrigerante = 1
valorMilkshake = 3

valorTotal = ( hamburger * valorHamburger )
valorTotal += ( cheeseburger * valorCheeseburger )
valorTotal += ( fritas * valorFritas )
valorTotal += ( refrigerante * valorRefrigerante )
valorTotal += ( milkshake * valorMilkshake )

print("O valor de seu pedido vai ser de R$ ", valorTotal)