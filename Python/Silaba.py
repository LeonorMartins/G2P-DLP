import pandas as pd
import regex as re  # Use the regex module for variable-width look-behinds

def load_column_to_list(file_path, sheet_name):
    try:
        df = pd.read_excel(file_path, sheet_name=sheet_name, header=None)
        column_data = df[0].dropna().tolist()
        return column_data
    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def load_regex_to_dict(file_path, sheet_name):
    try:
        df = pd.read_excel(file_path, sheet_name=sheet_name, header=None)
        # Convert all keys and values to strings
        regex_dict = {str(k): str(v) for k, v in zip(df[0], df[1])}
        return regex_dict
    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def apply_patterns_to_words(words_list, regex_dict, log_file_path="Debug/debug_silaba.txt"):
    processed_words = []
    with open(log_file_path, "w", encoding="utf-8") as log_file:  # Use UTF-8 encoding
        for word in words_list:
            processed_word = word
            for pattern, replacement in regex_dict.items():
                try:
                    if replacement == "nan":
                        replacement = ""
                    # Log the word before and after applying the pattern
                    new_word = re.sub(pattern, replacement, processed_word)
                    if new_word != processed_word:
                        log_file.write(f"Original Word: {processed_word} -> Processed Word: {new_word}\n")
                        log_file.write(f"Pattern Applied: {pattern}->{replacement}\n\n")
                    processed_word = new_word
                except re.error as e:
                    print(f"Regex error for pattern '{pattern}': {e}")
            processed_words.append(processed_word)
    return processed_words


if __name__ == "__main__":
    file_path = "ODS/Silaba.ods"  # Replace with your ODS file path
    folha_palavras = "Palavras"  # Replace with the desired sheet name
    folha_expressoes = "ExpressoesSilaba"

    words_list = load_column_to_list(file_path, folha_palavras)
    regex_dict = load_regex_to_dict(file_path, folha_expressoes)

    if words_list and regex_dict:
        processed_words = apply_patterns_to_words(words_list, regex_dict)
        print("Original Word -> Processed Word")
        for original, processed in zip(words_list, processed_words):
            print(f"{original} -> {processed}")

