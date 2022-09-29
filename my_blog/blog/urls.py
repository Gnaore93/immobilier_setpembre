from django.urls import path
from .import views
from .views import*
from blog.views import liste_hbt
urlpatterns = [
    path("",views.home,name="home"),
   

    #path("liste_hbt/",liste_hbt,name="liste_hbt"),
    
]