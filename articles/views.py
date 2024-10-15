from django.urls import reverse_lazy
from .models import Article
from django.views.generic import ListView, DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

class ArticleListView(ListView):
    model = Article
    template_name = 'articles/article_list.html'

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'articles/article_detail.html'

class ArticleUpdateView(UpdateView):
    model = Article
    fields = ( "title", "body", )
    template_name = 'articles/article_update.html'

class ArticleDeleteView(DeleteView):
    model = Article
    template_name = 'articles/article_delete.html'
    success_url = reverse_lazy("article_list")

class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    template_name = "articles/article_new.html"
    fields = ( "title", 
              "body",  
              )
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)