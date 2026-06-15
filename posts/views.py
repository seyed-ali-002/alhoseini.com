from django.shortcuts import render
from django.views.generic import ListView, DetailView

from posts.models import Post


# Create your views here.

class PostListView(ListView):
    template_name = 'posts.html'
    model = Post
    context_object_name = 'posts'

    queryset = Post.objects.filter(published=True).order_by('-published_date')

    paginate_by = 12


class PostDetailView(DetailView):
    template_name = 'post-detail.html'
    model = Post
    context_object_name = 'post'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)

        session_key = f'viewed_post_{obj.pk}'

        if not self.request.session.get(session_key, False):
            obj.views += 1
            obj.save()

            self.request.session[session_key] = True

        return obj
