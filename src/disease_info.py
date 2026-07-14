"""
disease_info.py
----------------
Static reference data for all 38 PlantVillage classes, plus the
confidence-based decision logic (get_result) that app.py uses to decide
whether a prediction is reliable enough to show as a diagnosis.

CONFIDENCE_THRESHOLD is the "soft" threshold: predictions above this
are shown as a full diagnosis; predictions below it (but still above
predict.py's HARD_REJECT_THRESHOLD) are shown as "not confident enough"
along with the top guesses, rather than a hard refusal.

If you're still seeing real leaf photos rejected after fixing
predict.py's model.eval() / preprocessing, try lowering this value
(e.g. to 50) — a plain softmax-threshold approach is inherently rougher
than a purpose-trained "is this a leaf" classifier, so it sometimes
needs tuning down for photos that differ from the training set
(different lighting, phone camera compression, cluttered background).
"""

CONFIDENCE_THRESHOLD = 60.0  # percent

# ---------------------------------------------------------------------------
# Crop display names / emoji
# ---------------------------------------------------------------------------
_CROP_DISPLAY = {
    "Apple": ("Apple", "🍎"),
    "Blueberry": ("Blueberry", "🫐"),
    "Cherry_(including_sour)": ("Cherry", "🍒"),
    "Corn_(maize)": ("Corn", "🌽"),
    "Grape": ("Grape", "🍇"),
    "Orange": ("Orange", "🍊"),
    "Peach": ("Peach", "🍑"),
    "Pepper,_bell": ("Bell Pepper", "🌶"),
    "Potato": ("Potato", "🥔"),
    "Raspberry": ("Raspberry", "🍇"),
    "Soybean": ("Soybean", "🌱"),
    "Squash": ("Squash", "🎃"),
    "Strawberry": ("Strawberry", "🍓"),
    "Tomato": ("Tomato", "🍅"),
}

SUPPORTED_CROPS = list(_CROP_DISPLAY.keys())


def get_crop_display(crop_key):
    """Return (display_name, emoji) for a raw crop key."""
    return _CROP_DISPLAY.get(crop_key, (crop_key.replace("_", " "), "🌿"))


def _display_disease(raw_disease):
    return raw_disease.replace("_", " ").replace("  ", " ").strip()


_GENERIC_SUGGESTIONS = [
    "Fill the frame with a single leaf, shot in good, even daylight.",
    "Avoid backgrounds like hands, tables, or other objects.",
    "Hold the camera steady and let it focus before capturing.",
]

_GENERIC_PREVENTION_FUNGAL = [
    "Avoid overhead watering; water at the base of the plant.",
    "Ensure good airflow and spacing between plants.",
    "Remove and destroy fallen or infected leaves promptly.",
]

_GENERIC_PREVENTION_BACTERIAL = [
    "Use certified disease-free seeds/seedlings.",
    "Avoid working with plants when foliage is wet.",
    "Rotate crops and sanitize tools between plants.",
]

_GENERIC_PREVENTION_VIRAL = [
    "Control insect vectors (aphids, whiteflies) that spread the virus.",
    "Remove and destroy infected plants to limit spread.",
    "Use resistant varieties where available.",
]


def _entry(crop, disease, status, description, symptoms, treatment, prevention):
    return {
        "crop": crop,
        "display_name": _display_disease(disease) if status != "Healthy" else "Healthy",
        "status": status,
        "description": description,
        "symptoms": symptoms,
        "treatment": treatment,
        "prevention": prevention,
        "suggestion": _GENERIC_SUGGESTIONS,
    }


def _healthy(crop):
    crop_name = get_crop_display(crop)[0]
    return _entry(
        crop,
        "healthy",
        "Healthy",
        f"This {crop_name.lower()} leaf shows no visible signs of disease.",
        ["Uniform green color", "No spots, lesions, or discoloration", "No wilting or curling"],
        ["No treatment needed — keep up good plant care."],
        ["Continue regular watering, fertilization, and pest monitoring."],
    )


