import os
import tempfile
import image


border_color = "#FF0000"  # red
square_color = "#0000FF"  # blue
img = os.path.join(tempfile.gettempdir(), "test.img")
xpm = os.path.join(tempfile.gettempdir(), "test.xpm")
width, height = 240, 60
midx, midy = width // 2, height // 2
image = image.Image(width, height, img, "#F0F0F0")
for x in range(width):
    for y in range(height):
        if x < 5 or x >= width - 5 or y < 5 or y >= height - 5:
            image[x, y] = border_color
        elif midx - 20 < x < midx + 20 and midy - 20 < y < midy + 20:
            image[x, y] = square_color
print(image.width, image.height, len(image.colors), image.background)
image.save()
image.export(xpm)
