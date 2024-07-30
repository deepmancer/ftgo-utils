import h3
from typing import List, Dict, Optional, Tuple, Any

from ..constants import ProvinceBoundaries, Provinces


def calculate_centroid(boundaries: Dict[str, Any]) -> Tuple[float, float]:
    coords = boundaries['coordinates'][0][0] if boundaries['type'] == 'Polygon' else boundaries['coordinates'][0][0][0]
    avg_lat = sum(coord[1] for coord in coords) / len(coords)
    avg_lng = sum(coord[0] for coord in coords) / len(coords)
    return avg_lat, avg_lng

PROVINCE_HEXAGONS = {
    province: list(h3.polyfill(boundaries, 8)) for province, boundaries in ProvinceBoundaries.items()
}

PROVINCE_CENTROIDS = {
    province: calculate_centroid(boundaries) for province, boundaries in ProvinceBoundaries.items()
}

def get_hexagon_id(lat: float, lng: float, resolution: int) -> str:
    return h3.geo_to_h3(lat, lng, resolution)

def get_hexagon_neighbors(hex_id: str, radius: int) -> List[str]:
    return h3.k_ring(hex_id, radius)

def get_province(lat: float, lng: float, return_closest: Optional[bool] = False) -> Optional[str]:
    location_hexagon = get_hexagon_id(lat, lng, 8)

    for province, province_hexagons in PROVINCE_HEXAGONS.items():
        if location_hexagon in province_hexagons:
            return province

    if return_closest:
        min_distance = float('inf')
        closest_province = None
        for province, centroid in PROVINCE_CENTROIDS.items():
            distance = h3.point_dist((lat, lng), centroid, unit='m')
            if distance < min_distance:
                min_distance = distance
                closest_province = province
        return closest_province
    
    return None

def get_country(lat: float, lng: float) -> str:
    return 'IR'

__all__ = ['get_hexagon_id', 'get_hexagon_neighbors', 'get_province', 'get_country']
