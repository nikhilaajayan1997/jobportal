from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import View,ListView,CreateView,DetailView,UpdateView,DeleteView,TemplateView,FormView
from employer.forms import JobForm
from employer.models import Jobs
from django.contrib.auth import authenticate,login,logout

from django.contrib.auth.models import User
from employer.forms import SignUpForm,LoginForm



class EmployerHomeView(TemplateView):
    template_name = "emp-home.html"

    # def get(self,request):
    #     return  render(request,"emp-home.html")


class AddJobView(CreateView):
    model=Jobs
    form_class=JobForm
    template_name ="emp-addjob.html"
    success_url = reverse_lazy("emp-alljobs")     # used in the place where we have  POST operation


    # def get(self,request):
    #     form=JobForm()
    #     return render(request,"emp-addjob.html",{"form":form})
    #
    # def post(self,request):
    #     form=JobForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect("emp-alljobs")
    #     else:
    #         return  render(request,"emp-addjob.html",{"form":form})



# All details
class ListJobView(ListView):
    model=Jobs
    context_object_name="jobs"  # this is the key in context dictionary
    template_name="emp-listjob.html"

    # def get(self,request):
    #     qs=Jobs.objects.all()
    #     return render(request,"emp-listjob.html",{"jobs":qs})






# Details of single record

class JobDetailView(DetailView):
    model = Jobs
    context_object_name= "job"
    template_name="emp-detailjob.html"
    pk_url_kwarg = "id"


    # def get(self,request,id):
    #     qs=Jobs.objects.get(id=id)
    #     return render(request,"emp-detailjob.html",{"job":qs})



 # Editing single record
class JobEditView(UpdateView):

    model=Jobs
    template_name = "emp-editjob.html"
    form_class = JobForm
    pk_url_kwarg = "id"
    success_url = reverse_lazy("emp-alljobs")

    # def get(self,request,id):
    #     qs=Jobs.objects.get(id=id)
    #     form=JobForm(instance=qs)  # This stmt(object creation) gives form with filled data
    #     return render(request,"emp-editjob.html",{"form":form})
    #
    # def post(self,request,id):
    #     qs=Jobs.objects.get(id=id)
    #     form=JobForm(request.POST,instance=qs)
    #     if form.is_valid():
    #         form.save()
    #         return redirect("emp-alljobs") # here we are actually calling ListJobView
    #     else:
    #         return render(request,"emp-editjob.html",{"form":form})

class JobDeleteView(DeleteView):

    template_name ="jobconfirmdelete.html"
    model = Jobs
    success_url = reverse_lazy("emp-alljobs")
    pk_url_kwarg = "id"


    # def get(self,request,id):
    #     qs=Jobs.objects.get(id=id)
    #     qs.delete()
    #     return  redirect("emp-alljobs")


class SignUpView(CreateView):
    model = User
    form_class = SignUpForm
    template_name = "usersignup.html"
    success_url = reverse_lazy("emp-alljobs")

class SignInView(FormView):
    form_class = LoginForm
    template_name = "login.html"

    def post(self, request,*args,**kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            uname = form.cleaned_data.get("username")
            pwd = form.cleaned_data.get("password")
            user = authenticate(request, username=uname, password=pwd)
            if user:
                login(request,user)
                return redirect("emp-home")
            else:
                return render(request,"login.html",{"form":form})


def signout_view(request,*args,**kwargs):
    logout(request)
    return redirect("signin")

class ChangePasswordView(TemplateView):
    template_name = "changepassword.html"

    def post(self,request,*args,**kwargs):
        pwd=request.POST.get("pwd")   #taking pwd from dictionary
        uname=request.user            #taking username
        user=authenticate(request,username=uname,password=pwd)
        if user:
            return redirect("passwordrest")
        else:
            return render(request,self.template_name)


class PasswordResetView(TemplateView):
    template_name = "passwordreset.html"

    def post(self,request,*args,**kwargs):
        pwd1=request.POST.get("pwd1")
        pwd2=request.POST.get("pwd2")
        if pwd1!=pwd2:
            return render(request,self.template_name,{"msg":"Password mismatch"})
        else:
            u=User.objects.get(username=request.user)
            # u=request.user  .....................  This is also working
            u.set_password(pwd1)
            u.save()
            return redirect("signin")




