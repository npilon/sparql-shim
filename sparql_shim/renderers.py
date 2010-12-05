from pymantic import content_type_to_rdflib_format

class AbstractGraphRenderer(object):
    def __init__(self, info, content_type):
        self.content_type = content_type
        self.name = info.name
    
    def __call__(self, value, system):
        request = system.get('request')
        if request is not None:
            request.response_content_type = self.content_type
        return value.serialize(
            format = content_type_to_rdflib_format[self.content_type])

class NTriplesGraphRenderer(AbstractGraphRenderer):
    def __init__(self, info):
        super(NTriplesGraphRenderer, self).__init__(info, 'text/plain')

class RDFXMLGraphRenderer(AbstractGraphRenderer):
    def __init__(self, info):
        super(RDFXMLGraphRenderer, self).__init__(info, 'application/rdf+xml')

class N3GraphRenderer(AbstractGraphRenderer):
    def __init__(self, info):
        super(N3GraphRenderer, self).__init__(info, 'text/rdf+n3')
