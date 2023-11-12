
from django.core.management.base import BaseCommand
from quiz.models import Result
from django.contrib.auth.models import User
import datetime

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        today = datetime.date.today()
        results = Result.objects.all()
        for result in results:
            if result.expired <= today:
                print(f"Dear {result.user}, please retake {result.quiz} as it expired on {result.expired}")
                # result.delete()

            
        
            # obj_dup =  Result.objects.filter(quiz_id=result.quiz_id)
            
            # if obj_dup.count() > 1:
            #     print(obj_dup)
