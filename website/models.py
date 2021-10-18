from django.db import models

# Create your models here.
class student(models.Model):
    name = models.CharField(max_length=100, blank=False)
    lastname = models.CharField(max_length=100, blank=False)
    email = models.CharField(max_length=100, blank=False)
    password = models.CharField(max_length=100, blank=False)
    birthday = models.CharField(max_length=100, blank=False)
    gender = models.CharField(max_length=100, blank=False)
    user_type = models.CharField(max_length=100, blank=False, default="normal")


    def __str__(self):
        return 'Name: {0} Lastname: {1} Email: {2} Password: {3} Birthday: {4} Gender: {5}'.format(self.name, self.lastname, self.email, self.password, self.birthday, self.gender)

class courses(models.Model):
    course_name = models.CharField(max_length=100, blank=False)
    price = models.FloatField(max_length=100, blank=False)

class prenotime(models.Model):
    course_name = models.CharField(max_length=100, blank=False)
    price = models.FloatField(max_length=100, blank=False)
    dita = models.CharField(max_length=100, blank=False)
    ora = models.CharField(max_length=100, blank=False)
    student = models.CharField(max_length=300, blank=False)