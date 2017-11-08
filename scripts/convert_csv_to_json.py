import sys, argparse
import csv
import json

def convert_file_to_json(csvFile):
   try:
      with open(csvFile, 'r') as f:
         reader = csv.reader(f, delimiter=' ')
         data_list = list()

         for row in reader:
            data_list.append(row)

      data = [dict(zip(data_list[0],row)) for row in data_list]
      data.pop(0)
   except IOError:
      print('File: ' + csvFile + ' not found!')

   boroughs = findBoroughs(data)
   jsonFile = createJsonFileName(data[0])

   try:
      with open(jsonFile, 'w') as f:
         # header is just the json file name without the .json extension
         header = jsonFile[:-5]
         f.write("{\n   \"" + header + "\" : {\n")
         for boroughNdx, borough in enumerate(boroughs):
            f.write("      \"" + borough + "\" : {\n")
            boroughData = getSubset(borough, data)
            for dataNdx, entry in enumerate(boroughData):
               if borough == entry["Borough"]:
                  key = validateKey(entry["linkName"])
                  f.write("         \"" + key + "\" : {\n")

                  for entryNdx, value in enumerate(entry):
                     f.write("            \"" + value + "\" : " + json.dumps(entry[value]))
                     if entryNdx == len(entry) - 1:
                        f.write("\n")
                     else:
                        f.write(",\n")
                  if dataNdx == len(boroughData) - 1:
                     f.write("         }\n")
                  else:
                     f.write("         },\n")

            if boroughNdx == len(boroughs) - 1:
               f.write("      }\n")
            else:
               f.write("      },\n")
         f.write("   }\n}")

   except IOError:
      print('File: ' + jsonFile + ' failed to be created')

def validateKey(key):
   if "." in key:
      key = key.replace(".", " ")
      #print("Key contains period")
   if "/" in key:
      key = key.replace("/", "|")
      #print("Key contains slash")
   if "$" in key:
      print("Key contains $")
   if "#" in key:
      print("Key contains #")
   if "[" in key:
      print("Key contains [")
   if "]" in key:
      print("Key contains ]")

   return key


def getSubset(borough, data):
   subset = []

   for entry in data:
      if entry["Borough"] == borough:
         subset.append(entry)

   return subset

def findBoroughs(data):
   boroughs = []

   for entry in data:
      borough = entry["Borough"]

      # Quick Fix to the Staten Island naming problem
      if borough == "Staten island":
         borough = "Staten Island";
         entry["Borough"] = borough

      if borough not in boroughs:
         boroughs.append(borough)

   return boroughs

def createJsonFileName(entry):
   info = entry["DataAsOf"].split()
   date_parts = info[0].split("/")
   month = date_parts[0]
   day = date_parts[1] if len(date_parts[1]) == 2 else "0" + date_parts[1]
   year = date_parts[2]
   date = year + "_" + month + "_" + day

   time = info[1].replace(":", "_")[:-3]

   return  date + "_" + time + ".json"

def main():
   parser = argparse.ArgumentParser()
   parser.add_argument('csvFile')
   options = parser.parse_args()

   convert_file_to_json(options.csvFile)

if __name__ == '__main__':
   main()
