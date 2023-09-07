from django.contrib import admin
from django.urls import path

# importing views from views..py
from .views import home, page1, demo, state_wise_literacy, sports, science, georgraphy, politics, ap, ap2, assam, bihar, chhattisgarh, goa, gujarat, haryana, hp, jharkhand, karnataka, kerala, meghalaya, mizoram, mp, nagaland, odisha, punjab, rajasthan, maharastra, manipur, sikkim, telangana, tn, uk, tripura, up, wb

urlpatterns = [
    path('home.html', home),
    path('', page1),
    path('page1.html', page1),
    path('demograph.html', demo),
    path('state.html', state_wise_literacy),
    path('achievements_in_sports.html', sports),
    path('science.html', science),
    path('geography.html', georgraphy),

    path('politics.html', politics),
    path('ap.html', ap),
    path('ap2.html', ap2),
    path('assam.html', assam),
    path('bihar.html', bihar),
    path('chhattisgarh.html', chhattisgarh),
    path('goa.html', goa),
    path('gujarat.html', gujarat),
    path('haryana.html', haryana),
    path('hp.html', hp),
    path('jharkhand.html', jharkhand),
    path('karnataka.html', karnataka),
    path('kerala.html', kerala),
    path('maharastra.html', maharastra),
    path('mp.html', mp),
    path('manipur.html', manipur),
    path('meghalaya.html', meghalaya),
    path('mizoram.html', mizoram),
    path('nagaland.html', nagaland),
    path('odisha.html', odisha),
    path('punjab.html', punjab),
    path('rajasthan.html', rajasthan),
    path('sikkim.html', sikkim),
    path('tn.html', tn),
    path('tripura.html', tripura),
    path('telangana.html', telangana),
    path('up.html', up),
    path('uk.html', uk),
    path('wb.html', wb),
]
