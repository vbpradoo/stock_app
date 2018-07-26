from django.forms import ModelForm

from .models import Lotes


class LotesForm(ModelForm):
    class Meta:
        model = Lotes
        exclude = ('date_created', 'date_updated', 'owner')