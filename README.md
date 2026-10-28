# 🤖 Desktop Voice Assistant Using Python

A Python-based desktop voice assistant that recognizes voice commands, responds through speech, searches the web, retrieves information from Wikipedia, plays music, and opens directories on your computer.

## 📌 About the Project

The **Desktop Voice Assistant** is a Python project designed to simplify everyday computer tasks through voice commands. It uses speech recognition to understand user instructions and text-to-speech technology to provide spoken responses.

The assistant can perform various tasks, such as searching Wikipedia, opening a web browser, playing music, speaking text aloud, and opening directories.

## ✨ Features

- 🎙️ **Voice Recognition:** Recognizes voice commands through a microphone.
- 🔊 **Text-to-Speech:** Converts text into speech and responds verbally.
- 🌐 **Web Search:** Opens a web browser to search for information online.
- 📚 **Wikipedia Search:** Searches Wikipedia for information on requested topics.
- 🎵 **Music Player:** Plays music on your computer.
- 📂 **Directory Access:** Opens specified directories on your computer.
- 💬 **Voice Interaction:** Responds to supported commands through voice output.
- 👋 **Greeting Feature:** Provides greetings and welcomes users.

## 🛠️ Technologies Used

- **Programming Language:** Python
- **Speech Recognition:** SpeechRecognition
- **Text-to-Speech:** pyttsx3
- **Web Browser Automation:** Python webbrowser module
- **Operating System Interaction:** os module
- **Wikipedia Search:** Wikipedia website integration
- **Date and Time:** datetime module

## 📁 Project Structure

```text
Desktop-Voice-Assistant/
│
├── 01Javvis.py             # Main assistant program
├── open_directory.py       # Opens directories
├── playsong.py             # Plays music
├── search_webbrowser.py    # Performs web searches
├── search_wikipedia.py     # Searches Wikipedia
├── speak.py                # Text-to-speech functionality
├── speech_Recognition.py   # Voice recognition
├── wish.py                 # Greeting functionality
└── README.md               # Project documentation
```

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
```

Replace `YOUR-USERNAME` and `YOUR-REPOSITORY` with your GitHub username and repository name.

### 2. Navigate to the Project Directory

```bash
cd YOUR-REPOSITORY
```

### 3. Install Dependencies

Install the required Python libraries:

```bash
pip install SpeechRecognition pyttsx3
```

**Additional requirements:**
- Install `PyAudio` if your microphone setup requires it for speech recognition.
- Ensure your computer has a working microphone and speakers.
- Some systems may require additional audio dependencies.

If your project uses other external libraries, install those as well.

### 4. Run the Application

Run the main Python file:

```bash
python 01Javvis.py
```

Make sure you run the command from the project directory and have configured any required file paths.

## 🚀 How to Use

1. Run the main Python program.
2. Allow microphone access if prompted.
3. Speak a supported command clearly.
4. The assistant processes the command and performs the corresponding action.
5. Listen to the assistant's spoken response.

### Example Commands

| Voice Command | Expected Action |
|---|---|
| Search Wikipedia for Python | Searches Wikipedia for Python |
| Search for machine learning | Opens a web search |
| Play music | Plays music from the configured location |
| Open directory | Opens the configured directory |
| Speak hello | Demonstrates text-to-speech functionality |

*Note: The exact commands depend on how they are implemented in your Python scripts.*

## 🎯 Project Objectives

- Learn Python automation and operating system interaction.
- Implement speech recognition and text-to-speech functionality.
- Integrate web search capabilities into a desktop application.
- Automate common computer tasks using voice commands.
- Improve practical programming and problem-solving skills.

## 🔮 Future Improvements

- Add an intelligent conversational interface.
- Integrate an AI-powered question-answering system.
- Add support for more voice commands.
- Improve error handling and speech recognition accuracy.
- Add a graphical user interface (GUI).
- Support customizable commands and user preferences.
- Add secure application launching and system controls.

## 🔐 Security and Privacy

This assistant may use microphone input and open websites based on user commands. Review the code before running it, configure file paths carefully, and avoid adding passwords, API keys, or other sensitive information to the repository.

## 👨‍💻 Author

**Dipendra Kushwaha**

Computer Science and Engineering Graduate | Python Developer | Technology Enthusiast

- GitHub: [@Dipu252](https://github.com/Dipu252)

## ⭐ Support

If you find this project useful, consider giving the repository a star ⭐ and sharing your feedback.

---

*Built with Python to explore voice recognition, desktop automation, and speech-based interaction.*
