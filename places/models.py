from django.db import models

# Create your models here.

class Person(models.Model):
    #attributes definition
    username = models.CharField(max_length=45, unique=True, null=False)
    name = models.CharField(max_length=45)
    lastname = models.CharField(max_length=45)
    email = models.EmailField(max_length=100, null=False)
    password = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    birthday = models.DateField()

    def __str__(self):
        return self.name

class Place(models.Model):
    #attributes definition
    place_name = models.CharField(max_length=45, unique=True, null=False)
    state = models.CharField(max_length=45)
    city = models.CharField(max_length=45)
    postal_code = models.IntegerField(null=False)
    clients = models.ManyToManyField(User, through='Eval_place')

    def __str__(self):
        return self.name

class Eval_place(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    price = models.IntegerField(null=False)
    score = models.IntegerField(null=False)
    comments =models.TextField()

   

class Category(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    category_name = models.CharField(max_length=45)

    def __str__(self):
        return self.name