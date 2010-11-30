from pyramid_beaker import session_factory_from_settings

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    from pyramid.configuration import Configurator
    config = Configurator(settings=settings)
    session_factory = session_factory_from_settings(settings)
    config.set_session_factory(session_factory)
    config.add_static_view('static', 'sparql_shim:static/')
    config.add_handler('action', '/{action}', 'sparql_shim.handlers:MyHandler')
    config.add_handler('home', '/', 'sparql_shim.handlers:MyHandler',
                       action='index')
    config.add_subscriber('sparql_shim.subscribers.add_renderer_globals',
                          'pyramid.events.BeforeRender')
    return config.make_wsgi_app()

