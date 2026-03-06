"""
6. Calcular preço de venda para produto por quilo.
"""

quantity = float(input("Digite a quantidade em gramas do produto: "))
price = float(input("Digite o valor de seu produto: "))

kgPrice = 1000*price/quantity

print(f"O valor de venda de seu produto por kilo é de {kgPrice:.2f} reais")