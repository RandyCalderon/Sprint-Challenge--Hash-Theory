def reconstruct_trip(tickets):

  trips = dict(tickets)

  source = None

  trip = []

  for i in range(len(tickets)):
    if source in places:
      if places[source] is not None:
        trip.append(places[source])
        source = places[source]
      else: 
        return []
  
  return trip
  pass 

if __name__ == '__main__':
  # You can write code here to test your implementation using the Python repl
  pass
