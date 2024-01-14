# Windows Shutdown App with CustomTkinter and Voice Commands

## Table of Contents
1. [Overview](#overview)
2. [Features](#features)
3. [Requirements](#requirements)
4. [Installation](#installation)
    - [Download through Git](#download-through-git)
    - [Download through ZIP file](#download-through-zip-file)
5. [Usage](#usage)
6. [Troubleshooting](#troubleshooting)
7. [Contributions](#contributions)
8. [License](#license)
9. [Acknowledgments](#acknowledgments)

## Overview
This graphical application is designed to provide a user-friendly interface for shutting down a Windows system. It utilizes CustomTkinter for a customized and aesthetically pleasing GUI. Additionally, the app is equipped with voice command functionality, allowing users to trigger the shutdown process through spoken commands.

## Features
- **CustomTkinter GUI:** The application employs CustomTkinter, a customized version of the Tkinter library, to create an intuitive and visually appealing user interface.
- **Shutdown Options:** Users can choose from various shutdown options, including immediate shutdown, scheduled shutdown, and restart.
- **Voice Command Integration:** The app supports voice commands for initiating the shutdown process. Users can simply speak predefined commands, and the app will interpret and execute the corresponding action.

## Requirements
- Python 3.9 or later
- CustomTkinter library
- SpeechRecognition library
- pyttsx3 library

## Installation
## Download through Git:
1. Clone the repository to your local machine using Git. Open your terminal and run the following command:
   ```bash
   git clone https://github.com/UltraDeveloper7/Shut-Down-PC.git
   ```
## Download through ZIP file:
1. Download the project as a zip file. You can do this by clicking on the "Code" button on the [GitHub repository page](https://github.com/UltraDeveloper7/Shut-Down-PC) and selecting "Download ZIP."
2. Extract the downloaded zip file to a location of your choice.
3. Open your terminal or command prompt and navigate to the extracted directory.
   ```bash
   cd path/to/extracted/folder
   ```
4. Run inside that folder te following command:
   ```bash
   python Shutdown-Windows.py
   ```

## Usage
1. Run the application:
    ```bash
    python Shutdown-Windows.py
    ```
2. Use the graphical interface to select shutdown options or use voice commands.
3. To initiate a voice command, click the voice-commands button and speak the predefined command.


## Troubleshooting
- If you encounter any issues with voice recognition, ensure that your microphone is properly connected and configured.
- Check for updates to the CustomTkinter library or other dependencies that may impact the application.

## Contributions
Contributions are welcome! Feel free to fork this repository and submit a pull request with your enhancements.

## License
This project is licensed under the [MIT License](LICENSE). You can find the full text of the license [here](https://opensource.org/licenses/MIT).

## Acknowledgments
- CustomTkinter: [https://github.com/TomSchimansky/CustomTkinter]
- SpeechRecognition: [https://pypi.org/project/SpeechRecognition/]
- pyttsx3: [https://pypi.org/project/pyttsx3/]
