# certificates/tasks.py
from celery import shared_task
from io import BytesIO
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from PIL import Image, ImageDraw, ImageFont

@shared_task
def generate_certificate(name):
    # Create a dummy certificate image
    certificate = Image.new('RGB', (800, 600), color=(255, 255, 255))
    draw = ImageDraw.Draw(certificate)

    # Add some text (you can use custom fonts)
    font = ImageFont.load_default()
    text = f"Certificate of Completion\n\n{str(name)}"
    draw.text((150, 250), text, fill="black", font=font)

    # Save the image to a temporary file
    buffer = BytesIO()
    certificate.save(buffer, format='PNG')
    buffer.seek(0)

    # Save the image in Django's file system (you can save it elsewhere)
    file_name = f"{name}_certificate.png"
    file_path = default_storage.save(file_name, ContentFile(buffer.read()))
    
    # Return the file path for use later (e.g., for email or downloading)
    return file_path
