
from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.

class BaseModel(models.Model):
    uid=models.UUIDField(default=uuid.uuid4,editable=False,primary_key=True)
    created_at=models.DateField(auto_now_add=True)
    updated_at=models.DateField(auto_now_add=True)

    class Meta:
        abstract=True
class PizzaCategory(BaseModel):
    category_name=models.CharField(max_length=100)

class Pizza(BaseModel):
    category=models.ForeignKey(PizzaCategory,on_delete=models.CASCADE,related_name='pizzas')
    pizza_name=models.CharField(max_length=100)
    price=models.IntegerField(default=100)
    imge=models.ImageField(upload_to="pizza")


class Cart(BaseModel):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,related_name='cards')
    is_paid=models.BooleanField(default=False)

class CardItems(BaseModel):
    card=models.ForeignKey(Cart,on_delete=models.CASCADE,related_name='card_items')
    pizza=models.ForeignKey(Pizza,on_delete=models.CASCADE)

