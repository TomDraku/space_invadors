import turtle
from ship import Ship
from bullet import Bullet
from alien import Alien
import tkinter as tk
import time
import random

# ZMIENNE
running = True

# EKRAN
# tworzenie obiektu ekranu 
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Space invadors")
screen.setup(width=800, height=600)

# funkcja wyświetlająca informację o wygranej
def display_winning_message():
    turtle.clear() # Wyczyść ekran, jeśli wcześniej był na nim rysowany tekst
    turtle.penup()
    turtle.shapesize(0.01, 0.01)
    turtle.goto(0,0)
    turtle.color("white")
    turtle.write("Wygrałeś!!!", align="center", font=("Arial", 24,"normal"))

# funkcja wyświetlająca informację o przegranej
def display_losing_message():
    turtle.clear() # Wyczyść ekran, jeśli wcześniej był na nim rysowany tekst
    turtle.penup()
    turtle.shapesize(0.01, 0.01)
    turtle.goto(0,0)
    turtle.color("white")
    turtle.write("Przegrałeś!!!", align="center", font=("Arial", 24,"normal"))

# STATEK GRACZA
# tworzenie statku gracza
my_ship = Ship()

# funkcja do poruszania statku w lewo
def ship_left():
    my_ship.move_left()
    
# funkcja do poruszania statku w prawo
def ship_right():
    my_ship.move_right()

# ODDAWANIE STRZAŁU PRZEZ UŻYTKOWNIKA
# funkcja tworzenia pocisku przez użytkownika
bullets = []

def shoot():
    global bullets
    new_bullet = Bullet(my_ship, 90)
    bullets.append(new_bullet)
    

    
    
# TWORZENIE STATKÓW OBCYCH
aliens =  []
num_rows = 2
num_cols = 8
y = 50
x = - 150
colors = ["yellow", "green", "blue"]


for row in range (num_rows):
    for column in range(num_cols):
        color = random.choice(colors)
        # Dodajemy obiekt alien na odpowiedniej pozycji
        alien1 = Alien(color, (x + column * 50, y - row * 50))
        aliens.append(alien1)
  

# ODDAWANIE STRZAŁU PRZEZ OBCYCH
# funkcja tworzenia pocisku 
al_bullets = []

def al_shoot():
    global al_bullets
    global aliens
    alien = random.choice(aliens)
    new_bullet = Bullet(alien, 270)
    new_bullet.color( "orange")
    al_bullets.append(new_bullet)


# METODY STEROWANIA GRĄ ZA POMOCĄ KLAWIATURY
# nasłuchiwanie klawiatura
turtle.listen()

# przypisanie funkcji do przycisków poruszanie statkiem gracza i oddawanie strzału
turtle.onkey(ship_left, "Left")
turtle.onkey(ship_right, "Right")
turtle.onkey(shoot, "space")


# GŁÓWNA PĘTLA GRY

# funkcja zamykająca okno w razie nagłego zamknięcia okna podczas działania pętli
def on_closing():
    global running
    running = False
    

# metoda pozwalająca wychwycić zamknięcie okna oraz uruchomić podaną wyżej funkcję
screen.getcanvas().master.protocol("WM_DELETE_WINDOW", on_closing)  

# kontrola prędkości poruszania się obiektów przypadku zwiększania się liczby elementów
# zmienna przechowująca czas początkowy pętli
start_time= time.time()

# poruszanie pociskiem wystrzelonym przez gracza oraz wprawienie statku obcych w ruch
while running:
    
    
    try:
        # aktualny czas pętli
        current_time = time.time()
      
        
        # obliczamy czas trwania pojedynczej iteracji pętli
        elapsed_time = current_time - start_time
       
        
        # aktualizujemy czas początkowy 
        start_time = current_time
    
        screen.update()
        
        
        
        # pętla wprawiajaca w ruch statki
        for alien in aliens:
            alien.move()
             
            # sprawdzanie czy statek obcych nie przekroczył lini obrony gracza
            if alien.ycor()<= -220:
                    display_losing_message()
                    time.sleep(5)
                    running = False
                    
        # losowe wywołanie funkcji oddawania strzału przez obcych            
        number = random.randint(1, 10) 
        if  number == 3:
            al_shoot()  
        for new_bullet in al_bullets:
            new_bullet.speed = elapsed_time*80
            new_bullet.move()
            # wykrywanie kolizji statku z pociskiem obcych
            if new_bullet.distance(my_ship) < 10 :
                display_losing_message()
                time.sleep(5)
                running = False
            # usunięcie pocisku po przekroczeniu dolnej granicy ekranu
            if new_bullet.ycor()  < -300:
                new_bullet.hideturtle()
                al_bullets.remove(new_bullet) 
            
                   
                    
                    
                    
                    
        # pętla wprawiająca w ruch pociski    
        for bullet in bullets:
            bullet.speed = elapsed_time*80
            bullet.move()
            # usunięcie pocisku po przekroczeniu górnej granicy ekranu
            if bullet.ycor()  > 300:
                bullet.hideturtle()
                bullets.remove(bullet) 
                    
                    
            # warunek sprawdzający kolizję statku obcych z pociskiem 
            for alien in aliens:       
                if bullet.distance(alien) < 30:
                        alien.hideturtle()
                        aliens.remove(alien)
                        # sprawdzenie czy graczowi udało się zbić wszystkie statki obcych
                        if len(aliens) == 0:
                            display_winning_message()
                            time.sleep(5)
                            running = False
            
    
    except turtle.Terminator:
        
        print("Program został zakończony")
        
    
        
     
        
            
            

    








screen.bye()
