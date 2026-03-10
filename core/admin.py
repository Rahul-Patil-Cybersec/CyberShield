from django.contrib import admin
from .models import AwarenessTopic

admin.site.register(AwarenessTopic)
from .models import ToolUsage

admin.site.register(ToolUsage)

from .models import QuizTopic, Question, QuizResult

admin.site.register(QuizTopic)
admin.site.register(Question)
admin.site.register(QuizResult)
