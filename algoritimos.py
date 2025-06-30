def calcular_conta_de_luz():
    print("============================")
    print("   CALCULADORA DE ENERGIA   ")
    print("============================")

    nome = input("Informe o nome do cliente: ")

    print("\nSelecione o tipo de cliente:")
    print("1 - Residência (R$ 0.60 por kWh)")
    print("2 - Comércio   (R$ 0.48 por kWh)")
    print("3 - Indústria  (R$ 1.29 por kWh)")
    
    tipo = input("Digite o número correspondente ao tipo: ")

    if tipo not in ['1', '2', '3']:
        print("Tipo de cliente inválido. Encerrando o programa.")
        return

    try:
        consumo = float(input("Informe a quantidade de kWh consumidos: "))
    except ValueError:
        print("Valor inválido. Consumo deve ser numérico.")
        return

    if tipo == '1':
        valor_kwh = 0.60
        tipo_nome = "Residencial"
    elif tipo == '2':
        valor_kwh = 0.48
        tipo_nome = "Comercial"
    elif tipo == '3':
        valor_kwh = 1.29
        tipo_nome = "Industrial"

    total = consumo * valor_kwh

    print("\nResumo da Conta de Luz")
    print("------------------------")
    print(f"Cliente: {nome}")
    print(f"Tipo de Cliente: {tipo_nome}")
    print(f"Consumo: {consumo:.2f} kWh")
    print(f"Valor por kWh: R$ {valor_kwh:.2f}")
    print(f"TOTAL A PAGAR: R$ {total:.2f}")

    print("\nEncerrando o sistema. Obrigado.")

# Executar a função principal
calcular_conta_de_luz()
