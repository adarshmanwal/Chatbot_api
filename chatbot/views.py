from django.http import JsonResponse
from django.views.decorators.http import require_GET
from .ml_model import model
from .advancedQAmodel import advancedQAmodel
import requests

# Microsoft Translator config
SUBSCRIPTION_KEY = 'FH5mFsY4o4dxZeKNGauIM48gZPCKOePQ6oiH3CahihiRudPM4GysJQQJ99BEACrJL3JXJ3w3AAAbACOGjw7J'  # Replace with your real key
ENDPOINT = 'https://api.cognitive.microsofttranslator.com/'
REGION = 'westcentralus'

def detect_language(text):
    url = f'{ENDPOINT}detect?api-version=3.0'
    headers = {
        'Ocp-Apim-Subscription-Key': SUBSCRIPTION_KEY,
        'Ocp-Apim-Subscription-Region': REGION,
        'Content-type': 'application/json'
    }
    body = [{'text': text}]
    response = requests.post(url, headers=headers, json=body)
    response.raise_for_status()
    result = response.json()
    print("==============",result)
    return result[0]['language']  # e.g., 'fr', 'hi', 'en'

def translate_text(text, to_language):
    url = f'{ENDPOINT}translate?api-version=3.0&to={to_language}'
    headers = {
        'Ocp-Apim-Subscription-Key': SUBSCRIPTION_KEY,
        'Ocp-Apim-Subscription-Region': REGION,
        'Content-type': 'application/json'
    }
    body = [{'text': text}]
    response = requests.post(url, headers=headers, json=body)
    response.raise_for_status()
    result = response.json()
    return result[0]['translations'][0]['text']

@require_GET
def ai_respond(request):
    user_message = request.GET.get('message', '')

    context = """
    His body color is black and he is 6.2 feet tall"""

    if user_message:
        try:
            # Step 1: Detect user message language
            user_language = detect_language(user_message)

            # Step 2: Generate AI response in English
            ai_response = advancedQAmodel.get_response(user_message, context)

            # Step 3: Translate response into detected language if it's not English
            if user_language != 'en':
                ai_response = translate_text(ai_response, to_language=user_language)

            return JsonResponse({'reply': ai_response})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'No message provided'}, status=400)
