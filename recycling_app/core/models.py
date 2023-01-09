from django.db import models


class Bucket(models.Model):
    id = models.IntegerField(primary_key=True)
    bucket_name = models.CharField(max_length=15)

    def __str__(self):
        return self.bucket_name


class Trash(models.Model):
    id = models.IntegerField(primary_key=True)
    trash_name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    bucket = models.ForeignKey(Bucket, on_delete=models.CASCADE)

    def __str__(self):
        return self.trash_name
