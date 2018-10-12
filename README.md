About this project
==================
Sample [Django 2.1]( https://docs.djangoproject.com/en/2.1/) project that shows how to define a custom `View` when using the [django-cruds-adminlte](https://django-cruds-adminlte.readthedocs.io) package.


Model
-----
The model for this app consist in Department, KnowledgeBase and Question.

A KnowledgeBase belongs to a Department and may contain many related Questions.


Custom view
-----------
The custom view defined in this project is the `Detail` view for the `KnowledgeBase` entity. In addition to showing the default fields for a KnowledgeBase object, in the custom view we are going to show a table with the Questions related to the KnowledgeBase as well.

The Questions table is built using the [django-datatable](https://pypi.org/project/django-datatable/) package.

App
===

Structure
---------
Unlike usual Django projects, this one follows a single-app structure, explained here: https://zindilis.com/blog/2017/01/06/django-anatomy-for-single-app.html


Installation
------------
```
pip install -r requirements.txt
```

Run
---
```
python manage.py migrate
python manage.py runserver
```

Navigate to http://localhost:8000/cruds/knowledgebase/list and you will see the list of KnowledgeBase objects stored in the database. This view is the default list view provided by `django-cruds-adminlte`.

When you click in the `Show` button next to a listed Knowledge Base, you will see a `Detail` view for the selected KnowledgeBase object. This is the custom `Detail` view created in this project.


Custom View Technical details
=============================

View class
----------
The custom detail view will add a table for showing the Questions related to the KnowledgeBase being shown.

```python
from cruds.models import KnowledgeBase
from cruds.tables import QuestionTable
from cruds_adminlte.crud import CRUDView


class KnowledgeBaseView(CRUDView):
    model = KnowledgeBase
    check_login = False
    check_perms = False
    def get_detail_view(self):
        View = super(KnowledgeBaseView, self).get_detail_view()
        class KnowledgeBaseDetailView(View):
            def question_table(self):
                knowledge_base = self.object
                # QuestionTable is implemented using `django-datatable`
                return QuestionTable(knowledge_base.question_set.all())
            def get_context_data(self, **kwargs):
                context = super(KnowledgeBaseDetailView, self).get_context_data()
                # 'question_table' is the name used in the template for including the Questions table
                context['question_table'] = self.question_table()
                return context
        return KnowledgeBaseDetailView
```

More about custom view classes at: https://django-cruds-adminlte.readthedocs.io/en/latest/usage.html#overwrite-views

Template
--------

### Location
The custom template must have a specific name and must be located at a specific directory too: `cruds/templates/cruds/detail.html`

More about location of custom templates at: https://django-cruds-adminlte.readthedocs.io/en/latest/usage.html#overwrite-templates


### Table tag
The custom [detail.html](./cruds/templates/knowledgebase/cruds/detail.html) template is a copy of the default, adding the `django-datatable` tag `render_table`:

```
{% extends 'cruds/base.html' %}
{% load i18n %}
{% load crud_tags %}
{% load table_tags %}

{% block content %}
  # Omitted KnowledgeBase fields...
  {% render_table question_table %}
```

`question_table` is the name of the context field set in `KnowledgeBaseDetailView`


URL
---
The KnowledgeBase detail view must be redefined in `urls.py`:

```python
from django.conf.urls import url, include
from django.contrib import admin
from cruds_adminlte.urls import crud_for_app
from cruds.views import KnowledgeBaseView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # Override default detail view for KnowledgeBase with the custom one.
    # Note that the override must be defined before all default CRUD URLs definition below.
    url('', include(KnowledgeBaseView().get_urls()))
]

# Default CRUD URLs definition
urlpatterns += crud_for_app('cruds', login_required=False, check_perms=False)
```
