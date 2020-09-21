import datetime
import hashlib
import random
import uuid

from io import BytesIO

from PIL import Image, ImageFont
from PIL.ImageDraw import ImageDraw
from django.contrib.auth.hashers import make_password,check_password
from django.core.cache import cache

from django.core.mail import send_mail
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.template import loader
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from UserApp.models import SxsdUser
from sxsd import settings


@csrf_exempt
def register(request):
    if request.method == 'POST':
        usernane = request.POST.get('username')
        password = request.POST.get('password')
        password = make_password(password)
        email = request.POST.get('email')
        head = request.FILES.get('head')
        u_token = uuid.uuid4()

        user = SxsdUser()
        user.username = usernane
        user.password = password
        user.email = email
        user.head = head
        user.token = u_token
        user.save()
        cache.set(u_token, user.id, timeout=60)
        active_user(usernane, email, u_token)
        # return HttpResponse('注册成功')

        return redirect(reverse('sxsduser:login'))

    else:
        return render(request, 'sxsd/user/register/register.html')


#  登录
@csrf_exempt
def login(request):
    if request.method == 'POST':
        verify_code = request.session.get('verify_code')
        check_code = request.POST.get('check_code')
        if verify_code.lower() == check_code.lower():
            username = request.POST.get('username')
            user = SxsdUser.objects.filter(username=username)
            if not user.count:
                context = {
                    'err': '用户名或密码错误'
                }
                return render(request, 'sxsd/user/login/login.html', context=context)
            else:
                password = request.POST.get('password')
                if check_password(password,user[0].password):
                    request.session['user_id'] = user[0].id
                    return redirect(reverse('sxsdmine:mine'))
                else:
                    context = {
                        'err': '用户名或密码错误'
                    }
                    return render(request, 'sxsd/user/login/login.html', context=context)
        else:
            context = {
                'err': '验证码错误'
            }
            return render(request, 'sxsd/user/login/login.html', context=context)
    else:
        return render(request, 'sxsd/user/login/login.html')


#  登出
def logout(request):
    request.session.flush()
    return redirect(reverse('sxsdmine:mine'))


#  获取验证码
def get_code(request):
    # 初始化画布，初始化画笔
    mode = "RGB"

    size = (100, 50)

    red = get_color()

    green = get_color()

    blue = get_color()

    color_bg = (red, green, blue)

    image = Image.new(mode=mode, size=size, color=color_bg)

    imagedraw = ImageDraw(image, mode=mode)

    imagefont = ImageFont.truetype(settings.FONT_PATH, 50)

    verify_code = generate_code()

    request.session['verify_code'] = verify_code

    for i in range(4):
        fill = (get_color(), get_color(), get_color())
        imagedraw.text(xy=(20 * i, 0), text=verify_code[i], font=imagefont, fill=fill)

    for i in range(100):
        fill = (get_color(), get_color(), get_color())
        xy = (random.randrange(100), random.randrange(50))
        imagedraw.point(xy=xy, fill=fill)

    fp = BytesIO()

    image.save(fp, "png")

    return HttpResponse(fp.getvalue(), content_type="image/png")


# 获取验证码的颜色
def get_color():
    return random.randrange(256)


# 获取四位验证码
def generate_code():
    source = "qwertyuiopasdfghjklzxcvbnm1234567890QWERTYUIOPASDFGHJKLZXCVBNM"
    code = ""
    for i in range(4):
        code += random.choice(source)
    return code


@csrf_exempt
def ajax_username(request):
    '''   判断用户名是否存在   '''
    username = request.POST.get('username')
    try:
        user = SxsdUser.objects.filter(username=username)[0]
        print(user.username)

        msg = {
            'flag': True
        }
        return JsonResponse(msg)
    except Exception:
        msg = {
            'flag': False
        }
        return JsonResponse(msg)


#  邮箱激活
def active_user(username, email, u_token):
    active_hitml = loader.get_template('sxsd/user/register/active.html')
    context = {
        'username': username,
        'url': f'http://49.235.252.5:8000/sxsduser/active/?xxxx={u_token}'
    }
    active_hitml_value = active_hitml.render(context)
    subject = '大世界开业大酬宾'
    html_massage = active_hitml_value
    from_email = 'dback96@163.com'
    recipient_list = [email]
    send_mail(subject=subject, message='', html_message=html_massage, from_email=from_email,
              recipient_list=recipient_list)


#  邮箱激活动作
def active(request):
    u_token = request.GET.get('xxxx')
    user_id = cache.get(u_token)
    if user_id:
        user = SxsdUser.objects.filter(token=u_token)[0]
        if not user.active:
            user.active = True
            user.save()
            return HttpResponse('激活成功')
        else:
            cache.delete(u_token)
            return HttpResponse('已激活，不需要再次激活')
    else:
        return HttpResponse('邮件已失效，请重新发送')
