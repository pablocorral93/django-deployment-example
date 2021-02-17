from django.urls import path
from basic_app import views



#TEMPLATE TAGGING




urlpatterns=[

	path('relative/', views.relative, name='relative'),
	path('other/', views.other, name='other'),
]