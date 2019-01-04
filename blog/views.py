from django.shortcuts import render

posts = [
    {
        'author':'roy',
        'title': 'blog post 1',
        'content': 'first post content',
        'date_posted': 'January 3 2019'
    },
    {
        'author':'wasibani',
        'title': 'blog post 2',
        'content': 'second post content',
        'date_posted': 'January 4 2019'
    }
]

def home(request):
    context = {
        'posts':posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'about'})
