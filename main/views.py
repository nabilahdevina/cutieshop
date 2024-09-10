from django.shortcuts import render

def show_main(request):
    context = {
        'name_store': 'cutieshop',
        'name' : 'Nabilah Devina Mumin' ,
        'class': 'PBP B',
        'stock' : '30',
    }

    return render(request, "main.html", context)
