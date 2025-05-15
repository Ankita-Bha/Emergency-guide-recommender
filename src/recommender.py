import pandas as pd

def analyze_risks(user_data):
    """Predicts possible emergency risks based on user profile."""
    risks = []

    if "outdoor sports" in user_data["hobbies"].lower():
        risks.append("High risk of falls & fractures.")
    if "hypertension" in user_data["parent_medical_history"].lower():
        risks.append("Higher risk of strokes.")

    return risks
