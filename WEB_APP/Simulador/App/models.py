from django.db import models

# Create your models here.

class Document(models.Model):
    title = models.CharField(max_length=250)
    uploadedFile = models.FileField(upload_to= "Uploaded Files/")
    dateTimeOfUpload = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title