from django.http import JsonResponse
from .ml_model import model

def ai_respond(request):
    user_message = request.GET.get('message', '')
    if user_message:
        ai_response = model.get_response(user_message)
        return JsonResponse({'reply': ai_response})
    return JsonResponse({'error': 'No message provided'}, status=400)
