# Criando um dicionário para armazenar os produtos e preços
produtos = {}

# Solicitando ao usuário que insira 5 produtos e seus preços
for i in range(5):
    nome_produto = input(f"Digite o nome do {i+1}º produto: ")
    preco_produto = float(input(f"Digite o preço do {i+1}º produto: R$ "))
    produtos[nome_produto] = preco_produto  # Adicionando ao dicionário

# Calculando o valor total da compra
valor_total = sum(produtos.values())

# Exibindo o valor total da compra
print("\nLista de Produtos e Preços:")
for produto, preco in produtos.items():
    print(f"{produto}: R$ {preco:.2f}")

print(f"\nValor total da compra: R$ {valor_total:.2f}")
