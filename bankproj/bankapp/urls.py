# banking_app/urls.py
from django.urls import path
from .views import home, user_logout, new_page, form_page, get_branches

urlpatterns = [
    path('', home, name='home'),

    path('new_page/', new_page, name='new_page'),
    path('form_page/', form_page, name='form_page'),
    path('logout/', user_logout, name='logout'),
    path('form_page/<slug:district_slug>/', form_page, name='form_page_with_district'),
    path('get_branches/', get_branches, name='get_branches'),

]



