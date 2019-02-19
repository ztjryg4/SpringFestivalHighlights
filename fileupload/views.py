from django.shortcuts import render,render_to_response
from django import forms
from django.http import HttpResponse
from fileupload.models import RawImg
from fileupload.process import ImgProcess
from random import Random
import os
from PIL import Image
# Create your views here.


def random_str(randomlength=4):
    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        str+=chars[random.randint(0, length)]
    return str


def image_process(file, code, i):
    file_name = str(i)+ '.jpg'
    file_path = os.path.join('upload', code, file_name).replace('\\', '/')
    fromImg = Image.open(file)
    exif = fromImg._getexif()
    orientation_key = 274  # cf ExifTags
    if exif and orientation_key in exif:
        orientation = exif[orientation_key]
        rotate_values = {
            3: Image.ROTATE_180,
            6: Image.ROTATE_270,
            8: Image.ROTATE_90
        }
    if orientation in rotate_values:
        fromImg = fromImg.transpose(rotate_values[orientation])
    width, height = fromImg.size
    region = (0,0,0,0)
    if width - height > 5:
        region = (int((width - height) / 2), 0, int((width - height) / 2 + height), height)
    elif width - height < 5:
        region = (0, int((height - width) / 2), width, int((height - width) / 2 + width))
    fromImg = fromImg.crop(region)
    fromImg.save(file_path, quality=95)


class UserForm(forms.Form):
    # username = forms.CharField()
    # file_field = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
    img_01 = forms.ImageField(label='第1张图片',)
    img_02 = forms.ImageField(label='第2张图片',)
    img_03 = forms.ImageField(label='第3张图片',)
    img_04 = forms.ImageField(label='第4张图片',)
    img_05 = forms.ImageField(label='第5张图片',)
    img_06 = forms.ImageField(label='第6张图片',)
    img_07 = forms.ImageField(label='第7张图片',)
    img_08 = forms.ImageField(label='第8张图片',)
    img_09 = forms.ImageField(label='第9张图片',)
    img_10 = forms.ImageField(label='第10张图片',)
    img_11 = forms.ImageField(label='第11张图片',)
    img_12 = forms.ImageField(label='第12张图片',)
    img_13 = forms.ImageField(label='第13张图片', )
    img_14 = forms.ImageField(label='第14张图片', )
    img_15 = forms.ImageField(label='第15张图片', )
    img_16 = forms.ImageField(label='第16张图片', )
    img_17 = forms.ImageField(label='第17张图片', )
    img_18 = forms.ImageField(label='第18张图片', )
    img_19 = forms.ImageField(label='第19张图片', )
    img_20 = forms.ImageField(label='第20张图片', )
    img_21 = forms.ImageField(label='第21张图片', )
    img_22 = forms.ImageField(label='第22张图片', )
    img_23 = forms.ImageField(label='第23张图片', )
    img_24 = forms.ImageField(label='第24张图片', )
    img_25 = forms.ImageField(label='第25张图片', )
    img_26 = forms.ImageField(label='第26张图片', )
    img_27 = forms.ImageField(label='第27张图片', )


def upload(request):
    if request.method == 'POST':
        uf = UserForm(request.POST,request.FILES)
        # img = request.FILES.getlist('file_field')
        # if len(img) < 27:
        #     return HttpResponse('必须上传27张及以上的照片'+str(len(img)))
        if uf.is_valid():
            # 创建提取码
            flag = 0
            while(flag==0):
                code = random_str()
                if RawImg.objects.filter(code__startswith=code):
                    flag = 0
                else:
                    flag = 1
            new_dir = 'upload/'+code
            os.makedirs(new_dir)

            # 从表单获取图像数据
            img = []
            for i in range(1,28):
                if i<10 :
                    s_str = 'img_0'+str(i)
                else:
                    s_str = 'img_'+str(i)
                img.append(uf.cleaned_data[s_str])

            # 图像处理
            for i in range(1,28):
                image_process(img[i-1], code, i)

            # 记录提取码
            user = RawImg()
            user.code = code
            user.save()

            ImgProcess(code)
            return render_to_response('extraction.html',{'code':code})
    else:
        uf = UserForm()
    return render_to_response('index.html',{'uf':uf})


def extraction(request, code):
    if code == '0':
        return render_to_response('extraction.html', {'code': code})
    else:
        return render_to_response('show.html',{'code': code})

def codeprocess(request):
    code = request.POST.get('code')
    return render_to_response('show.html', {'code': code})