# Pesquisa de Satisfação - Empresa TudoWeb

NUMERO_ENTREVISTADOS = 50

quantidade_excelente = 0
quantidade_ruim = 0
quantidade_bom = 0

print("=== PESQUISA DE SATISFAÇÃO - TUDOWEB ===")
print("Opiniões: 1-EXCELENTE | 2-BOM | 3-RUIM\n")

for i in range(1, NUMERO_ENTREVISTADOS + 1):
    print(f"--- Entrevistado {i}/{NUMERO_ENTREVISTADOS} ---")
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))
    
    # validação da opinião
    while True:
        opiniao = int(input("Digite sua opinião (1-EXCELENTE, 2-BOM, 3-RUIM): "))
        if opiniao in [1, 2, 3]:
            break
        else:
            print("Opção inválida! Digite apenas 1, 2 ou 3.")

    # estrutura de decisão para verificar a opinião
    if opiniao == 1:
        quantidade_excelente += 1
    elif opiniao == 2:
        quantidade_bom += 1
    else:
        quantidade_ruim += 1

# Exibição final - o que a atividade pede
print("\n========== RESULTADO FINAL ==========")
print(f"a) Quantidade de respostas EXCELENTE: {quantidade_excelente}")
print(f"b) Quantidade de respostas RUIM: {quantidade_ruim}")
print(f"   Quantidade de respostas BOM (extra): {quantidade_bom}")
print(f"   Total de entrevistados: {NUMERO_ENTREVISTADOS}")
