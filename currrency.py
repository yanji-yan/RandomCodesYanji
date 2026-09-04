pesos = float(input("What do you have left in COP? "))
soles = float(input("What do you have left in PEN? "))
reais = float(input("What do you have left in BRL? "))

# Conversion rates to USD
usd = (pesos * 0.00024) + (soles * 0.27) + (reais * 0.18)

print("You have a total of USD:")
print(usd)