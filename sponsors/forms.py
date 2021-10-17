from .models import Sponsor
from django.forms import ModelForm

class SponsorForm(ModelForm):
    class Meta:
        model = Sponsor
        fields = "__all__"