def juros(valor, taxa, tempo):
    return valor * (1 + taxa) ** tempo


def desconto(valor, taxa):
    return valor - (valor * taxa)


def formatar_real(valor):
    return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")