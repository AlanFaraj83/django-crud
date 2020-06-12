from django.forms import ModelForm

from products.models import Products

class ProductForm(ModelForm):
    class Meta:
        model = Products
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super(ProductForm,self).__init__(*args,**kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs={
                'class': 'form-control'
            }