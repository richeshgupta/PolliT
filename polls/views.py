from django.shortcuts import render
from .forms import CreatePollForm
from .models import Poll
from django.contrib.auth.mixins	import LoginRequiredMixin
from django.views.generic import CreateView

# Create your views here.
# def CreatePoll(request):
#     if request.method=='POST':
#         form=CreatePollForm(request.POST)
#         if form.is_valid():
            
#             form.save()
#     else:
#         form=CreatePollForm()
#     return render(request,"polls/createpoll.html",{'form':form})


class CreatePoll(LoginRequiredMixin,CreateView):
    model = Poll
    template_name='polls/createpoll.html'
    context_object_name='form'
    fields = ["name",'text','option1','option2','option3','option4','is_anon'] 
    def form_valid(self,CreatePollForm):
        # Always add .instance or your half hour is fucked
        CreatePollForm.instance.author = self.request.user
        return super().form_valid(CreatePollForm)
        
