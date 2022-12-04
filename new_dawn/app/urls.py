from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contacts/', views.contacts, name='contacts'),
    path('documents/', views.documents, name='documents'),
    path('documents/<int:documents_id>/', views.messages, name='doc_messages'),
    path('me/', views.user, name='user'),
    path('signup/', views.signup, name='signup'),
]
