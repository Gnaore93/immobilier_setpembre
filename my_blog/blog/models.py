from django.db import models




# Create your models here.
        
class Categorie(models.Model):
    nom = models.CharField(max_length=200)
    
    def __str__(self):
        return self.nom

class Habitat(models.Model):
    title = models.CharField(max_length=200)
    categorie= models.ForeignKey('Categorie',related_name='categorie_Habitat',on_delete=models.SET_NULL, null=True)
    desc = models.TextField()
    prix = models.DecimalField(max_digits=100000,decimal_places=2,default=1500000)
    image = models.ImageField()
    date_create = models.DateTimeField(auto_now_add=True)
    date_modif = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Rdv_Client(models.Model):
    nom = models.CharField(max_length=200,blank=False)
    ville = models. CharField(max_length=200)
    quartier = models.CharField(max_length=500)
    job = models.CharField(max_length=200)
    telephone = models.IntegerField(blank=False)
    date_rdv = models.DateTimeField(auto_now_add=False,blank=False)
    email = models.EmailField(max_length=200,blank=False,unique=True)
    date_create = models.DateTimeField(auto_now_add=True)
    date_modif = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nom


    


    




















