from django.db import models

class Photography(models.Model):
    OPTIONS_CATEGORY = [
        ('NEBULOSA', 'Nebulosa'),
        ('ESTRELA', 'Estrela'),
        ('GALÁXIA', 'Galáxia'),
        ('PLANETA', 'Planeta'),
    ]

    name = models.CharField(max_length=100, null=False, blank=False)
    caption = models.CharField(max_length=150, null=False, blank=False)
    category = models.CharField(max_length=100, choices=OPTIONS_CATEGORY, default='')
    description = models.TextField(null=True, blank=True)
    photo = models.ImageField(upload_to='photos/%m/%d/', blank=True)
    isPublic = models.BooleanField(default=False)

    def __str__(self):
        return self.name