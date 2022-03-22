def parrot_trouble(talking, hour):
    #this function says when parrots are horrible for us
  if ((talking and hour < 7) or (talking and hour > 20)):
    return True
  else:
    return False
