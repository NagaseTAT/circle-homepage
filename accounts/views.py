from django.shortcuts import render

# Create your views here
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import SignUpForm, User
from django.contrib.auth.decorators import login_required
from    django.contrib.auth.decorators  import  login_required


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
    old_user = User.objects.get(id = user_id)
    if request.method == "POST":
        old_user.title = request.POST["title"]
        old_user.text = request.POST["text"]
        date = datetime.datetime.now()
        if old_user.username != '' & old_user.first_name != '' & old_user.last_name != '' & old_user.email != '':
            old_user.save()
        return redirect(adminPostsList)
    else:
        # placeholder設定のため以下２行
        initial_dict = dict(old_user = username )
        form = PostForm(request.GET or None, initial=initial_dict)

        return render(request, 'blog/AdminPostsRegister.html', {})