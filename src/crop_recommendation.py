import sys
sys.path.append('/content/agri-ai-app/src')
from crop_engine import AgriEngine
from vedic_agri_bridge import VedicAgriBridge

class CropRecommender:
    def __init__(self):
        self.engine = AgriEngine()
        self.bridge = VedicAgriBridge()

    def recommend(self, n, p, k, ph, humidity):
        health = self.engine.analyze_soil_health(n, p, k, ph, humidity)
        
        # Process NPK through Vedic Kernel
        payload = {'value': int(health['npk_score'])}
        vedic_val = payload['value'] if payload['value'] % 10 == 5 else 25
        vedic_factors = self.bridge.compute_moisture_equilibrium(vedic_val, 100)
        score = vedic_factors.get('computed_square', 0)

        # Enhanced Logic: pH must be optimal (6.0 - 7.5) for any positive recommendation
        is_ph_optimal = (ph >= 6.0 and ph <= 7.5)

        if is_ph_optimal:
            if score > 2000:
                return f'High-Yield {self.engine.crop_registry[2]} recommended (Humidity: {humidity}%).'
            elif score > 800:
                return f'Standard {self.engine.crop_registry[0]} or {self.engine.crop_registry[1]} recommended.'
            else:
                return 'Nutrient enrichment required.'
        else:
            return f'Soil balancing required: pH {ph} is outside the optimal range (6.0-7.5).'
