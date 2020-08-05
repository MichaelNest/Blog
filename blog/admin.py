from django.contrib import admin
from .models import Post

# admin.site.register(Post)
@admin.register(Post) # декоратор для регистрации модели Post
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    list_filter = ('status', 'created', 'publish', 'author') # блок справа
    search_fields = ('title', 'body') # строка поиска
    prepopulated_fields = {'slug': ('title',)} # при создании статьи в админ-панели - slug генерируется автоматически на основе title
    raw_id_fields = ('author',) # поле поиска для среди авторов
    date_hierarchy = 'publish' # ссылки для навигации по датам под строкой поиска
    ordering = ('status', 'publish') # сортировка статей по статусу и дате публикации по умолчанию