def train(data, iterations, label_key):
    weights = {}
    bias = 0
    features = list(filter(lambda key: key != label_key, data[0].keys()))

    for feature in features:
        if feature != label_key:
            weights[feature] = 0

    for _ in range(iterations):
        for example in data:
            activation = compute_activation(weights, bias, features, example)
            y = example[label_key]

            if y * activation <= 0:
                for feature in features:
                    weights[feature] += (y * example[feature])
                bias += y

    return {'weights': weights, 'bias': bias, 'features': features}


def test(weights, bias, features, label, example):
    activation = compute_activation(weights, bias, features, example)
    return activation * label > 0


def compute_activation(weights, bias, features, example):
    summation = 0
    for feature in features:
        feature_value = example[feature]
        weight = weights[feature]
        weighted_value = feature_value * weight
        summation += weighted_value

    return summation + bias
