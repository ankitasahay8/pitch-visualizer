import google.generativeai as genai

genai.configure(api_key="AIzaSyBLqyav7q6q2vZZGHNvdivSDj-GTmmXUWM")

model = genai.GenerativeModel("gemini-pro")

def generate_prompt(scene):

    instruction = f"""
    Convert the following sentence into a detailed cinematic prompt
    suitable for AI image generation.

    Sentence: {scene}
    """

    try:
        response = model.generate_content(instruction)
        return response.text.strip()

    except:
        return f"{scene}, cinematic lighting, detailed environment, concept art"