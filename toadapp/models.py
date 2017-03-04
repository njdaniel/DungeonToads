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
    # --- Attributes of Character -----
    name = models.CharField(max_length=200)
    points = models.CharField(max_length=20, default='20')
    strength = models.CharField(max_length=20, default='8')
    dexterity = models.CharField(max_length=20, default='8')
    constitution = models.CharField(max_length=20, default='8')
    intelligence = models.CharField(max_length=20, default='8')
    health = models.CharField(max_length=20, default='40')
    gender = models.CharField(max_length=1, choices=GENDERS, default='Male')
    race = models.CharField(max_length=1, choices=RACES, default='Toad')
    armour_class = models.IntegerField(default=10)

    def __str__(self):
        self.name


class Monsters(models.Model):

    type = models.CharField(max_length=200)
    health = models.CharField(max_length=20, default='20')
    strength = models.CharField(max_length=20, default='8')
    dexterity = models.CharField(max_length=20, default='8')
    constitution = models.CharField(max_length=20, default='8')
    intelligence = models.CharField(max_length=20, default='8')
    actions = models.CharField(max_length=200)
    armour_class = models.IntegerField(default=10)
