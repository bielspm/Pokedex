from django.db import models

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

class Pokemon(models.Model):
    pokemon_number = models.SmallIntegerField(primary_key=True)
    pokemon_name = models.CharField(unique=True, max_length=30)
    attack = models.SmallIntegerField()
    classfication = models.CharField(max_length=100)
    defense = models.SmallIntegerField()
    height_m = models.CharField(max_length=10, blank=True, null=True)
    hp = models.SmallIntegerField()
    speed = models.SmallIntegerField()
    type1 = models.CharField(max_length=15)
    type2 = models.CharField(max_length=15)
    weight_kg = models.CharField(max_length=10)
    generation = models.IntegerField()
    is_legendary = models.IntegerField()
    abilities = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pokemon'
