from django.db import models
from django.forms import ModelForm
from django.db.models.functions import Now

class Item(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    cost = models.FloatField()

    def __str__(self):
        return "{} (${})".format(self.name, self.cost)

class Room(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Room_Item(models.Model):
    id = models.IntegerField(primary_key=True)
    room = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True)
    item = models.ForeignKey(Item, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return "Room: {}, Item: {}".format(self.room, self.item)

class Department(models.Model):
    cost_center = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    favorite = models.CharField(null=True, max_length=100)

    def __str__(self):
        return self.name

class Employee(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    dept = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

#=========================================================================================

class Purchase(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)
    dept = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)

class Room_Item_Purchase(models.Model):
    purchase = models.ForeignKey(Purchase, on_delete=models.SET_NULL, null=True)
    room_item = models.ForeignKey(Room_Item, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=1)

#===========================================================================================

class SimplePurchase(models.Model):
    created_at = models.DateTimeField(db_default=Now(), primary_key=True)
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)
    dept = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    room_item = models.ForeignKey(Room_Item, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=1)

class SimplePurchaseForm(ModelForm):
    class Meta:
        model = SimplePurchase
        fields = ["employee", "dept", "room_item", "quantity"]

#===========================================================================================

class PurchaseForm(ModelForm):
    class Meta:
        model = Purchase
        fields = ["employee", "dept"]