# ---------------------------------------------------------------------------
# Full disease information, keyed EXACTLY as "Crop___Disease" (matches the
# class names produced by ImageFolder / used in top_predictions).
# ---------------------------------------------------------------------------
disease_information = {
    "Apple___Apple_scab": _entry(
        "Apple", "Apple_scab", "Diseased",
        "A fungal disease causing dark, scabby lesions on leaves and fruit.",
        ["Olive-green to brown velvety spots on leaves", "Distorted or cracked fruit", "Premature leaf drop"],
        ["Apply fungicide (e.g. captan or myclobutanil) per label instructions", "Remove and destroy fallen leaves in autumn"],
        _GENERIC_PREVENTION_FUNGAL,
    ),
    "Apple___Black_rot": _entry(
        "Apple", "Black_rot", "Diseased",
        "A fungal disease causing leaf spots and fruit rot in apples.",
        ["Purple-bordered brown leaf spots ('frog-eye')", "Rotting, mummified fruit", "Cankers on branches"],
        ["Prune out cankers and dead wood", "Apply fungicide during the growing season"],
        _GENERIC_PREVENTION_FUNGAL,
    ),
    "Apple___Cedar_apple_rust": _entry(
        "Apple", "Cedar_apple_rust", "Diseased",
        "A fungal disease requiring both apple and cedar trees to complete its cycle.",
        ["Bright orange-yellow spots on leaves", "Tube-like structures on leaf undersides", "Early leaf drop"],
        ["Apply fungicide starting at bud break", "Remove nearby cedar/juniper hosts if practical"],
        _GENERIC_PREVENTION_FUNGAL,
    ),
    "Apple___healthy": _healthy("Apple"),
    "Blueberry___healthy": _healthy("Blueberry"),
    "Cherry_(including_sour)___Powdery_mildew": _entry(
        "Cherry_(including_sour)", "Powdery_mildew", "Diseased",
        "A fungal disease producing a white powdery coating on leaves.",
        ["White powdery patches on leaf surfaces", "Curled or distorted young leaves", "Stunted shoot growth"],
        ["Apply sulfur or potassium bicarbonate fungicide", "Prune to improve air circulation"],
        _GENERIC_PREVENTION_FUNGAL,
    ),
    "Cherry_(including_sour)___healthy": _healthy("Cherry_(including_sour)"),
    "Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot": _entry(
        "Corn_(maize)", "Cercospora_leaf_spot Gray_leaf_spot", "Diseased",
        "A fungal disease causing rectangular gray-brown lesions on corn leaves.",
        ["Rectangular tan-to-gray lesions running parallel to veins", "Lesions merging on severely affected leaves"],
        ["Apply foliar fungicide if severe", "Rotate with non-host crops"],
        _GENERIC_PREVENTION_FUNGAL,
    ),
    "Corn_(maize)___Common_rust_": _entry(
        "Corn_(maize)", "Common_rust", "Diseased",
        "A fungal disease producing reddish-brown rust pustules on corn leaves.",
        ["Small, cinnamon-brown pustules on both leaf surfaces", "Pustules rupture, releasing rust-colored spores"],
        ["Apply fungicide if infection is early and severe", "Plant rust-resistant hybrids"],
        _GENERIC_PREVENTION_FUNGAL,
    ),
    "Corn_(maize)___Northern_Leaf_Blight": _entry(
        "Corn_(maize)", "Northern_Leaf_Blight", "Diseased",
        "A fungal disease causing long, cigar-shaped gray-green lesions.",
        ["Long elliptical gray-green to tan lesions", "Lesions expand and merge, blighting the leaf"],
        ["Apply fungicide at early signs", "Use resistant hybrids and rotate crops"],
        _GENERIC_PREVENTION_FUNGAL,
    ),
    "Corn_(maize)___healthy": _healthy("Corn_(maize)"),
    "Grape___Black_rot": _entry(
        "Grape", "Black_rot", "Diseased",
        "A fungal disease causing leaf spots and shriveled, mummified fruit.",
        ["Brown circular leaf spots with dark borders", "Fruit shrivels into hard black 'mummies'"],
        ["Apply fungicide from bud break through veraison", "Remove mummified fruit and infected debris"],
        _GENERIC_PREVENTION_FUNGAL,
    ),
    "Grape___Esca_(Black_Measles)": _entry(
        "Grape", "Esca_(Black_Measles)", "Diseased",
        "A fungal trunk disease causing striped leaf discoloration and berry spotting.",
        ["'Tiger-stripe' yellow/brown streaking between leaf veins", "Dark spots on berries", "Sudden shoot dieback"],
        ["No full cure; remove and destroy severely affected vines", "Protect pruning wounds"],
        _GENERIC_PREVENTION_FUNGAL,
    ),
    "Grape___Leaf_blight_(Isariopsis_Leaf_Spot)": _entry(
        "Grape", "Leaf_blight_(Isariopsis_Leaf_Spot)", "Diseased",
        "A fungal disease causing angular brown leaf spots.",
        ["Small angular reddish-brown spots", "Spots merge, causing leaf browning and drop"],
        ["Apply fungicide during humid periods", "Remove infected leaves"],
        _GENERIC_PREVENTION_FUNGAL,
    ),
    "Grape___healthy": _healthy("Grape"),
    "Orange___Haunglongbing_(Citrus_greening)": _entry(
        "Orange", "Haunglongbing_(Citrus_greening)", "Diseased",
        "A serious bacterial disease spread by psyllid insects, with no cure.",
        ["Blotchy, asymmetric yellow mottling on leaves", "Lopsided, bitter, partially green fruit", "Twig dieback"],
        ["No cure — remove and destroy infected trees to protect nearby trees", "Control the Asian citrus psyllid vector"],
        _GENERIC_PREVENTION_BACTERIAL,
    ),
    "Peach___Bacterial_spot": _entry(
        "Peach", "Bacterial_spot", "Diseased",
        "A bacterial disease causing spots on leaves and fruit.",
        ["Small angular water-soaked spots that turn purple/brown", "Spots may fall out, leaving a 'shot-hole' look", "Sunken fruit lesions"],
        ["Apply copper-based bactericide", "Avoid overhead irrigation"],
        _GENERIC_PREVENTION_BACTERIAL,
    ),
    "Peach___healthy": _healthy("Peach"),
    "Pepper,_bell___Bacterial_spot": _entry(
        "Pepper,_bell", "Bacterial_spot", "Diseased",
        "A bacterial disease causing dark, scabby spots on leaves and fruit.",
        ["Small water-soaked spots turning brown/black", "Spots with yellow halo", "Fruit lesions with raised, scabby texture"],
        ["Apply copper-based bactericide early", "Avoid working in wet fields"],
        _GENERIC_PREVENTION_BACTERIAL,
    ),
    "Pepper,_bell___healthy": _healthy("Pepper,_bell"),
    "Potato___Early_blight": _entry(
        "Potato", "Early_blight", "Diseased",
        "A fungal disease causing target-like spots on lower leaves.",
        ["Dark brown spots with concentric rings ('target spot')", "Yellowing around lesions", "Lower/older leaves affected first"],
        ["Apply fungicide (chlorothalonil or similar)", "Remove infected lower leaves"],
        _GENERIC_PREVENTION_FUNGAL,
    ),
    "Potato___Late_blight": _entry(
        "Potato", "Late_blight", "Diseased",
        "An aggressive fungal-like disease that can destroy a crop within days.",
        ["Water-soaked gray-green lesions that turn brown/black rapidly", "White fungal growth on leaf undersides in humid weather", "Foul-smelling tuber rot"],
        ["Apply fungicide preventively in humid conditions", "Remove and destroy infected plants immediately"],
        _GENERIC_PREVENTION_FUNGAL,
    ),
    "Potato___healthy": _healthy("Potato"),
    "Raspberry___healthy": _healthy("Raspberry"),
    "Soybean___healthy": _healthy("Soybean"),
    "Squash___Powdery_mildew": _entry(
        "Squash", "Powdery_mildew", "Diseased",
        "A fungal disease producing a white powdery coating on leaves.",
        ["White powdery spots on upper leaf surfaces", "Leaves yellow and become brittle", "Reduced fruit yield/quality"],
        ["Apply sulfur or potassium bicarbonate fungicide", "Remove severely affected leaves"],
        _GENERIC_PREVENTION_FUNGAL,
    ),
    "Strawberry___Leaf_scorch": _entry(
        "Strawberry", "Leaf_scorch", "Diseased",
        "A fungal disease causing purplish spots that merge into scorched-looking patches.",
        ["Small purple spots that enlarge and merge", "Leaves appear scorched/dried at the edges", "Reduced plant vigor"],
        ["Apply fungicide in early spring", "Remove old/infected leaves after harvest"],
        _GENERIC_PREVENTION_FUNGAL,
    ),
    "Strawberry___healthy": _healthy("Strawberry"),
    "Tomato___Bacterial_spot": _entry(
        "Tomato", "Bacterial_spot", "Diseased",
        "A bacterial disease causing small dark spots on leaves and fruit.",
        ["Small, water-soaked, greasy-looking spots", "Spots turn dark brown with yellow halo", "Scabby raised spots on fruit"],
        ["Apply copper-based bactericide", "Avoid overhead watering and working with wet plants"],
        _GENERIC_PREVENTION_BACTERIAL,
    ),
    "Tomato___Early_blight": _entry(
        "Tomato", "Early_blight", "Diseased",
        "A fungal disease causing target-like spots, usually starting on older leaves.",
        ["Brown spots with concentric rings ('target spot')", "Yellowing around lesions", "Lower leaves affected first, progressing upward"],
        ["Apply fungicide (chlorothalonil or copper-based)", "Remove and destroy infected lower leaves"],
        _GENERIC_PREVENTION_FUNGAL,
    ),
    "Tomato___Late_blight": _entry(
        "Tomato", "Late_blight", "Diseased",
        "An aggressive, fast-spreading disease that can destroy plants within days.",
        ["Large water-soaked gray-green blotches", "White fuzzy growth on leaf undersides in humid weather", "Rapid collapse of foliage and fruit rot"],
        ["Apply fungicide preventively in cool, wet weather", "Remove and destroy infected plants immediately"],
        _GENERIC_PREVENTION_FUNGAL,
    ),
    "Tomato___Leaf_Mold": _entry(
        "Tomato", "Leaf_Mold", "Diseased",
        "A fungal disease favored by high humidity, common in greenhouses.",
        ["Pale green/yellow spots on upper leaf surface", "Olive-green to brown velvety mold on leaf undersides", "Leaves curl and die"],
        ["Improve ventilation to lower humidity", "Apply fungicide if conditions stay humid"],
        _GENERIC_PREVENTION_FUNGAL,
    ),
    "Tomato___Septoria_leaf_spot": _entry(
        "Tomato", "Septoria_leaf_spot", "Diseased",
        "A fungal disease causing many small, circular spots on leaves.",
        ["Small circular spots with dark borders and gray centers", "Tiny black specks (fungal fruiting bodies) in spot centers", "Progressive lower-leaf yellowing and drop"],
        ["Apply fungicide at first sign of spots", "Remove infected lower leaves and debris"],
        _GENERIC_PREVENTION_FUNGAL,
    ),
    "Tomato___Spider_mites Two-spotted_spider_mite": _entry(
        "Tomato", "Spider_mites Two-spotted_spider_mite", "Diseased",
        "Damage caused by tiny sap-sucking spider mites rather than a pathogen.",
        ["Fine yellow stippling/speckling on leaves", "Fine webbing on leaf undersides", "Leaves turn bronze/gray and dry out"],
        ["Apply miticide or insecticidal soap", "Increase humidity; mites thrive in hot, dry conditions"],
        ["Avoid drought stress on plants", "Introduce natural predators (e.g. predatory mites)", "Regularly hose down leaf undersides to dislodge mites"],
    ),
    "Tomato___Target_Spot": _entry(
        "Tomato", "Target_Spot", "Diseased",
        "A fungal disease producing target-like concentric ring spots.",
        ["Brown spots with concentric rings, similar to early blight", "Spots on leaves, stems, and fruit", "Lesions may coalesce, causing defoliation"],
        ["Apply fungicide at early signs", "Improve air circulation and remove infected debris"],
        _GENERIC_PREVENTION_FUNGAL,
    ),
    "Tomato___Tomato_Yellow_Leaf_Curl_Virus": _entry(
        "Tomato", "Tomato_Yellow_Leaf_Curl_Virus", "Diseased",
        "A viral disease spread by whiteflies, causing severe stunting.",
        ["Upward curling, yellowing leaves", "Stunted plant growth", "Significantly reduced fruit set"],
        ["No cure — remove and destroy infected plants", "Control whitefly populations with insecticide/traps"],
        _GENERIC_PREVENTION_VIRAL,
    ),
    "Tomato___Tomato_mosaic_virus": _entry(
        "Tomato", "Tomato_mosaic_virus", "Diseased",
        "A viral disease causing mottled, mosaic-patterned leaves.",
        ["Light/dark green mosaic mottling on leaves", "Leaf curling and distortion", "Stunted growth and reduced yield"],
        ["No cure — remove and destroy infected plants", "Disinfect tools and hands between plants"],
        _GENERIC_PREVENTION_VIRAL,
    ),
    "Tomato___healthy": _healthy("Tomato"),
}


def get_result(raw_label, confidence):
    """
    Decide whether a prediction is reliable enough to show as a full
    diagnosis, based on CONFIDENCE_THRESHOLD.

    Returns
    -------
    dict with:
        accepted (bool): True if confidence >= CONFIDENCE_THRESHOLD
        info (dict): the disease_information entry for raw_label
        crop_display (tuple): (display_name, emoji) for the crop
    """
    info = disease_information.get(raw_label)

    if info is None:
        # Label not found in our reference data (shouldn't normally
        # happen if predict.py's class list matches this file's keys).
        return {
            "accepted": False,
            "info": {
                "display_name": "Unrecognized class",
                "suggestion": _GENERIC_SUGGESTIONS,
            },
            "crop_display": ("Unknown", "🌿"),
        }

    accepted = confidence >= CONFIDENCE_THRESHOLD
    crop_display = get_crop_display(info["crop"])

    return {
        "accepted": accepted,
        "info": info,
        "crop_display": crop_display,
    }