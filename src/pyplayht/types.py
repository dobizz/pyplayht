from dataclasses import dataclass, field
from typing import List


@dataclass(frozen=True)
class OutputFormat:
    MP3 = "mp3"
    WAV = "wav"
    OGG = "ogg"
    FLAC = "flac"
    MULAW = "mulaw"


@dataclass(frozen=True)
class OutputQuality:
    DRAFT = "draft"
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    PREMIUM = "premium"


@dataclass(frozen=True)
class GenerateStatus:
    GENERATING = "generating"
    COMPLETED = "completed"
    ERROR = "error"


@dataclass
class VoiceType:
    value: str
    name: str
    language: str
    voiceType: str
    languageCode: str
    gender: str
    service: str
    sample: str
    isKid: bool = False
    isNew: bool = False
    styles: List[str] = field(default_factory=list)
