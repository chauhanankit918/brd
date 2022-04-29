from django.shortcuts import redirect, render

from Student.forms import Student_detailForm
from Home.models import email_data, q_form
import sweetify
# Create your views here.
def Home(request):
    # {{ request.get_host }}
    # print(request.get_host)
    # print(request.scheme)
    # print(request.META['HTTP_HOST'])
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        qform = q_form.objects.create(name = name , email=email , phone = phone , message = message)
        sweetify.success(request, 'Hey', text= 'You have successfully filled the form', persistent='Done')
        qform.save()
        
        return redirect('Home:Base')
        
    return render(request, 'Home/index.html')

def email_Data(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        emaildata = email_data.objects.create(email=email)
        emaildata.save()
        sweetify.success(request, 'Hey', text= 'You have successfully SUBSCRIBED', persistent='Done')
        return redirect('Home:Home')
        

def Addstudent(request):
    form = Student_detailForm()
    context = {
        'form':form
    }
    return render(request, 'Home/Addstudent.html' , context)
def About(request):
    return render(request, 'Home/about.html')
def Placement(request):
    return render(request, 'Home/placement.html')
def ContactUs(request):
    return render(request, 'Home/contactUs.html')
def Air_hostess(request):
    return render(request, 'Home/Air-hostess.html')
def airport_management(request):
    return render(request, 'Home/airport-management.html')
def cabin_crew(request):
    return render(request, 'Home/cabin-crew.html')
def cruise_ship(request):
    return render(request, 'Home/cruise-ship.html')
def diploma_in_avaition(request):
    return render(request, 'Home/diploma-in-avaition.html')
def hotel_management_backery(request):
    return render(request, 'Home/hotel-management-backery.html')
def hotel_management_fb(request):
    return render(request, 'Home/hotel-management-fb.html')
def hotel_management_in_kitchen(request):
    return render(request, 'Home/hotel-management-in-kitchen.html')
def hotel_management(request):
    return render(request, 'Home/hotel-management.html')
def travel_turisum(request):
    return render(request, 'Home/travel-turisum.html')



