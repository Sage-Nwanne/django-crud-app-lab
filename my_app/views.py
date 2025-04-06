from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView, ListView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.urls import reverse
from .models import Park, Attraction

class Home(LoginView):
    template_name = 'home.html'

def about(request):
    return render(request, 'about.html')

@login_required
def parks_index(request):
    parks = Park.objects.filter(user=request.user)
    return render(request, 'parks/index.html', { 'parks': parks })

@login_required
def parks_detail(request, park_id):
    park = Park.objects.get(id=park_id)
    return render(request, 'parks/detail.html', { 'park': park })

class ParkCreate(LoginRequiredMixin, CreateView):
    model = Park
    fields = ['name', 'location', 'description']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ParkUpdate(LoginRequiredMixin, UpdateView):
    model = Park
    fields = ['name', 'location', 'description']

class ParkDelete(LoginRequiredMixin, DeleteView):
    model = Park
    success_url = '/parks/'


class AttractionCreate(LoginRequiredMixin, CreateView):
    model = Attraction
    fields = ['name', 'description', 'type']
    
    def form_valid(self, form):
        form.instance.park_id = self.kwargs['park_id']
        return super().form_valid(form)


class AttractionDetail(LoginRequiredMixin, DetailView):
    model = Attraction


class AttractionList(LoginRequiredMixin, ListView):
    model = Attraction
    
    def get_queryset(self):
        return Attraction.objects.filter(park__user=self.request.user)


class AttractionUpdate(LoginRequiredMixin, UpdateView):
    model = Attraction
    fields = ['name', 'description', 'type']
    template_name = 'my_app/attraction_form.html'

    def get_success_url(self):
        return reverse('park-detail', kwargs={'park_id': self.object.park.id})


class AttractionDelete(LoginRequiredMixin, DeleteView):
    model = Attraction
    template_name = 'my_app/attraction-confirm-delete.html'
    
    def get_success_url(self):
        return reverse('park-detail', kwargs={'park_id': self.object.park.id})

@login_required
def add_attraction(request, park_id):
    park = Park.objects.get(id=park_id)
    if request.method == 'POST':
        Attraction.objects.create(
            name=request.POST['name'],
            description=request.POST['description'],
            type=request.POST['type'],
            park=park
        )
        return redirect('park-detail', park_id=park_id)
    return render(request, 'parks/add_attraction.html', {
        'park': park
    })

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('park-index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)
