def display_jogo(lista):
    '''
        Exibe a matriz do jogo em forma de matriz.
    '''

    a,b,c,d,e,f,g,h,i = lista

    print(f' {g[0]} | {h[0]} | {i[0]} ')
    print(f' {d[0]} | {e[0]} | {f[0]} ')
    print(f' {a[0]} | {b[0]} | {c[0]} ')

def verifica_vencedor(lista):
    '''
        Retorna 0 se o jogo acabou e 1 se o jogo prossegue.
    '''
    for k in [0,3,6]:
        if lista[k] == lista[k+1] and lista[k+1] == lista[k+2]:
            return 1
    for j in [0,1,2]:
        if lista[j] == lista[j+3] and lista[j+3] == lista[j+6]:
            return 1
    if lista[0] == lista[4] and lista[4] == lista[8]:
            return 1
    if lista[2] == lista[4] and lista[4] == lista[6]:
            return 1
    return 0

def jogo_da_velha():
    '''
        Inicializa o jogo de acordo com a escolha simbólica do primeiro jogador. A ordenação da matriz (1-9) é semelhante ao
        teclado de uma calculadora.
    '''

    jogo = [' a', ' b', ' c', ' d', ' e', ' f', ' g', ' h', ' i']
    cont = 0

    while True:

        player1 = input("Bem vindo ao jogo da velha, Player 1. Deseja jogar com X ou O? ").upper()

        if player1 in 'O':
            player2 = 'X'
            break
        elif player1 in 'X':
            player2 = 'O'
            break

#Guardar as posições em uma lista e receber as jogadas dos jogadores
    while True:

        while True:
            pos_pri = int(input("Jogador 1: Informe a posição que deseja jogar (1-9): "))
            if jogo[pos_pri - 1] != 'X' and jogo[pos_pri - 1] != 'O':
                break
            else:
                print("Posição inválida, tente novamente.")
        jogo[pos_pri - 1] = player1
        display_jogo(jogo)
        cont += 1

        if cont == 5:
            print("Deu velha!")
            resp = input("Você quer jogar de novo [s/n]? ")
            if resp in 'Ss':
                jogo_da_velha()
            else:
                break

        if verifica_vencedor(jogo) == 1:
            print("O jogador 1 venceu o jogo!")
            resp = input("Você quer jogar de novo [s/n]? ")
            if resp in 'Ss':
                jogo_da_velha()
            else:
                break
            break

        while True:
            pos_seg = int(input("Jogador 2: Informe a posição que deseja jogar (1-9): "))
            if jogo[pos_seg - 1] != 'X' and jogo[pos_seg - 1] != 'O':
                break
            else:
                print("Posição inválida, tente novamente.")
        jogo[pos_seg-1] = player2
        display_jogo(jogo)

        if verifica_vencedor(jogo) == 1:
            print("O jogador 2 venceu o jogo!")
            resp = input("Você quer jogar de novo [s/n]? ")
            if resp in 'Ss':
                jogo_da_velha()
            else:
                break

if __name__ == '__main__':
    jogo_da_velha()


