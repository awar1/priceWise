from django.shortcuts import render
from .forms import ModelForm
import pickle
import numpy as np

def predict_model(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ModelForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            rent = form.cleaned_data['rent']
            size = form.cleaned_data['size']
            no_of_rooms = form.cleaned_data['no_of_rooms']
            year = form.cleaned_data['year']
            dist_from_underground = form.cleaned_data['dist_from_underground']
            longitude = form.cleaned_data['longitude']
            lattitude = form.cleaned_data['lattitude']
            height = form.cleaned_data['height']

            feats = np.array([rent,size,no_of_rooms,year,dist_from_underground,longitude,lattitude,height]).reshape(1, -1)
            pred_model = pickle.load(open("predModel/prediction_model.pkl", "rb"))
            scaler =  pickle.load(open("predModel/scaler.pkl", "rb"))
            scaled_feats = scaler.transform(feats)
            # give prediction response
            prediction = int(pred_model.predict(scaled_feats)[0])
            return render(request, 'home.html', {'form': form, 'prediction': prediction})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ModelForm()

    return render(request, 'home.html', {'form': form})