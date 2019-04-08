from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.shortcuts import render, get_object_or_404
from registration.models import Profile
from django.views.generic.detail import DetailView

# Create your views here.
# Vista que lista los perfiles existentes
class ProfileListView(ListView):
    model = Profile
    # Template que usará la vista
    template_name = 'profiles/profile_list.html'
    paginate_by = 2

class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'profiles/profile_detail.html'
    
    # Se redefine este método para recuperar el perfil por medio del parametro <username>
    def get_object(self):
        return get_object_or_404(Profile, user__username=self.kwargs['username'])

