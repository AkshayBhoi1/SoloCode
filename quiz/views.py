from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from xhtml2pdf import pisa
from django.template.loader import get_template

from .models import *


# Create your views here.


def loginpage(request):
    if request.method == "POST":
        Username = request.POST['Username']
        password = request.POST['password']
        # print(Username, password)
        User = authenticate(request, username=Username, password=password)
        # print(User)
        if User is not None:
            login(request, User)
            return redirect('index')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('loginpage')
    else:
        return render(request, 'Login.html')

def signup(request):
    if request.method == "POST":
        name = request.POST['Name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['pass']
        if User.objects.filter(username=username).exists():
            messages.error(request, 'This username is already taken')
            return redirect('signuppage')
        elif User.objects.filter(email=email).exists():
            messages.error(request, "Email is already taken")
            return redirect('signuppage')
        else:
            students = User.objects.create_user(username=username, email=email, password=password)
            students.first_name = name
            students.save()
            messages.success(request, "Registered successfully")
            return redirect('loginpage')
    return render(request, 'signup.html')

def logout_view(request):
    logout(request)
    return redirect('loginpage')

@login_required(login_url='loginpage')
def cpp(request):
    if request.method == 'POST':
        id = request.user.id
        opt1 = request.POST['q1']
        opt2 = request.POST['q2']
        opt3 = request.POST['q3']
        opt4 = request.POST['q14']
        opt5 = request.POST['q5']
        opt6 = request.POST['q6']
        opt7 = request.POST['q7']
        opt8 = request.POST['q8']
        opt9 = request.POST['q9']
        opt10 = request.POST['q10']
        sub = "Cpp Quiz"
        Quiz.objects.filter(id=11).update(id=11, sub=sub)
        Quiz.objects.filter(id=1).update(id=1, ans=opt1)
        Quiz.objects.filter(id=2).update(id=2, ans=opt2)
        Quiz.objects.filter(id=3).update(id=3, ans=opt3)
        Quiz.objects.filter(id=4).update(id=4, ans=opt4)
        Quiz.objects.filter(id=5).update(id=5, ans=opt5)
        Quiz.objects.filter(id=6).update(id=6, ans=opt6)
        Quiz.objects.filter(id=7).update(id=7, ans=opt7)
        Quiz.objects.filter(id=8).update(id=8, ans=opt8)
        Quiz.objects.filter(id=9).update(id=9, ans=opt9)
        Quiz.objects.filter(id=10).update(id=10, ans=opt10)
        userv = Quiz.objects. all()
        questions = CppQuiz.objects.all()
        access = Cppaccess.objects.all()
        score = 0
        wrong = 0
        correct = 0
        total = 0
        for b in access:
            access = b.number
        for (q, a) in zip(userv, questions):
            total += 1
            uservale = {'opt1': q.ans}
            orignal = {'opt1': a.Corrans}
            if uservale == orignal:
                score += 10
                correct += 1
            else:
                wrong += 1
        percent = score / (total * 10) * 100
        # print(score)
        # print(correct)
        # print(percent)
        print(access)
        if access != 1:
            if percent >= 90:
                a = 1
                print(a)
                students = Cppaccess(id=id, number=a)
                students.save()
            else:
                pass
        else:
            pass


        newval = Cppaccess.objects.filter(id=id)
        for b in newval:
            newaccess = b.number
            print(newaccess)
        context = {
            'a': newaccess,
            'score': score,
            'correct': correct,
            'wrong': wrong,
            'percent': percent,
            'total': total
        }
        print(context)
        return render(request, 'result.html', context)
    else:
        questions = CppQuiz.objects.all()
        context = {
            'questions': questions
        }
        return render(request, 'cppquiz.html', context)

@login_required(login_url='loginpage')
def c(request):
    id = request.user.id
    if request.method == 'POST':
        opt1 = request.POST['q1']
        opt2 = request.POST['q2']
        opt3 = request.POST['q3']
        opt4 = request.POST['q14']
        opt5 = request.POST['q5']
        opt6 = request.POST['q6']
        opt7 = request.POST['q7']
        opt8 = request.POST['q8']
        opt9 = request.POST['q9']
        opt10 = request.POST['q10']
        sub = "C Quiz"
        Quiz.objects.filter(id=11).update(id=11, sub=sub)
        Quiz.objects.filter(id=1).update(id=1, ans=opt1)
        Quiz.objects.filter(id=2).update(id=2, ans=opt2)
        Quiz.objects.filter(id=3).update(id=3, ans=opt3)
        Quiz.objects.filter(id=4).update(id=4, ans=opt4)
        Quiz.objects.filter(id=5).update(id=5, ans=opt5)
        Quiz.objects.filter(id=6).update(id=6, ans=opt6)
        Quiz.objects.filter(id=7).update(id=7, ans=opt7)
        Quiz.objects.filter(id=8).update(id=8, ans=opt8)
        Quiz.objects.filter(id=9).update(id=9, ans=opt9)
        Quiz.objects.filter(id=10).update(id=10, ans=opt10)
        userv = Quiz.objects. all()
        questions = CQuiz.objects.all()
        access = Caccess.objects.all()
        score = 0
        wrong = 0
        correct = 0
        total = 0
        for b in access:
            access = b.number
        for (q, a) in zip(userv, questions):
            total += 1
            uservale = {'opt1': q.ans}
            orignal = {'opt1': a.Corrans}
            if uservale == orignal:
                score += 10
                correct += 1
            else:
                wrong += 1
        percent = score / (total * 10) * 100
        # print(score)
        # print(correct)
        # print(percent)

        if access != 1:
            if percent >= 90:
                a = 1
                print(a)
                students = Cppaccess(id=id, number=a)
                students.save()
            else:
                a = 0
                print(a)
                students = Cppaccess(id=id, number=a)
                students.save()
        else:
            pass

        newval = Cppaccess.objects.filter(id=id)
        for b in newval:
            newaccess = b.number
            print(newaccess)
        context = {
            'a': newaccess,
            'score': score,
            'correct': correct,
            'wrong': wrong,
            'percent': percent,
            'total': total
        }
        print(context)
        return render(request, 'result.html', context)
    else:
        questions = CQuiz.objects.all()
        context = {
            'questions': questions
        }
        return render(request, 'cquiz.html', context)

@login_required(login_url='loginpage')
def python(request):
    id = request.user.id
    if request.method == 'POST':
        opt1 = request.POST['q1']
        opt2 = request.POST['q2']
        opt3 = request.POST['q3']
        opt4 = request.POST['q14']
        opt5 = request.POST['q5']
        opt6 = request.POST['q6']
        opt7 = request.POST['q7']
        opt8 = request.POST['q8']
        opt9 = request.POST['q9']
        opt10 = request.POST['q10']
        sub = "Python Quiz"
        Quiz.objects.filter(id=11).update(id=11, sub=sub)
        Quiz.objects.filter(id=1).update(id=1, ans=opt1)
        Quiz.objects.filter(id=2).update(id=2, ans=opt2)
        Quiz.objects.filter(id=3).update(id=3, ans=opt3)
        Quiz.objects.filter(id=4).update(id=4, ans=opt4)
        Quiz.objects.filter(id=5).update(id=5, ans=opt5)
        Quiz.objects.filter(id=6).update(id=6, ans=opt6)
        Quiz.objects.filter(id=7).update(id=7, ans=opt7)
        Quiz.objects.filter(id=8).update(id=8, ans=opt8)
        Quiz.objects.filter(id=9).update(id=9, ans=opt9)
        Quiz.objects.filter(id=10).update(id=10, ans=opt10)
        userv = Quiz.objects. all()
        questions = PythonQuiz.objects.all()
        access = Pythonaccess.objects.all()
        score = 0
        wrong = 0
        correct = 0
        total = 0
        for b in access:
            access = b.number
        for (q, a) in zip(userv, questions):
            total += 1
            uservale = {'opt1': q.ans}
            orignal = {'opt1': a.Corrans}
            if uservale == orignal:
                score += 10
                correct += 1
            else:
                wrong += 1
        percent = score / (total * 10) * 100
        # print(score)
        # print(correct)
        # print(percent)
        if access != 1:
            if percent >= 90:
                a = 1
                print(a)
                students = Cppaccess(id=id, number=a)
                students.save()
            else:
                a = 0
                print(a)
                students = Cppaccess(id=id, number=a)
                students.save()
        else:
            pass

        newval = Cppaccess.objects.filter(id=id)
        for b in newval:
            newaccess = b.number
            print(newaccess)
        context = {
            'a': newaccess,
            'score': score,
            'correct': correct,
            'wrong': wrong,
            'percent': percent,
            'total': total
        }
        print(context)
        return render(request, 'result.html', context)
    else:
        questions = PythonQuiz.objects.all()
        context = {
            'questions': questions
        }
        return render(request, 'pyquiz.html', context)

@login_required(login_url='loginpage')
def java(request):
    id = request.user.id
    if request.method == 'POST':
        opt1 = request.POST['q1']
        opt2 = request.POST['q2']
        opt3 = request.POST['q3']
        opt4 = request.POST['q14']
        opt5 = request.POST['q5']
        opt6 = request.POST['q6']
        opt7 = request.POST['q7']
        opt8 = request.POST['q8']
        opt9 = request.POST['q9']
        opt10 = request.POST['q10']
        sub = "Java Quiz"
        Quiz.objects.filter(id=11).update(id=11, sub=sub)
        Quiz.objects.filter(id=1).update(id=1, ans=opt1)
        Quiz.objects.filter(id=2).update(id=2, ans=opt2)
        Quiz.objects.filter(id=3).update(id=3, ans=opt3)
        Quiz.objects.filter(id=4).update(id=4, ans=opt4)
        Quiz.objects.filter(id=5).update(id=5, ans=opt5)
        Quiz.objects.filter(id=6).update(id=6, ans=opt6)
        Quiz.objects.filter(id=7).update(id=7, ans=opt7)
        Quiz.objects.filter(id=8).update(id=8, ans=opt8)
        Quiz.objects.filter(id=9).update(id=9, ans=opt9)
        Quiz.objects.filter(id=10).update(id=10, ans=opt10)
        userv = Quiz.objects. all()
        questions = JavaQuiz.objects.all()
        access = Javaacces.objects.all()
        score = 0
        wrong = 0
        correct = 0
        total = 0
        for b in access:
            access = b.number
        for (q, a) in zip(userv, questions):
            total += 1
            uservale = {'opt1': q.ans}
            orignal = {'opt1': a.Corrans}
            if uservale == orignal:
                score += 10
                correct += 1
            else:
                wrong += 1
        percent = score / (total * 10) * 100
        # print(score)
        # print(correct)
        # print(percent)

        if access != 1:
            if percent >= 90:
                a = 1
                print(a)
                students = Cppaccess(id=id, number=a)
                students.save()
            else:
                a = 0
                print(a)
                students = Cppaccess(id=id, number=a)
                students.save()
        else:
            pass

        newval = Cppaccess.objects.filter(id=id)
        for b in newval:
            newaccess = b.number
            print(newaccess)
        context = {
            'a': newaccess,
            'score': score,
            'correct': correct,
            'wrong': wrong,
            'percent': percent,
            'total': total
        }
        print(context)
        return render(request, 'result.html', context)
    else:
        questions = JavaQuiz.objects.all()
        context = {
            'questions': questions
        }
        return render(request, 'javaquiz.html', context)

@login_required(login_url='loginpage')
def js(request):
    id = request.user.id
    if request.method == 'POST':
        opt1 = request.POST['q1']
        opt2 = request.POST['q2']
        opt3 = request.POST['q3']
        opt4 = request.POST['q14']
        opt5 = request.POST['q5']
        opt6 = request.POST['q6']
        opt7 = request.POST['q7']
        opt8 = request.POST['q8']
        opt9 = request.POST['q9']
        opt10 = request.POST['q10']
        sub = "Js Quiz"
        Quiz.objects.filter(id=11).update(id=11, sub=sub)
        Quiz.objects.filter(id=1).update(id=1, ans=opt1)
        Quiz.objects.filter(id=2).update(id=2, ans=opt2)
        Quiz.objects.filter(id=3).update(id=3, ans=opt3)
        Quiz.objects.filter(id=4).update(id=4, ans=opt4)
        Quiz.objects.filter(id=5).update(id=5, ans=opt5)
        Quiz.objects.filter(id=6).update(id=6, ans=opt6)
        Quiz.objects.filter(id=7).update(id=7, ans=opt7)
        Quiz.objects.filter(id=8).update(id=8, ans=opt8)
        Quiz.objects.filter(id=9).update(id=9, ans=opt9)
        Quiz.objects.filter(id=10).update(id=10, ans=opt10)
        userv = Quiz.objects. all()
        questions = JsQuiz.objects.all()
        access = Jsaccess.objects.all()
        score = 0
        wrong = 0
        correct = 0
        total = 0
        for b in access:
            access = b.number
        for (q, a) in zip(userv, questions):
            total += 1
            uservale = {'opt1': q.ans}
            orignal = {'opt1': a.Corrans}
            if uservale == orignal:
                score += 10
                correct += 1
            else:
                wrong += 1
        percent = score / (total * 10) * 100
        # print(score)
        # print(correct)
        # print(percent)

        if access != 1:
            if percent >= 90:
                a = 1
                print(a)
                students = Cppaccess(id=id, number=a)
                students.save()
            else:
                a = 0
                print(a)
                students = Cppaccess(id=id, number=a)
                students.save()
        else:
            pass

        newval = Cppaccess.objects.filter(id=id)
        for b in newval:
            newaccess = b.number
            print(newaccess)
        context = {
            'a': newaccess,
            'score': score,
            'correct': correct,
            'wrong': wrong,
            'percent': percent,
            'total': total
        }
        print(context)
        return render(request, 'result.html', context)
    else:
        questions = JsQuiz.objects.all()
        context = {
            'questions': questions
        }
        return render(request, 'jsquiz.html', context)

@login_required(login_url='loginpage')
def php(request):
    id = request.user.id
    if request.method == 'POST':
        opt1 = request.POST['q1']
        opt2 = request.POST['q2']
        opt3 = request.POST['q3']
        opt4 = request.POST['q14']
        opt5 = request.POST['q5']
        opt6 = request.POST['q6']
        opt7 = request.POST['q7']
        opt8 = request.POST['q8']
        opt9 = request.POST['q9']
        opt10 = request.POST['q10']
        sub = "Php Quiz"
        Quiz.objects.filter(id=11).update(id=11, sub=sub)
        Quiz.objects.filter(id=1).update(id=1, ans=opt1)
        Quiz.objects.filter(id=2).update(id=2, ans=opt2)
        Quiz.objects.filter(id=3).update(id=3, ans=opt3)
        Quiz.objects.filter(id=4).update(id=4, ans=opt4)
        Quiz.objects.filter(id=5).update(id=5, ans=opt5)
        Quiz.objects.filter(id=6).update(id=6, ans=opt6)
        Quiz.objects.filter(id=7).update(id=7, ans=opt7)
        Quiz.objects.filter(id=8).update(id=8, ans=opt8)
        Quiz.objects.filter(id=9).update(id=9, ans=opt9)
        Quiz.objects.filter(id=10).update(id=10, ans=opt10)
        userv = Quiz.objects. all()
        questions = PhpQuiz.objects.all()
        access = Phpaccess.objects.all()
        score = 0
        wrong = 0
        correct = 0
        total = 0
        for b in access:
            access = b.number
        for (q, a) in zip(userv, questions):
            total += 1
            uservale = {'opt1': q.ans}
            orignal = {'opt1': a.Corrans}
            if uservale == orignal:
                score += 10
                correct += 1
            else:
                wrong += 1
        percent = score / (total * 10) * 100
        # print(score)
        # print(correct)
        # print(percent)

        if access != 1:
            if percent >= 90:
                a = 1
                print(a)
                students = Cppaccess(id=id, number=a)
                students.save()
            else:
                a = 0
                print(a)
                students = Cppaccess(id=id, number=a)
                students.save()
        else:
            pass

        newval = Cppaccess.objects.filter(id=id)
        for b in newval:
            newaccess = b.number
            print(newaccess)
        context = {
            'a': newaccess,
            'score': score,
            'correct': correct,
            'wrong': wrong,
            'percent': percent,
            'total': total
        }
        print(context)
        return render(request, 'result.html', context)
    else:
        questions = PhpQuiz.objects.all()
        context = {
            'questions': questions
        }
        return render(request, 'phpquiz.html', context)



@login_required(login_url='loginpage')
def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'home.html')

