from PIL import Image
import os,sys

def ImgProcess(code):
    sz = 170
    cur_x = 650
    cur_y = 330
    
    toImage = Image.new('RGBA',(2000,2000),color='#F5F5DC')
    
    # 第一行 点（325 165）(650 330)
    fromImage = Image.open(r"upload/%s/1.jpg" % code)
    fromImage = fromImage.resize((170,170),Image.ANTIALIAS)
    toImage.paste(fromImage,(cur_x,cur_y))
    
    # 第二行 横
    cur_x -= 170
    cur_y += 170
    for i in range(2,9):
        fromImage = Image.open(r"upload/%s/%s.jpg" % (code,str(i)))
        fromImage = fromImage.resize((170, 170), Image.ANTIALIAS)
        toImage.paste(fromImage, (cur_x, cur_y))
        cur_x += 170
    
    # 第三行 两点
    cur_x = 310
    cur_y += 170
    fromImage = Image.open(r"upload/%s/9.jpg" % code)
    fromImage = fromImage.resize((170,170),Image.ANTIALIAS)
    toImage.paste(fromImage,(cur_x,cur_y))
    cur_x += 4*170
    fromImage = Image.open(r"upload/%s/10.jpg" % code)
    fromImage = fromImage.resize((170,170),Image.ANTIALIAS)
    toImage.paste(fromImage,(cur_x,cur_y))
    
    # 第四行 横
    cur_x -= 2*170
    cur_y += 170
    for i in range(11,16):
        fromImage = Image.open(r"upload/%s/%s.jpg" % (code,str(i)))
        fromImage = fromImage.resize((170, 170), Image.ANTIALIAS)
        toImage.paste(fromImage, (cur_x, cur_y))
        cur_x += 170
    
    # 第五行 两点
    cur_x = 650
    cur_y += 170
    fromImage = Image.open(r"upload/%s/16.jpg" % code)
    fromImage = fromImage.resize((170,170),Image.ANTIALIAS)
    toImage.paste(fromImage,(cur_x,cur_y))
    cur_x += 2*170
    fromImage = Image.open(r"upload/%s/17.jpg" % code)
    fromImage = fromImage.resize((170,170),Image.ANTIALIAS)
    toImage.paste(fromImage,(cur_x,cur_y))
    
    # 第六行 横
    cur_x = 310
    cur_y += 170
    for i in range(18,26):
        fromImage = Image.open(r"upload/%s/%s.jpg" % (code,str(i)))
        fromImage = fromImage.resize((170, 170), Image.ANTIALIAS)
        toImage.paste(fromImage, (cur_x, cur_y))
        cur_x += 170
    
    # 第七行 点
    cur_x = 650+2*170
    cur_y += 170
    fromImage = Image.open(r"upload/%s/26.jpg" % code)
    fromImage = fromImage.resize((170,170),Image.ANTIALIAS)
    toImage.paste(fromImage,(cur_x,cur_y))
    
    # 第八行 点
    cur_y += 170
    fromImage = Image.open(r"upload/%s/27.jpg" % code)
    fromImage = fromImage.resize((170,170),Image.ANTIALIAS)
    toImage.paste(fromImage,(cur_x,cur_y))
    
    # 边框
    fromImage = Image.open(r"upload/raw/bg.png")
    r,g,b,a = fromImage.split()
    toImage.paste(fromImage,(0,0),mask=a)
    save_path = os.path.join('upload', code, 'final.png').replace('\\', '/')
    toImage.show()
    toImage.save(save_path, quality=95)