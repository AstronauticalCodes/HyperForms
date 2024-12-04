from msilib.schema import RemoveRegistry

from django.shortcuts import render, redirect
from .forms import RegisterForm
from .models import RegisterFormModel
from django.views import View
# Create your views here.


def index(request):
    # records = RegisterForm.objects.all()
    print('hello')
    # print(RegisterForm.age)
    form_data = RegisterFormModel.objects.all()
    if len(form_data):
        data_avail = True
    else:
        data_avail = False
    return render(request, 'forms/index.html', context={'data_avail': data_avail, 'form': form_data})


def getdata():
    data = RegisterFormModel.objects.all()
    for x in data:
        print(x.name)
    # print(Data)


class RegisterFormView(View):
    template_name = 'forms/registerForm.html'
    form = RegisterForm()

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'form': self.form})

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            pass

        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            data = form.cleaned_data
            getdata()
            for key in data:
                print(f"{key}: {data[key]}")

        return redirect('/')
