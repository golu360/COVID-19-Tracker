from django.shortcuts import render
from django.http import HttpResponse
from .models import District,Case
import json
# Create your views here.


'''
def home(request):
    dataset = District.objects.all()

    district_names = list()
    positives = list()
    recovered = list()
    tested = list()
    deaths = list()
    quarantined = list()


    for district in dataset:
        district_names.append(district.district_name)
        positives.append(district.district_positive)
        recovered.append(district.district_recovered)
        tested.append(district.district_tested)
        quarantined.append(district.district_quarantined)
        deaths.append(district.district_deaths)

    context = {
        'names': json.dumps(district_names),
        'positives':json.dumps(positives),
        'recovered': json.dumps(recovered),
        'tested':json.dumps(tested),
        'deaths':json.dumps(deaths),
        'quarantined':json.dumps(quarantined)
    }    



    return render(request,'home.html',context=context)
'''


def home(request):
    cases = Case.objects.all()
    description = list()
    
    



    for case in cases:
        description.append(case.description)
        
        

    return render(request,'home.html',{'cases':cases,'total':len(description)})



