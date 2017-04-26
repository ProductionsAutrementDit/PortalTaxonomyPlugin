from django.db import models

class TaxonomyField(models.Model):
    fieldname = models.CharField(max_length=255)

class Term(models.Model):
    value = models.CharField(max_length=255, unique=True)

class TermInstance(models.Model):
    item_id = models.CharField(max_length=255)
    term = models.ForeignKey(Term, related_name="items", on_delete=models.CASCADE)
    taxonomy = models.ForeignKey(TaxonomyField, related_name="terms", on_delete=models.CASCADE)


