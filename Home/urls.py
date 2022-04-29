from unicodedata import name
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from  Home import views
app_name = "Home"

urlpatterns = [
    # path('Student_Admission', views.Student_Admission , name='Student_Admission'  ),
    path('', views.Home  ),
    path('Base', views.Home , name="Base" ),
    path('Home', views.Home , name="Home" ),
    path('email_Data', views.email_Data , name="email_Data" ),
    path('Online-Admission', views.Addstudent , name="Online-Admission" ),
    path('About-Us', views.About , name="About-Us" ),
    path('Placement', views.Placement , name="Placement" ),
    path('ContactUs', views.ContactUs , name="ContactUs" ),
    path('Air-hostess', views.Air_hostess , name="Air-hostess" ),
    path('airport-management', views.airport_management , name="airport-management" ),
    path('cabin-crew', views.cabin_crew , name="cabin-crew" ),
    path('cruise-ship', views.cruise_ship , name="cruise-ship" ),
    path('diploma-in-avaition', views.diploma_in_avaition , name="diploma-in-avaition" ),
    path('hotel-management-bakery', views.hotel_management_backery , name="hotel-management-bakery" ),
    path('hotel-management-fb', views.hotel_management_fb , name="hotel-management-fb" ),
    path('hotel_management_in_kitchen', views.hotel_management_in_kitchen , name="hotel-management-in-kitchen" ),
    path('hotel-management', views.hotel_management , name="hotel-management" ),
    path('travel-turisum', views.travel_turisum , name="travel-turisum" ),
    
    # path('Recheck', views.Student_Admission_recheck , name='Recheck' ),
    
    # path('Manage-Lecture',Lectureviews.Lecture_manage ,name='Manage-Lecture'),
    # path('Lecture_edit/<int:id>/',Lectureviews.Lecture_edit ,name='Lecture_edit'),

    # revenue
    # path('Revenue',revenueviews.revenue,name='Revenue'),
    # path('Todays_Revenue',revenueviews.Todays_Revenue,name='Todays_Revenue'),
    # path('totalrevenue',revenueviews.totalrevenue,name='totalrevenue'),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
