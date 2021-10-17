from django.shortcuts import redirect, render
from .models import Sponsor
from .forms import SponsorForm
from django.contrib.messages import error, success
# Create your views here.
def sponsors_view(request):
    sponsors = Sponsor.objects.all()
    context = {
        'sponsors': sponsors
    }
    return render(request, 'sponsors/sponsors.html', context=context)


def create_sponsor_view(request):
    sponsor_form = SponsorForm()
    if request.method == 'POST':
        sponsor_form = SponsorForm(request.POST)
        if sponsor_form.is_valid():
            sponsor_form.save()
            success(request, 'Sponsor Created successfully.')
            redirect('sponsors-view')
    context = {
        'form': sponsor_form
    }
    return render(request, 'sponsors/create_sponsor.html', context)