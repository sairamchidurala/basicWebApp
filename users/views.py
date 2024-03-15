from django.shortcuts import render, redirect
from .forms import UserForm
from .models import User

def input_form(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('data_table')
    else:
        form = UserForm()
    return render(request, 'input_form.html', {'form': form})

def data_table(request):
    users = User.objects.all()
    return render(request, 'data_table.html', {'users': users})
