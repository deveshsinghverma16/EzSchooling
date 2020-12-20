from django.db import models


class pizzaModel(models.Model):
    typeOfPizza = models.CharField(max_length=1000)
    sizeOfPizza = models.CharField(max_length=1000)
    toppingOfPizza = models.CharField(max_length=1000)

    def __str__(self):
        return self.typeOfPizza

class pizzaSize(models.Model):
    sizeOfPizza = models.CharField(max_length=1000)
    def __str__(self):
        return self.sizeOfPizza

class pizzaTopping(models.Model):
    toppingOfPizza = models.CharField(max_length=1000)
    def __str__(self):
        return self.toppingOfPizza

class typeOfPizza(models.Model):
    typeOfPizza = models.CharField(max_length=1000)
    def __str__(self):
        return self.typeOfPizza


