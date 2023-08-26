import openai

# Set your OpenAI API key
openai.api_key = "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"

def generate_image_from_prompt(prompt):
    response = openai.Image.create(
        model="image-alpha-001",
        prompt=prompt,
        n=1  # Number of images to generate
    )

    image_url = response['data'][0]['url']
    return image_url
