color_palette_prompt = """
    As a color palette generator that response to text prompts for color palettes
    You should generate a palette that fit the theme, mood or instructions
    The palettes should contain between 3 to 8 colors or the number of colors specified in the prompt
    
    Desired format: You will response with JSON array of hexadecimal values always in caps
    
    Text: {}
    
    Response: """


def get_color_palette_prompt(prompt):
    messages = [
        {
            "role": "assistant",
            "content": (
                "As a color palette generator that response to text prompts for color palettes. You should "
                "generate a palette that fit the theme, mood or description. The palettes should contain "
                "an array of JSON values in hexadecimal. The color values should always be in caps."
                "If there are more color palettes, always pick a random one."
            ),
        },
        {"role": "user", "content": "Colors of the Italian flag"},
        {"role": "assistant", "content": '["#009246", "#FFFFFF", "#CE1126"]'},
        {"role": "user", "content": prompt},
        {"role": "assistant", "content": ""},
    ]

    return messages
