# ePCR API Documentation

## Overview
This document provides guidelines and instructions for developers to work with the ePCR API.

## Environment Setup
- Python 3.6+
- Django 3.0+
- Django Rest Framework

Make sure all dependencies are installed using `pip install -r requirements.txt`.

## API Endpoints
The following endpoints are available:

- `/incidents/`: For operations on the Incident model.
- `/patients/`: For operations on the Patient model.
- `/personnel/`: For operations on the Personnel model.
- `/epcrs/`: For operations on the EPCR model.
- `/overdose_forms/`: For operations on the OverdoseForm model.

Each endpoint supports `GET`, `POST`, `PUT`, `PATCH`, and `DELETE` HTTP methods.

## Models
- `Incident`: Represents an emergency incident.
- `Patient`: Represents a patient involved in an incident.
- `Personnel`: Represents emergency personnel.
- `EPCR`: Represents an electronic patient care report.
- `OverdoseForm`: Represents an overdose form associated with an EPCR.

## Serialization
Serializers convert model instances to JSON and validate data for inserts and updates.

## Permissions
Currently, there are no specific permissions set, and the API is open to unauthenticated access. It's recommended to implement authentication and permissions as per your project requirements.

## Error Handling
The API uses standard HTTP status codes to indicate the success or failure of an API request.

## Notes
- Replace the `Unknown Location` placeholder in views with actual logic to determine the location.
- Replace the `Unknown` placeholder for the personnel's `certification_number` with logic to retrieve or create a personnel member.

For more detailed information, refer to Django and Django Rest Framework documentation.
