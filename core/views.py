from django.shortcuts import render

# Create your views here.


def index_page(request):
    return render(request, "core/index.html")


def team_page(request):
    return render(request, "core/team.html")


def project_page(request):
    return render(request, "core/project.html")


def about_page(request):
    return render(request, "core/about.html")