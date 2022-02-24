from django import forms

class IngredientForm(forms.Form):
    ingredients = forms.CharField(max_length=None, widget=forms.Textarea)