from django.shortcuts import render

posts = [
    {
        "author": "mohammed shabeeb",
        "title": "Blog post 1",
        "content": "First post content",
        "date_posted": "August 26, 2023",
    },
    {
        "author": "mohammed aslam",
        "title": "Blog post 2",
        "content": "second post content",
        "date_posted": "August 29, 2023",
    },
]


# Create your views here.
def home(request):
    context = {"posts": posts}
    return render(request, "blog/home.html", context)


def about(request):
    return render(request, "blog/about.html", {"title": "About"})
