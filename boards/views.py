from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from .models import Board, Topic, Post
from django.http import HttpResponse
from .models import Board
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from boards.models import Complaints
from boards.forms import ComplaintForm

def home(request):
    boards = Board.objects.all()
    return render(request, 'home.html', {'boards': boards})



def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def board_topics(request, pk):
    board = Board.objects.get(pk=pk)
    return render(request, 'topic.html', {'board': board})

def new_topic(request, pk):
    board = get_object_or_404(Board, pk=pk)

    if request.method == 'POST':
        subject = request.POST['subject']
        message = request.POST['message']

        user = User.objects.first()  # TODO: get the currently logged in user

        topic = Topic.objects.create(
            subject=subject,
            board=board,
            starter=user
        )

        post = Post.objects.create(
            message=message,
            topic=topic,
            created_by=user
        )

        return redirect('board_topics', pk=board.pk)  # TODO: redirect to the created topic page

    return render(request, 'new_topic.html', {'board': board})
def addComplaint(request):

    if(request.method=="POST"):
        row=Complaints()
        row.ComplaintRegarding=request.POST.get('ComplaintRegarding','')
        row.ProblemFacedOn=request.POST.get('ProblemFacedOn','')
        row.ContactNo=request.POST.get('ContactNo','')
        row.DescribeYourIssue = request.POST.get(' DescribeYourIssue', '')
        row.save()
        return  render(request,'home.html',{})
    else:
     drf=ComplaintForm
     return render(request,'Complaint.html',{'form':drf})