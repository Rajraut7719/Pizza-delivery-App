from django.shortcuts import redirect, render
from .models import *
from django.contrib import messages
from django.contrib.auth import login,authenticate
# Create your views here.
def home(request):
    pizza=Pizza.objects.all()
    return render(request,'home.html',{'pizza':pizza})

def login_page(request):
    if request.method=='POST':
        try:
            username=request.POST.get('username')
            password=request.POST.get('password')
            user_obj=User.objects.filter(username=username)
            if not user_obj.exists():
                messages.warning(request, 'User not found.')
                return redirect('/login/')
            user_obj=authenticate(username=username,password=password)
            if user_obj:
                login(request,user_obj)
                return redirect('/')

            messages.error(request, 'Wrong password.')
            return redirect('/login/')
        except Exception as e:
            messages.error(request, 'Something went wrong.')
            return redirect('/register/')
    return render(request,'login.html')

def register_page(request):
    if request.method=='POST':
        try:
            username=request.POST.get('username')
            password=request.POST.get('password')
            user_obj=User.objects.filter(username=username)
            if user_obj.exists():
                messages.error(request, 'Username is taken.')
                return redirect('/register/')
            user_obj=User.objects.create(username=username)
            user_obj.set_password(password)
            user_obj.save()

            messages.success(request, 'Account created.')
            return redirect('/login/')
        except Exception as e:
            messages.error(request, 'Something went wrong.')
            return redirect('/register/')

    return render(request,'register.html')



def add_card(request , pizza_uid):
    user=request.user
    pizza_obj=Pizza.objects.get(uid=pizza_uid)
    card , _ =Cart.objects.get_or_create(user=user,is_paid=False)
    card_items=CardItems.objects.create(
        card=card,
        pizza=pizza_obj
    )
    return redirect('/')

def cart(request):
    cart=Cart.objects.get(is_paid=False,user=request.user)
    return render(request,'cart.html',{cart:'cart'})