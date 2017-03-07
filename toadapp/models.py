from django.db import models


class Attacks(models.Model):
    name = models.CharField(max_length=200)
    damage = models.CharField(max_length=20)

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
    points = models.IntegerField(default=20)
    strength = models.IntegerField(default=8)
    dexterity = models.IntegerField(default=8)
    constitution = models.IntegerField(default=8)
    intelligence = models.IntegerField(default=8)
    health = models.IntegerField(default=40)
    max_health = models.IntegerField(default=40)
    gender = models.CharField(max_length=1, choices=GENDERS, default='Male')
    race = models.CharField(max_length=1, choices=RACES, default='Toad')
    armour_class = models.IntegerField(default=10)
    attacks = models.ManyToManyField(Attacks)

    def __str__(self):
        self.name


class Monsters(models.Model):

    type = models.CharField(max_length=200)
    health = models.IntegerField(default=20)
    strength = models.IntegerField(default=8)
    dexterity = models.IntegerField(default=8)
    constitution = models.IntegerField(default=8)
    intelligence = models.IntegerField(default=8)
    attacks = models.ManyToManyField(Attacks)
    armour_class = models.IntegerField(default=10)
    max_health = models.IntegerField(default=20)

