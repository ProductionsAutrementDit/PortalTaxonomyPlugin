# Portal Taxonomy Plugin

This plugin provide a list of terms used in selected tags fields in your Portal installation.
Whenever the metadata of an item is changed, each entry in the predefined tag field is analyzed, and the terms are stored in a database.


## Installation

Place the plugin's file in a "taxonomy" folder in /opt/cantemo/portal/portal/plugins.

In shell, type:  
cd /opt/cantemo/portal/  
./manage.py schemamigration taxonomy --initial  
./manage.py migrate taxonomy  


## Configuration

Go to http://\<Yourserverurl\>/taxonomy/admin/ or click in the "Taxonomy" menu item, under "Admin".  
Select a tag field to analyse and submit the form.  
You can add as many field as you need to analyse.


## Use
Each time an item is saved, their tags are analysed and stored.
You can view the list at http://\<Yourserverurl\>/taxonomy.
By clicking on the item number, you are redirected to a search page, showing all items corresponding to the selected term.

## TODO
1. Add a settings page, with a dropdown to choose the tag field to inspect.
2. Allow to inspect multiple tag fields
3. Add a function to inspect all Portal elements and replace synonyms (can be very long)
