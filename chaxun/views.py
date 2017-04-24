import string
from io import BytesIO
from django.shortcuts import render
import os
import random
from django.http import HttpResponse
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import chaxun.captcha


def captcha(request):
    """Captcha"""
    size = (120, 40)
    img, chars = chaxun.captcha.create(size=size)
    request.session['captcha'] = chars   # store the content in Django's session store
    buf = BytesIO()  # a memory buffer used to store the generated image
    img.save(buf, 'png')
    return HttpResponse(buf.getvalue(), 'image/png')  # return the image data stream as image/jpeg format, browser
    # will treat it as an image


def index(request):
    return render(request, 'chaxun/index.html')


def query(request):
    identify_number = request.POST['identify_number']
    name = request.POST['name']
    captcha_input = request.POST['captcha']
    del request.POST['captcha']
    if 'captcha' in request.session:
        captcha_stored = request.session['captcha']
        del request.session['captcha']
        if captcha_input.strip() == captcha_stored:
            return HttpResponse('account_numer')
    else:
        return HttpResponse('not found')


