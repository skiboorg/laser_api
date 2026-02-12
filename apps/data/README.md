# Data App - Услуги и Оборудование

## Структура приложения

```
apps/data/
├── models/
│   ├── __init__.py
│   ├── industry.py          # Отрасли применения
│   ├── project.py           # Реализованные проекты
│   ├── review.py            # Отзывы клиентов
│   ├── service.py           # Услуги + связанные модели
│   └── equipment.py         # Оборудование + связанные модели
├── serializers/
│   ├── __init__.py
│   ├── industry.py
│   ├── project.py
│   ├── review.py
│   ├── service.py           # ServiceListSerializer, ServiceDetailSerializer
│   └── equipment.py         # EquipmentListSerializer, EquipmentDetailSerializer
├── views/
│   ├── __init__.py
│   ├── industry.py          # IndustryViewSet
│   ├── project.py           # ProjectViewSet
│   ├── review.py            # ReviewViewSet
│   ├── service.py           # ServiceViewSet (с prefetch_related)
│   └── equipment.py         # EquipmentViewSet (с prefetch_related)
├── admin/
│   ├── __init__.py
│   ├── industry.py          # IndustryAdmin
│   ├── project.py           # ProjectAdmin
│   ├── review.py            # ReviewAdmin
│   ├── service.py           # ServiceAdmin + Inline для преимуществ и тех.характеристик
│   └── equipment.py         # EquipmentAdmin + Inline для преимуществ, тех.характеристик, фото
├── apps.py
├── urls.py
└── __init__.py
```

## Установка

### 1. Скопируйте папку в проект

```bash
cp -r data_app_structure /path/to/your/project/apps/data
```

### 2. Добавьте в INSTALLED_APPS

В `core/settings.py`:

```python
INSTALLED_APPS = [
    # ...
    'django_ckeditor_5',  # Не забудьте добавить!
    
    # Local apps
    'apps.data',
    # ...
]
```

### 3. Настройте CKEditor5

В `core/settings.py`:

```python
CKEDITOR_5_CONFIGS = {
    'default': {
        'toolbar': [
            'heading', '|',
            'bold', 'italic', 'link', 'bulletedList', 'numberedList', 'blockQuote', '|',
            'insertTable', 'tableColumn', 'tableRow', 'mergeTableCells', '|',
            'undo', 'redo'
        ],
    },
}
```

### 4. Добавьте URLs

В `core/urls.py`:

```python
urlpatterns = [
    # ...
    path('api/data/', include('apps.data.urls')),
    path('ckeditor5/', include('django_ckeditor_5.urls')),
]
```

### 5. Установите зависимости

```bash
pip install django-ckeditor-5
```

### 6. Примените миграции

```bash
./manage.sh makemigrations
./manage.sh migrate
```

## API Endpoints

Все endpoints доступны по адресу `/api/data/`:

- `GET/POST /api/data/industries/` - Список отраслей
- `GET/PUT/PATCH/DELETE /api/data/industries/{uuid}/` - Детали отрасли

- `GET/POST /api/data/services/` - Список услуг (краткий)
- `GET/PUT/PATCH/DELETE /api/data/services/{uuid}/` - Детали услуги (полный)

- `GET/POST /api/data/equipment/` - Список оборудования (краткий)
- `GET/PUT/PATCH/DELETE /api/data/equipment/{uuid}/` - Детали оборудования (полный)

- `GET/POST /api/data/reviews/` - Список отзывов
- `GET/PUT/PATCH/DELETE /api/data/reviews/{uuid}/` - Детали отзыва

- `GET/POST /api/data/projects/` - Список проектов
- `GET/PUT/PATCH/DELETE /api/data/projects/{uuid}/` - Детали проекта

## Модели

### Industry (Отрасли применения)
- name - название
- description - описание

### Review (Отзывы клиентов)
- tags - тэги (строка через запятую)
- photo - фото человека
- full_name - ФИО
- position - подпись к ФИО
- text - текст отзыва (HTML)

### Project (Реализованные проекты)
- title - название
- description - описание (HTML)
- image - изображение

### Service (Услуги)
**Основные поля:**
- title, meta_description
- short_description - для карточки
- icon - иконка SVG для карточки
- video_background, image_background - для страницы
- description_image - фото на описание
- tags - тэги (строка)
- description - описание (HTML)

**Связи:**
- industries (M2M) - отрасли применения
- projects (M2M) - реализованные проекты
- reviews (M2M) - отзывы клиентов
- advantages (FK) - преимущества услуги
- technical_specs (FK) - технические характеристики

### Equipment (Оборудование)
**Основные поля:**
- title, meta_description
- short_description - для главной
- main_image - основное фото (на главной)
- background_image - фото на задний фон
- description - описание (HTML)

**Связи:**
- industries (M2M) - отрасли применения
- reviews (M2M) - отзывы клиентов
- advantages (FK) - преимущества оборудования
- technical_specs (FK) - технические характеристики
- photos (FK) - фотографии оборудования

## Админка

Все модели зарегистрированы в админке с удобным интерфейсом:

- **Service/Equipment** - используют Inline для добавления преимуществ, характеристик и фото прямо на странице редактирования
- **filter_horizontal** для ManyToMany связей (отрасли, проекты, отзывы)
- Поддержка сортировки через поле `order`
- Readonly поля: uuid, created_at, updated_at

## Примеры использования

### Получить список услуг (краткий)
```bash
GET /api/data/services/
```

Вернёт только основные поля для карточек.

### Получить детали услуги
```bash
GET /api/data/services/{uuid}/
```

Вернёт полную информацию включая:
- Все преимущества (отсортированные по order)
- Все технические характеристики
- Связанные отрасли
- Связанные проекты
- Связанные отзывы

### Тэги

Тэги хранятся как строка через запятую и автоматически преобразуются в список через property `tags_list`:

```json
{
  "tags": "автоматизация, промышленность, роботы",
  "tags_list": ["автоматизация", "промышленность", "роботы"]
}
```

## Производительность

ViewSet'ы используют `prefetch_related()` для оптимизации запросов к БД:
- Service - prefetch: advantages, technical_specs, industries, projects, reviews
- Equipment - prefetch: advantages, technical_specs, photos, industries, reviews

## Права доступа

По умолчанию: `IsAuthenticatedOrReadOnly`
- Неавторизованные пользователи могут только читать
- Авторизованные пользователи могут создавать/редактировать/удалять
