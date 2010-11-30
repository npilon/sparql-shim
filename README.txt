sparql_shim provides a SPARQL 1.1 Uniform HTTP Protocol interface to any
SPARQL 1.1 Update-capable graph store.

The SPARQL 1.1 Uniform HTTP Protocol is described at:

http://www.w3.org/TR/sparql11-http-rdf-update/

The SPARQL 1.1 Update standard is described at:

http://www.w3.org/TR/2009/WD-sparql11-update-20091022/

Installation and Setup
======================

Install ``sparql_shim`` using easy_install::

    easy_install sparql_shim

Make a config file as follows::

    paster make-config sparql_shim config.ini

Tweak the config file as appropriate and then setup the application::

    paster setup-app config.ini

Then you are ready to go.
