from django.db import models

class Item(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    cost = models.FloatField()

class Room(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)

class Room_Item(models.Model):
    id = models.IntegerField(primary_key=True)
    room = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True)
    item = models.ForeignKey(Item, on_delete=models.SET_NULL, null=True)

class Department(models.Model):
    cost_center = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    favorite = models.CharField(null=True, max_length=100)

class Employee(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    dept = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)

class Purchase(models.Model):
    id = models.IntegerField(primary_key=True)
    dept = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)

class Room_Item_Purchase(models.Model):
    purchase = models.ForeignKey(Purchase, on_delete=models.SET_NULL, null=True)
    room_item = models.ForeignKey(Room_Item, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=1)