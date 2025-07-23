from django.db import models
from django.contrib.auth.models import User

class CustomOrder(models.Model):
    PRODUCT_CHOICES = [
        ('saree', 'Saree'),
        ('shirt', 'Shirt'),
        ('dhothi', 'Dhothi'),
    ]
    SIZE_CHOICES = [
        ('S', 'Small'), ('M', 'Medium'), ('L', 'Large'),
        ('XL', 'XL'), ('XXL', 'XXL'), ('XXXL', 'XXXL'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    product_type = models.CharField(max_length=20, choices=PRODUCT_CHOICES)
    fabric_type = models.CharField(max_length=100, blank=True)

    color_preferences = models.JSONField(blank=True, null=True)
    color_reference_image = models.ImageField(upload_to='color_refs/', blank=True, null=True)

    style_pattern = models.CharField(max_length=100, blank=True)
    sample_design = models.ImageField(upload_to='design_samples/', blank=True, null=True)

    size = models.CharField(max_length=10, choices=SIZE_CHOICES, blank=True)
    size_chart = models.FileField(upload_to='size_charts/', blank=True, null=True)

    brand_label = models.BooleanField(default=False)
    quantity = models.PositiveIntegerField()
    preferred_delivery_date = models.DateField()
    budget = models.DecimalField(max_digits=10, decimal_places=2)

    additional_instructions = models.TextField(blank=True)
    status = models.CharField(max_length=20, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order by {self.user.username} ({self.product_type})"
