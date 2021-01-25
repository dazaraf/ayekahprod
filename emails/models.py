from django.db import models

# Create your models here.
class Subscriber(models.Model):
    name = models.CharField(max_length=200)
    conf_num = models.CharField(max_length=15)
    confirmed = models.BooleanField(default=False)
    email = models.EmailField(unique=True)

#how to handle redundant email addresses?
    def __str__(self):
        return self.name

class Newsletter(models.Model):
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    subject = models.CharField(max_length=300)
    content = models.FileField(upload_to = 'newsletters')

    def __str__(self):
        return self.subject + " " + self.created_at.strftime("%B %d, %Y")

    