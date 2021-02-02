from django.shortcuts import render
from .forms import CreatePollForm
from .models import Poll
from django.contrib.auth.mixins	import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import CreateView,UpdateView,DeleteView
from django.contrib.auth.decorators import login_required
from django.db import connection
from django.http import HttpResponse
import json
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
        return ErrorPage(request,"No Poll found!")
    else:
        return render(request,"polls/poll.html",{'objs':objs.first()})

    
class UpdatePoll(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
	model = Poll
	fields = ["name",'text','option1','option2','option3','option4','is_anon']
	context_object_name = 'form'
	def form_valid(self,CreatePollForm):
		CreatePollForm.instance.author = self.request.user
		return super().form_valid(CreatePollForm)
	def test_func(self):
		test_case = self.get_object()
		if self.request.user == test_case.author:
			return True
		else:
			return False
class DeletePoll(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
	model = Poll
	success_url = '/'
	def test_func(self):
		test_case = self.get_object()
		if self.request.user == test_case.author:
			return True
		else:
			return False

@login_required 
def CountPoll(request):
    if request.method=='POST':
        pollId=request.POST['pollId']
        count=request.POST['count']
        cursor = connection.cursor()
        cursor.execute("select * FROM polls_poll where id=%s ",[pollId])
        if(count=='1'):
            count=cursor.fetchone()[-6]+1
            cursor.execute("update polls_poll set count1=%s where id=%s ",[count,pollId])
        elif(count=='2'):
            count=cursor.fetchone()[-5]+1
            cursor.execute("update polls_poll set count2=%s where id=%s ",[count,pollId])
        elif(count=='3'):
            count=cursor.fetchone()[-4]+1
            cursor.execute("update polls_poll set count3=%s where id=%s ",[count,pollId])
        else:
            count=cursor.fetchone()[-3]+1
            cursor.execute("update polls_poll set count4=%s where id=%s ",[count,pollId])
        a='done'
        return HttpResponse(json.dumps({'a': a}), content_type="application/json")

