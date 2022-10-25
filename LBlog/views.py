from django.shortcuts import render
from LBlog.models import blog 
from django.http import HttpResponse

# Create your views here.

#블로그 목록
def blog_list(request):   
    # blogs = blog.objects.all()
    # print(blogs)
    return HttpResponse ("잘 들어왔낭?")

#블로그작성
def blog_writing(request):
#작성Form(GET)
    if request.method == 'GET':
        return render(request, 'blog_writing.html')
# #작성(POST)
#     if request.method == 'POST':
#         my_auther = "승주"
#         new_blog = blog()
#         new_blog.auther = my_auther
#         new_blog.writer = request.POST.get("my_witer")
#         new_blog.save()
        
#         return HttpResponse ("작성완료!!")
    
#블로그 상세 페이지