from django.http import HttpResponse,JsonResponse

def home_page(request):
    friend=[
        'ali',
        'hassan',
        'hussain',
        'amir',
    ]
    return JsonResponse(friend,safe=False)
