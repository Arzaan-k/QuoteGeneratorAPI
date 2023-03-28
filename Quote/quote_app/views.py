import random
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
# from rest_framework.decorators import api_view,permission_classes,authentication_classes
# from rest_framework_simplejwt.authentication import JWTAuthentication
# from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
# from .models import Quote

@csrf_exempt
# @api_view(['GET'])
# @authentication_classes([JWTAuthentication])
# @permission_classes([IsAuthenticated])
def randquote(request):
    # quotes = Quote.objects.all()
    # quote =random.choice(quotes) 
    # data = {'text': quote.text, 'author': quote.author}
    data= "hello"
    return JsonResponse(data)
