from django.db import models
from django.urls import reverse
from category.models import Category

# Create your models here.
class Product(models.Model):
    product_name = models.CharField('désignation du produit', max_length=200, unique=True)
    slug = models.SlugField(max_length=400, unique=True)
    description = models.TextField(max_length=2000)
    images = models.ImageField(upload_to='photos/products')
    price = models.IntegerField('prix')
    stock = models.IntegerField('stock dispo')
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='catégorie')
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.product_name
    
    class Meta:
        verbose_name = 'produit'
    
    def get_url(self):
        return reverse('prod-detail-page', args=[self.category.slug, self.slug])

