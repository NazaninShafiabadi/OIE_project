import re

def parse_txt_file(file_path):
    result_dict = {}
    current_key = None
    current_value = []

    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line.startswith('#'):
                if current_key is not None:
                    result_dict[current_key] = current_value
                current_key = line[1:].strip()
                current_value = []
            elif line:  # Check if the line is not empty or just spaces
                current_value.append(line)

    # Add the last entry to the dictionary
    if current_key is not None:
        result_dict[current_key] = current_value

    return result_dict


def clean_square_brackets(input_string):
    clean_string = re.sub(r'\[.*?\]', '', input_string)
    return clean_string


def clean_brackets(input_string):
    clean_string = re.sub(r'\(.*?\)', '', input_string)
    return clean_string


def remove_last_opening_parenthesis(s):
    if "(" in s:
        last_opening_parenthesis_index = s.rfind("(")
        return s[:last_opening_parenthesis_index] + s[last_opening_parenthesis_index+1:]
    else:
        return s


def clean_slash(input_string):
    result_string = ""

    for word in input_string.replace("( ", "(").replace(" )", ")").split() :
      rm_single_bracket = False

      if "/" in word :
        print(word)
        i = word.find('/')
        if word[i+1] != "(" : # we dont need to change anything as brackets will be deleted
            word = word[0:i]

        print("2",word)

        if word [i-1] == ")" :
          print("tubercule")
          word = word.replace(")", "")
          rm_single_bracket = True

        print("3",word)

      word = word.replace("/", "")

      result_string += word + " "
      print(result_string)
      if rm_single_bracket :result_string = remove_last_opening_parenthesis(result_string)

    return result_string


def clean_tuple(tupl) :
  return clean_brackets(clean_slash(clean_square_brackets(tupl)))
