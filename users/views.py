from django.views.generic import ListView, CreateView, UpdateView
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import LoginForm, ManagerForm
from .models import CustomUser


def home(request):
	return render(request, 'home.html', {"user": request.user})


def sign_in(request):
	if request.method == 'GET':
		form = LoginForm()
		return render(request, 'registration/login.html', {'form': form})
	elif request.method == "POST":
		form = LoginForm(request.POST)

		if form.is_valid():
			email = form.cleaned_data['email']
			password = form.cleaned_data['password']

			user = authenticate(request, username=email, password=password)
			print(user)
			if user:
				login(request, user)
				messages.success(request, f'Hi {user.username}, welcome back!')
				return redirect('home')

		messages.error(request, f'Invalid username or password')
		return render(request, 'registration/login.html', {'form': form})


def sign_out(request):
	logout(request)
	messages.success(request, f'You have been logged out.')
	return redirect('login')


class ManagersListView(ListView):
	login_url = '/users/login/'
	model = CustomUser
	template_name = 'managers.html'
	raise_exception = True
	queryset = CustomUser.objects.filter(roles="manager")


class ManagerCreateView(CreateView):
	""" Apartment Create part """
	login_url = '/users/login/'
	form_class = ManagerForm
	model = CustomUser
	template_name = 'manager_add.html'

	def get(self, request, *args, **kwargs):
		form = self.form_class()
		query = self.model
		context = {
			'form': form,
			'object': query
		}
		return render(request, self.template_name, context)

	def post(self, request, *args, **kwargs):
		form = self.form_class(data=request.POST)

		if form.is_valid():
			data = form.save(commit=False)
			data.roles = "manager"
			data.save()
			return redirect('managers_list')

		form = self.form_class(data=request.POST)
		context = {
			'form': form
		}

		return render(request, self.template_name, context)


class ManagerUpdateView(UpdateView):
	""" AuthOrganization update part"""
	login_url = '/users/login/'
	model = CustomUser
	form_class = ManagerForm
	template_name = 'manager_update.html'

	def get_object(self, queryset=None):
		id = self.kwargs.get('id')
		obj = None
		if id is not None:
			obj = get_object_or_404(self.model, id=id)
		return obj

	def get(self, request, id=None, *args, **kwargs):
		query = self.get_object()
		if query is not None:
			form = self.form_class(instance=query)
			context = {'form': form, 'object': query}
			return render(request, self.template_name, context)

	def post(self, request, id=None, *args, **kwargs):
		query = self.get_object()
		if query is not None:
			form = self.form_class(data=request.POST, instance=query)
			if form.is_valid():
				form.save()
				return redirect('managers_list')

		return self.get(request, *args, **kwargs)


def manager_delete(request, id):
	""" Apartment delete object"""

	organ = get_object_or_404(CustomUser, id=id)
	if request.method == 'POST' and organ:
		organ.delete()
		return redirect('managers_list')
	context = {'manager': organ}
	return render(request, 'manager_delete.html', context)
