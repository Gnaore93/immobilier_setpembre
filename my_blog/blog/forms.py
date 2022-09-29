from turtle import title
from django import forms
from .models import Habitat,Rdv_Client

class habitatForm(forms.ModelForm):
    class Meta:
        model = Habitat
        fields = ['title','categorie','desc','prix','image']
        labels = {'titre':'Titre','categorie':'Catégorie','desc':'Descrition','prix':'Prix','image':'Image'}
        widgets ={
            'title':forms.TextInput(attrs = {'class':'form-control'}),
            'categorie':forms.Select(attrs = {'class':'form-control'}),
            'desc':forms.TextInput(attrs = {'class':'form-control'}),
            'prix':forms.TextInput(attrs = {'class':'form-control', 'rows':5}),
        }

class RdvForm(forms.ModelForm):
    class Meta:
        model = Rdv_Client
        fields = ['nom','ville','quartier','job','telephone','date_rdv','email']
        
