from django.db import models

# Create your models here.
from django.db import models

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=45)
    username = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    photo = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        managed = False
        db_table = 'user'


class DocumentType(models.Model):
    document_type_id = models.AutoField(primary_key=True)
    document_type_name = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'document_type'


class Contact(models.Model):
    contact_id = models.AutoField(primary_key=True)
    contact_user_id = models.IntegerField()
    user_user = models.ForeignKey(User, on_delete=models.CASCADE)
    contact_user_name = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'contact'


class Document(models.Model):
    document_id = models.AutoField(primary_key=True)
    contact_contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    document_type_document_type = models.ForeignKey(DocumentType, on_delete=models.CASCADE)
    document_name = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'document'


class Message(models.Model):
    message_id = models.AutoField(primary_key=True)
    user_user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    viewed = models.DateTimeField(auto_now_add=True)
    document_document = models.ForeignKey(Document, on_delete=models.CASCADE)
    class Meta:
        managed = False
        db_table = 'message'

