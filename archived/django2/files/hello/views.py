from django.http import HttpResponse
from django.template import loader


def index(request):
    template = loader.get_template('base.html')
    context = {
        'message': "Hello, and welcome to the Platform.sh world",
    }
    return HttpResponse(template.render(context, request))
