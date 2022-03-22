listbinario = []
listoctal = []
listhexadec = []

decimal = int(input('Digite um número decimal: '))


if decimal == 0 or decimal == 1:
    print(decimal)
else:
    partint = decimal
    while partint >= 1:
        binario = partint % 2
        partint = partint // 2
        listbinario.append(binario)
    convstr = [str(a) for a in listbinario]
    espaco = ''.join(convstr)
    pronto1 = espaco[::-1]

if 0 <= decimal <= 7:
    print(decimal)
else:
    partint = decimal
    while partint >= 1:
        octal = partint % 8
        partint = partint // 8
        listoctal.append(octal)
    convstr = [str(a) for a in listoctal]
    espaco = ''.join(convstr)
    pronto2 = espaco[::-1]
    
if 0 <= decimal <= 9:
    print(decimal)
else:
    partint = decimal
    while partint >= 1:
        hexadec = partint % 16
        partint = partint // 16
        if hexadec <= 9:
            listhexadec.append(hexadec)
        else:
            if hexadec == 10:
                listhexadec.append('A')
            elif hexadec == 11:
                listhexadec.append('B')
            elif hexadec == 12:
                listhexadec.append('C')
            elif hexadec == 13:
                listhexadec.append('D')
            elif hexadec == 14:
                listhexadec.append('E')
            elif hexadec == 15:
                listhexadec.append('F')
    convstr = [str(a) for a in listhexadec]
    espaco = ''.join(convstr)
    pronto3 = espaco[::-1]
    
print(f'Decimal: {decimal} \nBinário: {pronto1} \nOctal: {pronto2} \nHexadecimal: {pronto3}')