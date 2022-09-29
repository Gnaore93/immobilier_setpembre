

from django.shortcuts import render
from django.views.generic.edit import UpdateView,CreateView,DeleteView
from blog.models import Habitat, Rdv_Client
from blog.forms import habitatForm,RdvForm



# Create your views here.
def home(request):
    list_habitats = Habitat.objects.all()
    return render(request,"index.html",locals())

def detail(request,id_habitat):
    detail_article = Habitat.objects.get(id=id_habitat)

    categorie= detail_article.categorie

    #print(categorie)

    relations  = Habitat.objects.filter(categorie=categorie)
    #print("########")
    #print(relations)
    return render(request,'detail.html',locals())

def liste_hbt(request):
    list_habitats = Habitat.objects.all()
    return render(request,'liste_habitat.html',locals())

def Achat_home(request):
    
    return render(request,'rdv.html')

class Ajout_Abitat(CreateView):
    model = Habitat
    form_class = habitatForm
    template_name = "ajout-habitat.html"
    success_url = "liste_hbt"

class Rendez_Vous_Client(CreateView):
    model = Rdv_Client
    form_class = RdvForm
    template_name = "rdv.html"
    success_url = "Rendez_Vous_Client"






    

    
        
