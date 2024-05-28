def convert_contents(messages):
    contents = []
    if isinstance(messages, str):
        contents.append(messages)
    elif isinstance(messages, list):
        for item in messages:
            content = item.get('content')
            val = {
                "role": item.get('role', 'user'),
                "parts": []
            }
            if isinstance(content, str):
                val['parts'].append(
                    {
                        "text": item.get('content')
                    }
                )
            elif isinstance(content, dict):
                if content.get('type') == 'text':
                    val['parts'].append(
                        {
                            "text": content.get('text')
                        }
                    )
                elif content.get('type') == 'image':
                    image_data = str(content.get('image'))
                    if 'base64,' in image_data:
                        image_data = image_data.split('base64,')[-1]
                    val['parts'].append(
                        {
                            "inline_data": {
                                "mime_type": "image/jpeg",
                                "data": image_data
                            }
                        }
                    )
            contents.append(val)
    return contents
