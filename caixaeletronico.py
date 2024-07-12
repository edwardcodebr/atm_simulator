def cash(valor):
    if valor < 10 or valor > 600:
        print("Invalid! The amount should be between 10 and 600 reais.")
        return
    
    notas = [100, 50, 10, 5, 1]
    quantidade_notas = {}
    
    for nota in notas:
        quantidade = valor // nota
        if quantidade > 0:
            quantidade_notas[nota] = quantidade
        valor -= quantidade * nota
    
    print("Notes provided:")
    for nota, quantidade in quantidade_notas.items():
        print(f"{quantidade} note{'s' if quantidade > 1 else ''} of {nota} reais")

# Teste da função
cash(256)
print("\n")
cash(399)