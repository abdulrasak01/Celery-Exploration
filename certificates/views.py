# certificates/views.py
from django.http import JsonResponse
from .tasks import generate_certificate

def request_certificate(request, name):
    # Trigger the Celery task
    task = generate_certificate.delay(name)

    # Return the task ID so the user can check the status later
    return JsonResponse({"message": "Certificate generation started", "task_id": task.id})
