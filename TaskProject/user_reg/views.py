from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import redirect, render
from django.db.models.functions import Extract

from .forms import UserRegForm
from .models import User

# Create your views here.

# def index(request):
#     return HttpResponse('work')


def index(request):
    if request.method == 'POST':
        print(request.POST)
        form = UserRegForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('user_reg:index'))
        else:
            context = {'form': form}
    else:
        form = UserRegForm()
        users = User.objects.order_by('birth_date')[:]
        context = {'form': form, 'users': users }

    return render(request, 'user_reg/index.html', context)
