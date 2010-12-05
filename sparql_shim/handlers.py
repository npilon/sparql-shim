from cStringIO import StringIO

import rdflib

from pyramid.view import action
from pyramid.response import Response
from pyramid.httpexceptions import HTTPForbidden, HTTPOk, HTTPCreated,\
     HTTPAccepted, HTTPNoContent

from sparql_shim.parsers import parse_n3, parse_ntriples, parse_rdfxml

class GraphHandler(object):
    def __init__(self, request):
        self.request = request
        self.graph_uri = request.url # TODO: indirect specification handling.
        
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
    
    @action(name='graph', request_method='GET', accept='text/plain', renderer='nt')
    @action(name='graph', request_method='GET', accept='text/rdf+n3', renderer='n3')
    @action(name='graph', request_method='GET', accept='application/rdf+xml',
            renderer='rdfxml')
    def get_graph(self):
        return self._get_graph(self.graph_uri)
    
    @action(name='graph', request_method='POST', custom_predicates=[parse_n3],
            header='content-type:text/rdf\\+n3')
    @action(name='graph', request_method='POST', custom_predicates=[parse_rdfxml],
            header='content-type:application/rdf\\+xml')
    @action(name='graph', request_method='POST', custom_predicates=[parse_ntriples],
            header='content-type:text/plain')
    def post_graph(self):
        self._insert_graph(self.graph_uri, self.request.body_graph)
        return HTTPNoContent()
    
    @action(name='graph', request_method='PUT', custom_predicates=[parse_ntriples],
            header='content-type:text/plain')
    @action(name='graph', request_method='PUT', custom_predicates=[parse_n3],
            header='content-type:text/rdf\\+n3')
    @action(name='graph', request_method='PUT', custom_predicates=[parse_rdfxml],
            header='content-type:application/rdf\\+xml')
    def put_graph(self):
        self._replace_graph(self.graph_uri, self.request.body_graph)
        return HTTPNoContent()
    
    @action(name='graph', request_method='DELETE')
    def delete_graph(self):
        graph_uri = self.request.url
        try:
            self._drop_graph(graph_uri, silent = False)
            return HTTPNoContent()
        except:
            return HTTPForbidden()
    
    @action(name='graph', request_method='PATCH')
    def direct_patch(self):
        pass
