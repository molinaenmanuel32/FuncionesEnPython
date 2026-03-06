def exchange_money(budget, exchange_rate):
    return budget / exchange_rate

budget = float(input("Ingrese la cantidad de dinero: "))
exchange_rate = float(input("Ingrese la tasa de cambio: "))

resultado = exchange_money(budget, exchange_rate)

print("El dinero convertido es:", resultado)