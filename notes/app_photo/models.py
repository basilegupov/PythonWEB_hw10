from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.


def validate_file_size(value):
    filesize = value.size
    if filesize > 5242880:
        raise ValidationError("File size too large (max. 5 MB)")
    return value


class Picture(models.Model):
    description = models.CharField(max_length=150)
    path = models.ImageField(upload_to='images', validators=[validate_file_size])