@login_required(login_url='loginpage')
def score(request):
    return render(request, 'result.html')

def gen_cer(request):
    id=request.user.id
    if request.method == 'POST':
        fname = request.POST['fname']
        lname= request.POST['lname']
        mname = request.POST['mname']
        sub = Quiz.objects.all()
        for b in sub:
            access = b.sub
        print(fname, lname, mname, access)
        context = {
            'f': fname,
            'l': lname,
            'm': mname,
            's': access
        }
        # template_path = 'certificate.html'
        # # Create a Django response object, and specify content_type as pdf
        # response = HttpResponse(content_type='application/pdf')
        # response['Content-Disposition'] = 'attachment; filename="certificate.pdf"'
        # # find the template and render it.
        # template = get_template(template_path)
        # html = template.render(context)
        #
        # # create a pdf
        # pisa_status = pisa.CreatePDF(html, dest=response)
        #
        # # save pdf in DB
        # # savepdf = pisa_status
        # # pdf = certificate(file=savepdf)
        # # pdf.save()
        #
        # # if error then show some funy view
        # if pisa_status.err:
        #     return HttpResponse('We had some errors <pre>' + html + '</pre>')
        # return response
        return render(request, 'certificate.html',context)
    else:
        return render(request, 'gen_cer.html')

def certificate(request):
        return render(request, 'certificate.html')
