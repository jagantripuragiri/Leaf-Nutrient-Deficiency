remedies = {
    "nitrogen-N": [
        "Apply composted manure.",
        "Use vermicompost.",
        "Plant nitrogen-fixing cover crops (green manure)."
    ],
    "phosphorus-P": [
        "Apply bone meal.",
        "Use rock phosphate.",
        "Add composted chicken manure."
    ],
    "potasium-K": [
        "Apply wood ash.",
        "Use banana peel compost.",
        "Add kelp meal or greensand."
    ],
    "magnesium-Mg": [
        "Spray diluted Epsom salts (1 tbsp per gallon of water).",
        "Apply dolomitic lime (adjusts pH too)."
    ],
    "calcium-Ca": [
        "Apply crushed eggshells.",
        "Use gypsum or garden lime.",
        "Ensure consistent watering."
    ],
    "iron-Fe": [
        "Apply chelated iron.",
        "Use compost tea.",
        "Lower soil pH with sulfur if too alkaline."
    ],
    "manganese-Mn": [
        "Apply manganese sulfate.",
        "Foliar spray with compost tea.",
        "Adjust soil pH (availability drops in high pH)."
    ],
    "boron-B": [
        "Apply borax (very carefully, small amounts).",
        "Use compost rich in organic matter."
    ],
    "healthy": [
        "Your plant looks healthy! Keep up the good work.",
        "Maintain regular watering and sunlight."
    ],
    "more-deficiencies": [
        "Consult a local agricultural expert.",
        "Ensure balanced fertilization with general organic compost."
    ]
}

def get_remedy(deficiency_class):
    """Returns a list of remedies for a given deficiency class."""
    return remedies.get(deficiency_class, ["No specific remedy found. Consult an expert."])
