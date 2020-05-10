from django.urls import path
from django.conf.urls import url, include
from . import views
from django.views.generic import TemplateView


urlpatterns = [
    path('', views.home, name='home'),
    # path('search', views.search, name='search'),
    path('sheet/<pk>',views.ReadScore.as_view(), name='read'),
    path('contact/', views.contact, name='contact'),
    path('add_score/', views.add_score, name='add_score'),
    path('edit_score/<int:id>',views.edit_score, name='edit_score'),
    path('edit/<int:id>',views.EditScore.as_view(), name='edit_score'),
    path('scores_list', views.ListScores.as_view(), name="scores_list"),
    path('scores_list_by_cat/<category>', views.ListScores_by_cat.as_view(), name="scores_list_by_cat"),
    path('scores_list_by_compositor/<compositor>', views.ListScores_by_compositor.as_view(),
         name="scores_list_by_compositor"),
    # url(r'', TemplateView.as_view(template_name='search/welcome.html')),

]