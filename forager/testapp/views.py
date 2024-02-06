import json
import requests
from datetime import date
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from .models import User, Users
from .forms import SignInForm, WeatherForecastForm, SignUpForm, UserEditForm


# Castom error handler.
def not_found(request, exception):
    return render(request, '404.html', status=404)


def sign_in(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Your is logged as ')
            return render(request, 'registration/sign_in.html', {'pk': user.id, 'username': user})
    else:
        form = SignInForm()
    return render(request, 'registration/sign_in.html', {'form': form})


def users_list(request):
    try:
        users = Users.objects.all()
    except Users.DoesNotExist:
        raise Http404('Users not found')
    return render(request, 'testapp/users_list.html', {'users': users})


def user_detail(request, user_id):
    user_pk = get_object_or_404(Users, pk=user_id)
    if str(request.user) == str(user_pk):
        user = User.objects.filter(user_from_users=user_id).order_by('-date')
        form = WeatherForecastForm()
        if request.method == 'POST':
            form = WeatherForecastForm(request.POST)
            if form.is_valid():
                location = form.cleaned_data['location']
                # Get location id.
                url = f'http://dataservice.accuweather.com/locations/v1/search?apikey=lMwAPrFeGuUxGkW07yASMzf0IfZLkBCQ&q={location}'
                try:
                    response = requests.get(url, timeout=10)
                except requests.exceptions.Timeout:
                    raise
                if response.status_code == 200:
                    response_content = response.json()
                    try:
                        response_content[0]
                    except IndexError:
                        messages.error(request, f'Location {location} not found.')
                        return render(request, 'testapp/user_detail.html', {'form': form, 'user': user, 'pk': user_id})
                   
                    # Convert response content to string format.
                    response_content_str = json.dumps(response_content[0])
                    # Json parsing.
                    parsed_response_content = json.loads(response_content_str)
                    # Obtain data.
                    key_location = parsed_response_content['Key']
                    # Get daily weather forecast.
                    url = f'http://dataservice.accuweather.com/forecasts/v1/daily/1day/{key_location}?apikey=lMwAPrFeGuUxGkW07yASMzf0IfZLkBCQ'
                    try:
                        response = requests.get(url, timeout=10)
                    except requests.exceptions.Timeout:
                        raise
                    if response.status_code == 200:
                        response_content = response.json()
                        response_content_str = json.dumps(response_content)
                        parsed_response_content = json.loads(response_content_str)
                        forecast = parsed_response_content['Headline']['Category']
                    else:
                        return HttpResponse(f'Error: {response.status_code}')
                else:
                    return HttpResponse(f'Error: {response.status_code}')
                user = User.objects.create(date=date.today(), location=location, forecast=forecast, user_from_users=user_pk)
                user.save()
                return redirect('user_detail', user_id)
        if not user:
            messages.info(request, f'No user information yet')
            return render(request, 'testapp/user_detail.html', {'form': form, 'user': user, 'pk': user_id})
        item_id = request.GET.get('item_id')
        if item_id:
            return HttpResponseRedirect(reverse('delete_item', args=[user_id, int(item_id)]))
        return render(request, 'testapp/user_detail.html', {'form': form, 'user': user, 'username': user[0].user_from_users.username, 'pk': user_id})
    # If the user is not authenticated.
    return redirect('users_list')


def delete_item(request, user_id, item_id):
    item = User.objects.filter(user_from_users=request.user.id).filter(id=item_id)
    item.delete()
    return redirect('user_detail', user_id)


def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request, user)
            messages.success(request, f'Your profile as {user} is created successfully')
            return render(request, 'testapp/sign_up.html', {'pk': user.id})
    else:
        form = SignUpForm()
    return render(request, 'testapp/sign_up.html', {'form': form})


# Pass id attribute from url.
def user_edit(request, user_id):
    # Fetch the user instance related to passed id.
    user = get_object_or_404(Users, pk=user_id)
    if str(request.user) == str(user):
        if request.method == 'POST':
            # Pass the user as instance in form
            form = UserEditForm(request.POST, instance=request.user)
            if form.is_valid():
                # Save the data from the form and return to page.
                form.save()
                messages.success(request, 'Your profile is updated successfully')
                return render(request, 'testapp/user_edit.html', {'pk': user_id})
        else:
            form = UserEditForm(instance=request.user)
        return render(request, 'testapp/user_edit.html', {'form': form, 'pk': user_id})
    return redirect('users_list')


def log_out(request):
    logout(request)
    return redirect('users_list')


def user_delete(request, user_id):
    user = get_object_or_404(Users, pk=user_id)
# If the authenticated user matches the one obtained from the object instance.
    if str(request.user) == str(user):
        user.delete()
    return redirect('users_list')
