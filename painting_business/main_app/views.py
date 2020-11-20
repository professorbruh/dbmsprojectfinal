from django.shortcuts import render, Http404, redirect
from .models import painting_information
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import AnonymousUser
from .forms import  CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .filters import PaintFilter
# Create your views here.

def home_view(request, *args, **kwargs):
    print(args,kwargs)
    print(request.user)
    paintings = painting_information.objects.all()
    myfilter = PaintFilter(request.GET,queryset=paintings)
    paintings = myfilter.qs
    print(paintings)
    no_models = paintings.count()
    context = {'paintings': paintings,'myfilter': myfilter,'no_models': no_models}
    return render(request,"shop.html",context)

def product_view(request,slug):
    print(slug)
    try:
        painting = painting_information.objects.get(slug=slug)
        return render(request, 'shop-details.html', {'painting': painting})
    except:
        raise Http404
def index_view(request,*args,**kwargs):
    print(request.user)
    paintings = painting_information.objects.all()
    context = {'paintings':paintings}
    return render(request,"index.html",context)

def register_view(request):
    print(request.user)
    form = UserCreationForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(login_view)
    context = {'form': form}
    return render(request,"register.html",context)

def login_view(request):
    print(request.user)

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username = username, password = password)

        if user is not None:
            login(request,user)
            return redirect(home_view)
        else:
            messages.info(request,'Username or password is incorrect')
    return render(request,'login.html')
def logout_view(request):
    print(request.user)
    logout(request)
    return redirect(home_view)




