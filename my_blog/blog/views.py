from django.shortcuts import render
from .models import Habitat

# Create your views here.
def home(request):
    list_habitats = Habitat.objects.all()
    context = {"liste_habitats":list_habitats}
    return render(request,"index.html",context)

def detail(request,id_habitat):
    detailarticle = Habitat.objects.get(id=id_habitat)
    return render(request,'detail.html', locals())