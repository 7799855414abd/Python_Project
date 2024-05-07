import csv

def print_output(final_result):
    for number, names in final_result.items():
        names_string = ", ".join(names)
        print(f"The number {number} was saved with {len(names)} names: {names_string}")


def get_meaningful_result(duplicate_contacts, unique_numbers):
  final_result = {number: [] for number in unique_numbers}
  for i in duplicate_contacts:
    for j in final_result.keys():
      if i[4] == j:
        final_result[j].append(i[0])
  return final_result

    
def get_duplicate_contacts(new_list,numbers_list):
  result_list = []
  unique_numbers = []
  for i in numbers_list:
    count = 0
    for j in new_list:
      if i == j[4]:
        count += 1
        if count > 1:
          result_list.append(j)
          unique_numbers.append(j[4])
  return result_list,unique_numbers
          
def eliminate_gaps_between_number(csv_data):
  new_list = []
  numbers_list = []
  for i in csv_data:
    new_number = i[4].replace(" ","")
    numbers_list.append(new_number)
    i[4] = new_number
    new_list.append(i)
  return new_list, numbers_list


def read_data_from_file():
    jsonData = []
    with open('data.csv', 'rt') as f1:
        csv_reader = csv.reader(f1)
        next(csv_reader)
        for row in csv_reader:  
            jsonData.append(row)  
    return jsonData

csv_data = read_data_from_file()
new_list, numbers_list = eliminate_gaps_between_number(csv_data)
numbers_list = list(set(numbers_list))
duplicate_contacts, unique_numbers = get_duplicate_contacts(new_list,numbers_list)
unique_numbers = list(set(unique_numbers))
final_result = get_meaningful_result(duplicate_contacts, unique_numbers)
print_output(final_result)

  

