def reconstruct_trip(tickets):

  trips = dict(tickets)

  source = None

  trip = []

  for i in range(len(tickets)):
    if source in trips:
      if trips[source] is not None:
        trip.append(trips[source])
      source = trips[source]
    else: 
      return []
  
  return trip
  pass 

if __name__ == '__main__':
  # You can write code here to test your implementation using the Python repl
  pass
