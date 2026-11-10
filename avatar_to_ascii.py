pip install pillow

from PIL import Image

# Your GitHub profile picture
image = Image.open("avatar.png").convert("RGB")

# Terminal character dimensions
width = 35
height = 35

# Resize image
image = image.resize((width, height))

# Characters from dark to bright
chars = "@%#*+=-:. "

pixels = image.load()

for y in range(height):
    line = ""

    for x in range(width):
        r, g, b = pixels[x, y]

        # Convert RGB to brightness
        brightness = (r + g + b) / 3

        # Map brightness to ASCII
        index = int(brightness / 256 * len(chars))
        index = min(index, len(chars) - 1)

        line += chars[index]

    print(line)
