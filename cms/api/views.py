from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Blog, User
# Create your views here.


def data_view(request, username, password,api_key=None):
	if api_key == '2364jh234jh2v4hgv3h3234':	
		user = User.objects.filter(user_name=username, password = password).reverse()
		if len(user) == 0 : 
			return JsonResponse({'authenticate':False,'data':{}}) 
		data = Blog.objects.all()
		filtered_data = []
		for i in data: 
			filtered_data.append({
			'id': i.id, 
			'title': i.title,
			'description': i.description, 
			'content': i.content, 
			'created_at': i.created_at, 
			'img_link': i.img_link, })
		return JsonResponse({'authenticate':True, 'data':filtered_data})
	else : 
		return JsonResponse({'authenticate': False, 'data':{}})


def home(request):
	context = {
		'blogs' : Blog.objects.all().reverse(),
	}
	return render(request,'home.html', context)

def view_blog(request, post_id): 
	context = {
	'post_id': post_id, 
	'blog' : Blog.objects.get(id=post_id) 
	}
	return render(request,'view_blog.html', context)

def modify_blog(request, post_id):
	if request.POST : 
		blog = Blog.objects.get(id=post_id)
		blog.title = request.POST['rh_title'] 
		blog.description = request.POST['rh_description'] 
		blog.content = request.POST['rh_content'] 
		blog.save()
		return redirect(f'/view/{post_id}')
	context = {
	'blog' : Blog.objects.get(id=post_id) , 
	'title' : 'Update your blog', 
	'btn_text': 'Update'
	}
	return render(request, 'create_post.html', context)

def create_blog(request):
	if request.POST:
		Blog.objects.create(title=request.POST['rh_title'],
							description=request.POST['rh_description'],
						 	content=request.POST['rh_content'], 
						 	img_link= 'https://images.unsplash.com/photo-1580618672591-eb180b1a973f?ixlib=rb-1.2.1&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=1080&fit=max&ixid=eyJhcHBfaWQiOjIyNjM5fQ' )	
		# adding a temp img_link so if the user quits the porcess of selection of teh image in between the content written in safe
		request.session['blog_id'] = Blog.objects.latest('id').id
		print('this is the latest created blog id bitch ', request.session['blog_id']) 
		context = {}
		return render(request,'img_select.html', context)
	context = {
		'title' : 'Create a new post',
		 'btn_text': 'Update'
	}

	return render(request,'create_post.html', context)

def show_images(request,img_link):
	blog = Blog.objects.get(id=request.session['blog_id'])
	blog.img_link = img_link
	blog.save()
	return redirect('/')

def delete_post(request, post_id, confirmation=0):
	if confirmation == 1 : 
		Blog.objects.get(id=post_id).delete()
		return redirect('/')
	return render(request, 'confirmation.html')

def create_user(request): 
	if request.POST: 
		User.objects.create(user_name=request.POST['username'], password=request.POST['password'])
		return redirect('/')
	return render(request,'create_user.html')

