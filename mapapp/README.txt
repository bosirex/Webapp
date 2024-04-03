# README for Future Developers

## Incident/Map/Marker Feature

This feature allows incidents to be recorded, and displays them on a map using markers. Responders can also be assigned to incidents.

---

## Key Points:

1. **Markers**:
    - Markers for incidents and responders are intended to be displayed on a map.
    - Markers are determined based on the incident category (e.g., medical, security, etc.).
    - Custom markers can be fetched from the endpoint `/get_marker?category=<category_name>` which returns the marker image URL based on the incident type.

2. **Errors & Debugging**:
    - If markers aren't showing up, ensure the static file paths are correct.
    - Console logs show a 404 error for the marker images, indicating a problem with the static path. The path should be consistent with the Django static file structure.
    - The `/get_marker` endpoint should be functional and correctly configured in the `urls.py`.

3. **Map Coordinates**:
    - To change the default map coordinates, modify the latitude and longitude values in the map's initialization code.
    - For Hunt Valley Mall: Use Latitude: 39.49983 and Longitude: -76.64108.

4. **URL Endpoints**:
    - `/record_incident/`: Used to record new incidents.
    - `/save_coords/`: Used to save the coordinates of incidents and responders.
    - `/get_marker/`: Fetches the marker image based on the incident category.

5. **Javascript Functionality**:
    - The map uses Leaflet.js for rendering.
    - The `fetchMarkerImage` function retrieves the appropriate marker image.
    - The save button fetches and saves coordinates of the incident and responder markers.

---

Note: Always ensure the static file paths are consistent with Django's static file configuration. Any changes to the static file structure or naming should be reflected in the frontend code accordingly.

