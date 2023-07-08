from django.http import Http404, HttpResponse
from django.shortcuts import redirect, render,HttpResponse
from .models import makeurl
import random
# Create your views here.
def home(request):
    return render(request,'home.html')

def urlshort(request):
    longurl = request.POST.get('longurl')
    lu = getlist("longurl")
    if longurl in lu:
        ldata = makeurl.objects.get(longurl = longurl)
        surl = ldata.shorturl
        shorturl = "http://127.0.0.1:8000/"+surl
        #return HttpResponse("your shorted url for {} is {}".format(longurl,shorturl))
        return render(request,'home.html',{"data": shorturl})
    t = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ*&%$@!"
    shorturl = ("".join(random.sample(t,7)))
    su = getlist("shorturl")
    print(su)
    if shorturl in su:
        shorturl = forrepeat(longurl,t,su)
    makeurl.objects.create(shorturl=shorturl,longurl=longurl)
    shorturl = "http://127.0.0.1:8000/"+shorturl
    #return HttpResponse("your shorted url for {} is {}".format(longurl,shorturl))
    return render(request,'home.html',{"data": shorturl})

def toshort(request,shorturl):
    try:
        obj = makeurl.objects.get(shorturl=shorturl)
        longurl = obj.longurl
        obj.count += 1
        obj.save()
        return redirect(longurl)
    except:
        raise Http404

def forrepeat(longurl, t, li):
    #t = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ*&%$@!"
    shorturl = ("".join(random.sample(t,7)))
    if shorturl in li:
        shorturl = forrepeat(longurl,t,li)
    return shorturl
    
def getlist(url):
    li = []
    alldata = makeurl.objects.all()
    alldata = alldata.values()
    alldata = list(alldata)
    for single in alldata:
        li.append(single[url])
    return li