hartie = 1 
piatra = 2  
foarfeca = 3

def castigator(player1, player2):
    if player1 == player2:
        return "Egalitate!"
    if (player1, player2) in  [(hartie, piatra), (foarfeca, hartie), (piatra, foarfeca)]:
        return "Player 1 a castigat runda aceasta!"
    else:
        return "Player 2 a castigat runda aceasta!"

def alegere(choice):
    if int(choice) == 1:
        return 'Ai ales hartie'
    if int(choice) == 2:
        return 'Ai ales piatra'
    if int(choice) == 3:
        return 'Ai ales foarfeca'
    return int(choice)

def main():
    while True:
        castiguri_player_1 = 0
        castiguri_player_2 = 0
        egalitate = 0
        
        for _ in range(3):
            player1 = int(input("Jucator 1 : Alege: Hartie - 1, Piatra - 2, Foarfeca - 3--->"))
            player2 = int(input("Jucator 2 : Alege: Hartie - 1, Piatra - 2, Foarfeca - 3--->"))
            print(alegere(player1))
            print(alegere(player2))
            print(castigator(player1, player2))
            rezultat = castigator(player1, player2)
            if rezultat == "Player 1 a castigat runda aceasta!":
                castiguri_player_1 += 1
            elif rezultat == "Player 2 a castigat runda aceasta!":
                castiguri_player_2 += 1
            else:
                egalitate += 1
            
            
        print(f'Jucător 1 a castigat de {castiguri_player_1} ori.')
        print(f'Jucător 2 a castigat de {castiguri_player_2} ori.')
        print(f'A fost egalitate de {egalitate} ori. \n')
        
        if castiguri_player_1 > castiguri_player_2:
            print(f'Jucator 1 a castigat cu {castiguri_player_1} runde')
        if castiguri_player_1 < castiguri_player_2:
            print(f'Jucator 2 a castigat cu {castiguri_player_2} runde')
        if castiguri_player_1 == castiguri_player_2:
            print('Egalitate intre jucatori.')
        rematch = input("Doriti sa jucati din nou? (da/nu): ")
        if rematch.lower() != 'da':
            break 
    print('Jocul s-a terminat')
    
main()
