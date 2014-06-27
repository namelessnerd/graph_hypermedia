#------------------------------------------------------------------------------
# Python Dependencies
#------------------------------------------------------------------------------
import simplejson
import string
import time
import requests

#-----------------------------------------------------------------------------
# Django Dependencies
#----------------------------------------------------------------------------
from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt

import query_helper

query_URL = 'http://localhost:3030/work/Accenture/ACP/PoC/ontologies/query'


def get_hypermedia_transitions(query):
    payload = {'query': query}
    return requests.get(query_URL, params=payload).json()


def home(request):
    print request.META['HTTP_USER_TYPE']
    return HttpResponse(simplejson.dumps({'key': 'value'}))


def get_products(request):
    user_context = request.META['HTTP_USER_TYPE']
    query = query_helper.prefix + \
        query_helper.hyper_graph[user_context]['products']
    print query
    return HttpResponse(simplejson.dumps(get_hypermedia_transitions(query)))


def get_capabilities(request):
    user_context = request.META['HTTP_USER_TYPE']
    query = query_helper.prefix + \
        query_helper.hyper_graph[user_context]['capabilities']
    print query
    return HttpResponse(simplejson.dumps(get_hypermedia_transitions(query)))


def get_network(request):
    user_context = request.META['HTTP_USER_TYPE']
    query = query_helper.prefix + \
        query_helper.hyper_graph[user_context]['network']
    print query
    return HttpResponse(simplejson.dumps(get_hypermedia_transitions(query)))
