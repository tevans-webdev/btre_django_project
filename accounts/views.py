from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from contacts.models import Contact


def registerPage(request):
    if request.method == 'POST':
        # get form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        # check if passwords match
        if password == password2:
            # check username
            if User.objects.filter(username=username).exists():
                messages.error(request, 'That username is already registered')
                return redirect('register')
            else:
                # check for email
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'That email is already registered')
                    return redirect('register')
                else:
                    # checks pass continue registration
                    user = User.objects.create_user(
                        username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                    # login user after registration
                    # auth.login(request, user)
                    # messages.success(request, 'Registration complete. Logging you in now')
                    # return redirect('index')
                    user.save()
                    messages.success(
                        request, 'Registration complete. Please Login to continue')
                    return redirect('login')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')


def loginPage(request):
    if request.method == 'POST':
        # login user
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, ': You are now logged in')
            return redirect('dashboard')
        else:
            messages.error(request, 'Login Failed')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')


def logoutPage(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, ': You are now logged out')
        return redirect('login')


def dashboardPage(request):
    user_id = request.user.id
    user_contacts = Contact.objects.order_by(
        '-contact_date').filter(user_id=user_id)
    context = {
        'contacts': user_contacts
    }

    return render(request, 'accounts/dashboard.html', context)
