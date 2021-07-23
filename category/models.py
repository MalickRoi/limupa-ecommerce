from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    category_name = models.CharField('catégorie', max_length=50, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    cat_image = models.ImageField(upload_to='photos/categories', blank=True)
    
    def __str__(self):
        return self.category_name
    
    class Meta:
        verbose_name = 'catégorie'
    
    def get_url(self):
        return reverse('cat-products-page', args=[self.slug])

