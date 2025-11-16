# ml/model.py

"""
This file represents our ML model loader.
Right now it is a placeholder.
In Module 6 we will replace this with a real anomaly detection model.
"""

import time

class DummyFirmwareModel:
    def __init__(self):
        # Simulate "loading" a real ML model
        print("Loading Dummy Firmware ML Model...")
        time.sleep(1)
        print("Model loaded successfully.")

    def predict(self, features: dict):
        """
        Fake prediction logic.
        A real model would take numerical features and return probabilities.
        """
        # Completely fake — returns anomaly=True when passed value > 0.8
        score = features.get("firmware_entropy", 0)

        return {
            "anomaly": score > 0.8,
            "score": float(score)
        }


# GLOBAL SINGLETON — loads once at startup
model_instance = DummyFirmwareModel()