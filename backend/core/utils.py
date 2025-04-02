from math import radians, sin, cos, sqrt, atan2

def calculate_distance(lat1, lon1, lat2, lon2):
    """
    Calcula la distancia en metros entre dos puntos geográficos
    usando la fórmula de Haversine
    """
    # Radio de la Tierra en metros
    R = 6371000
    
    # Convertir coordenadas a radianes
    lat1_rad = radians(lat1)
    lon1_rad = radians(lon1)
    lat2_rad = radians(lat2)
    lon2_rad = radians(lon2)
    
    # Diferencias
    d_lat = lat2_rad - lat1_rad
    d_lon = lon2_rad - lon1_rad
    
    # Fórmula de Haversine
    a = sin(d_lat/2) * sin(d_lat/2) + cos(lat1_rad) * cos(lat2_rad) * sin(d_lon/2) * sin(d_lon/2)
    c = 2 * atan2(sqrt(a), sqrt(1-a))
    distance = R * c
    
    return distance

def is_location_valid(classroom_lat, classroom_lon, student_lat, student_lon, max_distance=50):
    """
    Verifica si el estudiante está dentro del radio permitido
    """
    distance = calculate_distance(classroom_lat, classroom_lon, student_lat, student_lon)
    return distance <= max_distance