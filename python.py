
carrinho=[]
total=0
while True:
 Produto= input ("Shampoo 13R$ (ou 'fim' para pagar):")
 if Produto.lower()=='fim':
    break 
 preço=float(input(f"Preço de {Produto}:"))
 carrinho.append(("produto, preço"))
 total += preço
 print("\n---Resumo da Compra---")
for item in carrinho:
 print(f"item[0]: R$ {item[1]}")
 print(f"TOTAL: R${total:2f}")
