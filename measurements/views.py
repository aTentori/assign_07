from django.shortcuts import render
from measurements.models import Area


# Create your views here.
def index(request):
    all_areas = Area.objects.all()
    context = {
        'all_areas': all_areas
    }
    return render(request, 'measurements/index.html', context)
