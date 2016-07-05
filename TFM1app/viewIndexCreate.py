from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required
def IndexCrear(request):
    return render(request, 'TFM1app/IndexCrear.html', {})    