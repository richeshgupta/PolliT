from django.shortcuts import render
from .forms import CreatePollForm
# Create your views here.
def CreatePoll(request):
    # if request.method=='POST':
    #     form = CreatePollForm(request.POST)
    #     if form.is_valid():
    #         # form = form.cleaned_data()
    #         form.save()
    # else:
    #     form = CreatePollForm()
    form=CreatePollForm(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request,"polls/createpoll.html",{'form':form})
