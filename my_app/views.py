from typing import ContextManager
from django.core.checks import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .models import Post

# Create your views here.
'''
posts = [
    { 'Product_name': 'sample', 'Product_description': 'random text', 'Min_Bid_Price': '1000', 'End_Time': 'time end' },
    { 'Product_name': 'sample', 'Product_description': 'random text', 'Min_Bid_Price': '2000', 'End_Time': 'time end' },
    { 'Product_name': 'sample', 'Product_description': 'random text', 'Min_Bid_Price': '2688', 'End_Time': 'time end' },
    { 'Product_name': 'sample', 'Product_description': 'random text', 'Min_Bid_Price': '226767', 'End_Time': 'time end' }


]
'''
def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.get(username = username)
        user = authenticate(request, username= username, password=password)
        #user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        if user is not None:
            login(request, user)
            return redirect(gallery)
        
            

        
    context={}
    return render(request, 'my_app/login_register.html', context)

def gallery(request):
    #will show all the posts in database
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'my_app/gallery.html', context)

def post(request, pk):
    #getting a single room
    post = Post.objects.get(Product_description=pk)
   
    context = {'post': post}
    return render(request, 'my_app/post.html', context)