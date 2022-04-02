from django.shortcuts import render
from django.shortcuts import redirect
# Create your views here.
# from logweb.models import user
from . import models
from . import forms

# 1017 email verification-add
import hashlib
import datetime
from django.conf import settings

# 1017 email verification-add
def hash_code(s, salt='mysite'):
    h = hashlib.sha256()
    s += salt
    h.update(s.encode())  # update方法只接收bytes类型
    return h.hexdigest()

def make_confirm_string(user):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    code = hash_code(user.nickname, now)
    models.ConfirmString.objects.create(code=code, user=user,)
    return code

def send_email(email, code):

    from django.core.mail import EmailMultiAlternatives

    subject = 'Confirm Your CUHK Big Battle Account Email Address'

    text_content = '''Thanks for registeration\
                    如果你看到这条消息,说明你的邮箱服务器不提供HTML链接功能'''

    html_content = '''
                    <p>Thanks for registeration. To confirm your email address and unlock the content, please click the link: <a href="http://{}/confirm/?code={}" target=blank>www.cuhkbigbattle.com</a></p>
                    <p>The link is valid for {} days!</p>
                    '''.format('127.0.0.1:8000', code, settings.CONFIRM_DAYS)

    msg = EmailMultiAlternatives(subject, text_content, settings.EMAIL_HOST_USER, [email])
    msg.attach_alternative(html_content, "text/html")
    msg.send()
# verification-add end

def index(request):
    if not request.session.get('is_login', None):
        return redirect('/login/')
    return render(request, 'logweb/index.html')


def login(request):
    # add a test for login:
    if request.session.get('is_login', None):  # 不允许重复登录
        return redirect('/index/')
    # end the test part
    # main part:
    if request.method == "POST":
        useremail = request.POST['email']
        password = request.POST['password']
        message = 'please check the input!'
        if useremail.strip() and password: 
            # 此处可增加对用户名字符合法性的验证
            try:
                user = models.user.objects.get(email=useremail)
            except:
                message = 'user not exist!'
                return render(request, 'logweb/login.html', locals())
            # 1017 email verification-add
            if not user.has_confirmed:
                message = 'user has not confirmed the email address'
                return render(request, 'logweb/login.html', locals())
            # end verification-add
            if user.password == password:
                # add a test for login:
                request.session['is_login'] = True
                request.session['user_id'] = user.id
                request.session['user_name'] = user.nickname
                # end the test part
                return redirect('/index/')
            else:
                message = 'password not correct!'
                #return render(request, 'logweb/login.html', {'message': message})
                return render(request, 'logweb/login.html', locals())
    return render(request, 'logweb/login.html', locals())

def logout(request):
    if not request.session.get('is_login', None):
        return redirect("/login/")
    request.session.flush()
    return redirect('/login/')


def register(request):
    if request.session.get('is_login', None):
        return redirect('/index/')

    if request.method == 'POST':
        register_form = forms.RegisterForm(request.POST)
        message = "please check the inpur"
        if register_form.is_valid():
            username = register_form.cleaned_data.get('username')
            password1 = register_form.cleaned_data.get('password1')
            password2 = register_form.cleaned_data.get('password2')
            email = register_form.cleaned_data.get('email')

            if password1 != password2:
                message = 'different password input'
                return render(request, 'logweb/register.html', locals())
            else:
                same_email_user = models.user.objects.filter(email=email)
                if same_email_user:
                    message = 'the email address has been used'
                    return render(request, 'logweb/register.html', locals())

                new_user = models.user()

                new_user.email = email
                new_user.nickname = username
                new_user.password = password1
                new_user.token = 0
                new_user.profile_photo = ''

                new_user.save()
                
                # 1017 email verification-add
                code = make_confirm_string(new_user)
                send_email(email, code)
                message = 'please go to your email for confirmation'
                
                # 1017 email verification-change
                return render(request, 'logweb/confirm.html', locals())
                #return redirect('/login/')
        else:
            return render(request, 'logweb/register.html', locals())
    register_form = forms.RegisterForm()
    return render(request, 'logweb/register.html', locals())


def user_confirm(request):
    code = request.GET.get('code', None)
    message = ''
    try:
        confirm = models.ConfirmString.objects.get(code=code)
    except:
        message = 'invalid request'
        return render(request, 'logweb/confirm.html', locals())

    c_time = confirm.c_time
    now = datetime.datetime.now()
    if now > c_time + datetime.timedelta(settings.CONFIRM_DAYS):
        confirm.user.delete()
        message = 'Your email is expired, please register again'
        return render(request, 'logweb/confirm.html', locals())
    else:
        confirm.user.has_confirmed = True
        confirm.user.save()
        confirm.delete()
        message = 'Thanks for confirmation, plase use your email to login'
        return render(request, 'logweb/confirm.html', locals())