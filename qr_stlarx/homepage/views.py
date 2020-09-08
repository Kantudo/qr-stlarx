from django.shortcuts import render

def index(request):
    params = {}
    params['logged'] = request.user.is_authenticated
    if params['logged']:
        params['user_email'] = request.user.email
        params['user_username'] = request.user.username

    return render(request, 'index.html', params)
