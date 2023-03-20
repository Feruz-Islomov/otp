from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView
from .forms import CustomUserCreationForm
from .models import CustomUser
from washers.models import Balance
import os
from .decorators import unauthenticated_user

# class registerPage(CreateView):
#     form_class = CustomUserCreationForm
#     success_url= reverse_lazy('login')
#     template_name= 'registration/signup.html'
@unauthenticated_user
def registerPage(request):
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # username = form.cleaned_data.get('username')
            group = Group.objects.get(name='client')
            user.groups.add(group)
            return redirect('login')
    context = {'form': form}
    return render(request, 'registration/signup.html', context)


@login_required
def clientProfileEdit(request, pk):
    client = CustomUser.objects.get(id=pk)

    if request.method == 'POST':
        # print('after post condition')
        if len(request.FILES) != 0:
            # print('after FILES condition')
            # print(bool(client.photo))
            if bool(client.photo) == True and len(client.photo) > 0:
                # print('after photo condition')
                os.remove(client.photo.path)
            client.photo = request.FILES['image']
        client.first_name = request.POST.get('first_name')
        client.last_name = request.POST.get('last_name')
        client.tel = request.POST.get('tel')
        client.shahar = request.POST.get('shahar')        
        client.save()
    
        messages.success(request, 'photo changed succesfully.')
        return redirect('/client_profile')
    
    context = {'user': client}
    return render(request, 'client/client_profile_edit.html', context)

@unauthenticated_user
class ClientProfileEdit(LoginRequiredMixin, UpdateView):
    model = CustomUser
    fields = ('first_name','last_name', 'tel', 'shahar','photo')
    template_name = 'client/client_profile_edit.html'