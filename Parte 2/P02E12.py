salario_atual = float(input("Digite o salário atual do colaborador: R$ "))

if salario_atual <= 280.00:
    percentual = 20
elif salario_atual <= 700.00:
    percentual = 15
elif salario_atual <= 1500.00:
    percentual = 10
else:
    percentual = 5
    
    
valor_aumento = salario_atual * percentual / 100
novo_salario = salario_atual + valor_aumento

print("\nRelatório de Reajuste Salarial")
print("=" * 30)
print(f"Salário antes do reajuste: R$ {salario_atual:.2f}")
print(f"Percentual de aumento aplicado: {percentual}%")
print(f"Valor do aumento: R$ {valor_aumento:.2f}")
print(f"Novo salário: R$ {novo_salario:.2f}")
print("=" * 30)