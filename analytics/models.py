
import datetime
from allauth.account.signals import user_logged_in, user_logged_out
from django.db import models
from django.conf import settings
# from django.contrib.sessions.models import Session
# from django.contrib.contenttypes.fields import GenericForeignKey
# from django.contrib.contenttypes.models import ContentType
from django.utils import timezone
# from django.db.models.signals import post_save

# from .signals import object_viewed_signal
from .utils import get_client_ip

User = settings.AUTH_USER_MODEL

# class ObjectViewed(models.Model):
#     user            = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
#     content_type    = models.ForeignKey(ContentType, on_delete=models.SET_NULL, null=True)
#     object_id       = models.PositiveIntegerField()
#     ip_address      = models.CharField(max_length=120, blank=True, null=True)
#     content_object  = GenericForeignKey('content_type', 'object_id')
#     timestamp       = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
        
#         return f"{self.user},Viewed {self.content_object}, {self.timestamp}"

#     class Meta:
#         ordering = ['-timestamp']
#         verbose_name = 'Object Viewed'
#         verbose_name_plural = 'Objects Viewed'


# def object_viewed_receiver(sender, instance, request, *args, **kwargs):
#     # print(sender, request, instance, *args, **kwargs)
#     c_type = ContentType.objects.get_for_model(sender) #same as instance.__class__
#     new_view_obj = ObjectViewed.objects.create(
#         user=request.user,
#         object_id = instance.id,
#         content_type = c_type,
#         ip_address = get_client_ip(request)
#     )

# object_viewed_signal.connect(object_viewed_receiver)


class UserSession(models.Model):
    user        = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    ip_address  = models.CharField(max_length=225)
    session_key = models.CharField(max_length=225)
    timestamp   = models.DateTimeField(auto_now_add=False)
    loggedout   = models.DateTimeField(auto_now_add=False, blank=True, null=True)
    active      = models.BooleanField(default=True)
    ended       = models.BooleanField(default=False)
    total       = models.CharField(max_length=225, blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.user}"

    # def save(self, *args, **kwargs):
    #     if self.ended:
    #        self.total= self.loggedout - self.timestamp
    #        res= self.total.total_seconds() / 3600 #returns hours
    #        res= f"{res:.2f}"
    #        return super().save(*args, **kwargs)
    @property
    def total(self):
        # get_one_hour = datetime.timedelta(days=1).total_seconds() / 24 # returns 1 hours in seconds
        if self.ended:
           td= self.loggedout - self.timestamp
           res= td.total_seconds() / 3600 #returns hours
    #    print(type(res)) # float
           return f"{res:.2f}"
    
    # def update_total(self):
    #     if float(self.total) != None:
    #         print(self.total,type(self.total))
    #         for instance in self.total:
    #             return instance
                # print(type(instance))
                # print((self.total))
            

def user_login_receiver(request, user, *args, **kwargs):
    user = user
    ip_address = get_client_ip(request)
    session_key = request.session.session_key
    timestamp=timezone.now()
    UserSession.objects.create(user=user,ip_address=ip_address,session_key=session_key,timestamp=timestamp)
    
user_logged_in.connect(user_login_receiver)

def user_logout_receiver(request, user, *args, **kwargs):
    user = user
    ended = True
    loggedout=timezone.now()
    
    UserSession.objects.filter(ended=False).update(user=user,ended=ended,loggedout=loggedout)
user_logged_out.connect(user_logout_receiver)





# @property
    # def total(self):
    #     num_secs_in_minute = 60
    #     if self.ended:
    #        td= self.loggedout - self.timestamp
    #        res= td.total_seconds() / num_secs_in_minute #returns minutes
    #        return f"{res:.2f}"

    # def update_total(self):
    #     arr = []
    #     arr.append(self.total)











# def get_total_login_time():
#     qs = UserSession.objects.filter(ended=True)
#     time_length = []
#     for i in qs:
#         start = i.timestamp
#         finish = i.loggedout
#         total = finish - start
#         time_length.append(total)
#         print(total)
#     print(str(time_length))
    
        

# def list_time():
#     qs = UserSession.objects.filter(ended=True)
#     total = [i.loggedout - i.timestamp for i in qs]
#     return total

    # [datetime.timedelta(seconds=459, microseconds=877444), datetime.timedelta(seconds=215, microseconds=42383), datetime.timedelta(seconds=129, microseconds=685476), datetime.timedelta(seconds=9097, microseconds=806348)]

# def list_times():
#     qs = UserSession.objects.filter(ended=True)
#     time_differnce = [i.loggedout - i.timestamp for i in qs]
#     times_as_list_of_strings = [str(delta) for delta in time_differnce]
    

    


# def get_time():
#     qs = UserSession.objects.filter(ended=True)
#     for i in qs:
#         start = i.timestamp
#         finish = i.loggedout
#         total = finish - start
#         print(total)
        
        # 0:07:39.877444
        # 0:03:35.042383
        # 0:02:09.685476
        # 2:31:37.806348

