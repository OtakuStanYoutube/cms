from django.shortcuts import render
from .models import Sponsors

# Create your views here.
def sponsors_view(request):
    sponsors = Sponsors.objects.all()
    context = {
        'sponsors': sponsors
    }
    return render(request, 'sponsors/sponsors.html', context=context)