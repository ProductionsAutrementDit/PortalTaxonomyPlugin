import logging
log = logging.getLogger(__name__)

from portal.vidispine.iitem import ItemHelper
from portal.vidispine.isearch import SearchHelper
from portal.plugins.taxonomy.models import TaxonomyField, Term, TermInstance


def updateItemTerms(item_id, item_terms, taxonomy_field):
    terms = []
    # check and create all item's terms
    for item_term in item_terms:
        term, term_created = Term.objects.get_or_create(value=item_term)
        terms.append(term)
        if term_created:
            log.debug('Term created: %s' % term.value)
        else:
            log.debug('Term loaded: %s' % term.value)
        term_instance, instance_created = TermInstance.objects.get_or_create(item_id=item_id, term=term, taxonomy=taxonomy_field)
        if instance_created:
            log.debug('Instance created for %s: %s' % (item_id, term.value))
        else:
            log.debug('Instance loaded for %s: %s' % (item_id, term.value))

    # delete all instances wich are not present anymore
    TermInstance.objects.filter(item_id=item_id, taxonomy=taxonomy_field).exclude(term__in=terms).delete()
    
def updateTermsFromItem(item_id, fields):
  
    ith = ItemHelper()      
    item = ith.getItem(item_id)
    
    terms = []
    
    for fieldname, taxonomy_field in fields.iteritems():
        log.debug('load terms for field %s' % fieldname)    
        system_field = item.getMetadataFieldByName(fieldname)
        terms = system_field.getFieldValues()
        log.debug('found %s terms' % len(terms))
        updateItemTerms(item_id, terms, taxonomy_field)
    
    return terms


def updateTermsFromSearchResult(searchresult_item, fields):
    
    if 'timespan' in searchresult_item['metadata']:
        if len(searchresult_item['metadata']['timespan']) > 0:
            timespan = searchresult_item['metadata']['timespan'][0]
            for field in timespan['field']:
                if field['name'] in fields.keys():
                    terms = []
                    if 'value' in field:
                        for value in field['value']:
                            terms.append(value['value'])
                        updateItemTerms(searchresult_item['id'], terms, fields[field['name']])
    

def processItem(item_id):
  
    taxonomy_fields = TaxonomyField.objects.all()

    fields = {}
    
    for taxonomy_field in taxonomy_fields:
        fields[taxonomy_field.fieldname] = taxonomy_field

    updateTermsFromItem(item_id, fields)
        

def updateAllPortalItems():
    sh = SearchHelper(searchdomain='item')
    
    taxonomy_fields = TaxonomyField.objects.all()
    
    page = 0
    duration = 0
    
    fields = {}
    
    for taxonomy_field in taxonomy_fields:
        fields[taxonomy_field.fieldname] = taxonomy_field
    
    content = {'content': 'metadata','field': fields.keys()}

    while True:
        searchresults = sh.search(_content=content,queryamount='1000', page=page)
        page = page + 1
        for searchresult_item in searchresults[0]['item']:
            updateTermsFromSearchResult(searchresult_item, fields)          
        if len(searchresults[0]['item']) < 1000:
            break