from django.shortcuts import render, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from pymongo import MongoClient
from bson.json_util import dumps
import json
# Create your views here.

@api_view(['GET'])
def get_All_SugRec(request):
    client = MongoClient()
    db = client.test
    sugrec = db.sugerencias
    jsonstr = dumps(sugrec.find())
    jsonstrindent = json.loads(jsonstr)
    # listsugrec = list(sugrec.find())
    # jsonstring = json.dumps(listsugrec)
    # jsondict = json.loads(jsonstring)
    return Response(jsonstrindent)