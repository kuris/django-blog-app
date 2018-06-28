from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .forms import PostModelForm, PostForm
# Create your views here.
from django.utils import timezone

from .models import Post


def post_list_old(request):
    name_var= 'Django'
    return HttpResponse('''<h2>Hello {name}</h2>'''.format(name=name_var))
def post_list(request):
    posts_list= Post.objects.filter(published_date__lte=timezone.now()).order_by('created_date')
    return render(request,'blog/post_list.html',{'posts':posts_list})

def post_detail(request,pk):
    post_obj= get_object_or_404(Post,pk=pk)
    return render(request,'blog/post_detail.html',{'post':post_obj})
#PostModelForm을 사용한 등록
def post_new_modelform(request):
    if request.method == "POST":
        myform = PostModelForm(request.POST)
        if myform.is_valid():
            print(myform.cleaned_data)
            post = myform.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail',pk=post.pk)
    else:
    #get 요청일때 입력 폼을 출력
        myform = PostModelForm()
    return  render(request,'blog/post_edit.html',{'form':myform})

#PostForm을 사용한 등록처리
def post_new(request):
    if request.method == "POST" :
        form = PostForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)

            post = Post(author=request.user,
                        title=form.cleaned_data['title'],
                        text=form.cleaned_data['text'],
                        published_date=timezone.now())
            post.save()
            return redirect('post_detail',pk=post.pk)
    else:
        form = PostForm()
    return  render(request,'blog/post_edit.html',{'form':form})

#PostModelForm을 사용한 수정처리
@login_required
def post_edit(request,pk):
    post = get_object_or_404(Post,pk=pk)
    if request.method == "POST":
        form = PostModelForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail',pk=post.pk)
    else :
        form = PostModelForm(instance=post)
    return render(request,'blog/post_edit.html',{'form':form})


