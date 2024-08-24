from gtts import gTTS
import pygame

Egnlish = "Hey, Sir How are You? and How can i help you?" # use en for english
Urdu = "ارے جناب کیسے ہیں آپ؟ اور میں آپ کی مدد کیسے کر سکتا ہوں؟" # use ur for urdu
Hindi = "अरे, सर आप कैसे हैं? और मैं आपकी कैसे मदद कर सकता हूँ?" #use hi for hindi
Punjabi = "ਹੇ, ਸਰ, ਤੁਸੀਂ ਕਿਵੇਂ ਹੋ? ਅਤੇ ਮੈਂ ਤੁਹਾਡੀ ਕਿਵੇਂ ਮਦਦ ਕਰ ਸਕਦਾ ਹਾਂ?" # use pa for punjabi

text = "Hey, This is GTTS module from python"
Language = "en"

speech = gTTS(text, lang=Language)
speech.save("Audio.mp3")

pygame.init()
pygame.mixer.music.load("Audio.mp3")
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick()