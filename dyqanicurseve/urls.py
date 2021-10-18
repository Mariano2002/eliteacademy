"""dyqanicurseve URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from website.views import *

urlpatterns = [
    path('admin/', admin.site.urls),

    path('home', home, name="home"),

    path('', home, name="home"),

    path('courses', courses_view, name="Courses"),

    path('about', about, name="About"),

    path('signup', sign_up, name="Sign Up"),

    path('login', login, name="Log In"),

    path('show_students', show_students, name="show_students"),

    path('logout', logout, name="logout"),

    path('all_students_courses', show_students, name="all_students_courses"),

    path('my_courses', show_students, name="my_courses"),

    path('apply/<path:kursi>', apply, name="apply"),



    # url(r'^addStudent$', addStudent, name='addStudent'),
]
