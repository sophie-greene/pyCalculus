import graphlab
import numpy as np

sales = sales = graphlab.SFrame('/media/sf_ubuntu/Regression/week2/kc_house_data.gl/')

def get_numpy_data(data_sframe, features, output):
    data_sframe['constant'] = 1 # add a constant column to an SFrame
    # prepend variable 'constant' to the features list
    features = ['constant'] + features
    # select the columns of data_SFrame given by the 'features' list into the SFrame 'features_sframe'
    features_sframe = data_sframe[features]
    # this will convert the features_sframe into a numpy matrix with GraphLab Create >= 1.7!!
    features_matrix = features_sframe.to_numpy()
    # assign the column of data_sframe associated with the target to the variable 'output_sarray'
    output_sarray = data_sframe[output]
    # this will convert the SArray into a numpy array:
    output_array = output_sarray.to_numpy() # GraphLab Create>= 1.7!!
    return(features_matrix, output_array)
def predict_output(feature_matrix, weights):
    predictions = np.dot(feature_matrix,weights)
    return(predictions)
'''
(example_features, example_output) = get_numpy_data(sales, ['sqft_living'], 'price') # the [] around 'sqft_living' makes it a list

#print example_features# this accesses the first row of the data the ':' indicates 'all columns'
#print example_output[0] # and the corresponding output
my_weights = np.array([1., 1.]) # the example weights
my_features = example_features[0,] # we'll use the first data point
predicted_value = np.dot(my_features, my_weights)
print predicted_value
test_predictions = predict_output(example_features, my_weights)
print test_predictions[0] # should be 1181.0
print test_predictions[1] # should be 2571.0
my_weights = np.array([1., 1.]) # the example weights
my_features = example_features[0,] # we'll use the first data point
predicted_value = np.dot(my_features, my_weights)
print predicted_value
'''
def feature_derivative(errors, feature):
    # Assume that errors and feature are both numpy arrays of the same length (number of data points)
    # compute twice the dot product of these vectors as 'derivative' and return the value
    derivative = 2 * np.dot(errors,feature)
    return(derivative)
'''
example_features, example_output = get_numpy_data(sales, ['sqft_living'], 'price') 
my_weights = np.array([0., 0.]) # this makes all the predictions 0
test_predictions = predict_output(example_features, my_weights) 
# just like SFrames 2 numpy arrays can be elementwise subtracted with '-': 
errors = test_predictions - example_output # prediction errors in this case is just the -example_output
feature = example_features[:,0] # let's compute the derivative with respect to 'constant', the ":" indicates "all rows"
derivative = feature_derivative(errors, feature)
print derivative
print -np.sum(example_output)*2 # should be the same as derivative
'''
def gradient_descent(feature_matrix, output, initial_weights, step_size, tolerance):
    converged = False 
    cnt=0
    weights = np.array(initial_weights) # make sure it's a numpy array
    while not converged:
        cnt+=1
        # compute the predictions based on feature_matrix and weights using your predict_output() function
        yh = predict_output(feature_matrix,weights)
        # compute the errors as predictions - output
        #print "yh:",yh.shape
        #print output.dtype
        e =  yh -output
        drv = feature_derivative(e, feature_matrix)
        #print "drv" ,drv.shape
        weights = -step_size*drv + weights
           # gradient_sum_squares =np.linalg.norm(x,order=1) # initialize the gradient sum of squares
        # while we haven't reached the tolerance yet, update each feature's weight
        #print weights
        # compute the square-root of the gradient sum of squares to get the gradient matnigude:
        gradient_magnitude =np.sqrt(drv.dot(drv))
        #print gradient_magnitude
        if gradient_magnitude < tolerance:
            converged = True
        if cnt>1000:
            converged=True
    print 'iterations',cnt       
    return(weights)

train_data,test_data = sales.random_split(.8,seed=0)
# let's test out the gradient descent
simple_features = ['sqft_living']
my_output = 'price'
(simple_feature_matrix, output) = get_numpy_data(train_data, simple_features, my_output)
initial_weights = np.array([-47000., 1.])
step_size = 7e-12
tolerance = 2.5e7
def regression_gradient_descent(feature_matrix, output, initial_weights, step_size, tolerance):
    converged = False 
    weights = np.array(initial_weights) # make sure it's a numpy array
    while not converged:
        # compute the predictions based on feature_matrix and weights using your predict_output() function
        yh = predict_output(feature_matrix,weights)
        # compute the errors as predictions - output
        #print yh.dtype
        #print output.dtype
        e = yh -output
        gradient_sum_squares = 0 # initialize the gradient sum of squares
        # while we haven't reached the tolerance yet, update each feature's weight
        for i in range(len(weights)): # loop over each weight
            # Recall that feature_matrix[:, i] is the feature column associated with weights[i]
            # compute the derivative for weight[i]:
            drv = feature_derivative(e, feature_matrix[:,i])
            # add the squared value of the derivative to the gradient magnitude (for assessing convergence)
            gradient_sum_squares += drv ** 2
            # subtract the step size times the derivative from the current weight
            weights [i]= -step_size * drv + weights[i]
        #print weights
        # compute the square-root of the gradient sum of squares to get the gradient matnigude:
        gradient_magnitude = np.sqrt(gradient_sum_squares)
        if gradient_magnitude < tolerance:
            converged = True
    return(weights)
simple_weights= gradient_descent(simple_feature_matrix, output, initial_weights, step_size, tolerance)
print 'simple weights',simple_weights
#print gradient_descent(simple_feature_matrix, output, initial_weights, step_size, tolerance)
(test_simple_feature_matrix, test_output) = get_numpy_data(test_data, simple_features, my_output)
test_simple_weights= gradient_descent(test_simple_feature_matrix, test_output, initial_weights, step_size, tolerance)
print 'test_simple weights',test_simple_weights