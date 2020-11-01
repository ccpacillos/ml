import csv


def csv_to_dict_list(file):
  reader = csv.DictReader(open(file, 'r'))
  dict_list = []
  for line in reader:
    dict_list.append(line)
  return dict_list


def dict_list_to_csv(file, data, fieldnames):
  writer = csv.DictWriter(open(file, 'w'), fieldnames)
  writer.writeheader()
  writer.writerows(data)
