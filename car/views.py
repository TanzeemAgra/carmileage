from django.shortcuts import render
import joblib
import pandas as pd
from .models import carmil

reloadModel = joblib.load('./models/RFModelforMPG.pkl')


def mileage(request):
    temp={}
    temp['cylinders']=1
    temp['displacement']=2
    temp['horsepower']=3
    temp['weight']=4
    temp['acceleration']=5
    temp['model_year']=6
    temp['origin']=1
    
    context={'temp':temp}
    return render(request, 'index.html',context)


def predictMPG(request):
    print(request)
    if request.method=='POST':
        temp={}
        temp['cylinders']=request.POST.get('cylinderVal')
        temp['displacement']=request.POST.get('dispVal')
        temp['horsepower']=request.POST.get('hrsPwrVal')
        temp['weight']=request.POST.get('weightVal')
        temp['acceleration']=request.POST.get('accVal')
        temp['model_year']=request.POST.get('modelVal')
        temp['origin']=request.POST.get('originVal')
        
        temp2=temp.copy()
        temp2['model year']=temp['model_year']
        del temp2['model_year']
        
        testDtaa=pd.DataFrame({'x':temp2}).transpose()
        scoreval = reloadModel.predict(testDtaa)[0]
        
    context={'scoreval':scoreval, 'temp':temp}
    
    return render(request, 'index.html', context)

def updatedb(request):
        cylinders=request.POST['cylinderVal']
        displacement=request.POST['dispVal']
        horsepower=request.POST['hrsPwrVal']
        weight=request.POST['weightVal']
        acceleration=request.POST['accVal']
        model_year=request.POST['modelVal']
        origin=request.POST['originVal']
        mpg=request.POST['mpgVal']
        o_ref = carmil(cylinders=cylinders, displacement=displacement, horsepower=horsepower, weight=weight, acceleration=acceleration,
                   model_year=model_year,origin=origin,mpg=mpg)
        o_ref.save()
        return render(request, 'index.html')
         
        
        
       
    
   
    
    
    
    
    
    
    
        
        
        
        
        
       
    
    
# Create your views here.
