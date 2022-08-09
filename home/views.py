
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Student, Joined, Batch, Trainer
from django.contrib import auth


# Create your views here.

def home(request):
    return render(request, 'home.html')


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        rpassword = request.POST['rpassword']
        if User.objects.filter(username=username).exists():
            messages.warning(request, 'Username Is already Exists')
            return redirect('/signup')
        elif User.objects.filter(email=email).exists():
            messages.warning(request, 'Email Already Exists')
            return redirect('/signup')
        elif password != rpassword:
            messages.error(request, 'Password is Missmatch')
            return redirect('/signup')
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            messages.success(request, 'Signup Sucsessful')
            return redirect('/')
    else:
        return render(request, 'signup.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return render(request,'base.html')
        else:
            messages.warning(request, 'Invalid Username And Password')
            return redirect('/login')
    else:
        return render(request, 'login.html')
    
def logout(request):
    auth.logout(request)
    messages.warning(request,'Sucsessfully Logout')
    return redirect('/')


def addstudent(request):
    if request.method == 'POST':
        username = request.POST['email']
        email = request.POST['email']
        fname = request.POST['fname']
        lname = request.POST['lname']
        password = request.POST['password']
        user = User.objects.create_user(
            username=username, first_name=fname, last_name=lname, email=email, password=password)
        user.save()
        s = Student()
        s.user = user
        s.name = fname
        s.mob = request.POST['mob']
        s.address = request.POST['address']
        s.course = request.POST['course']
        s.remarks = request.POST['remarks']
        s.edt = request.POST['edt']
        s.save()
        messages.info(request, 'Sucessfully Added')
        return render(request, 'addstudent.html')
    else:
        return render(request, 'addstudent.html')


def showstudent(request):
    st = Student.objects.all()
    return render(request, 'showstudent.html', {'st': st})


def updatestudent(request):
    id = request.POST['uid']
    s = Student.objects.filter(user_id=id).get()
    s.address = request.POST['address']
    s.mob = request.POST['mob']
    s.remarks = request.POST['remarks']
    s.course = request.POST['course']
    s.save()
    messages.info(request, 'Sucessfully Updated')
    st = Student.objects.all()
    return render(request, 'showstudent.html', {'st': st})


def searchstudent(request):
    if request.method == 'POST':
        name = request.POST['name']
        course = request.POST['course']
        mob = request.POST['mob']
        fdt = request.POST['fdt']
        tdt = request.POST['tdt']
        st = Student.objects.all()
        if name != "" and name is not None:
            st = st.filter(name=name)
        if course != "" and course is not None:
            st = st.filter(course=course)
        if mob != "" and mob is not None:
            st = st.filter(mob=mob)
        if fdt != "" and fdt is not None:
            st = st.filter(edt__gte=fdt)
        if tdt != "" and tdt is not None:
            st = st.filter(edt__lte=tdt)
        return render(request, 'showstudent.html', {'st': st})
    else:
        return render(request, 'searchstudent.html')


def joinstudent(request):
    if request.method == 'POST':
        id = request.POST['student']
        student = Student.objects.filter(user_id=id).get()
        j = Joined()
        j.student = student
        j.joined_dt = request.POST['joined_dt']
        j.total = request.POST['total']
        j.first_ins = request.POST['first_ins']
        j.first_dt = request.POST['first_dt']
        j.last_ins = request.POST['last_ins']
        j.last_dt = request.POST['last_dt']
        j.duration = request.POST['duration']
        j.dues = request.POST['dues']
        j.save()
        messages.info(request, "sucsessfully Joined")
        joined = Joined.objects.all()
        return render(request, 'showjoinedstudents.html', {'joined': joined})
    else:
        st = Student.objects.all()
        return render(request, 'joinstudent.html', {'st': st})


def showjoinedstudents(request):
    joined = Joined.objects.all()
    return render(request, 'showjoinedstudents.html', {'joined': joined})


def updatejoined(request):
    id = request.POST['id']
    j = Joined.objects.filter(id=id).get()
    j.last_ins = request.POST['last_ins']
    j.last_dt = request.POST['last_dt']
    j.dues = request.POST['dues']
    j.save()
    messages.info(request, 'Updated sucessfully')
    joined = Joined.objects.all()
    return render(request, 'showjoinedstudents.html', {'joined': joined})


def searchjoinedstudents(request):
    if request.method == 'POST':
        name = request.POST['name']
        mob = request.POST['mob']
        course = request.POST['course']
        fdt = request.POST['fdt']
        tdt = request.POST['tdt']
        dues = request.POST['dues']
        st = Student.objects.all()
        js = Joined.objects.all()
        if dues == 'No_Dues':
            js = js.filter(dues=0)
        else:
            js = js.filter(dues__gte=1)
        if fdt != "" and fdt is not None:
            js = js.filter(joined_dt__gte=fdt)
        if tdt != "" and tdt is not None:
            js = js.filter(joined_dt__lt=tdt)
        if name != "" and name is not None:
            st = st.filter(name=name)
            js = js.filter(student__in=st)
        if mob != "" and mob is not None:
            st = st.filter(mob=mob)
            js = js.filter(student__in=st)
        if course != "" and course is not None:
            st = st.filter(course=course)
            js = js.filter(student__in=st)
        return render(request, 'showjoinedstudents.html', {'joined': js})
    else:
        return render(request, 'searchjoinedstudents.html')
