from django.shortcuts import render
from .forms import CreatePollForm
from .models import Poll
from django.contrib.auth.mixins	import LoginRequiredMixin
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required

class CreatePoll(LoginRequiredMixin,CreateView):
    model = Poll
    template_name='polls/createpoll.html'
    context_object_name='form'
    fields = ["name",'text','option1','option2','option3','option4','is_anon'] 
    def form_valid(self,CreatePollForm):
        # Always add .instance or your half hour is fucked
        CreatePollForm.instance.author = self.request.user
        return super().form_valid(CreatePollForm)

@login_required        
def MyPolls(request):
    objs = Poll.objects.all().filter(author=request.user)
    return render(request,"polls/mypolls.html",{'objs':objs})

def ErrorPage(request,error):
    if len(error)<1:
        error = "No Valid Thrown error"
    return render(request,"users/error.html",{'error':error})

def SpecificPoll(request,pk):
    objs = Poll.objects.filter(id=pk)
    if not objs.count():
        print("Error")
        return ErrorPage(request,"No Poll found!")
    else:
        print(objs)
        return render(request,"polls/poll.html",{'objs':objs.first()})