from django.http import HttpResponse

def index(request):
    return HttpResponse("Grandeeeee!!! La tua richiesta di registrazione e accesso a OpenCRM è stata inoltrata all'amministratore.")