from django.shortcuts import render , redirect
from django.http import HttpResponse
from .forms import MemberForm
from .models import Member
from django.contrib import messages
import os

def homepage(request):
    return render(request, 'accounts/homepage.html')

def addMember(request):
    form = MemberForm()
    if request.method == 'POST':
        form = MemberForm(request.POST, request.FILES)
        print("form:", form)
        if form.is_valid():
            form.save()
            messages.success(request, "Data inserted successfully")
        else:
            messages.error(request, "Data was not inserted. Please correct the errors below.")
    context = {'form': form}
    return render(request, 'accounts/add-member.html', context)

def viewMember(request):
    form = Member.objects.all()
    context = {'form': form}
    return render(request, 'accounts/view-member.html', context)

def editMember(request, pk):
    member = Member.objects.get(id=pk)
    if request.method == 'POST':
            if len(request.FILES) != 0:
                if len(member.image) > 0:
                    os.remove(member.image.path)
                member.image = request.FILES['image']
            member.name=request.POST.get('name')
            member.age=request.POST.get('age')
            member.phone=request.POST.get('phone')
            member.email=request.POST.get('email')
            member.save()
            messages.success(request, "Member Updated Successfully")
            return redirect('/view-member')
    context = {'form': member}
    return render(request, 'accounts/edit-member.html', context)

def deleteMember(request,pk):
    member_data = Member.objects.get(id=pk)
    if len(member_data.image) > 0:
        os.remove(member_data.image.path)
    member_data.delete()
    messages.success(request,"Product Deleted Successfuly")
    return redirect('/view-member')

