def not_string(str):
    #this function returns string wit or without not in the front of the text 
  if len(str) >= 3 and str[:3] == "not":
    return str
  return "not " + str
  # str[:3] goes from the start of the string up to but not
  # including index 3