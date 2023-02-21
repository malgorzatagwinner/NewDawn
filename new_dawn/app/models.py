# Create your models here.
from django.db import models
#from django.contrib.auth.models import User, AbstractUser
from django.conf import settings

class DocumentType(models.Model):
    document_type_id = models.AutoField(primary_key=True)
    document_type_name = models.CharField(max_length=45)

    class Meta:
        db_table = 'document_type'


class Contact(models.Model):
    contact_id = models.AutoField(primary_key=True)
    contact_user_id = models.IntegerField()
    user_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    contact_user_name = models.CharField(max_length=45)

    class Meta:
        db_table = 'contact'


class Document(models.Model):
    document_id = models.AutoField(primary_key=True)
    contact_contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    document_type_document_type = models.ForeignKey(DocumentType, on_delete=models.CASCADE)
    document_name = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'document'


class Message(models.Model):
    message_id = models.AutoField(primary_key=True)
    user_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    viewed = models.DateTimeField(auto_now_add=True)
    document_document = models.ForeignKey(Document, on_delete=models.CASCADE)
    class Meta:
        db_table = 'message'

