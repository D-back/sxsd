from django.shortcuts import render, redirect


# Create your views here.
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from UserApp.models import SxsdUser


def mine(request):
    user_id = request.session.get('user_id')
    if user_id:
        user1 = SxsdUser.objects.get(pk=user_id)
        context = {
            'user1':user1
        }
        return render(request,'sxsd/main/mine/mine.html',context=context)
    else:
        return render(request, 'sxsd/main/mine/mine.html')


