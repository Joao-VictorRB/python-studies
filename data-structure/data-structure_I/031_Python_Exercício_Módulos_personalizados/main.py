import financas

valor = 1000
taxa = 0.1
tempo = 2

valor_com_juros = financas.juros(valor, taxa, tempo)
valor_com_desconto = financas.desconto(valor, 0.15)

print("Valor com juros:", financas.formatar_real(valor_com_juros))
print("Valor com desconto:", financas.formatar_real(valor_com_desconto))