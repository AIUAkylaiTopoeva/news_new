from django.contrib import admin
from .models import Article, Comment

class CommentInline(admin.StackedInline):#Это Django-класс, который позволяет отображать связанные объекты (в данном случае комментарии) в форме для редактирования родительской модели (в данном случае статьи).
    model = Comment

class ArticleAdmin(admin.ModelAdmin):#это вид инлайновой формы, в которой каждое поле объекта располагается на новой строке. Это удобно, если вам нужно отображать и редактировать большое количество полей. В данном примере все поля модели Comment будут отображаться вертикально для каждой записи комментария.
    inlines = [
        CommentInline,
               ]

admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)