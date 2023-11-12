
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login
from django.shortcuts import get_object_or_404, render, redirect
from django.core.mail import send_mail, BadHeaderError

from courses.models import Course, Module
from educa.settings.pro import DEFAULT_FROM_EMAIL
from quiz.models import Result
from analytics.models import UserSession
from .forms import ContactForm, CourseEnrollForm
from allauth.account.forms import SignupForm
from allauth.account.views import SignupView

class StudentRegistrationView(SignupView):
   template_name = 'students/student/registration.html'
   form_class = SignupForm
   success_url = reverse_lazy('student_course_list')

   def form_valid(self, form):
        result = super().form_valid(form)
        cd = form.cleaned_data
        user = authenticate(email=cd['email'], password=cd['password1'])
        login(self.request, user)
        return result



class StudentDashboard(LoginRequiredMixin, ListView):
    model = Result
    template_name = 'account/dashboard.html'

    def get_queryset(self):
        qs = Result.objects.filter(user=self.request.user)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['courses'] = Course.objects.filter(students=self.request.user)
        context['total_time'] = UserSession.objects.filter(user=self.request.user, ended=True)
        return context
   
        
# class StudentRegistrationView(CreateView):
#     template_name = 'students/student/registration.html'
#     form_class = SignupForm
#     success_url = reverse_lazy('student_course_list')

#     def form_valid(self, form):
#         result = super().form_valid(form)
#         cd = form.cleaned_data
#         user = authenticate(username=cd['username'], password=cd['password1'])
#         login(self.request, user)
#         return result

class StudentEnrollCourseView(LoginRequiredMixin, FormView):
    course = None
    form_class = CourseEnrollForm

    def form_valid(self, form):
        self.course = form.cleaned_data['course']
        self.course.students.add(self.request.user)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('student_course_detail', args=[self.course.slug])


class StudentCourseListView(LoginRequiredMixin, ListView):
    model = Course
    template_name = 'students/course/list.html'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(students__in=[self.request.user])


class StudentCourseDetailView(LoginRequiredMixin, DetailView):
    model = Course
    template_name = 'students/course/detail.html'
    
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(students__in=[self.request.user])                      
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        course = self.get_object()
        context['module_instances'] = Module.objects.filter(course=course)[0]
        # print( self.kwargs)
        if 'module_id' in self.kwargs:
            #get current module
            context['module'] = course.modules.get(id=self.kwargs['module_id'])
            
            mod_id = course.modules.get(id=self.kwargs['module_id'])
            prev_id = course.modules.filter(id__lt=mod_id.id).last()
            next_id = course.modules.filter(id__gt=mod_id.id).first()
            context['next_'] = next_id
            context['prev_'] = prev_id
        else:
            #get first module
           context['module'] = course.modules.all()[0]
    
        slug = self.kwargs['slug']
        context['slug'] = slug
        # context['quiz_list'] = Quiz.objects.all()
        return context
        


# qs = course.modules.get()
        # if qs.exists():
        #     context['module_id'] =  qs[0]
        # course.modules.filter()[:1].get()
        # course.modules.latest('id')
        # course.modules.get(pk=9)
    
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message+" - "+from_email,from_email, [DEFAULT_FROM_EMAIL] )
            except BadHeaderError:
                messages.warning(request, 'Invalid Header discovered')
                return redirect('course_list')
            messages.success(request, 'Thank you for your submission. We aim to respon within 3 working days')
            return redirect('course_list')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})