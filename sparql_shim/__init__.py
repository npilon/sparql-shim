from pyramid_beaker import session_factory_from_settings

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    from pyramid.configuration import Configurator
    config = Configurator(settings=settings)
    session_factory = session_factory_from_settings(settings)
    config.set_session_factory(session_factory)
    
    config.registry['sparql.url'] = settings['sparql.url']

    config.add_static_view('static', 'sparql_shim:static/')
    config.add_handler('indirect', '/', 'sparql_shim.handlers:GraphHandler',
                       action='indirect')
    config.add_handler('direct', '/{name:.+}', 'sparql_shim.handlers:GraphHandler',
                       action='direct')
    config.scan('sparql_shim.subscribers')
    return config.make_wsgi_app()
