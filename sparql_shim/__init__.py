from pyramid_beaker import session_factory_from_settings

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    from pyramid.configuration import Configurator
    config = Configurator(settings=settings)
    config.add_renderer(name = 'nt', factory='.renderers.NTriplesGraphRenderer')
    config.add_renderer(name = 'rdfxml', factory='.renderers.RDFXMLGraphRenderer')
    config.add_renderer(name = 'n3', factory='.renderers.N3GraphRenderer')
    
    session_factory = session_factory_from_settings(settings)
    config.set_session_factory(session_factory)
    
    config.registry['sparql.url'] = settings['sparql.url']

    config.add_static_view('static', 'sparql_shim:static/')
    config.add_handler('direct_graph', '/{name:.+}', '.handlers:GraphHandler',
                       action='graph')
    config.add_handler('indirect_graph', '/', '.handlers:GraphHandler',
                       action='graph')
    config.scan('sparql_shim.subscribers')
    return config.make_wsgi_app()
