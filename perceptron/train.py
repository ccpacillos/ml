def perceptron_train(iterations, features, dataset):
    # initialize weight to 0 for each feature
    # initialize bias to 0
    weights = [0] * len(features)
    bias = 0

    # for 1 to iterations do
    #     for each datapoint (input, output)
    #       activation = (summation (weight of each feature * value of each feature)) + bias
    #       if (output * activation) is less than or equal to zero, which simply means that current prediction is incorrect
    #         update weights of each feature: w_sub_d = w_sub_d + (output * feature_value_of_d)
    #         update bias: b = b + output
    #       end if
    #     end for
    # end for

    for n in range(iterations):

        # return weight for each feature, and bias
