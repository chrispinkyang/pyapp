import random
from PIL import Image,ImageDraw,ImageFont,ImageFilter

# 随机字母:
def rndChar():
    return chr(random.randint(65, 90))

# 随机颜色1用于背景填充:
def rndColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

# 随机颜色2用于字体颜色:
def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

w = 240
h = 60
im = Image.new('RGB',(w,h),(255,255,255))

font = ImageFont.truetype('C:/Windows/Fonts/Arial.ttf', 36)
draw = ImageDraw.Draw(im)

#使用point填充背景
for x in range(w):
	for y in range(h):
		draw.point((x,y), fill=rndColor())

#使用text写上字
for i in range(4):
	draw.text((60 * i + 10, 10), rndChar(),font=font, fill=rndColor2())

im = im.filter(ImageFilter.GaussianBlur)
#im = im.filter(ImageFilter.BLUR)

#生成随机文件名
from datetime import datetime
name = 'verifycode/' + datetime.now().strftime('%y%m%d') + str(int(random.random()*100))+'.jpeg'
im.save(name, 'JPEG')

