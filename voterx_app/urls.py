from django.conf.urls import url
from django.views.generic import ListView, DetailView

from voterx_app import views
from voterx_app import models

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^name/$', views.NameView.as_view()),
    url(r'^demographics/$', views.DemographicsView.as_view()),
    url(r'^residence/$', views.ResidenceView.as_view()),
    url(r'^phone/$', views.PhoneNumberView.as_view()),
    url(r'^email/$', views.EmailView.as_view()),
    url(r'^commercial/$', views.CommercialView.as_view()),
    url(r'^party/$', views.PartyView.as_view()),
    url(r'^district/$', views.DistrictView.as_view()),
    url(r'^commercial2/$', views.Commercial2View.as_view()),
    url(r'^commercial-fec/$', views.CommercialfecView.as_view()),
    url(r'^comercial-interest/$', views.CommercialinterestsView.as_view()),
    url(r'^commercial-home/$', views.CommercialhomepurchasingView.as_view()),
    url(r'^vote-history/$', views.VotehistoryView.as_view()),
    url(r'^cs-dr-tv/$', views.CsDrtvVoterView.as_view()),
    url(r'^r7-l2-voter/$', views.R7L2VoterView.as_view()),
    url(r'^aggregated-voter/$', views.AggregatedVoterView.as_view()),

]