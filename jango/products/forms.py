from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    title       = forms.CharField(required=True)
    description = forms.CharField(initial="some Desc", 
                        widget=forms.Textarea(
                            attrs = {
                                "cols": 80,
                            }
                        ))
    price       = forms.DecimalField(decimal_places=2)

    class Meta:
        model = Product
        fields = [
            "title",
            "description",
            "price",
        ]

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")
        if ("T" in title):
            return title
        else:
            raise forms.ValidationError("NOT vali")


class RawProductForm(forms.Form):
    title       = forms.CharField(required=True)
    description = forms.CharField(initial="Init Desc", 
                        widget=forms.Textarea(
                            attrs = {
                                "cols": 100,
                            }
                        ))
    price       = forms.DecimalField()