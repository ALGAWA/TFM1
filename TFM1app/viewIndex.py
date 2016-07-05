from django.shortcuts import render

def Index(request):
    return render(request, 'TFM1app/Index.html', {})