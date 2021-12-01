from django.shortcuts import render

# Create your views here
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from blog.views import adminPostsList
from .forms import SignUpForm, User
from django.contrib.auth.decorators import login_required
from    django.contrib.auth.decorators  import  login_required
from django.shortcuts import render,redirect # redirectを追記
from django.http import Http404



# class SignUpView(generic.CreateView):
#     form_class = UserCreationForm
#     success_url = reverse_lazy('login')
#     template_name = 'accounts/signup.html'

class SignUp(CreateView):
    form_class = SignUpForm
    template_name = "accounts/signup.html"
    success_url = reverse_lazy('adminPostsList')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        self.object = user
        return HttpResponseRedirect(self.get_success_url())

@login_required
def userEdit(request):
    user_id = request.user.id
    try:
        old_user = User.objects.get(id = user_id)
    except User.DoesNotExist:
        raise Http404
    if request.method == "POST":
        old_user.username = request.POST["username"]
        old_user.first_name = request.POST["first_name"]
        old_user.last_name = request.POST["last_name"]
        old_user.email = request.POST["email"]
        old_user.save()
        return redirect(adminPostsList)

    return render(request, 'accounts/useredit.html', {"old_user":old_user})