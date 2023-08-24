from django.db import models

# Create your models here.
class Drugs(models.Model):
    genes = models.CharField(max_length=2000, null=True)
    medicine = models.CharField(max_length=255, null= True)
    expression = models.CharField(max_length=255, null = True)
    
class Molecules(models.Model):
    pubMed = models.CharField(max_length=10, null=True)
    drug = models.CharField(max_length=80, null= True)
    cell_lo = models.CharField(max_length=255, null = True)
    control_cl = models.CharField(max_length=100, null = True)
    resistant_cl = models.CharField(max_length=100, null = True)
    molecules = models.CharField(max_length=100, null = True)
    name = models.CharField(max_length=100, null = True)
    gene_id = models.CharField(max_length=100, null = True)
    exp_inRes_cell = models.CharField(max_length=100, null = True)
    post_tm = models.CharField(max_length=100, null = True)
    driver_molecule = models.CharField(max_length=30, null = True)
    exp_method = models.CharField(max_length=100, null = True)
    fold_ratio = models.CharField(max_length=100, null = True)
    biomarker_type = models.CharField(max_length=100, null = True)
    pmid_marker = models.CharField(max_length=100, null = True)