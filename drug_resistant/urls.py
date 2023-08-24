from django.urls import path
from . import views

app_name = "drug_resistant"

urlpatterns = [
   path('',views.profile, name ="profile"),
    path('home0',views.home0, name ="home0"),
   path('home',views.home, name ="home"),
   path('home2',views.home2, name ="home2"),
   path('output',views.output, name ="output"),
   path('contact',views.contact, name ="contact"),
   path('search',views.search, name ="search"),
   path('error',views.output, name ="error"),
   path('output2',views.output2, name ="output2"),
   path('error2',views.output2, name ="error2"),
   path('error3',views.output2, name ="error3"),
   path('qsearch',views.qsearch, name ="qsearch"),
   path('QSoutput',views.qoutput, name ="qoutput"),
   path('faqs',views.faqs, name ="faqs"),
   path('browseinput',views.browseinput, name ="bin"),
   path('browseoutput',views.browseoutput, name ="bout"),
   path('pathway',views.pathway, name ="pw"),


]