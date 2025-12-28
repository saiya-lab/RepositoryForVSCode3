from django.shortcuts import render, get_object_or_404, redirect
from django.forms import ModelForm
from sample_app.models import Post

def create_post(request):
    post = Post()

    if request.method == 'GET':

        form = PostForm(isinstance=post)
        return render(request,
                      'sample_app/post_form.html',
                      {'form':form})
    
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)

    if form.is_valid():
        post = form.save(commit=False)
        post.save()

    return redirect('sample_app:read_post')

def read_post(request):
    posts = Post.objects.all().order_by('id')
    return render(request,
                  'sample_app/post_list.html',
                  {'posts': posts})

def edit_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if request.method == 'GET':
        form = PostForm(instance=post)
        return render(request,
                      'sample_app/post_form.html',
                      {'form': form,'post_id': post_id})
    
    elif request.method == 'POST':
        form = PostForm(request.POST, instance=post)

        if form.is_valid():
            post = form.save(commit=False)
            post.save()

        return redirect('sample_app:read_post')
    
def delete_post(request, post_id):
    post = get_object_or_404(post, pk=post_id)
    post.delete()

    return redirect('sample_app:read_post')


class PostForm(ModelForm):

    class Meta:
        model = Post
        fields = ('name', 'micropost')

