# views.py in your Django app
from django.http import HttpResponse
from xhtml2pdf import pisa
from django.template.loader import get_template
from mapapp.models import VenueName  # Import your VenueName model

def generate_pdf(request):
    # Get the venue ID from the request
    venue_id = request.GET.get('venue_id')
    try:
        venue = VenueName.objects.get(pk=venue_id)
    except VenueName.DoesNotExist:
        return HttpResponse("Venue not found.", content_type='text/plain')

    # Use the 'render_to_string' method to generate HTML string
    html = get_template('pdf/venue_template.html').render({'venue': venue})

    # Generate the PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{venue.name}.pdf"'
    pisa_status = pisa.CreatePDF(html, dest=response)

    if pisa_status.err:
        return HttpResponse('We had some errors while generating the PDF.', content_type='text/plain')

    return response

