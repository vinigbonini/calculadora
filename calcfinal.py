def convbindec():
    binario = int(input('Digite um número binário: '))

    if binario == 0 or binario == 1:
        print(binario)
        
    else:
        if 2<= binario <= 20:
            dezena = binario // 10
            unidade = binario % 10
            numero = (2*dezena) + unidade
            print(numero)
        
        elif 100 <= binario <= 200:
            centena = binario // 100
            dezena = (binario % 100) // 10
            unidade = (binario % 100) % 10
            numero = 4*centena + 2*dezena + unidade
            print(f'{numero:.0f}')
            
        elif 1000 <= binario <= 2000:
            milhar = binario // 1000
            centena = (binario % 1000) // 100
            dezena = ((binario % 1000) % 100) // 10
            unidade = (((binario % 1000) % 100) % 10) % 10
            numero = 8*milhar + 4*centena + 2*dezena + unidade
            print(f'{numero:.0f}')
            
        elif 10000<= binario <= 20000:
            dezmil = binario // 10000
            milhar = (binario % 10000) // 1000
            centena = ((binario % 10000) % 1000) // 100
            dezena = (((binario % 10000) % 1000) % 100) // 10
            unidade = ((((binario % 10000) % 1000) % 100) % 10) % 10 
            numero = 16*dezmil + 8*milhar + 4*centena + 2*dezena + unidade
            print(f'{numero:.0f}')
            
        elif 100000 <= binario <= 200000:
            cemmil = binario // 100000
            dezmil = (binario % 100000) // 10000 
            milhar = ((binario % 100000) % 10000) // 1000
            centena = (((binario % 100000) % 10000) % 1000) // 100 
            dezena = ((((binario % 100000) % 10000) % 1000) % 100) // 10 
            unidade = (((((binario % 100000) % 10000) % 1000) % 100) % 10) % 10
            numero = 32*cemmil + 16*dezmil + 8*milhar + 4*centena + 2*dezena + unidade
            print(f'{numero:.0f}')
            
        elif 1000000 <= binario <= 2000000:
            milhao = binario // 1000000
            cemmil = (binario % 10**6) // 10**5
            dezmil = ((binario % 10**6) % 10**5) // 10**4
            milhar = (((binario % 10**6) % 10**5) % 10**4) // 10**3 
            centena = ((((binario % 10**6) % 10**5) % 10**4) % 10**3) // 10**2
            dezena = (((((binario % 10**6) % 10**5) % 10**4) % 10**3) % 10**2) // 10
            unidade = ((((((binario % 10**6) % 10**5) % 10**4) % 10**3) % 10**2) % 10) % 10
            numero = 64*milhao + 32*cemmil + 16*dezmil + 8*milhar + 4*centena + 2*dezena + unidade
            print(f'{numero:.0f}')
            
        elif 10000000<= binario <= 20000000:
            dezmilh = binario // 10**7
            milhao = (binario % 10**7) // 10**6
            cemmil = ((binario % 10**7) % 10**6) // 10**5
            dezmil = (((binario % 10**7) % 10**6) % 10**5) // 10**4
            milhar = ((((binario % 10**7) % 10**6) % 10**5) % 10**4) // 10**3
            centena = (((((binario % 10**7) % 10**6) % 10**5) % 10**4) % 10**3) // 10**2
            dezena = ((((((binario % 10**7) % 10**6) % 10**5) % 10**4) % 10**3) % 10**2) // 10
            unidade = (((((((binario % 10**7) % 10**6) % 10**5) % 10**4) % 10**3) % 10**2) % 10) % 10 
            numero = 128*dezmilh + 64*milhao + 32*cemmil + 16*dezmil + 8*milhar + 4*centena + 2*dezena + unidade
            print(f'{numero:.0f}')

def convoctdec():
    octal = int(input('Digite um número octal: '))

    if 0 <= octal <= 7:
        print(octal)
        
    elif 10 <= octal <= 99:
        dezena = octal // 10
        unidade = octal % 10
        numero = 8*dezena + unidade
        print(numero)
        
    elif 100 <= octal <= 1000:
        centena = octal // 100
        dezena = (octal % 100) // 10
        unidade = ((octal % 100) % 10) % 10
        numero = 64*centena + 8*dezena + unidade
        print(numero)

def convhexdec():
    hexdex = input('Digite um número hexadecimal: ').upper()

    if hexdex == '1' or hexdex == '2' or hexdex == '3' or hexdex == '4' or hexdex == '5' or hexdex == '6' or hexdex == '7' or hexdex == '8' or hexdex == '9':
        print(f'{hexdex} em decimal é igual a {hexdex}')
    elif hexdex == 'A':
        print(f'{hexdex} em decimal é igual a 10')
    elif hexdex == 'B':
        print(f'{hexdex} em decimal é igual a 11')
    elif hexdex == 'C':
        print(f'{hexdex} em decimal é igual a 12')
    elif hexdex == 'D':
        print(f'{hexdex} em decimal é igual a 13')
    elif hexdex == 'E':
        print(f'{hexdex} em decimal é igual a 14')
    elif hexdex == 'F':
        print(f'{hexdex} em decimal é igual a 15')

    else:
        separ = list(hexdex)
        if separ[0] == '1' or separ[0] == '2' or separ[0] == '3' or separ[0] == '4' or separ[0] == '5' or separ[0] == '6' or separ[0] == '7' or separ[0] == '8' or separ[0] == '9':
            a = int(separ[0])
        elif separ[0] == 'A':
            a = 10
        elif separ[0] == 'B':
            a = 11
        elif separ[0] == 'C':
            a = 12
        elif separ[0] == 'D':
            a = 13
        elif separ[0] == 'E':
            a = 14
        elif separ[0] == 'F':
            a = 15
        if separ[1] == '1' or separ[1] == '2' or separ[1] == '3' or separ[1] == '4' or separ[1] == '5' or separ[1] == '6' or separ[1] == '7' or separ[1] == '8' or separ[1] == '9':
            b = int(separ[1])
        elif separ[1] == 'A':
            b = 10
        elif separ[1] == 'B':
            b = 11
        elif separ[1] == 'C':
            b = 12
        elif separ[1] == 'D':
            b = 13
        elif separ[1] == 'E':
            b = 14
        elif separ[1] == 'F':
            b = 15
        else:
            b = 0
        
        decimal = (a * 16) + (b * 1)
        print(f'{hexdex} em decimal é igual a {decimal}')

def chamar_menu():

    menu = input('Digite: \n[1] para converter binário para decimal \n[2] para converter octal para decimal \n[3] para converter hexadecimal para decimal: ')

    if menu == '1':
        convbindec()
    elif menu == '2':
        convoctdec()
    elif menu == '3':
        convhexdec()

    outra_conversao = input('Digite <1> para fazer outra conversão ou qualquer tecla para sair: ').upper()
    if outra_conversao == '1':
        chamar_menu()

chamar_menu()