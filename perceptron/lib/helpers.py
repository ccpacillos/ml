import csv


def csv_to_dict_list(file):
  reader = csv.DictReader(open(file, 'r'))
  dict_list = []
  for line in reader:
    dict_list.append(line)
  return dict_list


def examples_to_vectors(modifier, examples):
  return list(map(lambda x: modifier(x), examples))
