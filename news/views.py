from django.shortcuts import render
from django.utils import timezone
from django.urls import reverse_lazy
from datetime import datetime
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
# импортируем необходимые дженерики
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# импортируем класс, говорящий о том, что в этом представлении будем выводить список объектов из БД

#from django.core.paginator import Paginator
from django_filters.views import FilterView
from .models import Post
# импортируем недавно написанный фильтр
from .filters import PostFilter
# импортируем нашу форму
from .forms import PostForm

# Create your views here.
class PostsList(ListView):
# указываем модель, объекты которой мы будем выводить
    model = Post
# указываем имя шаблона, в котором будет лежать HTML,
# в нём будут все инструкции о том, как именно пользователю должны вывестись наши объекты
    template_name = 'news/newslist.html'
# далее имя списка (по заданию нужно 'news'), в котором будут лежать все объекты,
# его надо указать, чтобы обратиться к самому списку объектов через HTML-шаблон
    context_object_name = 'news'
# сортировка по id в порядке убывания
#    queryset = Post.objects.all().order_by('-id')
# вывод объектов в обратном порядке, начиная с последнего созданного объекта
#    queryset = Post.objects.all().order_by('-postCreated')
# или можно так - вывод объектов в обратном порядке, начиная с последнего созданного объекта
    ordering = ['-postCreated']
#    paginate_by = 2 # поставим постраничный вывод в 2 элемента
    paginate_by = 10 # поставим постраничный вывод в 10 элементов
#    filterset_class = PostFilter

# метод get_context_data нужен нам для того, чтобы передать переменные в шаблон.
# В возвращаемом словаре context будут храниться все переменные.
# Ключи этого словаря и есть переменные, к которым можно потом обратиться через шаблон.
    def get_context_data(self, **kwargs):  # забираем отфильтрованные объекты переопределяя метод get_context_data у наследуемого класса (полиморфизм)
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())  # вписываем наш фильтр в контекст
        #context['choices'] = Post.POST_TYPE
        #context['form'] = PostForm()
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST) # создаём новую форму, забиваем в неё данные из POST-запроса
        if form.is_valid(): # если пользователь ввёл всё правильно и нигде не накосячил, то сохраняем новый пост
            form.save()
        return super().get(request, *args, **kwargs)

# дженерик для получения деталей об объекте (посте)
# создаём представление, в котором будут детали конкретного отдельного поста
class PostDetailView(DetailView):
# модель всё та же, но мы хотим получать детали конкретно отдельного поста
    template_name = 'news/post_detail.html' # вместо шаблона post.html, сделаем post_detail.html
    queryset = Post.objects.all()

# дженерик для создания объекта.
# Надо указать только имя шаблона и класс формы. Остальное он сделает за нас
class PostCreateView(PermissionRequiredMixin, CreateView):
    permission_required = ('news.add_post', 'news.change_post')
    template_name = 'news/post_create.html'
    form_class = PostForm

# дженерик для редактирования объекта
class PostUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
   permission_required = ('news.change_post')
   template_name = 'news/post_create.html'
   form_class = PostForm

   # метод get_object используем вместо queryset, чтобы получить информацию об объекте, который собираемся редактировать
   def get_object(self, **kwargs):
       id = self.kwargs.get('pk')
       return Post.objects.get(pk=id)

# дженерик для удаления объекта
class PostDeleteView(PermissionRequiredMixin, DeleteView):
   permission_required = ('news.delete_post')
   template_name = 'news/post_delete.html'
   queryset = Post.objects.all()
   success_url = reverse_lazy('news:newslist') # не забываем импортировать функцию reverse_lazy из пакета django.urls

class PostSearchView(FilterView):
    model = Post
    context_object_name = 'posts'
    template_name = 'news/post_search.html'
    queryset = Post.objects.all().order_by('-postCreated')
    filterset_class = PostFilter
