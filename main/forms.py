from django.forms import ModelForm
from main.models import item

class ProductForm(ModelForm):
    class Meta:
        model = item
        fields = ["name", "amount", "description", "price", "image_url"]