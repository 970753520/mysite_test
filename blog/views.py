from django.shortcuts import render_to_response,get_object_or_404
from django.core.paginator import Paginator
from .models import Blog,BlogType



# Create your views here.
def blog_list(request):
    blogs_all_list = Blog.objects.all()
    paginator = Paginator(blogs_all_list,10)#每10篇博客为一页
    page_num = request.GET.get('page',1)#获取页码参数(get请求),如果没有默认打开第1页
    page_of_blogs = paginator.get_page(page_num)
    currentr_page_num = page_of_blogs.number #获取当前页码
    
    
    context={}
    context['blogs'] = page_of_blogs.object_list
    #context['blogs_count'] = Blog.objects.all().count()
    context['page_of_blogs'] = page_of_blogs
    context['blog_types'] = BlogType.objects.all()
    return render_to_response('blog/blog_list.html',context)


def blog_detail(request,blog_pk):
    context={}
    context['blog'] = get_object_or_404(Blog,pk=blog_pk)
    return render_to_response('blog/blog_detail.html',context)


def blogs_with_type(request,blog_type_pk):
    context={}
    blog_type = get_object_or_404(BlogType,pk=blog_type_pk)
    context['blog_type'] = blog_type
    context['blogs'] = Blog.objects.filter(blog_type=blog_type)
    context['blog_types'] = BlogType.objects.all()
    return render_to_response('blog/blogs_with_type.html',context)
