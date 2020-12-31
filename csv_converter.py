# Python program to convert 
# JSON file to CSV 

import json 
import csv 

"""def json_to_csv(game_results):
    data = game_results
    with open('my_json.txt', 'w') as fp:
        json.dump(data, fp)
"""    
def update_csv():
  # Opening JSON file and loading the data 
  # into the variable data 
  with open('game_results.json') as json_file: 
      data = json.load(json_file) 
    
  # now we will open a file for writing 
  #The 'w' arg is for overwriting while the 'a+' arg is for appending
  data_file = open('data_file.csv', 'a+') 

  #print(data)

  # create the csv writer object 
  csv_writer = csv.writer(data_file) 
    
  # Counter variable used for writing  
  # headers to the CSV file 
  count = 1
    
  for key in data:
      if count == 0: 
    
          # Writing headers of CSV file 
          header = data[key].keys() 
          csv_writer.writerow(header) 
          count += 1
      
      #print(data[key].values())
      # Writing data of CSV file 
      csv_writer.writerow(data[key].values()) 
    
  data_file.close() 
  return
