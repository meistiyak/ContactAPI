from django.db import models

class Contact(models.Model):
    contact_name = models.CharField(max_length=50)
    contact_number = models.CharField(max_length=20)
    contact_address = models.TextField(max_length=200)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{name} {number}".format(name=self.contact_name,number=self.contact_number)