from pyramid.response import Response

from pymantic import content_type_to_rdflib_format

class AbstractGraphRenderer(object):
    def __init__(self, info, content_type):
        self.content_type = content_type
        self.name = info['name']
    
    def __call__(self, value, system):
        serialized = value.serialize(
            format = content_type_to_rdflib_format[self.content_type])
        response = Response(body = serialized, content_type = self.content_type)

class NTriplesGraphRenderer(AbstractGraphRenderer):
    def __init__(self, info):
        super(NTriplesGraphRenderFactory, self).__init__(info, 'text/plain')

class RDFXMLGraphRenderer(AbstractGraphRenderer):
    def __init__(self, info):
        super(NTriplesGraphRenderFactory, self).__init__(info, 'application/rdf+xml')

class N3GraphRenderer(AbstractGraphRenderer):
    def __init__(self, info):
        super(NTriplesGraphRenderFactory, self).__init__(info, 'text/rdf+n3')
