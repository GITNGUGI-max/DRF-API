from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'donors', views.DonorViewSet)
router.register(r'counties', views.CountyViewSet)
router.register(r'sub_counties', views.SubCountyViewSet)
router.register(r'patients', views.PatientViewSet)
router.register(r'messages', views.MessageViewSet)

urlpatterns =[
	# path('', views.api_root),
	# path('donors/', views.DonorList.as_view(), name='donor-list'),
	# path('patients/', views.PatientList.as_view(), name='patient-list'),
	# path('counties/', views.CountyList.as_view(), name='county-list'),
	# path('sub_counties/', views.SubCountyList.as_view(), name='sub_county-list'),
	# path('donor_messages/', views.DonorMessageList.as_view()),
	# path('patient_messages/', views.PatientMessageList.as_view()),
	# path('donor/<int:pk>/', views.DonorDetail.as_view(), name='donor-detail'),
	# path('patient/<int:pk>/', views.PatientDetail.as_view(),  name='patient-detail'),
	# path('county/<int:pk>/', views.CountyDetail.as_view(),  name='county-detail'),
	# path('sub_county/<int:pk>/', views.SubCountyDetail.as_view(),  name='subcounty-detail'),
	# path('donor_message/<int:pk>/', views.DonorMessageDetail.as_view()),
	# path('patient_message/<int:pk>/', views.PatientMessageDetail.as_view()),
	# path('users/', views.UserList.as_view(), name='user-list'),
	# path('user/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
	path('api/', include(router.urls)),

]


# urlpatterns = format_suffix_patterns(urlpatterns)