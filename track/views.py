from django.shortcuts import render
from django.http import HttpResponse
from .models import District,Case
import pandas as pd
import json
import os
# Create your views here.




def home(request):
    cases = Case.objects.all()
    description = list()
    
    



    for case in cases:
        description.append(case.description)
        
        

    return render(request,'home.html',{'cases':cases,'total':len(description)})



def stats(request):
    data = pd.read_csv('data/patient_data.csv')

    recovered = list()
    hospitalized = list()
    deaths = list()
    locations = list()
    case_by_loc = list()

    for d in data['Status']:
        if d == 'Discharged':
            recovered.append(d)
        if d =='Hospitalized':
            hospitalized.append(d)
        if d =='Death':
            deaths.append(d)

    ##FOR COLUMN CHART

    unique = data['Location'].unique()
    counts = data['Location'].value_counts()

    for i in unique:
        locations.append(i)
        case_by_loc.append(int(counts[i]))

           





    context = {
        'recovered':json.dumps(len(recovered)),
        'hospitalized':json.dumps(len(hospitalized)),
        'deaths':json.dumps(len(deaths)),
        'locations':json.dumps(locations),
        'cases':json.dumps(case_by_loc)
    }        







    return render(request,'statistics.html',context=context)



def aboutus(request):
    return render(request,'aboutus.html')