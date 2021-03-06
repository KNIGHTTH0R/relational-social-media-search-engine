from django.conf.urls import url
from . import views

app_name = 'testApp'
urlpatterns = [
    url(r'^index', views.index, name='index'),
	url(r'^$', views.index, name='index'),
	url(r'^upload/', views.upload, name='upload'),
	url(r'^searchNow/', views.formSearch, name='searchNow'),
	url(r'^batchSearch/', views.batchSearch, name='batchSearch'),
	url(r'^searchgradaction/',views.searchUnderGrad, name='searchgradaction'),
	url(r'^sortviewaction/$', views.sortView, name='sortviewaction'),
	url(r'^searchgrad/', views.searchgrad2, name='searchgrad'),
	url(r'^employ/', views.employ, name='employ'),
	url(r'^retrive/', views.retrive, name='retrive'),
	url(r'^filter/', views.filter, name='filter'),
	url(r'^search/', views.search, name='search'),
	url(r'^delete/', views.delete, name='delete'),
	url(r'^remove/', views.remove, name='remove'),
	url(r'^update/(?P<email_id>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/$', views.update, name='update'),
	url(r'^updateByID/(?P<personId>[0-9]+)/$', views.updateByID, name='updateByID'),
	url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^results/$', views.results, name='results'),
	url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    url(r'^utdsearch/$', views.utdsearch, name='utdsearch'),
    url(r'^merge_update/$', views.mergedUpdate, name='mergedUpdate_update'),
	## Facebook starts
    url(r'^fetchSocialScores/$', views.fetchSocialScores, name='fetchSocialScores'),
	url(r'^fetchVisualRecogResults/$', views.fetchVisualRecogResults, name='fetchVisualRecogResults'),
	url(r'^groundtruth/$', views.facebooktwo, name='facebooktwo'),
	url(r'^combined/$', views.facebookthree, name='facebookthree'),
    url(r'^allresults/$', views.allresults, name='allresults'),

	url(r'^facebook/$', views.facebook, name='facebook'),


	url(r'^combinedexc/$', views.facebookthreeand, name='facebookthreeand'),
	url(r'^listing/$', views.facebookfive, name='facebookfive'),
	url(r'^verifiednonverified/$', views.facebooksix, name='facebooksix'),
	url(r'^seedunverified/$', views.facebookseven, name='facebookseven'),

	url(r'^markProfile/$', views.markProfile, name='markProfile')
	## Facebook ends
	]
