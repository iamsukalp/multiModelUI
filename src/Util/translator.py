from openai import OpenAI
import streamlit as st

# openai.api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])


def translate_text(input_text, output_language):
    """
    Translates the input text to the specified output language using ChatGPT 3.5.

    Args:
    input_text (str): The text to be translated.
    output_language (str): The target language for translation.

    Returns:
    str: The translated text.
    """
    try:
        # Construct the prompt for the ChatGPT model
        prompt = f"Translate the following text to {output_language}:\n\n{input_text}\n\nTranslation:"

        # Make the API call to ChatGPT
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant that translates text accurately.",
                },
                {"role": "user", "content": prompt},
            ],
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.7,
        )

        # Extract the translated text from the response
        translated_text = response.choices[0].message.content.strip()

        return translated_text

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None


# Example usage
if __name__ == "__main__":
    input_text = "Hello, how are you?"
    output_language = "French"

    translated = translate_text(input_text, output_language)

    if translated:
        print(f"Original: {input_text}")
        print(f"Translated to {output_language}: {translated}")
    else:
        print("Translation failed.")
