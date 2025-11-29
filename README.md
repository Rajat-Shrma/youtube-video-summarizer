# YouTube Transcript Summarizer

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Stars](https://img.shields.io/github/stars/Rajat-Shrma/youtube-video-summarizer)

A powerful, user-friendly web application that automatically fetches YouTube video transcripts and generates concise, well-structured summaries using Google's Gemini AI. Perfect for students, researchers, content creators, and professionals who want to quickly understand long videos without watching them entirely.

## Features

- **🎯 Automatic Transcript Extraction** - Fetches transcripts directly from YouTube videos
- **🤖 AI-Powered Summarization** - Uses Google Gemini 2.5 Flash model for intelligent summaries
- **🎨 Clean Web Interface** - Built with Streamlit for a smooth, intuitive user experience
- **⚡ Fast Processing** - Quickly processes and summarizes videos of any length
- **🔒 Secure** - API keys stored securely in `.env` and `secret.toml` files
- **📝 Structured Output** - Summaries are formatted in markdown for easy reading

## Table of Contents

- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Troubleshooting](#troubleshooting)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [License](#license)

## Tech Stack

- **Frontend**: Streamlit (Python web framework)
- **Backend**: Python 3.8+
- **AI Model**: Google Gemini 2.5 Flash API
- **Transcript API**: YouTube Transcript API
- **Environment Management**: python-dotenv, pathlib

### Dependencies

```
youtube-transcript-api     # Extract transcripts from YouTube videos
streamlit                   # Web UI framework
google-generativeai         # Google Gemini API client
python-dotenv               # Load environment variables
pathlib                     # File path handling
```

## Project Structure

```
youtube-video-summarizer/
├── app.py                  # Main application file
├── requirements.txt        # Python dependencies
├── .env                    # Environment variables (non-sensitive)
├── secret.toml             # Sensitive configuration (API keys)
├── .gitignore              # Git ignore rules
└── README.md               # This file
```

## Prerequisites

- **Python 3.8 or higher** installed on your system
- **pip** (Python package manager)
- **Google API Key** for Gemini API
  - Get it from: [Google AI Studio](https://aistudio.google.com/app/apikey)
- **Internet connection** for accessing YouTube and APIs

## Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/Rajat-Shrma/youtube-video-summarizer.git
cd youtube-video-summarizer
```

### Step 2: Create a Virtual Environment

```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

## Configuration

### Step 1: Set Up Environment Variables

Create a `.env` file in the project root:

```bash
# .env
DEBUG=False
STREAMLIT_CONFIG_SERVER_PORT=8501
```

### Step 2: Set Up API Keys

Create a `secret.toml` file in the project root:

```toml
# secret.toml
GOOGLE_API_KEY = "your-google-api-key-here"
```

**⚠️ Important Security Notes:**
- Never commit `.env` or `secret.toml` to version control
- These files are already in `.gitignore`
- Keep your API keys confidential
- Regenerate keys if accidentally exposed

### Step 3: Verify Configuration

Ensure both files are created and contain the correct values.

## Usage

### Running the Application

```bash
# Make sure your virtual environment is activated
streamlit run app.py
```

The application will open in your default browser at `http://localhost:8501`

### Using the Application

1. **Enter YouTube URL**: Paste the full YouTube video URL in the text input field
   - Example: `https://www.youtube.com/watch?v=dQw4w9WgXcQ`
   - Also supports: `https://youtu.be/dQw4w9WgXcQ`

2. **Wait for Processing**: The app will:
   - Extract the video ID
   - Fetch the transcript
   - Generate a summary using Gemini AI

3. **View Summary**: The structured summary appears below the input field

## How It Works

### Workflow

```
YouTube URL → Video ID Extraction → Transcript Fetching → 
AI Summarization → Formatted Output → Display to User
```

### Technical Details

1. **URL Parsing**: Extracts video ID from standard YouTube URL formats
   - Handles `youtube.com/watch?v=` and `youtu.be/` formats

2. **Transcript Extraction**: Uses `YouTubeTranscriptApi` to fetch captions
   - Combines all transcript chunks into a single text

3. **AI Summarization**: Sends transcript to Google Gemini 2.5 Flash
   - Model Configuration:
     - Temperature: 1.0 (Creative responses)
     - Top P: 0.95
     - Top K: 40
     - Max Output Tokens: 8192

4. **Markdown Formatting**: Converts AI response to readable markdown
   - Formats bullet points and indentation

## Troubleshooting

### Common Issues

#### 1. "No module named 'streamlit'"
```bash
# Solution: Install dependencies again
pip install -r requirements.txt
```

#### 2. "Invalid YouTube URL"
- Ensure the URL is complete and valid
- Try: `https://www.youtube.com/watch?v=VIDEO_ID`
- Remove any extra parameters or timestamps

#### 3. "API Key Error"
```bash
# Verify your secret.toml exists in project root:
# - GOOGLE_API_KEY must be set
# - Check for typos in the key
# - Regenerate key from Google AI Studio if expired
```

#### 4. "Transcript not available"
- Some videos have disabled transcripts
- Try with a different video
- Ensure the video has auto-generated or manual captions

#### 5. Connection Timeout
- Check your internet connection
- Verify API rate limits haven't been exceeded
- Try again after a few moments

### Debug Mode

To enable debug mode, set in `.env`:
```
DEBUG=True
```

## Future Enhancements

- [ ] Support for multiple languages
- [ ] Customizable summary length (Short/Medium/Detailed)
- [ ] Export summaries as PDF, DOCX, or TXT
- [ ] Batch processing for multiple videos
- [ ] Summary caching to reduce API calls
- [ ] User authentication and summary history
- [ ] Support for non-English transcripts with translation
- [ ] Integration with other platforms (Vimeo, etc.)
- [ ] Sentiment analysis of video content
- [ ] Keyword extraction from summaries

## Contributing

Contributions are welcome! Please follow these steps:

1. **Fork** the repository
2. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Commit your changes**
   ```bash
   git commit -m "Add your meaningful commit message"
   ```
4. **Push to the branch**
   ```bash
   git push origin feature/your-feature-name
   ```
5. **Open a Pull Request** with a clear description of changes

### Development Guidelines

- Write clean, readable code
- Add comments for complex logic
- Test thoroughly before submitting PR
- Follow PEP 8 style guide
- Update documentation as needed

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

If you encounter issues or have questions:

- Check the [Troubleshooting](#troubleshooting) section
- Review [GitHub Issues](https://github.com/Rajat-Shrma/youtube-video-summarizer/issues)
- Create a new issue with detailed description

## Acknowledgments

- [YouTube Transcript API](https://github.com/jdepoix/youtube-transcript-api)
- [Google Generative AI](https://ai.google.dev/)
- [Streamlit](https://streamlit.io/)

---

**Made with ❤️ by [Rajat Sharma](https://github.com/Rajat-Shrma)**

If you found this project helpful, consider giving it a ⭐ on GitHub!
