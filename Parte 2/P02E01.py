tamanho_mb = float(input("Tamanho do arquivo (MB): "))
velocidade_mbps = float(input("Velovidade do link (Mbps): "))

tamanho_megabits = tamanho_mb * 8

tempo_segundos = tamanho_megabits / velocidade_mbps

tempo_minutos = tempo_segundos / 60

print(f"Tempo aproximadi de dowload: {tempo_minutos:.1f} minutos")