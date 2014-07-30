#!/home/pritishc/Envs/nereid/bin/python
from nereid import Nereid

CONFIG = dict(

    # The name of database
    DATABASE_NAME = 'nereid_db',

    # Static file root. The root location of the static files. The static/ will
    # point to this location. It is recommended to use the web server to serve
    # static content
    STATIC_FILEROOT = 'static/',

    # Tryton Config file path
    TRYTON_CONFIG = '../trytond.conf',

    # If the application is to be configured in the debug mode
    DEBUG = False,

    # Load the template from FileSystem in the path below instead of the
    # default Tryton loader where templates are loaded from Database
    TEMPLATE_LOADER_CLASS = 'nereid.templating.FileSystemLoader',
    TEMPLATE_SEARCH_PATH = '.',
    SECRET_KEY = 'cr@p123',
)

# Create a new application
app = Nereid()

# Update the configuration with the above config values
app.config.update(CONFIG)

# Initialise the app, connect to cache and backend
app.initialise()


class NereidHostChangeMiddleware(object):
    """
    A middleware which alters the HTTP_HOST so that you can test
    the site locally. This middleware replaces the HTTP_HOST with
    the value you prove to the :attr: site

    :param app: The application for which the middleware needs to work
    :param site: The value which should replace HTTP_HOST WSGI Environ
    """
    def __init__(self, app, site):
        self.app = app
        self.site = site

    def __call__(self, environ, start_response):
        environ['HTTP_HOST'] = self.site
        return self.app(environ, start_response)


if __name__ == '__main__':
    # The name of the website
    site = 'nereidblog.com'

    app.wsgi_app = NereidHostChangeMiddleware(app.wsgi_app, site)
    app.debug = True
    app.static_folder = '{0}/static'.format(site)
    app.run('0.0.0.0')