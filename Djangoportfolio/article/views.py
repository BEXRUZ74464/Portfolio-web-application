from django.shortcuts import render, get_object_or_404
from .models import Article
from .forms import CommentForm

def detail_article(request, pk):
    article = get_object_or_404(Article, pk=pk)
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=True)
            obj.article = article
            obj.save()

    comments = article.comments.all()

    context = {
        "article": article,
        "form": form,
        "comments": comments
    }
    return render(request, "blog-single.html", context=context)