from .models import Category,Subcategory
from django import forms


class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields=('catid','name')



class SubCategoryForm(forms.ModelForm):
    class Meta:
        model=Subcategory
        fields=('subcatid','name')
