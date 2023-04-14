from django.shortcuts import render


def home(request):
    return render(request, 'barbershop/pages/home.html')

def contact(request):
    return render(request, 'barbershop/pages/contact.html')