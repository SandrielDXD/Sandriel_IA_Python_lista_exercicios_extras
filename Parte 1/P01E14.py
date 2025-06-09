valor = input("quanto você ganha por hora? ")
horas = input("quantas horas você trabalha por mês? ")
salariobruto= float(valor) * float(horas)  
ir = salariobruto * 0.11
inss = salariobruto * 0.08
sindicato = salariobruto * 0.05
salarioliquido = salariobruto - (ir + inss + sindicato)
print(f"Seu salário bruto é R$ {salariobruto:.2f}.")
print(f"- IR (11%)          : R$ {ir:.2f}")
print(f"- INSS (8%)         : R$ {inss:.2f}")
print(f"- Sindicato (5%)    : R$ {sindicato:.2f}")
print(f"Seu salário líquido é R$ {salarioliquido:.2f}.")