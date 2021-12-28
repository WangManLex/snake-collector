from django.db import models
from django.urls import reverse

class Snake(models.Model):
   name = models.CharField(max_length=100)
   breed = models.CharField(max_length=100)
   description = models.TextField(max_length=250)
   age = models.IntegerField()

   def __str__(self):
      return self.name

   def get_absolute_url(self):
      return reverse("snakes_detail", kwargs={"snake_id": self.id})

MEALS = (
   ('B', 'Breakfast'),
   ('L', 'Lunch'),
   ('D', 'Dinner')
)

class Feeding(models.Model):
   date = models.DateField('Feeding Date')
   meal = models.CharField(
      max_length=1,
      choices=MEALS,
      default=MEALS[0][0]
   )
   
   snake = models.ForeignKey(Snake, on_delete=models.CASCADE)
   
   def __str__(self):
      return f"{self.get_meal_display()} on {self.date}"
   