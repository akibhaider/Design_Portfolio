# Reload the new image
new_image_path = "C:\Users\User\OneDrive\Desktop\Design_Portfolio\llbd\ll.jpg"
new_image = Image.open(new_image_path)

# Prepare the draw object
draw = ImageDraw.Draw(new_image)

# Define text properties
font_path = "C:\Users\User\OneDrive\Desktop\Design_Portfolio\llbd\Raleway-Bold.ttf"  # Default font path
font_size = 20  # Approximate size, may need adjustment
font = ImageFont.truetype(font_path, font_size)
text_color = "#FFCC99"

# Text positions, approximated for now, these should be adjusted manually
texts = [
    ("OUR SERVICES", (30, 90)),
    ("Ocean Freight Management", (30, 140)),
    ("Air Freight Management", (30, 170)),
    ("Customs Brokerage", (30, 200)),
    ("Supply Chain Management", (30, 230)),
    ("Project Management", (30, 260)),
    ("Sea-Air Combined Transport", (30, 290)),
    ("Warehousing", (30, 320)),
    ("Our expertise", (30, 370)),
    ("Machinery", (30, 420)),
    ("Building Materials", (30, 450)),
    ("Boilers", (30, 480)),
    ("Crane", (30, 510)),
    ("Vehicles", (30, 540)),
    ("Wind Project", (30, 570)),
    ("Power Project", (30, 600)),
    ("Marble & Granite Blocks", (30, 630)),
    ("WHY LIYANA?", (450, 90)),
    ("One-Stop Solution", (450, 140)),
    ("Time Sensitive", (450, 170)),
    ("Pro-active & available 24/7", (450, 200)),
    ("Personalized Approach", (450, 230)),
    ("Our Partners are specialist in respective Countries remain as your eyes", (450, 260)),
    ("Multi Cultural Environment", (450, 290)),
    ("We care utmost our clients comfort providing full visibility of the consignment", (450, 320)),
    ("At Liyana BD we take work at home", (450, 350)),
    ("Do visit and check out the details at : www.liyanalogistics.com", (450, 670))
]

# Draw new text on the image
for text, position in texts:
    draw.text(position, text, font=font, fill=text_color)

# Save the updated image
updated_image_path = "C:\Users\User\OneDrive\Desktop\Design_Portfolio\llbd\ll_u.jpg"
new_image.save(updated_image_path)

updated_image_path
