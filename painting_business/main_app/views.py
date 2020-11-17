from django.shortcuts import render, Http404
from .models import painting_information
# Create your views here.


def home_view(request, *args, **kwargs):
    print(args,kwargs)
    print(request.user)
    paintings = painting_information.objects.all()
    return render(request,"shop.html",{'paintings' : paintings})

def product_view(request,slug):
    print(slug)
    try:
        painting = painting_information.objects.get(slug=slug)
        return render(request, 'shop-details.html', {'painting': painting})
    except:
        raise Http404



