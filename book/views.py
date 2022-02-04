from django.shortcuts import render, redirect
from .models import Book
# Create your views here.
from django.utils import timezone

def create(request):
    if request.method == "POST":
        im = request.POST.get("impo")
        sn = request.POST.get("sname")
        su = request.POST.get("surl")
        sc = request.POST.get("scon")
        
        if sn and su and sc:
            if im:
                imp = True
            else:
                imp = False
            Book(site_name=sn, site_url=su, content=sc, user=request.user, impo=imp, pubdate=timezone.now()).save()
            return redirect("book:index")
    return render(request, "book/create.html")

def index(request):
    b = request.user.book_set.all().order_by('-pubdate')
    context = {
        "blist" : b
    }
    return render(request, "book/index.html", context)