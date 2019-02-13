from django.shortcuts import render

posts= [
    {
        'author':'CoreyMS',
        'title': 'Blog Post 1',
        'content': 'First Post Content',
        'date_posted': '13th February, 2019'
    },
    {
        'author':'Jane Doe',
        'title': 'Blog Post 2',
        'content':'Second Post Content',
        'date_posted': '13th February, 2019'
    }

        ]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title':'About'})
