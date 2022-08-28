# AUTOGENERATED! DO NOT EDIT! File to edit: ../00_core.ipynb.

# %% auto 0
__all__ = ['YoutubeTimestamper']

# %% ../00_core.ipynb 4
from urllib.parse import urlparse, parse_qs
from contextlib import suppress

from youtube_transcript_api import YouTubeTranscriptApi
from deepmultilingualpunctuation import PunctuationModel
import spacy
from spacy.lang.en import English
from fastcore.all import *
import datetime
import re

# %% ../00_core.ipynb 6
class YoutubeTimestamper:
    """A class that extracts the transcript from a youtube video, identifies the questions in it and attaches timestamps to them."""

    punct_model = PunctuationModel()
    nlp = English()
    nlp.add_pipe("sentencizer")

    def __init__(self, video_url: str):  # A url of a YouTube Video
        store_attr()

    __repr__ = basic_repr("video_url")

# %% ../00_core.ipynb 8
@patch
def _get_yt_id(self: YoutubeTimestamper) -> None:
    """Extracts the id from the url"""
    query = urlparse(self.video_url)
    if query.hostname == "youtu.be":
        return query.path[1:]
    if query.hostname in {"www.youtube.com", "youtube.com", "music.youtube.com"}:
        with suppress(KeyError):
            return parse_qs(query.query)["list"][0]
        if query.path == "/watch":
            return parse_qs(query.query)["v"][0]
        if query.path[:7] == "/watch/":
            return query.path.split("/")[1]
        if query.path[:7] == "/embed/":
            return query.path.split("/")[2]
        if query.path[:3] == "/v/":
            return query.path.split("/")[2]

# %% ../00_core.ipynb 12
@patch
def _get_transcript(self: YoutubeTimestamper) -> None:
    """Fetches the transcripts for the video using the `youtube_transcript_api` package and stores it in the `transcript` variable."""
    self._yt_transcript_api = YouTubeTranscriptApi()
    video_id = self._get_yt_id()
    self.transcript = self._yt_transcript_api.get_transcript(video_id)
    self._transcript_str = " ".join([ts["text"] for ts in self.transcript])

# %% ../00_core.ipynb 19
@patch
def _restore_punctuations(self: YoutubeTimestamper) -> None:
    """Punctuates the transcript string"""
    self._transcript_punct = YoutubeTimestamper.punct_model.restore_punctuation(
        self._transcript_str
    )

# %% ../00_core.ipynb 25
@patch
def _get_sentences(self: YoutubeTimestamper) -> None:
    """Parses the transcript into sentences using spacy's sentenciser"""
    transcript_parsed = YoutubeTimestamper.nlp(self._transcript_punct)
    self.transcript_sents = L(transcript_parsed.sents)

# %% ../00_core.ipynb 28
@patch
def _get_questions(
    self: YoutubeTimestamper,
    next_q_thresh: int = 15,  # The number of tokens within a question which if the next question is present, it'll be considered part of the same question
) -> None:
    """Gets a continuous block of question sentences"""
    questions = L("")
    prev_q_end = -90
    for sent in self.transcript_sents:
        if "?" in sent.text:
            if (sent.start - prev_q_end) <= next_q_thresh:
                questions[-1] += " " + sent.text
            else:
                questions.append(sent.text)
            prev_q_end = sent.end

    self.questions = L(q for q in questions if q.strip() != "")

# %% ../00_core.ipynb 31
@patch
def _get_timestamps_for_questions(
    self: YoutubeTimestamper,
) -> None:
    """Matches the questions with the timestamps"""
    timestamps = L([(0, "Introduction")])
    transcript_pieces = [t for t in self.transcript]
    for question in self.questions:
        question_nopunct = re.sub("[,.?!]", "", question)
        for ts in transcript_pieces:
            if (ts["text"] in question_nopunct) and (
                question_nopunct[10:20] in ts["text"]
            ):
                timestamps.append((ts["start"], question))
                # print((ts["start"], ts["text"], question))
                break
        transcript_pieces.remove(ts)
    self.timestamps = timestamps

# %% ../00_core.ipynb 35
@patch
def _render_timestamps(self: YoutubeTimestamper, limit=None) -> None:
    """Renders the timestamps in the right format"""
    render_ts = self.timestamps[:limit] if limit else self.timestamps
    for t in render_ts:
        timestamp = f"{datetime.timedelta(seconds=t[0])}"
        timestamp = timestamp.split(".")[0].rjust(8, "0")
        print(timestamp, t[1])
    print(
        "\nCreated using youtube-timestamper (https://ilangurudev.github.io/youtube-timestamper/)"
    )

# %% ../00_core.ipynb 37
@patch
def suggest_question_timestamps(
    self: YoutubeTimestamper,
    next_q_thresh: int = 15,  # The number of tokens within a question which if the next question is present, it'll be considered part of the same question
) -> None:
    """Suggest timestamps based on questions found in the transcripts."""
    if "self.questions" not in vars():
        self._get_transcript()
        self._restore_punctuations()
        self._get_sentences()
    self._get_questions(next_q_thresh)
    self._get_timestamps_for_questions()
    self._render_timestamps()
