def extract_image_generation_keywords():
    return {
        "name": "extract_image_generation_keywords",
        "description": "The function examines the input text for keywords and phrases that suggest a desire to draw, "
                       "such as 'draw', 'sketch', 'paint' or descriptions of visual scenes or objects. "
                       "If drawing intent is detected, the function identifies and extracts keywords that provide "
                       "information about the desired drawing",
        "parameters": {
            "type": "object",
            "properties": {
                "adjectives": {
                    "type": "string",
                    "description": "Descriptive words that specify the characteristics of the subject or the overall "
                                   "style of the drawing (e.g., colorful, realistic, abstract)"
                },
                "subject": {
                    "type": "string",
                    "description": "The main object or scene to be drawn (e.g., cat, landscape, portrait)"
                },
            },
            "required": ["adjectives", "subject"]
        }
    }
