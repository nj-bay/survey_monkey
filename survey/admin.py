from django.contrib import admin
from survey.models import Survey, Question
# Register your models here.


class QuestionInLineAdmin(admin.TabularInline):
    model = Question
    extra = 2


class SurveyAdmin(admin.ModelAdmin):
    list_display = ("id",)
    inlines = [QuestionInLineAdmin]






admin.site.register(Survey,SurveyAdmin)
admin.site.register(Question)

# Register your models here.
