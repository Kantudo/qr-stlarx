from django.shortcuts import render
from django.http import JsonResponse
from django.template.loader import render_to_string

from .forms import str2qr_charfield, UploadFileForm
from . import qr


# default index rn it contains the upload file form
def mon_index(request):
    context = {}
    context['logged'] = request.user.is_authenticated
    if context['logged']:
        context['user_email'] = request.user.email
        context['user_username'] = request.user.username

    if request.method == 'POST':  # i asume ajax is used for post requests
        context['form'] = UploadFileForm(request.POST, request.FILES)
        if context['form'].is_valid():
            fileName = request.FILES['file'].name
            mon_qr_path = qr.write_pdf(request.FILES['file'])
            resp_data = {
                        'src': mon_qr_path,
            }
            return JsonResponse(resp_data, status=200)
    elif request.is_ajax():
        context = {}
        context['form'] = UploadFileForm()
        mon_app = render_to_string(request=request, template_name="pdf2qr.html", context=context)
        resp_data = {
            'app_html': mon_app,
        }
        return JsonResponse(resp_data, status=200)
    else:
        context['form'] = UploadFileForm()

        return render(request, 'qr_index.html', context)


# other view, this one generates qr based on a string
def qr_strgen(request):

    context = {}
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        context['form'] = str2qr_charfield(request.POST, auto_id=False)
        form = context['form']
        print(form.is_valid())
        print(form.errors)
        if form.is_valid():
            mon_data = form.cleaned_data
            has_generated=True
            mon_qr_path = qr.createqr(mon_data['str2encode'])
            resp_data = {
                        'src': mon_qr_path,
            }
            return JsonResponse(resp_data, status=200)
    # if a GET (or any other method) we'll create a blank form
    elif request.is_ajax():
        context = {}
        context['form'] = str2qr_charfield(auto_id=False)
        mon_app = render_to_string(request=request, template_name="str2qr.html", context=context)
        resp_data = {
            'app_html': mon_app,
        }
        return JsonResponse(resp_data, status=200)
    else:
        context['form'] = str2qr_charfield(auto_id=False)
        if request.user.is_authenticated:
            display = 'logged in as ' + request.user.username
            print(display)

    return render(request, 'qr_strgen.html', context)
