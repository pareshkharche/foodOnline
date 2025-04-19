from django import forms

from accounts.validators import allow_only_images_validator
from .models import Category, FoodItem


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category_name', 'description']