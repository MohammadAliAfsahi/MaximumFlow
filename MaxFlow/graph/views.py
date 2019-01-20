from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from . import FordFulkerson
import networkx as nx
import numpy as np

class myClass:
    G = nx.DiGraph()


def index(request):
    template = loader.get_template('DragAndDrop.html')
    context = {"key":10}



    if request.method == 'POST':
        if 'from' in request.POST:
            source = request.POST['from']
            destination = request.POST['to']
            weight = request.POST['label']
            myClass.G.add_weighted_edges_from([(source, destination, weight)])
            return HttpResponse("done")
    if request.method == 'POST':
        if 's' in request.POST:
            source = request.POST['s']
            sink = request.POST['t']
            max_flow = FordFulkerson.max_flow(nx.to_numpy_array(myClass.G).tolist(),int(source),int(sink))
            print('max_flow:',max_flow)
            return HttpResponse(max_flow)  # return max flow to html page

    return HttpResponse(template.render(context,request))
