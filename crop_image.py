from PIL import Image, ImageDraw

# Open the image
img = Image.open("assets/img/vignesh_headshot_circle.jpeg").convert("RGBA")

# Create a mask
size = min(img.size)
mask = Image.new("L", img.size, 0)
draw = ImageDraw.Draw(mask)
draw.ellipse((0, 0, size, size), fill=255)

# Apply the mask to the image
result = Image.new("RGBA", img.size, (0, 0, 0, 0))
result.paste(img, (0, 0), mask=mask)

# Crop to the bounding box of the circle
result = result.crop((0, 0, size, size))
result.save("assets/img/circular_image.png")
