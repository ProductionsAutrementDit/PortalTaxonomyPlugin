import logging
log = logging.getLogger(__name__)

from portal.vidispine.iitem import ItemHelper
from portal.plugins.taxonomy.taxonomy import processItem

def item_post_modify_handler(instance, method, **kwargs):
            
    log.debug('Call post modify')
    if method == 'setItemMetadata':
        
        processItem(instance)

def item_post_delete_handler(instance, method, **kwargs):
    if method == 'removeItem':
        TermInstance.objects.filter(item_id=instance).delete()



