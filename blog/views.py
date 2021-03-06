from django.views.generic import ListView
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.core.mail import send_mail
from .models import Post
from .forms import EmailPostForm

# class PostListView(ListView):
#     model = Post
#     # queryset = Post.objects.all()
#     context_object_name = 'posts'
#     paginate_by = 3
#     template_name = 'blog/post/list.html'


def post_list(request):
    # posts = Post.objects.all()
    object_list = Post.objects.all()
    paginator = Paginator(object_list, 2)  # по три статьи на странице
    page = request.GET.get('page')  # получаем номер страници из request.GET
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # если страница не является целым числом, то переходим на первую страницу
        posts = paginator.page(1)
    except EmptyPage:
        # если номер страници больше, чем общее количество, то выбираем последнюю
        posts = paginator.page(paginator.num_pages)

    context = {'posts': posts, 'page': page}
    return render(request, 'blog/post/list.html', context)


def post_detail(request, year, month, day, post): # по этим параметрам будет найден пост в базе данных
    post = get_object_or_404(Post, slug=post,
                             status='published',
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)
    context = {'post': post}
    return render(request, 'blog/post/detail.html', context)

def post_share(request, post_id):
    post = get_object_or_404(Post, id=post_id, status='published')
    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data()

    else:
        form = EmailPostForm()
    context = {'post': post, 'form': form}
    return render(request, 'blog/post/share.html', context)


