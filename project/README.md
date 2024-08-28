# Document Language Translator and Text to Speech Conversion by Charlotte Dack
#### Video Demo: https://www.youtube.com/watch?v=bgXYCrFylLs
#### Description of program
This program translates a .txt file to a target language specified via command-line arguments, with the original and target languages gathered from user input. The document is translated using Deepl's API. The original .txt file is then merged with the translated text line by line, creating a new merged .txt file. Using Google's Text to Speech API, the merged file is converted to an .MP3 file, which you can then play. You can customize the speed and download the MP3 file.

Design Choices:

Command-line Arguments
Initially, I considered having the target language specified via command-line arguments to allow the program to run immediately. However, this approach proved confusing and less user-friendly, so I decided to prompt for the target language interactively instead.

Supported Language List
To enhance user experience, I decided to print the list of supported languages. This ensures users are aware of the available options and can make informed choices. Additionally, the program prints the location of the generated documents and notifies users when they are ready.

Multiple Outputs: translated.txt, merged.txt, fileas.mp3
The program produces outputs at each stage to allow users access to all stages of the document processing. Initially, the program was intended to help me learn a new language by allowing me to see the words while listening to the text. This is why I ensured the translated .txt file, merged file, and .mp3 were all separate.

Organizing Files
Having multiple outputs made the file system messy, so I decided to organize them into folders. This required learning the differences between absolute and relative paths, which was a valuable lesson.

Supported Document Types
One limitation I had to consider was that the Deepl API for the free version only allows translations from .txt files. This necessitated checking the file extension. Although I considered using regex for this task, I opted for a simpler solution using .split(). In the future, I aim to expand the code's capabilities to support other file types, enabling it to translate full documents.

Methodology
Throughout this process, I developed a structured methodology for coding in sections. I started with the text-to-speech translator, then moved on to the translation functionality, and finally the merging of the documents, including all necessary checks, edge cases, and exceptions. This approach naturally led to the creation of well-defined functions.

Unit Testing and Mocking
Unit testing was a significant learning curve. I had to learn how to mock command-line arguments, which was time-consuming but ultimately rewarding. This experience greatly improved my understanding of testing in software development.

- **input**: This is where you upload the .txt document.
- **result**:
  - **merged_txt**: Contains merged files of the original and translated text.
  - **mp3**: Contains MP3 files, each saved in its own folder.
  - **translated_txt**: Contains the translated text files.
- **project.py**: The main program file.
- **README.md**: This document.
- **requirements.txt**: Lists all the libraries that need to be installed.
- **test_project.py**: The unit test script for `project.py`.
Set Up:
1. Install all necessary libraries:
    ```sh
    pip install -r requirements.txt
    ```
2. Upload the .txt document you want to translate to the `./project/input` directory.
3. Run the program with one argument in the command line, which is the name of the .txt file you want to translate:
    ```sh
    python project.py yourfile.txt
    ```
4. The program will then ask you for the source language and target language.




