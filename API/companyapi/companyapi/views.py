from django.http import HttpResponse,JsonResponse

def home_page(request):
    friend=[
        'ali',
        'hassan',
        'hussain',
    ]
    return JsonResponse(friend,safe=False)