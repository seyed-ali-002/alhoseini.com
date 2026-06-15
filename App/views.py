from django.shortcuts import render
from django.views.generic import TemplateView

from posts.models import Post


# Create your views here.

class Index(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        context['posts'] = Post.objects.all().order_by('-views', 'published_date')[:6]
        context['latest_posts'] = context['posts'][:3]

        return context


def breadcrumbs_partial_view(request):
    # request.path
    return render(request, 'breadcrumbs.html')
