from django.db import models


# Qurilish sharoitlari modeli
class Condition(models.Model):
    name = models.CharField(max_length=100, unique=True)


# Qurilish materiallari modeli
class Material(models.Model):
    condition = models.ForeignKey(Condition, on_delete=models.CASCADE, related_name='materials')
    name = models.CharField(max_length=100)


# Qurilish turini saqlash modeli
class ConstructionType(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()


# Qurilish materiallarining narxlari jadvali
class MaterialPricing(models.Model):
    material = models.ForeignKey(Material, on_delete=models.CASCADE, related_name='pricing')
    price_per_unit = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=10)
