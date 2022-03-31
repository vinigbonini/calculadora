listbinario = []
listoctal = []
listhexadec = []

def convbin(decimal):
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
        print(f'O decimal {decimal} é igual a {pronto1} em binário')
        
def convoctal(decimal):
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
        print(f'O decimal {decimal} é igual a {pronto2} em octal')
        
def convhexdex(decimal):
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
        print(f'O decimal {decimal} é igual a {pronto3} em hexadecimal')

def chamar_menu():
    menu = input('Digite: \n<1> Para converter decimal para binário \n<2> Para converter decimal para octal \n<3> Para converter decimal para hexadecimal: ')
    decimal = int(input('Digite um número decimal: '))

    if menu == '1':
        convbin(decimal) 
    elif menu == '2':       
        convoctal(decimal)
    elif menu == '3':
        convhexdex(decimal)
        
    outra_conversao = input('Digite <1> para fazer outra conversão ou qualquer tecla para sair: ').upper()
    if outra_conversao == '1':
        chamar_menu()

chamar_menu()
