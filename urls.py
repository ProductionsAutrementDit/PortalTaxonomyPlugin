"""

"""
import logging

from django.conf.urls.defaults import *

# This new app handles the request to the URL by responding with the view which is loaded 
# from portal.plugins.taxonomy.views.py. Inside that file is a class which responsedxs to the 
# request, and sends in the arguments template - the html file to view.
# name is shortcut name for the urls.

urlpatterns = patterns('portal.plugins.taxonomy.views',
    url(r'^$', 'TermsView', kwargs={'template': 'taxonomy/terms_list.html'}, name='terms_list'),
    url(r'^taxonomy/add$', 'TermEditView', kwargs={'template': 'taxonomy/term_edit.html'}, name='term_new'),
    url(r'^taxonomy/(?P<term_id>\d+)$', 'TermEditView', kwargs={'template': 'taxonomy/term_edit.html'}, name='term_edit'),
    url(r'^taxonomy/(?P<term_id>\d+)/remove$', 'TermRemoveView', kwargs={}, name='term_remove'),
    url(r'^admin/$', 'SettingsView', kwargs={'template': 'taxonomy/admin/settings.html'}, name='settings'),
    url(r'^admin/removefield/(?P<field_id>\d+)$', 'RemoveSettingView', kwargs={'template': 'taxonomy/admin/settings.html'}, name='remove_setting'),
)
