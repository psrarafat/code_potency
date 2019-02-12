from django.shortcuts import render

posts = [
    {
        'author':'CoreyMS',
        'title': 'Blog Post 1',
        'title': 'First Post Content',
        'date_posted': 'February 12, 2018',
    },
    {
        'author':'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second Post Content',
        'date_posted': 'February 12, 2018',
    }
        ]


def home(request):
    context = {
        'posts': posts
        }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title':'About'})
