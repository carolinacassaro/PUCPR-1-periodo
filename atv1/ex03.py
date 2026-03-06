"""
3. Leia do teclado a temperatura em Celsius e imprima o equivalente em Fahrenheit.
(Fórmula: (X ºC × 9/5) + 32
"""

celsius = float(input("Digite a temperatura em Celsius: "))
fahrenheit = (celsius * 9/5) + 32

print(f"{celsius:.1f} graus celsius é igual a {fahrenheit:.1f} graus fahrenheit.")