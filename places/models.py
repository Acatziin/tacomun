from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    #attributes definition
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    phone = models.CharField(max_length=12)
    postal_code = models.IntegerField(null=False)
    birthday = models.DateField()
    friends = models. ManyToManyField('self', through='Friend', symmetrical=False)
    
    def __str__(self):
        return self.user.username

class Friend(models.Model):
    user = models.ForeignKey(Profile, related_name='related_user', on_delete = models.CASCADE)
    friend = models.ForeignKey(Profile, related_name='friend', on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user

class Category(models.Model):
    name = models.CharField(max_length=45)

    def __str__(self):
        return self.name

class Place(models.Model):
    #attributes definition
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=45, unique=True, null=False)
    state = models.CharField(max_length=45)
    city = models.CharField(max_length=45)
    postal_code = models.IntegerField(null=False)
    categories = models.ManyToManyField(Category) #Creación de relación muchos a muchos simple
    evaluations = models.ManyToManyField(User, through='EvalPlace', related_name='evaluations') #Relación muchos a muchos a través de una tercer tabla

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