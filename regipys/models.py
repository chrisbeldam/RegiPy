from django.db import models

# Create your models here.

class Year(models.Model):
    year_one = "year_one"
    year_two = "year_two"
    year_three = "year_three"
    year_four = "year_four"
    year_group_choices = (
        (year_one, "year_one"),
        (year_two, "year_two"),
        (year_three, "year_three"),
        (year_four, "year_four"),
    )
    year_group = models.CharField(max_length = 30, choices = year_group_choices, default = year_one)

    class Meta:
        verbose_name_plural = "Years"

class Child(models.Model):
    """Class relating to Children"""
    year_group = models.ForeignKey(Year, on_delete = models.CASCADE)
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)

    class Meta:
        verbose_name_plural = "Children"
        
    def __str__(self):
        return self.text
