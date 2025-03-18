from django.http import JsonResponse

def home_page(request):
    friends = [
        {
            "name": "John",
            "age": 25
        },
        {
            "name": "Jane",
            "age": 22
        }
    ]
    return JsonResponse(friends, safe=False)