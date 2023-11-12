
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
# from django.views.generic.base import TemplateView

# from courses.views import CourseListView
urlpatterns = [
    path('accounts/', include('allauth.urls')),
    # path('', TemplateView.as_view(template_name='home.html')),
    # path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    # path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('admin/', admin.site.urls),
    path('', include('courses.urls')),
    path('api/', include('courses.api.urls', namespace='api')),
    # path('', CourseListView.as_view(), name='course_list'),
    path('students/', include('students.urls')),
    path('quizes/', include('quiz.urls', namespace='quiz')),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)