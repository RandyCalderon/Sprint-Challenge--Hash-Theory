def get_indices_of_item_weights(weights, limit):
  weight = {}

  #for every item weight in the weights list 
  for i in range(len(weights)):
    # if the weights list is not found in the dictionary
    if weights[i] not in weight:
      weight[weights[i]] = i

    include = limit - weights[i]

    if include in weight and weight[include] != i:
      return (i, weight[include])
  return ()

if __name__ == '__main__':
  # You can write code here to test your implementation using the Python repl
  pass 

# Store each weight's list index as the value for example weight = index[2]   