import random

from django.conf import settings
from django.contrib.auth.hashers import make_password
from django.db import IntegrityError
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from twilio.rest import Client

from .forms import VoterForm
from .models import Voter
from django.contrib import messages
def homepage(request):
    return render(request,'homepage.html')
def navbar(request):
    return render(request,'navbar.html')


from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from .models import Voter


def register(request):
    if request.method == "POST":
        username = request.POST['username']
        epic_number = int(request.POST['epic_number'])
        password = make_password(request.POST['password'])

        # Check if a user with the given username or epic number already exists
        if Voter.objects.filter(username=username).exists() or Voter.objects.filter(epic_number=epic_number).exists():
            messages.error(request, 'User already exists.')
            return render(request, 'register.html')

        # Proceed with user creation...
        voter = Voter(username=username, epic_number=epic_number, password=password)
        voter.save()

        # Redirect or show a success message
        messages.success(request, 'Registration successful.')
        return redirect('display')

    return render(request, 'register.html')

def login(request):
    return render(request,'login.html')
def votehere(request):
    return  render(request,'votehere.html')
def aboutus(request):
    return  render(request,'aboutus.html')
def voteguide(request):
    return render(request,'voteguide.html')
def nav(request):
    return render(request,'nav.html')
def display(request):
    return render(request,'display.html')

def exist(request):
    return render(request,'exist.html')

def viewvoters(request):
    # Fetch all voter objects from the database
    voters = Voter.objects.all()

    # Pass the voters to the template
    return render(request, 'viewvoters.html', {'voters': voters})

def edit_voter(request, voter_id):
    # Example edit logic (you'll need to implement this according to your requirements)
    voter = get_object_or_404(Voter, pk=voter_id)
    # Assume you have a form for editing; handle form submission and rendering here
    return render(request, 'edit_voter.html', {'voter': voter})

def delete_voter(request, voter_id):
    # Example delete logic
    voter = get_object_or_404(Voter, pk=voter_id)
    voter.delete()
    return redirect('viewvoters')  # Redirect to the list of voters after deleting

class EditVoterView(UpdateView):
    model = Voter
    form_class = VoterForm
    template_name = 'edit_voter.html'  # Specify your template name
    pk_url_kwarg = 'voter_id'  # This should match the keyword in your URL pattern
    success_url = reverse_lazy('viewvoters')  # Redirect to the voter list view after successful update

    def edit_voter(request, voter_id):
        voter = get_object_or_404(Voter, pk=voter_id)
        if request.method == 'POST':
            form = VoterForm(request.POST, instance=voter)
            if form.is_valid():
                form.save()
                return redirect('viewvoters')  # Redirect to the voter listing page
        else:
            form = VoterForm(instance=voter)
        return render(request, 'edit_voter.html', {'form': form})

