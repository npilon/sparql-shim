from pyramid.view import action
from pyramid.response import Response


class GraphHandler(object):
    def __init__(self, request):
        self.request = request
        
    def _get_triples(self, graph_uri):
        query = 'CONSTRUCT { ?s ?p ?o } WHERE { GRAPH <%(graph_uri)s> { ?s ?p ?o } }'
        query = query % dict(graph_uri = graph_uri)
        graph = self.request.sparql.query(query)
        return graph
    
    @action(name = 'direct', request_method = 'GET', accept='text/plain')
    def direct_get_nt(self):
        graph_uri = self.request.url
        graph = self._get_triples(graph_uri)
        return Response(body = graph.serialize(format = 'nt'),
                        content_type = 'text/plain')
    
    @action(name = 'direct', request_method = 'POST',
            header='content-type:text/plain')
    def direct_post_nt(self):
        pass
    
    @action(name = 'direct', request_method = 'PUT',
            header='content-type:text/plain')
    def direct_put_nt(self):
        pass
    
    @action(name = 'direct', request_method = 'GET', accept='text/rdf+n3')
    def direct_get_n3(self):
        graph_uri = self.request.url
        graph = self._get_triples(graph_uri)
        return Response(body = graph.serialize(format = 'n3'),
                        content_type = 'text/rdf+n3')
    
    @action(name = 'direct', request_method = 'POST',
            header='content-type:text/rdf+n3')
    def direct_post_n3(self):
        pass
    
    @action(name = 'direct', request_method = 'PUT',
            header='content-type:text/rdf+n3')
    def direct_put_n3(self):
        pass

    @action(name = 'direct', request_method = 'GET',
            accept='application/rdf+xml')
    def direct_get_rdfxml(self):
        pass
    
    @action(name = 'direct', request_method = 'POST',
            header='content-type:application/rdf+xml')
    def direct_post_rdfxml(self):
        pass
    
    @action(name = 'direct', request_method = 'PUT',
            header='content-type:application/rdf+xml')
    def direct_put_rdfxml(self):
        pass
    
    @action(name = 'direct', request_method = 'DELETE')
    def direct_delete(self):
        pass
    
    @action(name = 'direct', request_method = 'PATCH')
    def direct_patch(self):
        pass
