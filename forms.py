from django import forms

from portal.plugins.taxonomy.models import TaxonomyField, Term, TermInstance

def get_system_fields():
    from portal.vidispine.iitem import ItemHelper

    itemhelper = ItemHelper()
    system_fields = itemhelper.getAllMetadataFields(onlySortables=False, includeSystemFields=False, onlyReusables=False, onlyXMP=False)
    
    # get all portal metadatas
    fields = ()
    for system_field in system_fields:
        fields = fields + ((system_field.getName(),system_field.getLabel()),)
    return fields


# Create the form class.
class TermForm(forms.ModelForm):
    class Meta:
        model = Term
        fields = ['value']


class TaxonomyFieldForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(TaxonomyFieldForm, self).__init__(*args, **kwargs)
        self.fields['fieldname'] = forms.ChoiceField(choices=(('','Select a Tag field'),) + get_system_fields())
    
    class Meta:
        model = TaxonomyField
        fields = ('fieldname',)