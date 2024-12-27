# generated by datamodel-codegen:
#   filename:  https://publishing.c3voc.de/openapi.json
#   timestamp: 2024-11-14T20:15:24+00:00

from __future__ import annotations

from typing import Any, Dict, List, Optional, Union

from pydantic import BaseModel, Field


class BodyCreateOrUpdateFileApiConferenceEventsGuidFilePut(BaseModel):
    file: bytes = Field(..., title='File')
    meta: str = Field(..., title='Meta')


class BodyRecordingsApiRecordingsPost(BaseModel):
    payload: Dict[str, Any] = Field(..., title='Payload')


class Recording(BaseModel):
    filename: str = Field(..., title='Filename')
    mime_type: str = Field(..., title='Mime Type')
    language: str = Field(..., title='Language')
    folder: Optional[str] = Field(..., title='Folder')
    size: Optional[int] = Field(..., title='Size')
    length: Optional[int] = Field(..., title='Length')
    state: Optional[str] = Field(..., title='State')
    high_quality: bool = Field(..., title='High Quality')
    width: Optional[int] = Field(..., title='Width')
    height: Optional[int] = Field(..., title='Height')
    updated_at: str = Field(..., title='Updated At')
    recording_url: str = Field(..., title='Recording Url')


class ValidationError(BaseModel):
    loc: List[Union[str, int]] = Field(..., title='Location')
    msg: str = Field(..., title='Message')
    type: str = Field(..., title='Error Type')


class Video(BaseModel):
    filename: str = Field(..., title='Filename')


class DetailedEvent(BaseModel):
    guid: str = Field(..., title='Guid')
    slug: str = Field(..., title='Slug')
    title: str = Field(..., title='Title')
    date: str = Field(..., title='Date')
    subtitle: Optional[str] = Field(..., title='Subtitle')
    link: str = Field(..., title='Link')
    description: str = Field(..., title='Description')
    original_language: str = Field(..., title='Original Language')
    persons: List[str] = Field(..., title='Persons')
    tags: List[str] = Field(..., title='Tags')
    view_count: int = Field(..., title='View Count')
    promoted: bool = Field(..., title='Promoted')
    release_date: str = Field(..., title='Release Date')
    updated_at: str = Field(..., title='Updated At')
    length: int = Field(..., title='Length')
    duration: int = Field(..., title='Duration')
    thumb_url: str = Field(..., title='Thumb Url')
    poster_url: str = Field(..., title='Poster Url')
    timeline_url: str = Field(..., title='Timeline Url')
    thumbnails_url: str = Field(..., title='Thumbnails Url')
    frontend_link: str = Field(..., title='Frontend Link')
    url: str = Field(..., title='Url')
    related: List[str] = Field(..., title='Related')
    recordings: List[Recording] = Field(..., title='Recordings')


class EventSummary(BaseModel):
    guid: str = Field(..., title='Guid')
    slug: str = Field(..., title='Slug')
    title: str = Field(..., title='Title')
    date: str = Field(..., title='Date')
    video: Video


class HTTPValidationError(BaseModel):
    detail: Optional[List[ValidationError]] = Field(None, title='Detail')


class Conference(BaseModel):
    id: str = Field(..., title='Id')
    title: str = Field(..., title='Title')
    events: List[EventSummary] = Field(..., title='Events')