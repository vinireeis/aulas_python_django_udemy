from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.core.validators import validate_email
from django.contrib.auth.decorators import login_required


def login(request):
    if request.method != 'POST':
        return render(request, 'accounts/login.html')

    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')
    user = auth.authenticate(request, username=usuario, password=senha)

    if not user:
        messages.error(request, 'Usuário ou senha inválido')
        return render(request, 'accounts/login.html')
    auth.login(request, user)
    messages.success(request, 'Login realizado com sucesso')
    return redirect('dashboard')


def logout(request):
    auth.logout(request)
    return redirect('login')


def register(request):
    if request.method != 'POST':
        return render(request, 'accounts/register.html')

    usuario = request.POST.get('usuario')
    nome = request.POST.get('nome')
    sobrenome = request.POST.get('sobrenome')
    email = request.POST.get('email')
    senha = request.POST.get('senha')
    senha2 = request.POST.get('senha2')

    if not nome or not usuario or not sobrenome or not email or not senha or not senha2:
        messages.error(request, "Preencha todos os campos para se cadastrar")
        return render(request, 'accounts/register.html')

    try:
        validate_email(email)
    except:
        messages.error(request, 'Email inválido')
        return render(request, 'accounts/register.html')

    if len(senha) < 6:
        messages.error(request, 'Senha muito curta, digite uma senha de 6 caracteres ou mais')
        return render(request, 'accounts/register.html')

    if senha != senha2:
        messages.error(request, 'As senhas digitadas são diferentes')
        return render(request, 'accounts/register.html')

    if len(usuario) < 4:
        messages.error(request, 'Usuário deve conter ao menos 4 caracteres')
        return render(request, 'accounts/register.html')

    if User.objects.filter(username=usuario).exists():
        messages.error(request, 'Usuário já utilizado')
        return render(request, 'accounts/register.html')

    if User.objects.filter(email=email).exists():
        messages.error(request, 'Email já utilizado')
        return render(request, 'accounts/register.html')

    messages.success(request, 'Cadastro realizado com sucesso. Informe seus dados para logar')

    user = User.objects.create_user(username=usuario, email=email, password=senha, first_name=nome, last_name=sobrenome)
    user.save()
    return redirect('login')

@login_required(redirect_field_name='login')
def dashboard(request):
    return render(request, 'accounts/dashboard.html')
