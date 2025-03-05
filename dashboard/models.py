from django.db import models

# Create your models here.
class RedesSociais(models.Model):
    facebook = models.URLField(max_length=200, blank=True, null=True)
    twitter = models.URLField(max_length=200, blank=True, null=True)
    linkedin = models.URLField(max_length=200, blank=True, null=True)
    instagram = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f"Redes sociais: Facebook: {self.facebook}, Twitter: {self.twitter}, LinkedIn: {self.linkedin}, Instagram: {self.instagram}"