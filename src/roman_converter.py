def decimal_to_roman(number):
    if number < 1 or number > 3999:
        return ""

    valores = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]

    resultado = ""

    for valor, simbolo in valores:
        while number >= valor:
            resultado += simbolo
            number -= valor

    return resultado
