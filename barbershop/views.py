from django.shortcuts import render


def home(request):
    return render(request, 'barbershop/pages/home.html', context={
        'name': 'Vinícius Franco',
    })

def contact(request):
    pass