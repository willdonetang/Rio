from django.db import models

# Create your models here.


class Contacts(models.Model):
    family_name = models.CharField(max_length=100)
    #False为男，True为女
    sex = models.BooleanField(help_text="False为男，True为女")
    phone_number = models.CharField(max_length=50)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.family_name+("女生" if self.sex else "男生")+":"+self.phone_number

