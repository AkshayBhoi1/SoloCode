from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render
from .models import *
from django.contrib import messages

# Create your views here.


@login_required(login_url='loginpage')
def profile(request):
    name = request.user.first_name
    email = request.user.email
    id = request.user.id
    ak = UserData.objects.filter(id=id)

    mname = None;
    lname = None;
    contact = None;
    address = None;
    city = None;
    state = None;
    zip = None;

    for i in ak:
        lname = i.lname
        mname = i.mname
        contact = i.contact
        address = i.address
        city = i.city
        state = i.state
        zip = i.zip
    context = {
        'name': name, 'email': email, 'mname': mname, 'lname': lname, 'contact': contact, 'address': address, 'city': city, 'state': state, 'zip': zip
    }
    if request.method == 'POST':
        first_name = request.POST['fname']
        mname = request.POST['mname']
        lname = request.POST['lname']
        contact = request.POST['contact']
        email = request.POST['Email']
        address = request.POST['address']
        city = request.POST['city']
        state = request.POST['state']
        zip = request.POST['zip']
        print(zip)
        # Save or Update data in UserData
        students = UserData(id=id, first_name=first_name,  mname=mname, lname=lname, contact=contact, email=email, address=address, city=city, state=state, zip=zip)
        students.save()
        # Update data in User
        User.objects.filter(id=id).update(first_name=first_name, last_name=lname, email=email)
    return render(request, 'profile.html', context)


# @login_required(login_url='loginpage')
def help(request):
    if request.method == 'POST':
        # id = request.user.id
        N = request.POST['fname']
        email = request.POST['Email']
        contact = request.POST['contact']
        message = request.POST['message']
        students = Help(Fname=N, email=email, contact=contact, Message=message)
        students.save()
        messages.success(request, "Message send successfully")
    return render(request, 'help.html')
