from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from .models import Document, Contact, User, Message
from django.views.decorators.csrf import csrf_exempt
import json

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
    user = User.objects.filter(user_id='1').values('username', 'photo') #user_id będzie z autentykacji
    user = list(user)
    return JsonResponse(user, safe=False)

def messages(request):
    messages = Message.objects.all().values('message_id', 'user_user, content, created_at, viewed')
    messages = list(messages)
    return JsonResponse(messages, safe=False)

@csrf_exempt 
def signup(request):
    req = dict()
    if request.method != 'POST':
        return HttpResponseBadRequest()
    try:
        req = json.loads(request.body)
    except json.JSONDecodeError:
        print(req)
        
    if len(req) != 4:
        return HttpResponseBadRequest()
    return HttpResponse()

