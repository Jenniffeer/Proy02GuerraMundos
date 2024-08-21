from Juego import Juego

def main():
    juego = Juego() #Objeto con toda la info y funcionalidades del juego
    juego.configurarJuego(5, 3) #Establcer (numeroCasillas, numeroCarros)
    juego.empezarJuego() #Empieza el juego o partida

main()