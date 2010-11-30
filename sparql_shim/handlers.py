from cStringIO import StringIO

import rdflib

from pyramid.view import action
from pyramid.response import Response
from pyramid.httpexceptions import HTTPForbidden, HTTPOk, HTTPCreated,\
     HTTPAccepted, HTTPNoContent

class GraphHandler(object):
    def __init__(self, request):
        self.request = request
        
    def _get_graph(self, graph_uri):
        query = 'CONSTRUCT { ?s ?p ?o } WHERE { GRAPH <%(graph_uri)s> { ?s ?p ?o } }'
        query = query % dict(graph_uri = graph_uri)
        graph = self.request.sparql.query(query)
        return graph
    
    def _insert_graph(self, graph_uri, graph):
        query = 'INSERT INTO <%(graph_uri)s> { %(payload)s }'
        payload = graph.serialize(format = 'nt')
        query = query % dict(graph_uri = graph_uri, payload = payload)
        self.request.sparql.query(query)
    
    def _replace_graph(self, graph_uri, graph):
        self._drop_graph(graph_uri, silent = True)
        self._insert_graph(graph_uri, graph)
    
    def _drop_graph(self, graph_uri, silent = False):
        query = 'MODIFY GRAPH <%(graph_uri)s> DELETE { ?s ?p ?o } INSERT { } WHERE { ?s ?p ?o }'
        query = query % dict(graph_uri = graph_uri)
        self.request.sparql.query(query)
    
    @action(name = 'direct', request_method = 'GET', accept='text/plain')
    def direct_get_nt(self):
        graph_uri = self.request.url
        graph = self._get_graph(graph_uri)
        return Response(body = graph.serialize(format = 'nt'),
                        content_type = 'text/plain')
    
    @action(name = 'direct', request_method = 'POST',
            header='content-type:text/plain')
    def direct_post_nt(self):
        graph_uri = self.request.url
        graph = rdflib.Graph()
        graph.parse(StringIO(self.request.body), format = 'nt')
        self._insert_graph(graph_uri, graph)
        return HTTPNoContent
    
    @action(name = 'direct', request_method = 'PUT',
            header='content-type:text/plain')
    def direct_put_nt(self):
        graph_uri = self.request.url
        graph = rdflib.Graph()
        graph.parse(StringIO(self.request.body), format = 'nt')
        self._replace_graph(graph_uri, graph)
        return HTTPNoContent
    
    @action(name = 'direct', request_method = 'GET', accept='text/rdf+n3')
    def direct_get_n3(self):
        graph_uri = self.request.url
        graph = self._get_graph(graph_uri)
        return Response(body = graph.serialize(format = 'n3'),
                        content_type = 'text/rdf+n3')
    
    @action(name = 'direct', request_method = 'POST',
            header='content-type:text/rdf+n3')
    def direct_post_n3(self):
        graph_uri = self.request.url
        graph = rdflib.Graph()
        graph.parse(StringIO(self.request.body), format = 'n3')
        self._insert_graph(graph_uri, graph)
        return HTTPNoContent
    
    @action(name = 'direct', request_method = 'PUT',
            header='content-type:text/rdf+n3')
    def direct_put_n3(self):
        graph_uri = self.request.url
        graph = rdflib.Graph()
        graph.parse(StringIO(self.request.body), format = 'n3')
        self._replace_graph(graph_uri, graph)
        return HTTPNoContent

    @action(name = 'direct', request_method = 'GET',
            accept='application/rdf+xml')
    def direct_get_rdfxml(self):
        graph_uri = self.request.url
        graph = self._get_graph(graph_uri)
        return Response(body = graph.serialize(format = 'xml'),
                        content_type = 'text/rdf+n3')
    
    @action(name = 'direct', request_method = 'POST',
            header='content-type:application/rdf+xml')
    def direct_post_rdfxml(self):
        graph_uri = self.request.url
        graph = rdflib.Graph()
        graph.parse(StringIO(self.request.body), format = 'xml')
        self._insert_graph(graph_uri, graph)
        return HTTPNoContent
    
    @action(name = 'direct', request_method = 'PUT',
            header='content-type:application/rdf+xml')
    def direct_put_rdfxml(self):
        graph_uri = self.request.url
        graph = rdflib.Graph()
        graph.parse(StringIO(self.request.body), format = 'xml')
        self._replace_graph(graph_uri, graph)
        return HTTPNoContent
    
    @action(name = 'direct', request_method = 'DELETE')
    def direct_delete(self):
        graph_uri = self.request.url
        try:
            self._drop_graph(graph_uri, silent = False)
            return HTTPNoContent
        except:
            return HTTPForbidden
    
    @action(name = 'direct', request_method = 'PATCH')
    def direct_patch(self):
        pass
