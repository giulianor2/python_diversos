# O Zodíaco chinês é composto por animais com ciclo de 12 anos. Uma maneira simplificada de identificá-lo é verificando-se apenas o ano de seu nascimento do seguinte modo:

ano = int(input('Digite o ano do seu nascimento: '))

signosChines = ['Macaco',   #0
                'Galo',     #1
                'Cão',      #2
                'Porco',    #3
                'Rato',     #4
                'Boi',      #5
                'Tigre',    #6
                'Coelho',   #7
                'Dragão',   #8
                'Serpente', #9
                'Cavalo',   #10
                'Carneiro'] #11

seuSigno = signosChines[ano % 12]
print(f'O seu signo Chines é: {seuSigno}.')