from django.db import models
import uuid
import os
# Create your models here.
class Folder(models.Model):
    uid = models.UUIDField(primary_keys = True,editable=True,default=uuid.uuid)
    created_at = models.DateField(auto_now=True)
    
def get_upload_path(instance,filename):
    return os.path.join(str(instance.folder.uid),filename)    
class Files(models.Model):
    folder = models.ForeignKey(Folder,on_delete=models.CASCADE)
    file = models.FileField(upload_to=get_upload_path)  