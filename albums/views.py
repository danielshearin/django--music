from django.shortcuts import render

def post_list(request):
    return render(request, 'albums/post_list.html', {})
