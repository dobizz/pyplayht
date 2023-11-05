import os
from typing import List, Union
from urllib.parse import urljoin, urlparse, urlunparse

import requests
from retry import retry

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
        """
        Get list of available voices from server

        Returns:
            List[VoiceType]: list of available voice types
        """
        path = "/api/v1/getVoices"
        response = self._request("GET", path)
        voices = response.json().get("voices")
        voices = [VoiceType(**voice) for voice in voices]
        self._voices = voices
        return voices

    def new_conversion_job(
        self,
        text: Union[str, List[str]],
        voice: str = "en-US-JennyNeural",
    ) -> dict:
        """
        Create new transcription job

        Args:
            text (Union[str, List[str]]): text to transcribe
            voice (str, optional): voice model to use.
                Defaults to "en-US-JennyNeural".

        Returns:
            dict: new transcription job details
        """
        path = "/api/v1/convert"
        content = text if isinstance(text, list) else [text]
        payload = {
            "content": content,
            "voice": voice,
        }
        response = self._request("POST", path, json=payload)
        return response.json()

    def get_coversion_job_status(self, transcription_id: str) -> dict:
        """
        Check status of job specified by transcription_id

        Args:
            transcription_id (str): job to check

        Returns:
            dict: status of specified job
        """
        path = "/api/v1/articleStatus"
        params = {"transcriptionId": transcription_id}
        response = self._request("GET", path, params=params)
        return response.json()

    def download_file(self, uri: str) -> bytes:
        """
        Download bytes of given file

        Args:
            uri (str): location of file

        Returns:
            bytes: byte data of file
        """
        parsed_url = urlparse(uri)
        # Create a new URL without the query string
        new_url = urlunparse(
            (
                parsed_url.scheme,
                parsed_url.netloc,
                parsed_url.path,
                "",
                "",
                "",
            ),
        )
        response = self._request("GET", new_url)
        return response.content

    @retry(tries=3, delay=5, backoff=2)
    def _request(
        self,
        method: str,
        path: str,
        params: dict = None,
        json: dict = None,
        stream: bool = False,
        timeout: int = 30,
    ) -> requests.Response:
        url = urljoin(self.base_url, path)
        if urlparse(path).scheme:
            url = path
        response = self.session.request(
            method=method,
            url=url,
            params=params,
            json=json,
            stream=stream,
            timeout=timeout,
        )
        response.raise_for_status()
        return response
