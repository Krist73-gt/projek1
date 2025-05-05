import pygame
import time
import requests
from io import BytesIO

# Inisialisasi pygame
pygame.init()

# Tentukan ukuran layar
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Animasi Mobil")

# Warna
WHITE = (255, 255, 255)

# Load gambar mobil
car_image = pygame.image.load(r"C:\Users\kristo\Downloads\20220223_173557_62160e0da4441.jpeg")
car_width, car_height = car_image.get_size()

# Ambil gambar latar belakang dari URL
background_url = "https://images.unsplash.com/photo-1506748686214-e9df14d4d9d0?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MXwyMDg3N3wwfDF8c2VhcmNofDF8fG1vdG9yfGVufDB8fHx8MTYyOTU4MDYyOA&ixlib=rb-1.2.1&q=80&w=1080"  # Gambar latar belakang dari Unsplash
response = requests.get(background_url)
background_image = pygame.image.load(BytesIO(response.content))

# Posisi awal mobil
x = -car_width
y = (screen_height - car_height) // 2

# Kecepatan mobil
car_speed = 5

# Loop utama
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update posisi mobil
    x += car_speed
    if x > screen_width:
        x = -car_width  # Reset ke posisi kiri jika sudah melewati batas kanan

    # Menggambar background dan mobil
    screen.blit(background_image, (0, 0))  # Menggambar latar belakang
    screen.blit(car_image, (x, y))  # Menggambar mobil

    # Update layar
    pygame.display.update()

    # Batasi frame per detik
    time.sleep(0.01)

# Keluar dari pygame
pygame.quit()
