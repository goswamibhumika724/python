#findout python package to convert english text into gujarati text and use it 

import asyncio
from googletrans import Translator

async def main():
    translator = Translator()
    
    text = "Hello, how are you?"
    translated = await translator.translate(text, dest='gu')
    
    print("Original:", text)
    print("Gujarati:", translated.text)

asyncio.run(main())