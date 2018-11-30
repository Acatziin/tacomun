from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    #attributes definition
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    phone = models.CharField(max_length=12)
    postal_code = models.IntegerField(null=False)
    birthday = models.DateField()

    def __str__(self):
        return self.user

class Category(models.Model):
    name = models.CharField(max_length=45)

    def __str__(self):
        return self.name

class Place(models.Model):
    #attributes definition
    name = models.CharField(max_length=45, unique=True, null=False)
    state = models.CharField(max_length=45)
    city = models.CharField(max_length=45)
    postal_code = models.IntegerField(null=False)
    categories = models.ManyToManyField(Category) #Creación de relación muchos a muchos simple
    eval = models.ManyToManyField(User, through='EvalPlace') #Relación muchos a muchos a través de una tercer tabla

    def __str__(self):
        return self.name

class EvalPlace(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    price = models.IntegerField(null=False)
    score = models.IntegerField(null=False)
    comment = models.TextField()

    def __str__(self):
        return 'score: {}'.format(self.score)