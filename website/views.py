from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from .models import *




# Create your views here.
def home(request):
    print(request.GET)
    print(request.POST)
    studenti = request.session.get('email')
    try:
        user_type = student.objects.all().filter(email=request.session.get('email'))[0].user_type
        print(user_type)
        context = {
            'std' : studenti,
            'user_type': user_type
        }
    except:
        context = {
            'std' : studenti,
        }

    return render(request, 'index.html', context)

def courses_view(request):
    studenti = request.session.get('email')

    try:
        user_type = student.objects.all().filter(email=request.session.get('email'))[0].user_type
        print(user_type)
        context = {
            'std' : studenti,
            'user_type': user_type
        }
    except:
        context = {
            'std' : studenti,
        }

    return render(request, 'courses.html', context)

def about(request):
    studenti = request.session.get('email')
    try:
        user_type = student.objects.all().filter(email=request.session.get('email'))[0].user_type
        print(user_type)
        context = {
            'std' : studenti,
            'user_type': user_type
        }
    except:
        context = {
            'std' : studenti,
        }

    return render(request, 'about.html', context)

def sign_up(request):
    if(request.method) == "POST":
        req = request.POST
        print(req['name'], req['lastname'], req['email'], req['password'], req['birthday'], req['gender'])
        items = student.objects.all().filter(email=request.POST['email'])
        if len(items)>0:
            context = {
                "error":"Email already used!"
            }
            return render(request, 'singup.html', context)
        student_instance = student.objects.create(name=req['name'], lastname=req['lastname'], email=req['email'], password=req['password'], birthday=req['birthday'], gender=req['gender'], )
        student_instance.save()
        print("ok")
        return redirect(login)
    return render(request, 'singup.html', {})

def login(request):
    if(request.method) == "POST":
        items = student.objects.all().filter(email=request.POST['email'], password=request.POST['password'])
        print(items)
        if len(items)>0:
            request.session['email'] = request.POST['email']
            request.session['name'] = items[0].name
            return redirect(show_students)
        else:
            context = {
                "error":"Email or password incorrect!"
            }
            return render(request, 'login.html', context)
    else:
        return render(request, 'login.html', {})



# @user_passes_test(check_admin)

def show_students(request):
    studenti = request.session.get('email')
    name = request.session.get('name')
    if studenti == None:
        return redirect(login)
    if student.objects.all().filter(email=request.session.get('email'))[0].user_type == "superuser":
        print("admin")
        students = student.objects.all()
        prenotimet = prenotime.objects.all()
        try:
            user_type = student.objects.all().filter(email=request.session.get('email'))[0].user_type
            print(user_type)
            context = {
                'std': name,
                'user_type': user_type,
                'students' : students,
                'prenotime' : prenotimet,
                'header': "All Students",
            }
        except:
            context = {
                'std' : name,
                'students' : students,
                'prenotime' : prenotimet,
                'header': "All Students",
            }

        return render(request, 'all_students_courses.html', context)
    else:
        print(request.session.get("email"))
        prenotimet = prenotime.objects.all().filter(student=request.session.get("email"))
        print(prenotimet)

        try:
            user_type = student.objects.all().filter(email=request.session.get('email'))[0].user_type
            print(user_type)
            context = {
                'std': name,
                'prenotime' : prenotimet,
                'user_type': user_type
            }
        except:
            context = {
                'std': name,
                'prenotime' : prenotimet,
            }

        return render(request, 'my_courses.html', context)

def logout(request):
    request.session['email'] = None
    request.session['name'] = None
    return redirect(login)

def apply(request, kursi):
    if request.session.get('email') == None:
        return redirect(login)

    if request.method == "POST":
        ora = request.POST.get("hour_checked")
        dita = ",".join(request.POST.getlist("day_checked"))

        kursi = request.POST.get("kursi")
        cmimi = request.POST.get("cmimi")

        kursi_blere = prenotime.objects.create(
            course_name=kursi, price=cmimi, dita=dita, ora=ora, student=request.session.get('email'),
        )

        kursi_blere.save()
        return redirect(show_students)
    else:
        studenti = request.session.get('email')
        print(studenti)
        name = request.session.get('name')
        print(kursi)
        try:
            user_type = student.objects.all().filter(email=request.session.get('email'))[0].user_type
            print(user_type)
            context = {
                'std': studenti,
                'user_type': user_type,
                'kursi' : kursi,
                'cmimi': courses.objects.filter(course_name=kursi)[0].price
            }
        except:
            context = {
                'std' : name,
                'kursi' : kursi,
                'cmimi': courses.objects.filter(course_name=kursi)[0].price
    ,
            }
        return render(request, 'apply.html', context)
