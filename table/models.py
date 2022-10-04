from distutils.command.upload import upload
import black
from django.db import models


# Create your models here.

class Txt(models.Model):
    file = models.FileField(upload_to="txt/")