from django.shortcuts import render, redirect
from .models import Work, Category
from teacher.models import Teacher
from django.core.paginator import Paginator
from article.models import Article
from contact.models import Contact
from contact.forms import ContactForm

def home(request):
    teachers = Teacher.objects.all()[:4]
    paginator = Paginator(Work.objects.all(), 4)
    articles = Article.objects.all()[:4]

    page = request.GET.get("page")
    # page = int(page)
    if not page or not isinstance(page, int):
        page = 1

    all_pages = paginator.num_pages
    if int(page) > all_pages or page < 0:
        return redirect("not_found")

    works = paginator.get_page(page)

    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()

    context = {
        "works": works,
        "page": page,
        "teachers": teachers,
        "articles": articles,
        "form": form
    }

    return render(request, "index.html", context=context)


def not_found(request):
    return render(request, '404_not_found.html')