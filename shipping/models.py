from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)

    length_cm = models.DecimalField(max_digits=8, decimal_places=2)  # cm
    width_cm = models.DecimalField(max_digits=8, decimal_places=2)   # cm
    height_cm = models.DecimalField(max_digits=8, decimal_places=2)  # cm

    weight_kg = models.DecimalField(max_digits=8, decimal_places=2)  # kg

    def __str__(self):
        return self.name

class Box(models.Model):
    name = models.CharField(max_length=100)

    length_cm = models.FloatField()
    width_cm = models.FloatField()
    height_cm = models.FloatField()

    max_weight_kg = models.FloatField()

    cost = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    def __str__(self):
        return self.name

class Order(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Order {self.id}"

class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )

    quantity = models.PositiveIntegerField()