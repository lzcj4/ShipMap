from sysadmin.models_car import CarFeature
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.utils.decorators import method_decorator
from django.views import generic


class CarListView(generic.ListView):
    template_name = 'car_list.html'
    context_object_name = 'list_result'

    def get_queryset(self):
        """Return cars group by brand and model"""
        return self.get_cars(self.request)

        # def get_context_data(self, **kwargs):
        #     # Call the base implementation first to get a context
        #     context = super(CarListView, self).get_context_data(**kwargs)
        #     # Add in the publisher
        #     context['publisher'] = self.publisher
        #     return context

    # @permission_required(Perms.CAR_LIST, login_url=reverse_lazy('sysadmin:index'))
    @method_decorator(login_required)
    def get_cars(self, request):
        """Return cars group by brand and model"""
        all_list = CarFeature.objects.all().order_by('id')
        page = request.GET.get('page', 1)
        paginator = Paginator(all_list, 10)
        try:
            cars = paginator.page(page)
        except PageNotAnInteger:
            cars = paginator.page(1)
        except EmptyPage:
            cars = paginator.page(paginator.num_pages)

        group_result = {}
        for item in cars:
            sub_brand = item.model.brand
            sub_model = item.model
            if sub_brand not in group_result:
                group_result[sub_brand] = {}
            b_dict = group_result[sub_brand]
            if sub_model not in b_dict:
                b_dict[sub_model] = []
            b_dict[sub_model].append(item)
        return {'cars': cars, 'group_cars': group_result, "user": request.user}

        # class DetailView(generic.DetailView):

# model = Question
#     template_name = 'polls/detail.html'
