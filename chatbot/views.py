from django.http import JsonResponse

def respond(request):
    return JsonResponse({'message': 'Thank you, your message adarsh'})
