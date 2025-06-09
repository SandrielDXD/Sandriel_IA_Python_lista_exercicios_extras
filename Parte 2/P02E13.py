valor_hora = float(input("Digite o valor da sua hora de trabalho: R$ "))
horas_trabalhadas = float(input("Digite a quantidade de horas trabalhadas no mês: "))

salario_bruto = valor_hora * horas_trabalhadas

if salario_bruto <= 900.00:
    percentual_ir = 0
elif salario_bruto <= 1500.00:
    percentual_ir = 5
elif salario_bruto <= 2500.00:
    percentual_ir = 10
else:
    percentual_ir = 20
    
valor_ir = salario_bruto * percentual_ir / 100

percentual_inss = 10
valor_inss = salario_bruto * percentual_inss / 100

percentual_sindicato = 3
valor_sindicato = salario_bruto * percentual_sindicato / 100

percentual_fgts = 11
valor_fgts = salario_bruto * percentual_fgts / 100

total_descontos = valor_ir + valor_inss + valor_sindicato

salario_liquido = salario_bruto - total_descontos

print("\n" + "=" * 50)
print("FOLHA DE PAGAMENTO".center(50))
print("=" * 50)
print(f"Salário Bruto: ({valor_hora} * {horas_trabalhadas}){'':<15}: R$ {salario_bruto:.2f}")

if percentual_ir > 0:
    print(f"(-) IR ({percentual_ir}%){'':<24}: R$ {valor_ir:.2f}")
else:
    print(f"(-) IR (Isento){'':<23}: R$ {valor_ir:.2f}")

print(f"(-) INSS ({percentual_inss}%){'':<22}: R$ {valor_inss:.2f}")
print(f"(-) Sindicato ({percentual_sindicato}%){'':<17}: R$ {valor_sindicato:.2f}")
print(f"FGTS ({percentual_fgts}%){'':<24}: R$ {valor_fgts:.2f}")
print(f"Total de descontos{'':<27}: R$ {total_descontos:.2f}")
print(f"Salário Líquido{'':<30}: R$ {salario_liquido:.2f}")
print("=" * 50)