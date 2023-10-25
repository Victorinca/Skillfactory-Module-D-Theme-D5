# импорт скрипта models из модуля django.db
from django.db import models
from datetime import datetime
# импорт скрипта пользователя
from django.contrib.auth.models import User
# импорт функции Sum,
# предоставляющей возможность выполнять агрегацию суммы значений поля в запросах к базе данных
from django.db.models import Sum
# для удаления всех HTML-тегов из строки
from django.utils.html import strip_tags
# для обратного поиска URL-адреса на основе имени шаблона URL или объекта представления,
# когда нужно сгенерировать URL-адрес в коде, а не в шаблоне.
from django.urls import reverse


# Create your models here.
# наследуемся от класса Model, определяющего основные функции работы с моделью
class Author(models.Model):
    authorUser = models.OneToOneField(User, on_delete=models.CASCADE)
    authorRating = models.SmallIntegerField(default=0)

    def __str__(self):
            return self.authorUser.username

# Метод update_rating() модели Author, который обновляет рейтинг пользователя, переданный в аргумент этого метода.
    def update_rating(self):
# 1) суммарный рейтинг каждой статьи postRating автора postAuthor умножается на 3
        sumPR = self.post_set.all().aggregate(sumPostRating=Sum('postRating'))
        # с помощью post_set.all() - получим все связанные с автором посты в модели Post,
        # и с помощью aggregate получаем все значения поля рейтинг и суммируем их
        # далее создадим промежуточную переменную
        pRate = 0
        pRate += sumPR.get('sumPostRating')
# 2) суммарный рейтинг всех комментариев commentRating автора authorUser
        sumAuthorCR = self.authorUser.comment_set.all().aggregate(sumAuthorComRating=Sum('commentRating'))
        authorCRate = 0
        authorCRate += sumAuthorCR.get('sumAuthorComRating')
# 3) суммарный рейтинг всех комментариев commentRating к статьям автора postAuthor
        sumPostCR = Comment.objects.filter(commentForPost__postAuthor=self).values('commentRating').aggregate(sumPostComRating=Sum('commentRating'))
        postCRate = 0
        postCRate += sumPostCR.get('sumPostComRating')

# print('pRate =', pRate * 3, 'authorCRate =', authorCRate, 'postCRate =', postCRate)
        self.authorRating = pRate * 3 + authorCRate + postCRate
        self.save()


class Category(models.Model):
    categoryName = models.CharField(max_length=64, unique=True)

    def __str__(self):
            return self.categoryName

class Post(models.Model):
    article = 'A'
    news = 'N'

    POST_TYPE = [
        (article, "Статья"),
        (news, "Новость")
    ]

    postAuthor = models.ForeignKey(Author, on_delete=models.CASCADE)
    post_type = models.CharField(max_length=1, choices=POST_TYPE, default=article)
    postCreated = models.DateTimeField(auto_now_add=True)
    postCats = models.ManyToManyField(Category, through='PostCategory')
    postTitle = models.CharField(max_length=128)
    postText = models.TextField()
    postRating = models.SmallIntegerField(default=0)

    def __str__(self):
        return f'Пост #{self.pk} - Заголовок: {self.postTitle}'

    def get_absolute_url(self):
        # добавим абсолютный путь, чтобы после создания нас перебрасывало на страницу с постом
        # return f'/news/{self.id}'
        # Функция reverse() принимает имя шаблона или объект представления в качестве аргумента
        # и возвращает соответствующий URL-адрес.
        # Если URL-шаблон принимает аргументы, можно передать их в reverse() в виде списка args или словаря kwargs.
        return reverse('news:post_detail', args=[str(self.id)])

# Рейтинг для postRating:
    def like(self):
        self.postRating += 1
        self.save()

    def dislike(self):
        self.postRating -= 1
        self.save()

# Метод preview() модели Post, который возвращает
# начало статьи (предварительный просмотр) длиной 124 символа и добавляет многоточие в конце.
# вариант 1
#    def preview(self):
#        preview_length = 124
#        return self.postText[:preview_length] + '...' if len(self.postText) > preview_length else self.postText
# вариант 2
#    def preview(self):
#        return f"{self.postText[:124]}..."

# Модифицированный вариант 2 с функцией strip_tags из модуля django.utils.html.
# Применяем функцию strip_tags к self.postText, чтобы удалить все HTML-теги из текста
    def preview(self):
            text_without_tags = strip_tags(self.postText)[:124]
            return f"{text_without_tags}..."

class PostCategory(models.Model):
    fromPost = models.ForeignKey(Post, on_delete=models.CASCADE)
    fromCategory = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    commentForPost = models.ForeignKey(Post, on_delete=models.CASCADE)
    commentUser = models.ForeignKey(User, on_delete=models.CASCADE)
    commentText = models.TextField()
    commentCreated = models.DateTimeField(auto_now_add=True)
    commentRating = models.SmallIntegerField(default=0)

# Рейтинг для commentRating:
    def like(self):
        self.commentRating += 1
        self.save()

    def dislike(self):
        self.commentRating -= 1
        self.save()

# КАК МОЖНО ДОБРАТЬСЯ ЧЕРЕЗ ДЛИННЫЕ СВЯЗИ (НЕСКОЛЬКО СВЯЗЕЙ) ДО КАКОГО-ЛИБО ПОЛЯ.
# Обращаемся в определенной модели к её связанному полю, которое связано с другой моделью,
# у которой есть связанное поле с другой моделью, и так получаем нужное поле.
    def __str__(self):
        try:
            return self.commentForPost.postAuthor.authorUser.username
        except:
            return self.commentUser.username
