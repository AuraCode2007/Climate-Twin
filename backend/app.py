from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI(
    title="AQI & HCHO Hotspot Detection API",
    description="Real-time air quality monitoring for India",
    version="0.1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {
        "message": "🌍 AQI & HCHO Hotspot Detection API",
        "version": "0.1.0",
        "status": "online"
    }

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.get("/api/aqi/india")
def get_india_aqi():
    return {
        "aqi": 85,
        "category": "Moderate",
        "timestamp": "2024-06-28T12:00:00Z"
    }

@app.get("/api/hotspots")
def get_hotspots():
    return {
        "hotspot_count": 5,
        "hotspots": [
            {
                "name": "Delhi NCR",
                "hcho": 0.0015,
                "severity": "High",
                "lat": 28.7041,
                "lon": 77.1025
            }
        ]
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)