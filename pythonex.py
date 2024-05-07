# Given data
data = [
    "sudheer,Sudheer Kumar,1507,1001,76768 07475,94906 81223,Hosa Road,sudhir.april09@gmail.com,enabled",
    "bhagavan,Bhagavan Prasad,1000,1001,99020 96750,,Bommanahalli,,enabled",
    "sai,Sai Kumar,1000,1001,99457 08707,,Bangalore, ,enabled",
    "pavan,Pavan Kumar,1500,1001,98863 04081,,Bommanahalli,,enabled",
    "bhag,Prasad,1000,1001,9902096750,,Bommanahalli,,enabled",
    "harsha,Harsha Vardhan,1501,1001,9902369277,,Bommanahalli,,enabled",
    "mohansai,Mohan Sai,1503,1001,9379741678,,Bommanahalli,,enabled",
    "swathi,Swathi,1504,1001,9902369277,,Marathahalli,,enabled",
    "prasad,Prasad,1000,1001,67890234,9902096750,Bommanahalli,,enabled",
    "warun,Warun Kumar,1505,1001,81471 37168,,Maruthi Nagar,warun_0452@hotmail.com,enabled",
    "Vachan,Vachan,1000,1001,99020 96750,9902096750,Bommanahalli,,enabled",
    "sudeep,Sudheep Reddy,1506,1001,97421 88842,,Bommanahalli,sudeepreddy4@gmail.com,enabled",
    "Saketh,Saketh,1000,1001,,9902 096 750,Bommanahalli,,enabled",
    "mayuri,P Mayuri,1508,1001,990 236 9277,00000 00000,BTM Layout,mayurireddy86@gmail.com,enabled",
    "haritha,N Haritha,1509,1001,9620447662,00000 00000,BTM Layout,nareddy.haritha14@gmail.com,enabled",
    "prathyusha,M Prathyusha,1510,1001,,99023 69277,BTM Layout,prathyu_1231@ymail.com,enabled",
    "mohan,C Mohan Krishna,1511,1001,76769 79832,00000 00000,HSR Layout,cmkr2007@gmail.com,enabled",
    "parvathi,Duggi Parvathi,1512,1001,96207 91113,94919 40156,Virathanagara,dparvathi54@gmail.com,enabled",
    "pavithra,V Pavithra,1513,1001,9886885570,,Madiwala,vpavithra233@gmail.com,enabled",
    "kalyan,Kalyan Tej,1514,1001,89511 77217,99489 53809,Bommanahalli,geniuskalyan1@gmail.com,enabled",
    "teja,Teja Kadapa,1515,1001,8123850122,99489 53809,Bommanahalli,teja@gmail.com,enabled",
    "Lavanya,Lavanya D,1234,1000,789067576,08563333456,Chittoor,lavanya@aura.com,enabled"
]

# Function to sort data based on the given fields
def sort_data(data, fields):
    # Split each line into a list of values and sort based on the specified fields
    sorted_data = sorted(data, key=lambda x: [x.split(',')[fields.index(field)] for field in fields])
    return sorted_data

# Fields to sort by
fields_to_sort = ['name', 'fullname', 'uid', 'gid', 'mobile', 'home', 'address', 'email', 'enabled']

# Sort the data based on the specified fields
sorted_data = sort_data(data, fields_to_sort)

# Print the sorted data
for line in sorted_data:
    print(line)
