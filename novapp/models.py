from django.db import models


# Create your models here.
class Contact(models.Model):
    yourname = models.CharField(max_length=250)
    youremail = models.EmailField()
    subject = models.CharField(max_length=50)
    message = models.TextField()

    def __str__(self):
        return self.yourname


class Member(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=15)

    def __str__(self):
        return self.firstname + " " + self.lastname


class UploadedDocument(models.Model):
    title = models.CharField(max_length=255)
    document = models.FileField(upload_to='images/')

    def __str__(self):
        return self.title
