"""
This is your new plugin handler code.

Put your plugin handling code in here. remember to update the __init__.py file with 
you app version number. We have automatically generated a GUID for you, namespace, and a url 
that serves up index.html file
"""
import logging

from portal.pluginbase.core import Plugin, implements
from portal.generic.plugin_interfaces import (IPluginURL, IPluginBlock, IAppRegister, IPluginBootstrap)

log = logging.getLogger(__name__)

class TaxonomyPluginURL(Plugin):
    """ Adds a plugin handler which creates url handler for the index page """
    implements(IPluginURL)

    def __init__(self):
        self.name = "Taxonomy App"
        self.urls = 'portal.plugins.taxonomy.urls'
        self.urlpattern = r'^taxonomy/'
        self.namespace = r'taxonomy'
        self.plugin_guid = '4edf9c96-ed31-47fa-b375-6ebb78900d00'
        log.debug("Initiated Taxonomy App")

pluginurls = TaxonomyPluginURL()

# Create a menu item for ingest in the ingest section in the navbar
class TaxonomytMenuNavigationPlugin(Plugin):
    implements(IPluginBlock)

    def __init__(self):
        self.name = "NavigationManagePlugin"
        self.plugin_guid = "9a21d34f-1714-4a02-bb83-c9dd327e57b3"

    def return_string(self, tagname, *args):
        return {'guid': self.plugin_guid, 'template': 'taxonomy/menuitem.html'}

navbarplugin = TaxonomytMenuNavigationPlugin()


class TaxonomyAdminNavigationPlugin(Plugin):
    # This adds your app to the navigation bar
    # Please update the information below with the author etc..
    implements(IPluginBlock)

    def __init__(self):
        self.name = "NavigationAdminPlugin"
        self.plugin_guid = 'b57ae5b7-161a-4fe0-b4bc-97a34ee608aa'
        log.debug('Initiated navigation plugin')

    # Returns the template file navigation.html
    # Change navigation.html to the string that you want to use
    def return_string(self, tagname, *args):
        return {'guid': self.plugin_guid, 'template': 'taxonomy/navigation.html'}

navplug = TaxonomyAdminNavigationPlugin()

class TaxonomyAdminMenuPlugin(Plugin):
    u""" adds a menu item to the admin screen
    """
    implements(IPluginBlock)

    def __init__(self):
        self.name = 'AdminLeftPanelBottomPanePlugin'
        self.plugin_guid = '63eadfa2-aa3b-4a0c-9232-b3ff568e5eb6'

    def return_string(self, tagname, *args):
        return {'guid': self.plugin_guid, 'template': 'taxonomy/admin/admin_leftpanel_pane.html'}

pluginblock = TaxonomyAdminMenuPlugin()


class TaxonomyRegister(Plugin):
    # This adds it to the list of installed Apps
    # Please update the information below with the author etc..
    implements(IAppRegister)

    def __init__(self):
        self.name = "Taxonomy Registration App"
        self.plugin_guid = 'ca1250a1-1edc-4104-a874-51adf8d8bf82'
        log.debug('Register the App')

    def __call__(self):
        from __init__ import __version__ as versionnumber
        _app_dict = {
                'name': 'Taxonomy',
                'version': '0.0.1',
                'author': 'Camille Darley - Productions Autrement Dit',
                'author_url': 'www.pad.fr',
                'notes': 'Copyright 2016. All Rights Reserved.'}
        return _app_dict

taxonomyplugin = TaxonomyRegister()



class TaxonomyBootstrap(Plugin):

    implements(IPluginBootstrap)

    def bootstrap(self):
        from portal.plugins.taxonomy.plistner import item_post_modify_handler, item_post_delete_handler
        from portal.vidispine.signals import vidispine_post_modify, vidispine_post_create, vidispine_post_delete
    
        vidispine_post_modify.connect(item_post_modify_handler)
        vidispine_post_create.connect(item_post_modify_handler)
        vidispine_post_delete.connect(item_post_delete_handler)

TaxonomyBootstrap()