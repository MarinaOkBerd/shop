import datetime

from django import forms


class ProductFormWidget(forms.Form):
    title = forms.CharField(max_length=100,
                            widget=forms.TextInput(attrs={'class': 'form-control',
                                                          'placeholder': 'название товара'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control',
                                                               'placeholder': 'описание товара'}))
    price = forms.FloatField(min_value=100, max_value=10_000,
                             widget=forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01',
                                                             'placeholder': 'стоимость товара'}))
    amount = forms.IntegerField(min_value=0, max_value=100,
                                widget=forms.NumberInput(attrs={'class': 'form-control',
                                                                'placeholder': 'товар в наличии'}))
    date_added = forms.DateField(initial=datetime.date.today,
                                 widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date',
                                                               'placeholder': 'дата добавления товара'}))
    image = forms.ImageField(widget=forms.FileInput())