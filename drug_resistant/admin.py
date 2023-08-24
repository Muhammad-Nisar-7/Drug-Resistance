from django.contrib import admin
from django.urls import path
from django.shortcuts import render

from .models import Drugs
from . models import Molecules
from django.contrib import messages
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django import forms
import pandas as pd


# from .models import drugs

from . import models

# Register your models here.

class CsvImportForm(forms.Form):
    csv_upload=forms.FileField()

class DrugsAdmin(admin.ModelAdmin):
    list_display = ['genes', 'medicine']
    
    def get_urls(self):
        urls=super().get_urls()
        new_urls = [path('upload-csv/',self.upload_csv),]
        return new_urls+urls

    def upload_csv(self, request):
        if (request.method == 'POST' ):
            csv_file = request.FILES['csv_upload']


            df = pd.read_excel(csv_file)
            # df.fillna('', inplace=True)
            # df['Stimuli'] = df['Stimuli'].str.replace('/','_')

            df_records = df.to_dict('records')

            for data in df_records:
                print(data)
                created = Drugs.objects.update_or_create (
                    genes = data['genes'],
                    medicine = data['medicine'],
                    tf = data['tf'],
                    # experiment_type = data['Experiment Type'],
                    # cell_line = data['Cell line'],
                    # lncrna_name = data['lncRNA name as in article'],
                    # ncbi_gene = data['NCBI_Gene_symbol'],8
                    # ensembl_id = data['Ensembl_id'],
                    # foldchange = data['Foldchange'],
                    # expression = data['Expression'],
                    # pubmed_id = data['PubMed_ID'],
                    # reference =data['Reference']
                    )


        form = CsvImportForm()
        data = {'form': form }
        return render(request,'admin/csv_upload.html',data)

admin.site.register(models.Drugs, DrugsAdmin)



class MoleculesAdmin(admin.ModelAdmin):
    list_display = ['pubMed', 'drug']
    
    def get_urls(self):
        urls=super().get_urls()
        new_urls = [path('upload-csv/',self.upload_csv),]
        return new_urls+urls

    def upload_csv(self, request):
        if (request.method == 'POST' ):
            csv_file = request.FILES['csv_upload']


            df = pd.read_excel(csv_file)
            # df.fillna('', inplace=True)
            # df['Stimuli'] = df['Stimuli'].str.replace('/','_')

            df_records = df.to_dict('records')

            for data in df_records:
                print(data)
                created = Molecules.objects.update_or_create (
                    pubMed = data['PubMed ID'],
                    drug = data['Drug Name'],
                    cell_lo = data['Cell line Origin'],
                    control_cl =  data['Control cell line'],
                    resistant_cl =  data['Resistant cell  line'],
                    molecules =  data['Molecules'],
                    name =  data['Name'],
                    gene_id =  data['Gene ID'],
                    exp_inRes_cell = data['Expression in resistant cell'],
                    post_tm =  data['Post-translational modification(s)'],
                    driver_molecule =  data['Driver molecule of Drug resistance (Validated)'],
                    exp_method =  data['Experimental method'],
                    fold_ratio = data['Fold change/Ratio'],
                    biomarker_type = data['Biomarker type'],
                    pmid_marker = data['PMID_Biomarker'],
                    # experiment_type = data['Experiment Type'],
                    # cell_line = data['Cell line'],
                    # lncrna_name = data['lncRNA name as in article'],
                    # ncbi_gene = data['NCBI_Gene_symbol'],8
                    # ensembl_id = data['Ensembl_id'],
                    # foldchange = data['Foldchange'],
                    # expression = data['Expression'],
                    # pubmed_id = data['PubMed_ID'],
                    # reference =data['Reference']
                    )


        form = CsvImportForm()
        data = {'form': form }
        return render(request,'admin/csv_upload.html',data)

admin.site.register(models.Molecules, MoleculesAdmin)