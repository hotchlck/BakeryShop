from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name': 'Salma Kurnia Dewi',
        'class': 'PBP B',
        'product' : 'BakeryShop'
    }

    return render(request, "main.html", context)