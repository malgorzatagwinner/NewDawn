from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from .models import Document, Contact, Message
from django.views.decorators.csrf import csrf_exempt
import json
from django.db.models import Q
from django.contrib.auth.models import User
import re
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate
#from django.core import serializers
#from .serializer import SignUpReq


def index(request):
    return JsonResponse({'text':"Siemkaaa"})

def document(request):
    document = Document.objects.values('document_id', 'contact_contact', 'document_name', 'created_at', 'updated_at')
    document = list(document)
    return JsonResponse(document, safe=False)

def documents(request):
    documents = Document.objects.all().values('document_id', 'contact_contact', 'document_name', 'created_at', 'updated_at')
    documents = list(documents)
    return JsonResponse(documents, safe=False)


def contacts(request):
    contacts = Contact.objects.all().values('contact_user_name')
    contacts = list(contacts)
    return JsonResponse(contacts, safe=False)

def user(request):
    user_ = User.objects.get(username)
    #user = User.objects.filter(user_id='1').values('username', 'photo') #user_id będzie z autentykacji
    user = list(user_)
    return JsonResponse(user, safe=False)

def messages(request):
    messages = Message.objects.all().values('message_id', 'user_user, content, created_at, viewed')
    messages = list(messages)
    return JsonResponse(messages, safe=False)

@csrf_exempt 
def signup(request):
    req = dict()
    if request.method != 'POST':
        return HttpResponsebadRequest()
    try:
#        req = serializers.deserialize("json", request.body)
        req = json.loads(request.body)

    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")
    
    if len(req) !=4 or set(req.keys()) != set(["email", "username", "password", "password_conf"]):
        return HttpResponseBadRequest("Wrong request")

    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if not re.fullmatch(regex, req["email"]):
        return HttpResponseBadRequest("Invalid email")
    
    if req["password"] != req["password_conf"]:
        print(req["password_conf"])
        return HttpResponseBadRequest("Passwords did not match")
    #u1 = User.objects.get(Q(email=req["email"]) | Q(username = req["username"]))
    try:
        u1 = User.objects.get(email=req["email"]) or User.objects.get(username=req["username"])
    except User.DoesNotExist:
        user = User.objects.create_user(email=req["email"], username = req["username"], password = req["password"])
        user.save()
        return HttpResponse("OK")
    print("user istnieje")
    return HttpResponseBadRequest("lol")


@csrf_exempt 
def signin(request):
    req = dict()
    if request.method != 'POST':
        return HttpResponsebadRequest()
    try:
#        req = serializers.deserialize("json", request.body)
        req = json.loads(request.body)

    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")
    
    if len(req) !=2 or set(req.keys()) != set(["email", "password"]):
        return HttpResponseBadRequest("Wrong request")
    
    u = authenticate(email=req["email"], password=req["password"]) or authenticate(username=req["email"], password=req["password"])
    if u is not None:
        return HttpResponse("OK")
    return HttpResponseBadRequest("lol")

