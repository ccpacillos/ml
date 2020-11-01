import pprint
import random
from lib import csv_helper
from lib import vectors
from modifiers import credit
from lib import model

pp = pprint.PrettyPrinter(width=150)

training_data_csv = csv_helper.csv_to_dict_list('datasets/training.csv')
test_data_csv = csv_helper.csv_to_dict_list('datasets/test.csv')

training_data = vectors.to_vectors(credit.modifier, training_data_csv)
test_data = vectors.to_vectors(credit.modifier, test_data_csv)

params = model.train(training_data, 8, 'class')

weights = params['weights']
bias = params['bias']
features = params['features']

# pp.pprint(bias)
# pp.pprint(weights)
predictions = list(map(lambda example: model.test(
    weights, bias, features, example['class'], example), test_data)
)

correct = list(
    filter(lambda pred: pred == True, predictions)
)

accuracy = (len(correct) / len(test_data)) * 100
pp.pprint(accuracy)
