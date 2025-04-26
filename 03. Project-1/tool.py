'''PyCODE | @_py.code'''
from googletrans import Translator
import asyncio
import threading

# Create thread-local storage for event loops
local = threading.local()

def get_event_loop():
    try:
        return local.loop
    except AttributeError:
        local.loop = asyncio.new_event_loop()
        return local.loop

def translate(text: str, from_: str = 'en', to: str = 'hi'):
    loop = get_event_loop()
    asyncio.set_event_loop(loop)
    
    translator = Translator()
    translated = loop.run_until_complete(
        translator.translate(text, src=from_, dest=to)
    )
    
    class TranslationResult:
        def __init__(self, text, pronunciation):
            self.output = text
            self.pronunciation = pronunciation
    
    return TranslationResult(translated.text, translated.pronunciation)