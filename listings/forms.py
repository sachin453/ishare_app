from django.forms import ModelForm
from .models import Listing

class ListingForm(ModelForm):
    class Meta:
        model = Listing
        fields = ['title', 'category', 'address', 'type', 'College', 'description', 'price', 'photo_main']
    
class UpdateForm(ModelForm):
    class Meta:
        model = Listing
        fields = ['title','description','price','photo_main']
