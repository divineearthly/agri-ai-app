# 🌿 Agri-AI App: Precision Agriculture Powered by Vedic Logic

## Overview
An AI-driven application for intelligent precision agriculture and crop management. The system integrates traditional soil science with high-performance Vedic-Quantum mathematical kernels.

## 🚀 Key Features
- **Soil Health Diagnostics**: Real-time NPK analysis via `AgriEngine`.
- **Vedic Optimization**: Non-linear scaling of nutrient equilibrium using the `Ekadhikena Purvena` sutra.
- **Intelligent Recommendations**: Multi-parameter crop selection factoring in pH, Humidity, and NPK stability scores.

## 🏗 Architecture
- `src/crop_engine.py`: Core diagnostic logic.
- `src/vedic_agri_bridge.py`: High-performance bridge to the C++ Vedic Engine.
- `src/crop_recommendation.py`: Hardened logic for environmental validation.

## 🛠 Installation
```bash
pip install -r requirements.txt
```

## 🧪 Usage
```python
from src.crop_recommendation import CropRecommender
recommender = CropRecommender()
result = recommender.recommend(n=70, p=75, k=80, ph=6.8, humidity=60)
print(result)
```
