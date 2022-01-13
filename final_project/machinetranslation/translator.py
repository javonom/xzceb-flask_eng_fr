import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
authenticator = IAMAuthenticator('lj4w9TGprEN5L0Ho0WpKJDvUB-gvZ_k0H40T1LyMnSsJ')
language_tranlator = LanguageTranslatorV3(
    version = '2018-05-01',
    authenticator = authenticator
)

language_tranlator.set_service_url('https://api.us-south.language-translator.watson.cloud.ibm.com/instances/e6dd6427-fccc-40ae-bc58-440358c72717')

def english_to_french(english_text):
    translation = language_tranlator.translate(text=english_text,model_id="en-fr").get_result()
    french_text = translation['translations'][0]['translation']
    return french_text

def french_to_english(french_text):
    translation = language_tranlator.translate(text=french_text, model_id="fr-en").get_result()
    english_text = translation['translations'][0]['translation']
    return english_text

