from django.shortcuts import render
# Create
def Index(request):
    return render(request, 'TFM1app/Index.html', {})