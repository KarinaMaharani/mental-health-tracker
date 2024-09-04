from django.shortcuts import render

# Create your views here.

def show_main(request):
    context = {
        'npm' : '2306165736',
        'name': 'Karina Maharani',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)