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
                "setting": {
                    "type": "string",
                    "description": "The place where the subject should be drawn (e.g, lake, street or building)"
                },
                "action": {
                    "type": "string",
                    "description": "An action word that describes what subject is doing (e.g., swim, run)"
                }
            },
            "required": ["adjectives", "subject"]
        }
    }


def generate_image_prompt(arguments, message):
    prompt = f"Generate a picture about {arguments.get('subject')}. The prompt is {message}"
    # if arguments.get('adjectives'):
    #     prompt += f"Adjectives about {arguments.get('subject')} are as follows: {arguments.get('adjectives')}."
    # if arguments.get('setting'):
    #     prompt += f"The place where {arguments.get('subject')} is located is the {arguments.get('setting')}."
    # if arguments.get('action'):
    #     prompt += f"The actions the {arguments.get('subject')} is performing are as follows: {arguments.get('action')}."
    prompt += 'Make it more vivid based on your understanding.'
    return prompt
