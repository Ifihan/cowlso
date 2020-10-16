import pandas as pd
from PIL import Image, ImageDraw, ImageFont
 
data = pd.read_csv('registered.csv') 
name_list = data["Name"].tolist()

for i in name_list:
    if len(i)>20:
        font_size = ImageFont.truetype(r"fonts/Aulyars Regular.otf", 20)
        nameloc = (600, 490)
    else:
        font_size = ImageFont.truetype(r"fonts/Aulyars Regular.otf", 30)
        nameloc = (640, 480)
    im = Image.open('certificate.jpeg')
    d = ImageDraw.Draw(im)
    # signature = (520, 700)
    # date = (850, 710)
    text_color = (0, 0, 0)
    font = ImageFont.truetype(r"fonts/Cinzel-Bold.otf", 40)
    d.text(nameloc, i, fill = text_color, font = font_size)
    # d.text(signature, "Sodiq Akinjobi", fill = text_color, font = font)
    # d.text(date, "05-08-2020", fill = text_color, font = font_size)
    im.save(i + ".jpg")