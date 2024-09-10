from django.shortcuts import render

def show_main(request):
    context = {
        'name_store': 'cutieshop',
        'name' : 'Nabilah Devina Mumin' ,
        'class': 'PBP B',
    }

    return render(request, "main.html", context)
