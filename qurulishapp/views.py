from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Condition, Material


@csrf_exempt
def add_condition(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        condition_name = data.get('name')
        materials = data.get('materials', [])

        condition, created = Condition.objects.get_or_create(name=condition_name)

        for material in materials:
            Material.objects.get_or_create(condition=condition, name=material.strip())

        return JsonResponse({"message": "Qurilish sharoiti muvaffaqiyatli qo‘shildi!"})


@csrf_exempt
def recommend(request):
    if request.method == 'POST':
        try:
            if request.content_type == 'application/json':
                data = json.loads(request.body)
            else:
                data = request.POST  # Formdan kelayotgan ma'lumotlarni olish

            condition_name = data.get('condition')
            if not condition_name:
                return JsonResponse({"error": "Qurilish sharoiti tanlanmagan!"}, status=400)

            condition = get_object_or_404(Condition, name=condition_name)
            materials = [m.name for m in condition.materials.all()]

            return JsonResponse({"recommendation": f"Tavsiya etilgan materiallar: {', '.join(materials)}"})
        except json.JSONDecodeError:
            return JsonResponse({"error": "Noto‘g‘ri JSON format!"}, status=400)


def home(request):
    conditions = Condition.objects.all()
    return render(request, "index.html", {"conditions": conditions})