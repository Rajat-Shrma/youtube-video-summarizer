import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi as yt
import google.generativeai as genai
import textwrap
from dotenv import load_dotenv
import os
load_dotenv()

api_key = os.getenv("API_KEY")

def get_video_id(url):
    if "v=" in url:
        return url.split("v=")[1].split("&")[0]
    elif "youtu.be/" in url:
        return url.split("youtu.be/")[1].split("?")[0]
    else:
        return None

def to_markdown(text):
    text = text.replace('•', ' *')
    return textwrap.indent(text, '> ', predicate=lambda line: True)


st.title("YouTube Transcript Summarizer")


url = st.text_input("Enter YouTube video URL:")

if url:

    video_id = get_video_id(url)

    if video_id:
        with st.spinner("Fetching and summarizing transcript..."):
            try:
     
                transcript = yt.get_transcript(video_id)
                full_text = [dic['text'] for dic in transcript]
                full_transcript = ' '.join(full_text)


                gemini_api_key = st.secrets["GEMINI_API_KEY"]


                genai.configure(api_key=gemini_api_key)
                generation_config = {
                    "temperature": 1,
                    "top_p": 0.95,
                    "top_k": 40,
                    "max_output_tokens": 8192,
                    "response_mime_type": "text/plain",
                }
                model = genai.GenerativeModel(
                    model_name="gemini-1.5-flash",
                    generation_config=generation_config,
                )

                # Generate summary
                prompt = f"Summarize the provided YouTube video transcript ({full_transcript}) in a structured format."
                response = model.generate_content(prompt)

                # Display summary
                st.markdown("## Summary:")
                st.markdown(to_markdown(response.text))

            except Exception as e:
                st.error(f"An error occurred: {e}")
    else:
        st.error("Invalid YouTube URL. Please provide a valid URL.")
