from django.shortcuts import render
from .models import Drugs , Molecules
import pandas as pd
import numpy as np
import json
from django.db.models import Q

def profile(request):
    return render(request, 'drug_resistant/profile.html',{})

def home0(request):
    return render(request, 'drug_resistant/home0.html',{})

def home(request):
    exp = Drugs.objects.all().values('expression').distinct()
    print(exp)
    return render(request, 'drug_resistant/home.html',{'exp': exp})

def home2(request):
    dname = Molecules.objects.all().values('drug').distinct()
    cline = Molecules.objects.all().values('cell_lo').distinct()
    print(dname)
    # hn = Drugs.objects.all().values('').distinct()
    return render(request, 'drug_resistant/home2.html',{'dname': dname, 'cline':cline})
   
   

def output(request):
    data = request.POST.get('sample1')
    print(data)
    data1 = request.POST.get('sample2')
    print(data1)
    genes = data.split()
    genes1 = data1.split()
    exp1 = 'Overexpression'
    exp2 = 'Downregulation '
    q1 = Q(genes__in=genes, expression=exp1)
    q2 = Q(genes__in=genes1, expression=exp2)

    combined_query = q1 | q2

    medicines = Drugs.objects.filter(combined_query).values()
            
               
    if not medicines:
        return render(request, 'drug_resistant/error.html',{})
    else:
        df = pd.DataFrame(list(medicines))
        df = df.groupby('genes').agg(pd.Series.tolist) 
        del df['id']
        df.reset_index(inplace=True)
        new_df = df.explode('medicine')
        new_df = (
            pd.crosstab(new_df['genes'], new_df['medicine'],
                        margins=True, margins_name='Total')
                .iloc[:-1]
                .rename_axis(columns=None)
                .reset_index()
        )
        drug_res=new_df.sort_values("Total")
        new_drugres = drug_res
        sum = new_drugres.sum()
        sum.name = 'Sum'
        new_drugres = new_drugres._append(sum.transpose())
        new_drugres = new_drugres.reset_index()          
        new_drugres = new_drugres.drop(['index'], axis=1)
        new_drugres.iat[-1,0] = 'Sum'
        new_drugres = new_drugres.set_index('genes').transpose()
        new_drugres = new_drugres.drop('Total')
        new_drugres=new_drugres.sort_values("Sum")
        new_drugres = new_drugres.drop('Sum', axis=1)
        genes = drug_res["genes"].tolist()
        drug_res = drug_res.drop('Total', axis=1)
        data = drug_res.drop('genes', axis=1)
        meds = data.columns.values.tolist()
        drug = ['Cisplatin', 'paclitaxel','5 fluorouracil', 'Gemcitabine', 'Pingyangmycin', 'Cetuximab', 'Docetaxel', 'Doxorubicin', 'Panobinostat']
        allDrug_list = set(drug) 
        drug_list = set(meds)  
        left_out_drugs = allDrug_list.difference(drug_list)  
        left_out_drugs = list(left_out_drugs)
        data = {'meds':left_out_drugs}
        rem_med = pd.DataFrame(data)
        rem_med.set_index('meds',inplace=True)
        rem_med1 = rem_med
        rem_med = rem_med.transpose()
        values = drug_res.set_index('genes')
        new_drugres = rem_med1._append(new_drugres)
        new_drugres = new_drugres.fillna(0)
        new_drugres = new_drugres.to_numpy()
        combined_data = rem_med._append(values)
        combined_data = combined_data.fillna(0)
        header_list = list(combined_data.columns)
        return render(request, 'drug_resistant/output.html',{'genes':genes,'n':header_list,'new_drugres':new_drugres})

def contact(request):
    return render(request, 'drug_resistant/contact.html',{})

def search(request):
    return render(request, 'drug_resistant/search.html',{})

def output2(request):
    molecule = request.POST.get('tf')
    print(molecule)
    if molecule == 'select':
        gene = request.POST.get('sample')
        gene = gene.split()
        print(gene)

    
        data = Molecules.objects.filter(name__in=gene).values()
        print(data)
        return render(request, 'drug_resistant/output2.html',{'data':data})

    else:
        gene = request.POST.get('sample')
        gene = gene.split()

        data = Molecules.objects.filter(name__in=gene,molecules = molecule).values()
        return render(request, 'drug_resistant/output2.html',{'data':data})

    
    


     
     
def qsearch(request):

    return render(request, 'drug_resistant/qsearch.html',{})
     
def qoutput(request):
    gene = request.POST.get('t1')
    selected_columns = request.POST.getlist('checkboxes')
    column_list = ['cell_lo','control_cl','exp_inRes_cell','exp_method','drug','driver_molecule','post_tm','fold_ratio','biomarker_type','pmid_marker']
    if 'select_all' in selected_columns:
        selected_columns = column_list
    gene_list = [gene]  # If gene is None, use an empty list
    data = Molecules.objects.filter(name__in=gene_list).values(*selected_columns)
    if not data:
        return render(request, 'drug_resistant/error.html',{})
        
   
    return render(request, 'drug_resistant/QSoutput.html',{'data':data, 'gene':gene})
    
def faqs(request):
    return render(request, 'drug_resistant/faqs.html',{})

def browseinput(request):
    drug = Molecules.objects.filter().values('drug').distinct()
    cancer =Molecules.objects.filter().values('cell_lo').distinct()
    molecule =Molecules.objects.filter().values('molecules').distinct()

    return render(request, 'drug_resistant/browseinput.html',{"drug":drug,"cell":cancer, "molecules":molecule})

def browseoutput(request): 
    drug = request.POST.getlist('selected_value1')
    drug = [json.loads(d.replace("'", "\"")) for d in drug]
    drug = [d['drug'] for d in drug]
    print(drug)

    cancer = request.POST.getlist('selected_value2')
    cancer = [d.replace("'", "\"").replace("\\xa0", " ") for d in cancer]
    cancer = [json.loads(d) for d in cancer]
    cancer = [d['cell_lo'] for d in cancer]
    print(cancer)

    molecule = request.POST.getlist('selected_value3')
    molecule = [json.loads(d.replace("'", "\"")) for d in molecule]
    molecule = [d['molecules'] for d in molecule]
    print(molecule)

    # query = Molecules.objects.all()

    # q1 = Q(genes__in=genes, expression=exp1)
    # q2 = Q(genes__in=genes1, expression=exp2)

    # combined_query = q1 | q2

    # medicines = Drugs.objects.filter(combined_query).values()

    # if drug:
    #     query = query.filter(drug__in=drug)
    # if cancer:
    #     query = query.filter(cell_lo__in=cancer)
    # if molecule:
    #     query = query.filter(molecules__in=molecule)


    # data = query.values()

    q1 = Q(drug__in=drug)
    q2 = Q(cell_lo__in=cancer)
    q3 = Q(molecules__in=molecule)

    combined_query = q1 | q2| q3

    data = Molecules.objects.filter(combined_query).values()

    if not data:
        return render(request, 'drug_resistant/error3.html', {"data": data})
    else:
        return render(request, 'drug_resistant/browseoutput.html', {"data": data})
    
def pathway(request):
    return render(request, 'drug_resistant/pathway.html', {})





   
