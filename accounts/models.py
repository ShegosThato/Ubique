from django.db import models
from django.urls import reverse
from uuid import uuid4
from django.conf import settings as set


def person_directory_with_uuid(instance, filename):
    return '{}/{}'.format(instance.id_num, uuid4())


class Person(models.Model):
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    born = models.DateField()
    died = models.DateField(null=True, blank=True)
    id_num = models.PositiveIntegerField(primary_key=True)
    house_num = models.PositiveSmallIntegerField()
    street_name = models.CharField(max_length=50)
    town = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    province = models.CharField(max_length=30)
    zip_code = models.PositiveSmallIntegerField()
    

    class Meta:
        ordering = (
            'last_name', 'first_name', 'id_num'
        )
    
    def __str__(self):
        return '{0} {1} ID No: {2}'.format(self.first_name, self.last_name, self.id_num)
    
    def get_absolute_url(self):
        return reverse("ubi:index")
    