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
                current_key = line.split()[0].split("#")[1].strip().replace(":",'')
                current_value = []
            elif line:  # Check if the line is not empty or just spaces
                current_value.append(line)

    # Add the last entry to the dictionary
    if current_key is not None:
        result_dict[current_key] = current_value

    return result_dict


def nb_anaphora (corpus):
  count = 0
  for sentence in corpus:
    anaphora = False
    for tup in corpus[sentence]:
      tup = tup.split()
      for word in tup:
        if "/" in word:
          anaphora = True
          break
      if anaphora:
        count += 1
        break

  return count


def avg_tuples_per_sentence(corpus):
  total = 0
  for sentence in corpus:
    total += len(corpus[sentence])

  return round(total/len(corpus), 2)


def dist_elements_per_tuple(corpus):
  dist = {}
  for sentence in corpus:
    for tup in corpus[sentence]:
      tup = tup.split('<TAB>')
      if len(tup) not in dist:
        dist[len(tup)] = 0
      dist[len(tup)] += 1
      if len(tup) == 1:
        print(tup)
  
  return dist

corpus = parse_txt_file("IE_AKGC_GOLD.txt")
