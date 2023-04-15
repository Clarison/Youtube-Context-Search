# youtubecontextsearch

appliaction - https://clarison-youtubecontextsearch-welcome-kefb0r.streamlit.app/

codelabs - https://codelabs-preview.appspot.com/?file_id=1HwKvjj4OvVfTC3GWpBapFol0qG8PUMQ2HaEGbdlU0MI#0

## Objectives
To build a retrieval-enhanced generative question-answering system with Pinecone and OpenAI. This will allow us to retrieve relevant contexts to our queries from Pinecone, and pass these to a generative OpenAI model to generate an answer backed by real data sources.

1. Choose a product - MacBook
2. Use pytube or Youtube-transcript-API to transcribe 4 to 5 product reviews on product from Youtube
3. Develop an application to ask a question and get answers based on context-based-searches and RAG
4. Build a streamlit application

## Requirements
1. Streamlit
2. Pinecone API
3. Open AI API
4. Youtube transcription API

## Description
Large Language Models are a subset of artificial intelligence that has been trained on vast quantities of text data (read: the entire internet in the case of ChatGPT) to produce human-like responses to dialogue or other natural language inputs.

In order to produce these natural language responses, LLMs use deep learning models, which use multi-layered neural networks to process, analyse, and make predictions with complex data.

### Transformers

Transformers are a type of neural network architecture that has become popular in LLM research. These networks use self-attention mechanisms to process input data, allowing them to effectively capture long-term dependencies in human language.

These algorithms are crucial to the performance of LLMs as they enable them to process and understand natural language inputs and generate outputs as human-like as possible.

## Retrieval-Augmented Generation

We introduce RAG models where the parametric memory is a pre-trained seq2seq model and the non-parametric memory is a dense vector index of Wikipedia, accessed with a pre-trained neural retriever. We compare two RAG formulations, one which conditions on the same retrieved passages across the whole generated sequence, and the other can use different passages per token. We fine-tune and evaluate our models on a wide range of knowledge-intensive NLP tasks and set the state-of-the-art on three open-domain QA tasks, outperforming parametric seq2seq models and task-specific retrieve-and-extract architectures. For language generation tasks, we find that RAG models generate more specific, diverse and factual language than a state-of-the-art parametric-only seq2seq baseline.
