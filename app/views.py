from django.shortcuts import render
from app.models import *

from django.http import HttpResponse
def form(request):
    return render(request,'form.html')

def insertTopic(request):
    if request.method=='POST':
        tn=request.POST['tn']
        TO=Topic.objects.get_or_create(topic_name=tn)
        return HttpResponse(f'{tn} is Created')
    return render(request,'insertTopic.html')

def insertwebpage(request):
    LTO=Topic.objects.all()
    d={'LTO':LTO}

    if request.method=='POST':
        tn=request.POST['tn']
        na=request.POST['na']
        em=request.POST['em']
        ur=request.POST['ur']

        TO=Topic.objects.get(topic_name=tn)

        WO=Webpage.objects.get_or_create(topic_name=TO,name=na,email=em,url=ur)
        return HttpResponse('Webpage is Created Successfully')
    return render(request,'insertwebpage.html',d)

def select_multiple(request):
    LTO=Topic.objects.all()
    d={'LTO':LTO}
    if request.method=='POST':
        MTN=request.POST.getlist('tn')
        print(MTN)
        EQST=Webpage.objects.none()
        for topic in MTN:
            EQST=EQST|Webpage.objects.filter(topic_name=topic)
        d1={'EQST':EQST}
        return render(request,'display_webpage.html',d1)


    return render(request,'select_multiple.html',d)

def checkbox(request):
    LTO=Topic.objects.all()
    d={'LTO':LTO}
    return render(request,'checkbox.html')