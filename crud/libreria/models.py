from django.db import models

class Book(models.Model):
    id = models.AutoField(primary_key = True)
    title = models.CharField(max_length=100, verbose_name = 'Título')
    image = models.ImageField(upload_to='images/', verbose_name = 'Imagen', null = True)
    description = models.TextField(verbose_name = 'Descripción', null=True)

    def __str__(self):
        row = "Título: " + self.title + " - " + "Descripción: " + self.description
        return row

    def delete(self, using=None, keep_parents=False):
        self.image.storage.delete(self.image.name)
        super().delete()