from django.shortcuts import render

# Create your views here.
from HomeApp.models import SxsdWheel, SxsdNav, SxsdMustbuy, SxsdMainShow


def home(request):
    wheels = SxsdWheel.objects.all()
    navs = SxsdNav.objects.all()
    mustbuys = SxsdMustbuy.objects.all()
    mainshows = SxsdMainShow.objects.all()

    return render(request,'sxsd/main/home/home.html',context=locals())