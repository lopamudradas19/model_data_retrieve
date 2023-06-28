from django.shortcuts import render

# Create your views here.
from app.models import *
from django.db.models.functions import Length
def display_topic(request):
    T=Topic.objects.all()
    T=Topic.objects.filter(Topic_name='cricket')

    D={'sr':T}
    return render(request,'display_topic.html',D)

def display_webpage(request):
    T=Webpage.objects.all()
    T=Webpage.objects.filter(Topic_name='football')
    T=Webpage.objects.all()[3::]
    T=Webpage.objects.all()[::-1]
    T=Webpage.objects.all().order_by('name')
    T=Webpage.objects.all().order_by('-name')
    T=Webpage.objects.all().order_by(Length('name'))
    T=Webpage.objects.all().order_by(Length('name').desc())
    T=Webpage.objects.filter(url__startswith='http')
    T=Webpage.objects.all()
    T=Webpage.objects.filter(name__startswith='d')
    T=Webpage.objects.all()
    T=Webpage.objects.filter(name__contains='i')
    T=Webpage.objects.filter(url__contains='com')

    d={'pq':T}
    return render(request,'display_webpage.html',d)


def display_access(request):
    ao=AccessRecords.objects.all()
    ao=AccessRecords.objects.filter(name__contains='i')

    d={'accessrecords':ao}
    return render(request,'display_access.html',d)