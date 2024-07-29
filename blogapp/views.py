from django.shortcuts import render, redirect
from django.views import View
from .models import Article
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class Index(ListView):
    model = Article
    queryset = Article.objects.all().order_by('-date')
    template_name = 'blogapp/index.html'

class Featured(ListView):
    model = Article
    queryset = Article.objects.filter(featured=True).order_by('-date')
    template_name = 'blogapp/featured.html'


class UpdateArticleView(LoginRequiredMixin, UpdateView):
    model = Article
    template_name = 'blogapp/blog_update.html'
    fields = ['title', 'content', 'featured']

    def get_success_url(self):
        return reverse_lazy('detail_article', kwargs={'pk': self.object.pk})
    
class DetailArticleView(DetailView):
    model = Article
    template_name = 'blogapp/blog_post.html'

    def get_context_data(self, *args, **kwargs):
        context = super(DetailArticleView, self).get_context_data(*args, **kwargs)
        context['liked_by_user'] = False
        article = Article.objects.get(id=self.kwargs.get('pk'))
        if article.likes.filter(pk=self.request.user.id).exists():
            context['liked_by_user'] = True
        return context
    
class LikeArticle(View):
    def post(self, request, pk):
        article = Article.objects.get(id=pk)

        if article.likes.filter(pk=self.request.user.id).exists():
            article.likes.remove(self.request.user.id)
        else:
            article.likes.add(self.request.user.id)

        article.save()
        return redirect('detail_article', pk)

class DeleteArticleView(DeleteView):
    model = Article
    template_name = 'blogapp/blog_delete.html'
    success_url = reverse_lazy('index')

class CreateArticleView(LoginRequiredMixin, CreateView):
    model = Article
    template_name = 'blogapp/blog_create.html'
    fields = ['title', 'content', 'featured']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('index') 
