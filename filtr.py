"pip install pillow"
from PIL import Image

obrazek = Image.open("2.jpg")
sirka, vyska = obrazek.size
x = 0

while x < sirka:
    y = 0
    while y < vyska:
        r, g, b = obrazek.getpixel((x, y))
        prumer = int((r + g + b) / 3)
        obrazek.putpixel((x, y), (r, b, r))

        if prumer > 200:
            obrazek.putpixel((x, y), (255, 150, 255))  # Bílá pro světlé pixely
        elif 160 < prumer <= 200:
            obrazek.putpixel((x, y), (240, 210, 190))  # Teplý odstín s vyšší intenzitou
        elif 120 < prumer <= 160:
            obrazek.putpixel((x, y), (100, 200, 240))  # Chladný odstín s vyšší intenzitou
        elif 80 < prumer <= 120:
            obrazek.putpixel((x, y), (100, 130, 160))  # Střední intenzita šedé

        elif prumer <= 40:
            obrazek.putpixel((x, y), (140, 30, 30))      # Mírně do červena s vyšší intenzitou pro tmavé pixely

        y += 1
    x += 1

obrazek.show()#display(obrazek)