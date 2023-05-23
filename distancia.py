import streamlit as st
from geopy.geocoders import Nominatim
from geopy.distance import geodesic

def main():
    st.title("Búsqueda de supermercados cercanos")
    st.write("Ingrese su ubicación para encontrar los supermercados cercanos:")

    # Obtener ubicación del usuario
    location = get_user_location()
    if location is None:
        st.error("No se pudo obtener la ubicación. Verifique su conexión a internet.")
        return

    st.write("Ubicación actual:")
    st.write(f"Latitud: {location.latitude}, Longitud: {location.longitude}")

    # Lista de supermercados (ejemplo)
    supermarkets = [
        {"name": "Supermercado A", "latitude": 37.123, "longitude": -122.456},
        {"name": "Supermercado B", "latitude": 37.456, "longitude": -122.789},
        {"name": "Supermercado C", "latitude": 37.789, "longitude": -122.123}
    ]

    st.write("Supermercados cercanos:")
    for supermarket in supermarkets:
        supermarket_coords = (supermarket["latitude"], supermarket["longitude"])
        distance = calculate_distance(location, supermarket_coords)
        st.write(f"- {supermarket['name']}: {distance} km")

def get_user_location():
    try:
        geolocator = Nominatim(user_agent="supermarket-finder")
        location = geolocator.geocode("me")
        return location.point
    except:
        return None

def calculate_distance(coords1, coords2):
    return round(geodesic(coords1, coords2).kilometers, 2)

if __name__ == "__main__":
    main()
