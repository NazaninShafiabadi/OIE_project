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


def string_to_tuple(input_string):
    lines = input_string.strip().split('\n')
    first_three_elements = lines[:3]

    # Check if this is a mono argument relation
    if len(lines) > 3 and (not lines[3].strip() or lines[3].strip().isdigit()):
        tuples = ' <TAB> '.join(first_three_elements)
    else:
        tuples = ' <TAB> '.join(lines)

    return tuples


def parse_reverb_file(file_path):
    data_dict = {}

    with open(file_path, 'r') as file:
        content = file.read().split("raw_files/p7-li_2023_ie-akgc_project-corpus.txt")

        for i, fragment in enumerate(content[1:]):
            lines = fragment.strip().split('\n', 1)

            if len(lines) > 1:
                key = lines[0].strip()
                value = lines[1].strip()

                if key not in data_dict:
                    data_dict[key] = []

                data_dict[key].append(string_to_tuple(value))

    return data_dict


def parse_tuple(input_string):

    elements = input_string.split("<TAB>")

    elements = [elem.strip() for elem in elements if elem]

    return {
        'arg1': elements[0] if len(elements) > 0 else None,
        'rel': elements[1] if len(elements) > 1 else None,
        'arg2': elements[2] if len(elements) > 2 else None,
        'arg3': elements[3] if len(elements) > 3 else None,
        'arg4': elements[4] if len(elements) > 4 else None,
        'arg5': elements[5] if len(elements) > 5 else None
    }


def parse_txt_file_complex(file_path, resolve=False):
    result_dict = {}
    current_key = None
    current_value = []
    sentence_dic = {}

    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line.startswith('#'):

                first_line = line[1:].strip()
                current_key = int(first_line.split(":")[0])
                sentence_dic[current_key]= " ".join(first_line.split(":")[1:])
                current_value = []
            elif line:  # Check if the line is not empty or just spaces
                if resolve:
                    current_value.append(parse_tuple(line))
                else:
                    current_value.append(parse_tuple(clean_tuple(line)))


            if current_key is not None:
                    result_dict[current_key] = current_value

    # Add the last entry to the dictionary
    if current_key is not None:
        result_dict[current_key] = current_value

    return result_dict