from django.db import models
from django.forms import ModelForm
from django.db.models.functions import Now
'''
class Department(models.Model):
    cost_center = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
'''
class Item(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    cost = models.FloatField()

    def __str__(self):
        return "{} (${})".format(self.name, self.cost)
'''

class Employee(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

#=========================================================================================

class Purchase(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)

class Item_Purchase(models.Model):
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE, null=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField(default=1)

#===========================================================================================

class SimplePurchase(models.Model):
    created_at = models.DateTimeField(db_default=Now(), primary_key=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField(default=1)


class SimplePurchaseForm(ModelForm):
    class Meta:
        model = SimplePurchase
        fields = ["employee", "dept", "item", "quantity"]
    def clean(self):
        cleaned_data = super().clean()
        cleaned_data["quantity"] = 2
        return cleaned_data


#===========================================================================================

class PurchaseForm(ModelForm):
    class Meta:
        model = Purchase
        fields = ["employee", "dept"]

class Item_Purchase_Form(ModelForm):
    class Meta:
        model = Item_Purchase
        fields = ["purchase", "item", "quantity"]

class RIPF(Item_Purchase_Form):
    def clean(self):
        cleaned_data = super().clean()
        cleaned_data["purchase"] = 1
        return cleaned_data
'''