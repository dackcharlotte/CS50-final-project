import deepl
import textract as te
from gtts import gTTS
import pathlib
import sys
import re


def main():
    try:
        if len(sys.argv) < 2:
            sys.exit("Too few arguments. Please provide the name of your scource .txt. For example 'python project.py yourfile.txt'")
        elif len(sys.argv) > 2:
            sys.exit("Too many arguments. Please only provide the name of your scource .txt. For example 'python project.py yourfile.txt.")
        else:
            s_lang = check_if_souce_eng()
            if check_extention() == True:
                name_of_file, type_of_file = sys.argv[1].split(".")
                checked_t_lang = check_lang_in_dict()
                file_tranlated = file_translate(checked_t_lang, name_of_file)
                merger = merging_txt(name_of_file)
                if merger == True:
                    print("You can now find your merge of desired and target language text in project/results/merged_txt called merged")
                    speech_creator = text_to_speech(checked_t_lang, name_of_file)
    except IndexError:
        sys.exit("There is a probelm. Please try again.")

def check_extention():
    name_of_file, type_of_file = sys.argv[1].split(".")
    if type_of_file == "txt":
        return True
    else:
        sys.exit("The file type is invalid. The File must be a .txt file")

def check_if_souce_eng():
    s_lang = input("What language is your .txt doc current in?\nPlease note that this program current only supports translations from English. ")
    if s_lang.capitalize().strip() == "English" or s_lang.capitalize().strip() == "EN":
        s_lang = "EN"
        return s_lang
    else:
        sys.exit("This source language is currently not supported.")

def check_lang_in_dict():
    target_languages = {
    "German": "DE",
    "Spanish": "ES",
    "French": "FR",
    "Italian": "IT",
    "Japanese": "JA",
    "Dutch": "NL",
    "Polish": "PL",
    "Portuguese": "PT",
    "Brazilian": "PT-BR",
    "Russian": "RU",
    }
    print("We support the following languages:")
    for l in target_languages:
        print(l)
    tar_lang = input(f"What language would you like to translate {sys.argv[1]} too? ").capitalize().strip()


    if tar_lang in target_languages:
        intials_t_lang = target_languages[tar_lang]
        return intials_t_lang
    elif tar_lang not in target_languages:
        sys.exit("Language not valid")

    #return none and put in sys_len_check != None

#using Deepl API translate the file
def file_translate(checked_t_lang, name_of_file):
    auth_key = "8a5e7ca8-5b65-4035-badc-cd3b7d9fda1c:fx"  # using a deepL.com token
    translator = deepl.Translator(auth_key)

    #defining pathway to fiules
    input_path = f"./input/{sys.argv[1]}" #projectIF ISSUEL: might have to change path way depending on file location
    output_path = f"./results/translated_txt/{name_of_file}_translation.txt"
    try:
        # Using translate_document_from_filepath() with file paths
        translator.translate_document_from_filepath(
            input_path,
            output_path,
            source_lang="EN",
            target_lang=f"{checked_t_lang}",
            formality="more"
        )
        print("You can now find your translated txt in project/results/translated_txt called translated")

    #error checking
    except deepl.DocumentTranslationException as error:
        doc_id = error.document_handle.id
        doc_key = error.document_handle.key
        print(f"Error after uploading ${error}, id: ${doc_id} key: ${doc_key}")
    except deepl.DeepLException as error:
        # Errors during upload raise a DeepLException
        print(error)

def merging_txt(name_of_file):
    combine =[]

    with open(f"/workspaces/96585110/project/input/{sys.argv[1]}") as og:
        with open(f"/workspaces/96585110/project/results/translated_txt/{name_of_file}_translation.txt") as translated:
            with open(f"/workspaces/96585110/project/results/merged_txt/{name_of_file}_merged.txt", "w") as merge:
                # Read first file
                xlines = og.readlines()
                # Read second file
                ylines = translated.readlines()

                # Determine the minimum length of the two lists
                min_length = min(len(xlines), len(ylines))

                # Combine content of both lists up to the minimum length
                for i in range(min_length):
                    line = ylines[i].strip() + ' ' + xlines[i]
                    merge.write(line)

                # Handle any remaining lines if the lists are of different lengths
                if len(ylines) > min_length:
                    for i in range(min_length, len(ylines)):
                        merge.write(ylines[i])
                elif len(xlines) > min_length:
                    for i in range(min_length, len(xlines)):
                        merge.write(xlines[i])

    return True


def text_to_speech(checked_t_lang, name_of_file):
    filename = f"{name_of_file}_merged.txt"
    path = str(pathlib.Path().absolute())
    text = te.process(path+ "/results/merged_txt/" + filename).decode("utf-8")
    lower_t_lang = checked_t_lang.lower()
    tts = gTTS(text, lang=f"{lower_t_lang}", slow=True)  # slow changes speed
    #bookname = pathlib.Path(name_of_file).stem
    #tts.save(f"{bookname}.mp3")
    bookname = pathlib.Path(name_of_file).stem
    save_directory = f"/workspaces/96585110/project/results/mp3/{name_of_file}"
    pathlib.Path(save_directory).mkdir(parents=True, exist_ok=True)
    tts.save(f"{save_directory}/{bookname}.mp3")
    print("You can now find your convert .txt doc in the mp3 folder.")

if __name__ == "__main__":
    main()

