from django.shortcuts import render , redirect
from django.http import HttpResponse
from .forms import MemberForm, ChapterForm
from .models import Member, Chapter
from django.contrib import messages
import os

def modal(request):
    return render(request, 'components/modal.html')

def homepage(request):
    return render(request, 'accounts/homepage.html')

def addMember(request):
    form = MemberForm()
    if request.method == 'POST':
        form = MemberForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Data inserted successfully")
        else:
            messages.error(request, "Data was not inserted. Please correct the errors below.")
    # context = {'form': form}
    return render(request, 'accounts/add-member.html')

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

def addChapter(request):
    form = ChapterForm()
    if request.method == "POST":
        form = ChapterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Added Chapter Successfully")
            return redirect('/chapter')
        else:
            messages.error(request,"Error")
    # context = {"form": form}
    # return render(request, "accounts/chapter.html")

def viewChapter(request):
    form = Chapter.objects.all()
    print("form",form)
    context = {'form': form}
    return render(request, "accounts/chapter.html", context)

def editChapter(request, pk):
    form = Chapter.objects.get(id=pk)
    if request.method == "POST":
        form.title=request.POST.get("title")
        form.description=request.POST.get("description")
        form.date=request.POST.get("date")
        form.save()
        messages.success(request,"Edited Successfully")
        context = {'form': form}

        return render(request, "accounts/chapter.html", context)
