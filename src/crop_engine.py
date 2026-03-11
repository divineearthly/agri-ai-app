import numpy as np

class AgriEngine:
    def __init__(self):
        self.crop_registry = ['Rice', 'Wheat', 'Maize']

    def analyze_soil_health(self, n, p, k, ph, humidity):
        # Composite diagnostic logic
        npk_score = (n + p + k) / 3.0
        # Ideal pH is roughly 6.5; calculate variance
        ph_stability = 100 - abs(ph - 6.5) * 10
        
        status = 'Optimal' if (npk_score > 50 and ph_stability > 70) else 'Action Required'
        
        return {
            'npk_score': npk_score,
            'ph_stability': ph_stability,
            'humidity': humidity,
            'status': status
        }
