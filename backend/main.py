from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from model_loader import model_loader
from remedies import get_remedy
import uvicorn
import io
import os

app = FastAPI(title="Plant Nutrient Deficiency Detector")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for dev
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "plant_disease_model.pt")
CLASS_INDICES_PATH = os.path.join(BASE_DIR, "class_indices.json")

@app.on_event("startup")
async def startup_event():
    try:
        model_loader.load_model(MODEL_PATH, CLASS_INDICES_PATH)
    except Exception as e:
        print(f"Failed to load model on startup: {e}")

@app.get("/")
def home():
    return {"message": "Plant Nutrient Deficiency Detector API is running"}

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    if not model_loader.model:
        return {"error": "Model not loaded"}, 500
    
    contents = await file.read()
    image_stream = io.BytesIO(contents)
    
    try:
        prediction = model_loader.predict(image_stream)
        predicted_class = prediction["class"]
        remedies = get_remedy(predicted_class)
        
        return {
            "deficiency": predicted_class,
            "confidence": prediction["confidence"],
            "organic_remedy": remedies
        }
    except Exception as e:
        return {"error": str(e)}, 500

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
