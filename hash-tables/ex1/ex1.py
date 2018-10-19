def get_indices_of_item_weights(weights, limit):
  #declare dictionary - figure out a better name
  weight = {}

  #for every item weight in the weights list 
  for i in range(len(weights)):
    # if the weights list is not found in the dictionary
    if weights[i] not in weight:
      weight[weights[i]] = i

    # Find the acceptable weight that doesn't exceed the set limit
    include = limit - weights[i]

    # The condition to return the result as a tuple
    if include in weight and weight[include] != i:
      return (i, weight[include])

    # Returns an empty tuple if pair isn't found
  return ()

if __name__ == '__main__':
  # You can write code here to test your implementation using the Python repl
  pass 

# Store each weight's list index as the value for example weight = index[2]   