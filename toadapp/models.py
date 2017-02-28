from django.db import models

# Create your models here.
class CharacterAttributes(models.Model):

    GENDERS = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    RACES = (
        ('H','Human'),
        ('D', 'Dwarf'),
        ('E', 'Elf'),
        ('T', 'Toad')

    )

    name = models.CharField(max_length=200)
    points = models.CharField(max_length=200)
    strength = models.CharField(max_length=200)
    dexterity = models.CharField(max_length=200)
    constitution = models.CharField(max_length=200)
    intelligence = models.CharField(max_length=200)
    health = models.CharField(max_length=200)
    gender = models.CharField(max_length=1, choices=GENDERS)
    race = models.CharField(max_length=1, choices=RACES)