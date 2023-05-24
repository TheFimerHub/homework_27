import json

from django.core.exceptions import ValidationError
from django.http import JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView

from categories.models import Categories


@method_decorator(csrf_exempt, name="dispatch")
class AllCatergoryView(View):
    def get(self, request, *args, **kwargs):
        categories_data = Categories.objects.all()
        response = []

        for category in categories_data:
            response.append({
                "id": category.id,
                "name": category.name,
            })

        return JsonResponse(response, safe=False)

    def post(self, request):
        categories_data = json.loads(request.body)
        categories_ = Categories()
        categories_.name = categories_data["name"]

        try:
            categories_.full_clean()
        except ValidationError as e:
            return JsonResponse(e.message_dict, status=422)

        categories_.save()

        return JsonResponse(categories_data, safe=False)



@method_decorator(csrf_exempt, name="dispatch")
class CategoryView(DetailView):
    model = Categories

    def get(self, request, *args, **kwargs):
        categories_ = self.get_object()

        return JsonResponse({
            "id": categories_.id,
            "name": categories_.name,
        })


@method_decorator(csrf_exempt, name="dispatch")
class DownloadCategoriesView(View):
    def get(self, request):
        with open('./datasets/categories.json', 'r') as file:
            data = json.load(file)

            for item in data:
                categories_ = Categories(name=item['name'])
                categories_.save()

        return JsonResponse({"status": "ok"}, status=200)
