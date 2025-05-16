#!/usr/bin/env python3
from pathlib import Path
from typing import Literal, Any

import click

from helpers import check_response, vss_api_call, Chat


def upload_video_to_vss():
    """ TODO """


def summarize_video():
    """ TODO """

@click.command()
@click.argument('video_files', type=click.Path(exists=True), nargs=-1)
@click.option('--vss-url', envvar='VSS_URL', default="http://via-server:8100",
              help="URL to the VIA Server API")
def pipeline(video_files: list[str], vss_url: str):
    """Run the bridge inspection pipeline."""
    
    for video in video_files:

        # upload the video
        video_id = upload_video_to_vss(video)

        # summarize the video
        body = {
            "id": "899f58fe-739f-43c0-b2b9-1d191f073bb7",
            "prompt": "You are a bridge inspector. Describe any concerns you have with this bridge in detail. Your concerns may be: cosmetic, structural, landscaping, or vandalism in nature.Start each event description with a start and end time stamp of the event.",
            "caption_summarization_prompt": "If any descriptions have the same meaning and are sequential then combine them under one sentence and merge the time stamps to a range. Format the timestamps as 'mm:ss'",
            "summary_aggregation_prompt": "Based on the available information, generate a report that describes the condition of the bridge. The report should be organized into cosemetic, structual, vegetation overgrowth, and vandalism. The report must include timestamps. This should be a concise, yet descriptive summary of all the important events. The format should be intuitive and easy for a user to understand what happened. Format the output in Markdown so it can be displayed nicely.",
            "model": "nvila",
            "max_tokens": 1024,
            "temperature": 0.9,
            "top_p": 0.9,
            "num_frames_per_chunk": 15,
            "chunk_duration": 35,
            "chunk_overlap_duration":5,
            "enable_chat": True,
        }
        report = summarize_video(video_id, body)

        # connect to the chat server
        chat_client = Chat(
            vss_url, 
            video_id=upload_response.get("id"),
            model_id=models_response["data"][0]["id"]
        )

        # ask follow up questions
        escalations = chat_client.query("List any necessary escelations for maintenance.")
        priority = chat_client.query("Score the priority of this report.")
        title = chat_client.query("Create a title for this report.")
        emergencies = chat_client.query("Does this the bridge require immediate structural attention?")

        write_report(title, priority, emergencies, escalations, report)
        

if __name__ == "__main__":
    # run our custom pipeline
    pipeline()