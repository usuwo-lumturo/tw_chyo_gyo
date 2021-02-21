from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.MonthWithScheduleCalendar.as_view(), name='month_with_schedule'),
    path(
        'month_with_schedule/',
        views.MonthWithScheduleCalendar.as_view(), name='month_with_schedule'
    ),
    path(
        'month_with_schedule/<int:year>/<int:month>/',
        views.MonthWithScheduleCalendar.as_view(), name='month_with_schedule'
    ),
    path(
        'add_money/',
        views.add_money.as_view(), name='add_money'
    ),
    path('mycalendar/', views.MyCalendar.as_view(), name='mycalendar'),
    path(
        'mycalendar/<int:year>/<int:month>/<int:day>/', views.MyCalendar.as_view(), name='mycalendar'
    ),
]
