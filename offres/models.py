from django.db import models
from django.contrib.auth.models import User


class Offre(models.Model):
    titre = models.CharField(max_length=200)
    description = models.TextField()
    nb_poste = models.IntegerField(null=False, default=1) 
    entreprise = models.ForeignKey(User, related_name='entreprise', on_delete=models.CASCADE, null=True)
    masqué=models.BooleanField(default=False)
    def __str__(self):
        return self.titre

class Condidature(models.Model):
    nom = models.CharField(max_length=200)
    prenom = models.CharField(max_length=200)
    email = models.EmailField()
    CV = models.FileField(upload_to='CvExtractor')
    offre = models.ForeignKey(Offre, related_name='condidatures', on_delete=models.CASCADE, null=True)
    etat = models.IntegerField(default=0)
    mobile_number = models.TextField( default='0', null=True)
    college_name = models.TextField( default='0', null=True)
    company_names = models.TextField(default='0', null=True)
    degree = models.CharField(max_length=200, default='0', null=True)
    designation = models.CharField(max_length=200, default='0', null=True)
    skills = models.TextField(default='0', null=True)
    total_experience = models.IntegerField(default=0, null=True)
    experience = models.TextField( default='0', null=True) 
    def __str__(self):
        return self.nom
