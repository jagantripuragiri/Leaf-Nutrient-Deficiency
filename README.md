# 🌿 Plant Nutrient Deficiency Detector - Run Guide

Follow these steps in your terminal to run the project.

## Step 1: Backend Setup
Open your terminal and run the following commands:

```bash
cd "/Users/jagantripuragiri/Desktop/leaf Deficiency"
pip install -r backend/requirements.txt
```

## Step 2: Train the Model
You must train the model once before running the app.

```bash
python3.11 train_model.py
```
*Wait for the training to finish. It will create a `plant_disease_model.pt` file.*

## Step 3: Start the Backend Server
This needs to stay running.

```bash
python3.11 backend/main.py
```
*You will see: `Uvicorn running on http://0.0.0.0:8000`*

## Step 4: Start the Frontend (New Terminal)
Open a **new terminal tab/window** and run:

```bash
cd "/Users/jagantripuragiri/Desktop/leaf Deficiency/frontend"
npm install
npm run dev
```

## Step 5: Open App
Click the link shown in the terminal (usually **http://localhost:5173**) to open the app.
