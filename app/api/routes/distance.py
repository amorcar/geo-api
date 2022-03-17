# from fastapi import APIRouter, Body, Depends, HTTPException
# from starlette.status import HTTP_400_BAD_REQUEST
from fastapi import APIRouter
from app.models.schema.latlon import LatLonDecimal
from app.models.schema.distance import DistanceResponse
from app.services.distance import get_distance_response
from app.models.domain.calculate_distance import (
    get_distance_between_positions_haversine,
    get_distance_between_positions_law_cosines,
    get_distance_between_positions_equirectangular
)


router = APIRouter()

@router.post(
    "/haversine/",
    response_model=DistanceResponse,
    name="Distance in meters between two GPS Lat,Lon coordinates")
async def process_haversine_distance(
        latlon1: LatLonDecimal,
        latlon2: LatLonDecimal
) -> DistanceResponse:
    lat1, lon1 = latlon1.dict().values()
    lat2, lon2 = latlon2.dict().values()
    return DistanceResponse(
        **(await get_distance_response(
            get_distance_between_positions_haversine,
            first_lat_deg = lat1,
            first_lon_deg = lon1,
            second_lat_deg = lat2,
            second_lon_deg = lon2,
        ))
    )

@router.post(
    "/cosines/",
    response_model=DistanceResponse,
    name="Distance in meters between two GPS Lat,Lon coordinates")
async def process_cosine_distance(
        latlon1: LatLonDecimal,
        latlon2: LatLonDecimal
) -> DistanceResponse:
    lat1, lon1 = latlon1.dict().values()
    lat2, lon2 = latlon2.dict().values()
    return DistanceResponse(
        **(await get_distance_response(
            get_distance_between_positions_law_cosines,
            first_lat_deg = lat1,
            first_lon_deg = lon1,
            second_lat_deg = lat2,
            second_lon_deg = lon2,
        ))
    )

@router.post(
    "/equirectangular/",
    response_model=DistanceResponse,
    name="Distance in meters between two GPS Lat,Lon coordinates")
async def process_cosine_distance(
        latlon1: LatLonDecimal,
        latlon2: LatLonDecimal
) -> DistanceResponse:
    lat1, lon1 = latlon1.dict().values()
    lat2, lon2 = latlon2.dict().values()
    return DistanceResponse(
        **(await get_distance_response(
            get_distance_between_positions_equirectangular,
            first_lat_deg = lat1,
            first_lon_deg = lon1,
            second_lat_deg = lat2,
            second_lon_deg = lon2,
        ))
    )
