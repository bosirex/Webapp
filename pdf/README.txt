# Project Name

## Description
This project includes a Django application for generating PDF reports of ePCR forms including venue information.

## Setup
1. Install dependencies: `pip install -r requirements.txt`
2. Migrate the database: `python manage.py migrate`
3. Run the server: `python manage.py runserver`

## Usage
1. Navigate to `/epcr/form` to fill out the ePCR form.
2. Choose a venue from the dropdown and click 'Print' to generate a PDF report.

## Development
To add new venues, update the VenueName model in the `mapapp` application.

## PDF Template Customization
To change the PDF output, edit the `venue_template.html` in the `pdf_generator/templates/pdf` directory.

## Contributing
Future developers can contribute to the project by following the guidelines provided in this README.

## License
Specify the project license here.
