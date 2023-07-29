# email_system_project/email_system_app/views.py

from django.core.mail import EmailMessage
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def send_email(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        subject = data.get('subject', '')
        body = data.get('body', '')
        to_email = data.get('to_email', '')

        if subject and body and to_email:
            try:
                email = EmailMessage(
                    subject=subject,
                    body=body,
                    to=[to_email]
                )
                email.send()
                return JsonResponse({'message': 'Email sent successfully'})
            except Exception as e:
                return JsonResponse({'error': str(e)}, status=500)
        else:
            return JsonResponse({'error': 'Invalid request data'}, status=400)

