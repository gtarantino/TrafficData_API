import sys, argparse
import csv
import json

def convert_file_to_json(csvFile, jsonFile):
   try:
      with open(csvFile, 'r') as f:
         reader = csv.reader(f, delimiter=' ')
         data_list = list()

         for row in reader:
            data_list.append(row)

      data = [dict(zip(data_list[0],row)) for row in data_list]
      data.pop(0)
   except IOError:
      print('File: ' + csvFile_no_ext + ' not found!')

   try:
      with open(jsonFile, 'w') as f:
         f.write('[')
         for ndx, entry in enumerate(data):
            f.write(json.dumps(entry))
            if ndx < len(data) - 1:
               f.write(',\n')
            else:
               f.write(']')

   except IOError:
      print('File: ' + jsonFile + ' failed to be created')

def main():
   parser = argparse.ArgumentParser()
   parser.add_argument('csvFile')
   parser.add_argument('jsonFile')
   options = parser.parse_args()

   convert_file_to_json(options.csvFile, options.jsonFile)

if __name__ == '__main__':
   main()
