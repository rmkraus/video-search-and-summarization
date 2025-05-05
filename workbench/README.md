# Quickstart for NVIDIA AI Workbench 

This blueprint is for developers who want a quick start to set up a video search and summarization solution with a path-to-production using NVIDIA NIM.

> **Note**
> This app runs in [NVIDIA AI Workbench](https://docs.nvidia.com/ai-workbench/user-guide/latest/overview/introduction.html). It's a free, lightweight developer platform that you can run on your own systems to get up and running with complex AI applications and workloads in a short amount of time. 

> You may want to [**fork**](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo#forking-a-repository) this repository into your own account before proceeding. Otherwise you won't be able to fully push any changes you make because this NVIDIA-owned repository is **read-only**.

*Navigating the README*: [Project Overview](#project-overview) | [Get Started](#get-started) | [License](#license)

*Other Resources*: [:arrow_down: Download AI Workbench](https://www.nvidia.com/en-us/deep-learning-ai/solutions/data-science/workbench/) | [:book: User Guide](https://docs.nvidia.com/ai-workbench/) |[:open_file_folder: Other Projects](https://docs.nvidia.com/ai-workbench/user-guide/latest/quickstart/example-projects.html) | :rotating_light: User Forum (Coming Soon)

## Project Overview

Insightful, accurate, and interactive video analytics AI agents enable a range of industries to make better decisions faster. These AI agents are given tasks through natural language and can perform complex operations like video summarization and visual question-answering, unlocking entirely new application possibilities. The NVIDIA AI Blueprint makes it easy to get started building and customizing video analytics AI agents for video search and summarization — all powered by generative AI, vision language models (VLMs) like Cosmos Nemotron VLMs, large language models (LLMs) like Llama Nemotron LLMs, NVIDIA NeMo Retriever, and NVIDIA NIM.

The NVIDIA AI Blueprint for Video Search and Summarization addresses the challenge of efficiently analyzing and summarizing large volumes of video data. This can be used to create vision AI agents, that can be applied to a multitude of use cases such as monitoring smart spaces, warehouse automation, and SOP validation. This is important where quick and accurate video analysis can lead to better decision-making and enhanced operational efficiency.

[Read More](../README.md#software-components)

## Get Started

Ensure you have satisfied the prerequisites for this Blueprint ([details](../README.md#hardware-requirements)). 

### Local Deployment (Single GPU)

1. Open NVIDIA AI Workbench. Select a **Location** to work in.

1. **Clone** the project with URL: https://github.com/NVIDIA-AI-Blueprints/video-search-and-summarization

    * Alternatively, fork the repo into your account for write permissions. Use this forked repo URL. 

1. On the **Project Dashboard**, resolve the yellow unconfigured secrets warning by inputting your ``NVIDIA_API_KEY``.

1. Select ``local-deployment-single-gpu`` compose profiles from the dropdown under the **Compose** section of the Project Dashboard.

1. Select **Start** under the **Compose** section of the Project Dashboard. The compose services may take several minutes to pull and build.

1. When the compose services are ready, you can access the frontend on the IP address, eg. ``http://<ip_addr>:9010``. 

1. You can now interact with Video Search and Summarization through its browser interface. [Navigating the UI](https://docs.nvidia.com/vss/latest/content/ui_app.html)

### Local Deployment (Multi-GPU)
<details>
<summary>
<b>Click here to Expand</b>
</summary>

1. Open NVIDIA AI Workbench. Select a **Location** to work in.

1. **Clone** the project with URL: https://github.com/NVIDIA-AI-Blueprints/video-search-and-summarization

    * Alternatively, fork the repo into your account for write permissions. Use this forked repo URL. 

1. On the **Project Dashboard**, resolve the yellow unconfigured secrets warning by inputting your ``NVIDIA_API_KEY``.

1. Select **Open Jupyterlab** on the top right of the AI Workbench window. Jupyterlab should automatically open in a browser

1. Navigate to ``variables.env``. **Comment out** the ``LOCAL_DEPLOYMENT_SINGLE_GPU`` section and **uncomment** the ``LOCAL_DEPLOYMENT`` section. 

    ```
    ### LOCAL_DEPLOYMENT: Set VLM to VILA ###
    VLM_MODEL_TO_USE=vila-1.5
    MODEL_PATH=ngc:nim/nvidia/vila-1.5-40b:vila-yi-34b-siglip-stage3_1003_video_v8
    
    ### LOCAL_DEPLOYMENT_SINGLE_GPU: Set VLM to NVILA ###
    #VLM_MODEL_TO_USE=nvila 
    #MODEL_PATH=git:https://huggingface.co/Efficient-Large-Model/NVILA-15B
    #NVILA_VIDEO_MAX_TILES=1
    ```

1. Navigate to ``workbench/config.yaml``. Swap out ``base_url`` and ``model`` as follows:

```
    (TODO)
```

1. On the **Project Dashboard** of the AI Workbench window, select ``local-deployment-multi-gpu`` compose profiles from the dropdown under the **Compose** section of the Project Dashboard.

1. Select **Start** under the **Compose** section of the Project Dashboard. The compose services may take several minutes to pull and build.

1. When the compose services are ready, you can access the frontend on the IP address, eg. ``http://<ip_addr>:9010``. 

1. You can now interact with Video Search and Summarization through its browser interface. [Navigating the UI](https://docs.nvidia.com/vss/latest/content/ui_app.html)

</details>

### Remote Deployment (local VLM)

1. Open NVIDIA AI Workbench. Select a **Location** to work in.

1. **Clone** the project with URL: https://github.com/NVIDIA-AI-Blueprints/rag

1. On the **Project Dashboard**, resolve the yellow unconfigured secrets warning by inputting your ``NVIDIA_API_KEY``.

1. On the **File Browser**, locate the ``variables.env`` file.

1. From the hamburger menu, select **Edit**. Comment out the overriding variables for Build endpoints. 

1. Select ``ingest``, ``rag``, ``vectordb``, and ``local`` compose profiles from the dropdown under the **Compose** section.

1. Select **Start**. The compose services may take several minutes to pull and build.

1. When the compose services are ready, select **View Compose Settings**.

1. Locate the ``rag-playground`` service and select the **Open in Browser** icon.

    * Alternatively, you can access the frontend on the IP address, eg. ``http://<ip_addr>:8090``. 

1. You can now interact with the RAG Chatbot through its browser interface.

### Remote Deployment (remote VLM)

1. Open NVIDIA AI Workbench. Select a **Location** to work in.

1. **Clone** the project with URL: https://github.com/NVIDIA-AI-Blueprints/rag

1. On the **Project Dashboard**, resolve the yellow unconfigured secrets warning by inputting your ``NVIDIA_API_KEY``.

1. On the **File Browser**, locate the ``variables.env`` file.

1. From the hamburger menu, select **Edit**. Comment out the overriding variables for Build endpoints. 

1. Select ``ingest``, ``rag``, ``vectordb``, and ``local`` compose profiles from the dropdown under the **Compose** section.

1. Select **Start**. The compose services may take several minutes to pull and build.

1. When the compose services are ready, select **View Compose Settings**.

1. Locate the ``rag-playground`` service and select the **Open in Browser** icon.

    * Alternatively, you can access the frontend on the IP address, eg. ``http://<ip_addr>:8090``. 

1. You can now interact with the RAG Chatbot through its browser interface.
## License
The software and materials in this repository are governed by the [NVIDIA Software License Agreement](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-software-license-agreement/) and the Product-Specific Terms for [NVIDIA AI Products](https://www.nvidia.com/en-us/agreements/enterprise-software/product-specific-terms-for-ai-products/); except for models which are governed by the [NVIDIA Community Model License](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-community-models-license/).

ADDITIONAL INFORMATION: [Llama 3.1 Community License Agreement](https://www.llama.com/llama3_1/license/) for Llama-3.1-70b-instruct; [Llama 3.2 Community License Agreement](https://www.llama.com/llama3_2/license/) for NVIDIA Retrieval QA Llama 3.2 1B Embedding v2 and NVIDIA Retrieval QA Llama 3.2 1B Reranking v2, Apache, Version 2.0 for https://github.com/google-research/big_vision/blob/main/LICENSE and Apache License, Version 2.0 for https://github.com/01-ai/Yi/blob/main/LICENSE. Built with Llama.
