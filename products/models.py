from django.db import models


class Products(models.Model):
    
    name = models.CharField(max_length=54)
    slug = models.SlugField()

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"

    def __str__(self):
        return "{} - {}".format(self.name, self.slug)