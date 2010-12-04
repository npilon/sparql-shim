from cStringIO import StringIO

import rdflib
from pymantic import content_type_to_rdflib_format

def parse_graph(request, content_type):
    request.body_graph = rdflib.Graph()
    request.body_graph.parse(StringIO(self.request.body),
                             format=content_type_to_rdflib_format[content_type])

def parse_n3(context, request):
    try:
        parse_graph(request, 'text/rdf+n3')
        return True
    except:
        return False

def parse_rdfxml(context, request):
    try:
        parse_graph(request, 'application/rdf+xml')
        return True
    except:
        return False

def parse_ntriples(context, request):
    try:
        parse_graph(request, 'text/plain')
        return True
    except:
        return False
