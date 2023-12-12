import io
import pikepdf
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def unlock(request):
    buffer = io.BytesIO()
    
    return HttpResponse("pdf unlocked")
