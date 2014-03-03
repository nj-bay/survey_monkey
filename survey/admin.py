from django.contrib import admin
from survey.models import Survey, Question
# Register your models here.



# class BlogPostAdmin(admin.ModelAdmin):
#     readonly_fields = ("author",)
#
#     def save_model(self, request, obj, form, change):
#         obj.author = request.user
#         obj.save()

# class CommentInlineAdmin(admin.TabularInline):
#     model = Comment
#     extra = 1




class SurveyAdmin(admin.ModelAdmin):
    list_display = ("id", "posted", "title", "author")
    search_fields = ("title", "author__username")
    # inlines = [CommentInlineAdmin]
    readonly_fields = ("author",)
    # filter_horizontal = ("tag",)

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()



admin.site.register(Survey,SurveyAdmin)
admin.site.register(Question)

# Register your models here.
