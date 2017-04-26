"""
This is where you can write a lot of the code that responds to URLS - such as a page request from a browser
or a HTTP request from another application.

From here you can follow the Cantemo Portal Developers documentation for specific code, or for generic 
framework code refer to the Django developers documentation. 

"""
import logging

from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

from portal.generic.baseviews import ClassView
from portal.vidispine.iitem import ItemHelper
from portal.vidispine.iexception import NotFoundError

from portal.plugins.taxonomy.models import TaxonomyField, Term, TermInstance
from portal.plugins.taxonomy.forms import TermForm, TaxonomyFieldForm


log = logging.getLogger(__name__)


class TermsView(ClassView):

    def __call__(self):
        
        # Get all Metadata Mappings
        terms = Term.objects.all()
        fields = TaxonomyField.objects.all()
        
        ctx = {'terms': terms, 'fields': fields}
        
        return self.main(self.request, self.template, ctx)

# setup the object, and decorate so that only logged in users can see it
TermsView = TermsView._decorate(login_required)


class TermEditView(ClassView):

    def __call__(self):
        
        ctx = {}
            

        if 'term_id' in self.kwargs:
            try:
                term = Term.objects.get(pk=self.kwargs['term_id'])     
            except Term.DoesNotExist as e:
                return redirect('terms_list')
        else:
            term = Term()
            
        form = TermForm(self.request.POST or None, instance=term)
      
        if self.request.method == 'POST' and form.is_valid():
            term = form.save()
            return redirect('terms_list')
        
        ctx['form'] = form
        ctx['term'] = term
                
        return self.main(self.request, self.template, ctx)

# setup the object, and decorate so that only logged in users can see it
TermEditView = TermEditView._decorate(login_required)

class TermRemoveView(ClassView):

    def __call__(self):

        if 'term_id' in self.kwargs:
            try:
                Term.objects.get(pk=self.kwargs['term_id']).delete()   
            except Term.DoesNotExist as e:
                return redirect('terms_list')
        
        return redirect('terms_list')
          


# setup the object, and decorate so that only logged in users can see it
TermRemoveView = TermRemoveView._decorate(login_required)

class SettingsView(ClassView):

    def __call__(self):
        
        ctx = {}

        taxonomy_fields = TaxonomyField.objects.all()

        if self.request.method == u'POST':
            taxonomy_form = TaxonomyFieldForm(self.request.POST, prefix='settings')
            if taxonomy_form.is_valid():
                taxonomy = taxonomy_form.save()
        else:
            taxonomy_form = TaxonomyFieldForm(prefix='settings')      
        
        
        ctx = {'taxonomy_fields': taxonomy_fields, 'taxonomy_form': taxonomy_form}
        return self.main(self.request, self.template, ctx)

# setup the object, and decorate so that only logged in users can see it
SettingsView = SettingsView._decorate(login_required)

class RemoveSettingView(ClassView):

    def __call__(self):
        
        ctx = {}
        
        if 'field_id' in self.kwargs:
            try:
                TaxonomyField.objects.get(pk=self.kwargs['field_id']).delete()
            except Term.DoesNotExist as e:
                return redirect('terms_list')

        return redirect('settings')

# setup the object, and decorate so that only logged in users can see it
RemoveSettingView = RemoveSettingView._decorate(login_required)

class GenericAppView(ClassView):
    """ Show the page. Add your python code here to show dynamic content or feed information in
        to external apps
    """
    def __call__(self):
        # __call__ responds to the incoming request. It will already have a information associated to it, such as self.template and self.request

        log.debug("%s Viewing page" % self.request.user)
        ctx = {}
        
        # return a response to the request
        return self.main(self.request, self.template, ctx)

# setup the object, and decorate so that only logged in users can see it
GenericAppView = GenericAppView._decorate(login_required)
