# GEOAPI

A very simple API to calculate distance between lat-lon points.

To run:
```python
python3 -m venv venv --prompt fastapi
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Docs at: ```http://120.0.0.1:8000/docs```

Examples:
```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/api/distance/haversine/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "latlon1": {
    "latitude": 40.41694,
    "longitude": -3.70361
  },
  "latlon2": {
    "latitude": 40.41634,
    "longitude": -3.703861
  }
}'
# Distance (using haversine): 70.01915m
```

```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/api/distance/cosines/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "latlon1": {
    "latitude": 40.41694,
    "longitude": -3.70361
  },
  "latlon2": {
    "latitude": 40.41634,
    "longitude": -3.703861
  }
}'
# Distance (using law of cosines): 70.01920m
```

```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/api/distance/equirectangular/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "latlon1": {
    "latitude": 40.41694,
    "longitude": -3.70361
  },
  "latlon2": {
    "latitude": 40.41634,
    "longitude": -3.703861
  }
}'
# Distance (using the equirectangular approximation): 68.10714m
```

Project structure:
```
.
├─ app
│  ├── api
│  │  ├── errors
│  │  └── routes
│  ├── core
│  ├── models
│  │  ├── domain
│  │  └── schema
│  ├── resources
│  └── services
├── log
│  └── main.log
├── main.py
└── README.md
```
