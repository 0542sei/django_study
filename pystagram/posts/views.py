from django.shortcuts import render, redirect
from posts.models import Post, Comment, PostImage, HashTag
from posts.forms import CommentForm, PostForm
from django.views.decorators.http import require_POST
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.urls import reverse

def feeds(request):
    user = request.user
    if not user.is_authenticated:
        return redirect("users:login")

    posts = Post.objects.all()
    comment_form = CommentForm()
    context = {"posts": posts,
               "comment_form": comment_form,}
    return render(request, "posts/feeds.html", context)

@require_POST
def comment_add(request):
    form = CommentForm(data=request.POST)

    if form.is_valid():
        comment = form.save(commit=False)
        comment.user = request.user
        comment.save()

        print(comment.id)
        print(comment.content)
        print(comment.user)
    # URL로 "next"값을 전달받았다면 댓글 작성 완료 후 전달받은 값으로 이동한다
        if request.GET.get("next"):
            url = request.GET.get("next")

        # "next"값을 전달받지 않았다면 피드페이지의 글 위치로 이동한다
        else:
            url = reverse("posts:feeds") + f"#post-{comment.post.id}"

        return HttpResponseRedirect(url)

@require_POST
def comment_delete(request, comment_id):
    comment = Comment.objects.get(id=comment_id)
    if comment.user == request.user:
        comment.delete()

        urls_next = reverse("posts:feeds")+ f"#post-{comment.post.id}"
        return HttpResponseRedirect(urls_next)
    else:
        return HttpResponseForbidden("이 댓글을 삭제할 권한이 없습니다.")

def post_add(request):
    if request.method == "POST":
          
        form = PostForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            for image_file in request.FILES.getlist("images"):
                PostImage.objects.create(
                    post = post,
                    photo = image_file,

                )
            tag_string = request.POST.get("tags")
            if tag_string:
                tag_names = [tag_name.strip() for tag_name in tag_string.split(",")]
                for tag_name in tag_names:
                    tag, _ = HashTag.objects.get_or_create(name=tag_name)
                    # get_or_create로 생성하거나 가져온 HashTag객체를 Post의 tags에 추가한다
                    post.tags.add(tag)

        url = reverse("posts:feeds") + f"#post-{post.id}"
        return HttpResponseRedirect(url)
    else:
        form = PostForm()

    context = {"form":form}
    return render(request, "posts/post_add.html", context)

def tags(request, tag_name):
    try:
        tag = HashTag.objects.get(name=tag_name)
    except HashTag.DoesNotExist:
          # tag_name에 해당하는 HashTag를 찾지 못한 경우 빈 QuerySet을 돌려준다
        posts = Post.objects.none()
    else:
        posts = Post.objects.filter(tags=tag)
    context = {
        "tag_name": tag_name,
        "posts": posts,
    }
    return render(request, "posts/tags.html", context)


def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    comment_form = CommentForm()
    context = { "post": post,
                "comment_form": comment_form }
    return render(request, "posts/post_detail.html", context)

def post_like(request, post_id):
    post = Post.objects.get(id=post_id)
    user = request.user

    if user.like_posts.filter(id=post.id).exists():
        user.like_posts.remove(post)

    else:
        user.like_posts.add(post)

    url = request.GET.get("next") or reverse("posts:feeds") + f"#post-{post.id}"
    return HttpResponseRedirect(url)




    