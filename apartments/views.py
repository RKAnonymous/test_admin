from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.db import transaction
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from .forms import ApartmentForm
from .models import Apartment, BookingApartment


class ApartmentListView(ListView):
    """ Apartment List """
    model = Apartment
    template_name = 'apartments.html'
    context_object_name = "apartments"
    raise_exception = True
    queryset = Apartment.objects.all().order_by('-id')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ApartmentListView, self).get_context_data(**kwargs)
        context["apartments"] = self.model.objects.all()
        return context

    def get_object(self, id):
        object = {}
        try:
            object = self.model.objects.get(id=id)
        except ObjectDoesNotExist:
            return object

        return object

    def get_queryset(self):
        apartments = self.queryset
        for apartment in apartments:
            booked_apartment = self.get_object(id=apartment.id)

            if booked_apartment:
                apartment.customer = booked_apartment

        return apartments


class ApartmentCreateView(CreateView):
    """ Apartment Create """
    login_url = '/users/login/'
    form_class = ApartmentForm
    model = Apartment
    template_name = 'apartment_add.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        query = self.model
        context = {
            'form': form,
            'object': query
        }
        return render(request, self.template_name, context)

    @transaction.atomic()
    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')

        form = self.form_class(data=request.POST)
        context = {
            'form': form
        }

        return render(request, self.template_name, context)


class ApartmentDetail(DetailView):
    """AuthOrganization Detail part"""
    login_url = '/users/login/'
    model = Apartment

    def get(self, request, id, *args, **kwargs):
        query = self.model.objects.get(id=id)
        context = {
            'object': query
        }
        return render(request, 'apartment_detail.html', context)


class ApartmentUpdate(UpdateView):
    """ Apartment update """
    login_url = '/users/login/'
    model = Apartment
    form_class = ApartmentForm
    template_name = 'apartment_update.html'

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

    @transaction.atomic()
    def post(self, request, id=None, *args, **kwargs):
        query = self.get_object()
        if query is not None:
            form = self.form_class(data=request.POST, instance=query)
            if form.is_valid():
                form.save()
                return redirect('list')

        return self.get(request, *args, **kwargs)


@transaction.atomic()
def apartment_delete(request, id):
    """ Apartment delete object"""

    organ = get_object_or_404(Apartment, id=id)
    if request.method == 'POST' and organ:
        organ.delete()
        return redirect('list')
    context = {'object': organ}
    return render(request, 'apartment_delete.html', context)


# API Views
def filters(request):
    """API for filters"""
    status = request.query_params.get("status") or "active"
    building = request.query_params.get("building") or "Prime City"
    apartments = Apartment.objects.filter(status=status, building=building)
    return JsonResponse(apartments)
