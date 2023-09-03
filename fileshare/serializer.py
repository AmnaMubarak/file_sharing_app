from rest_framework import serializers
from models import *
import shutil

class FileListSerializer(serializers.Serializer):
    files = serializers.ListField(
        child=serializers.FileField(max_length=100000, allow_empty_file=False, use_url=False)
        )
    def zip_file(self,folder):
        shutil.make_archive(folder, 'zip', folder)
        
        
    def create(self, validated_data):
        folder = Folder.objects.create()
        files =  validated_data.pop('files')
        file_obj = []
        for file in files:
            file_objs = Files.objects.create(folder=folder,file=file)
            file_obj.append(file_objs)
        self.zip_file(folder.uid)
            
        return {'folder':str(folder.uid),'files':{}}
            