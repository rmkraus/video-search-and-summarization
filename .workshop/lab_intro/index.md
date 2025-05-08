# Introduction to VSS

## Architecture
The Video Search and Summarization is comprised of two pipelines: the **Ingestion** pipeline and the **Retrieval** pipeline.

As video is streamed or uploaded into the agent, the video will be pre-processed into chunks of time intervals. These chunks are then used to generate high level summaries as well as a detailed database of observations.

The combination of these chunked summaries and knowledge database are then used by the Retrival pipeline to summarize and chat with video streams.

<img src="lab_intro/vss_arch.png" />

## Meet the NIMs

This blueprint employs up to four NVIDIA NIMs.

| | |
| --- | --- |
| [meta/llama-3.3-70b-instruct <i class="fas fa-external-link-alt"></i>](https://build.nvidia.com/meta/llama-3_3-70b-instruct) | Large Language Model used for performing Question and Answering and directly chatting with the end user. |
| [nvidia/vila <i class="fas fa-external-link-alt"></i>](https://build.nvidia.com/nvidia/vila) | Multi-modal vision-language model that used for creating informative insights about images and video. |
| [nvidia/nv-embedqa-e5-v5 <i class="fas fa-external-link-alt"></i>](https://build.nvidia.com/nvidia/nv-embedqa-e5-v5) | Embedding model for converting human text into vector representations. |
| [nvidia/llama-3_2-nv-rerankqa-1b-v2 <i class="fas fa-external-link-alt"></i>](https://build.nvidia.com/nvidia/llama-3_2-nv-rerankqa-1b-v2) | Reranking model for determining content most relevant to a user prompt. |

## Explore the GUI

## Explore the API

<button onclick="openOrCreateFileInJupyterLab('labs/Intro_To_VSS.ipynb');"><i class="fas fa-book-open"></i> Intro to VSS</button>

## Wrap up