import os
from typing import List, Union
from urllib.parse import urlencode, urljoin

import requests

from pyplayht.types import VoiceType


class Client:
    base_url: str = "https://api.play.ht/"

    def __init__(self) -> None:
        self.session = requests.Session()
        # Set default headers for the session
        headers = {
            "AUTHORIZATION": os.getenv("PLAY_HT_API_KEY"),
            "X-USER-ID": os.getenv("PLAY_HT_USER_ID"),
            "accept": "application/json",
            "content-type": "application/json",
        }
        self.session.headers.update(headers)
        self._voices = []

    @property
    def voices(self) -> List[VoiceType]:
        return self._voices if self._voices else self.get_voices()

    def get_voices(self) -> List[VoiceType]:
        path = "/api/v1/getVoices"
        url = urljoin(self.base_url, path)
        response = self.session.get(url)
        response.raise_for_status()
        voices = response.json().get("voices")
        voices = [VoiceType(**voice) for voice in voices]
        self._voices = voices
        return voices

    def new_conversion_job(
        self,
        text: Union[str, List[str]],
        voice: str = "en-US-JennyNeural",
    ) -> dict:
        path = "/api/v1/convert"
        url = urljoin(self.base_url, path)
        content = text if isinstance(text, list) else [text]
        payload = {
            "content": content,
            "voice": voice,
        }
        response = self.session.post(url, json=payload)
        response.raise_for_status()
        return response.json()

    def get_coversion_job_status(self, transcription_id: str) -> dict:
        path = "/api/v1/articleStatus"
        params = {"transcriptionId": transcription_id}
        url = urljoin(self.base_url, path)
        url = urljoin(url, "?" + urlencode(params))
        response = self.session.get(url)
        response.raise_for_status()
        return response.json()

    def download_file(self, uri: str):
        response = self.session.get(uri)
        response.raise_for_status()
        return response.content
