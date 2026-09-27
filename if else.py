print ("---------- LOJA ONLINE ----------")
print ("")
print ("produtos:")
print ("")
print ("Camisetas -- R$50,00")
print ("")
print ("Calças -- R$180,00")
print ("")
print ("Tenis -- R$100,00")
print ("")
compra = input("Quais produtos deseja comprar?")
total = 0
if "camiseta" in compra:
    total = total + 50
if "calça" in compra:
    total = total + 180
if "tenis" in compra: 
    total = total + 100 
if total < 200:
    desconto = "5%"
    total_final = total - (total * 0.05)
if total < 300:
    desconto = "10%"
    total_final = total - (total * 0.1)
else:
    desconto = "15%"
    total_final = total - (total * 0.15)
print ("")
print("---- RESUMO DA COMPRA ----")
print("Valor total: R$", total)
print ("")
print("Valor do desconto: R$", desconto)
print ("")
print("Valor final a pagar: R$", total_final)