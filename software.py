#Question 1
#remove duplicates and print list

genes = ["MLH1", "AHR", "BRCA2", "BRCA1", "MLH1", "CAT"]

genes = list(dict.fromkeys(genes))

print(genes)

#Question 2
#find mean of a column

read_depth = []

#prints data
with open("Gene_RD.txt", "r") as gene_list:
    data = gene_list.readlines()
    print(data)
    
	#removes \n
    data = [i.replace("\n","") for i in data]
    print(data)
    
	#removes headers
    data.pop(0)
    print(data)
    
	#isolates read_depth from gene name
    for gene in data:
        gene = (gene.split(",")[1])
        read_depth.append(gene)
print(read_depth)

#changes read_depth to int
read_depth = [int(k) for k in read_depth]
print(read_depth)

#calculates mean
print(sum(read_depth)/len(read_depth))


#Question 3
# remove all duplicate lines from text file
# you may need to recreate the input file each time this is run

lines_seen = set()

with open("Gene_RD_rpt.txt", "r") as gene_repeat, open("Gene_RD_NoDup.txt", "w") as NoDup:
    for line in gene_repeat:
        if line not in lines_seen:
            NoDup.write(line)
            lines_seen.add(line)

#Question 4
#Write a function that takes as input intergers N and L to generate N million random DNA fragments of length L

#ask for interger N and L

N = int(input("How many million DNA fragments? "))
L = int(input("How long? "))

bases = ["A", "T", "G", "C"]

#randomly generates base

import random
print(random.choice(bases))

#prints bases
def DNA_Fragments(number, length):
    for i in range(0, (number * 100000)):
        print("\n")
        for j in range(0, length):
            print(random.choice(bases), end = " ")

DNA_Fragments(N, L)

#Question 5
#Write a function which expexts, as its input, a dictionary, with names as the keys and ages as the values.
#The function passses back a dictionary of age averages for people aged 10-20, 20-30, and over 30

age_dict = {
    'Hayden Brandt': 10,
    'Lydia Weiss': 13,
    'Jadyn Faulkner': 11,
    'Tatiana Ruiz': 20,
    'Francesca Burnett': 27,
    'James Olsen': 30,
    'Aedan Russo': 32,
    'Shane Key': 55,
    'Cyrus Rodgers': 60,
    'Reina Pace': 81
}

total_10_20 = []
total_20_30 = []
total_30 = []

def age_average(dictionary):
    for value in dictionary.values():
        if value < 20 or value  == 20:
            total_10_20.append(value)
        elif value > 20 and value < 30 or value == 30:
            total_20_30.append(value)
        else:
            total_30.append(value)

age_average(age_dict)
print(total_10_20)
print(total_20_30)
print(total_30)

def average(list):
    return sum(list)/len(list)
    
average_dict = {}
average_dict["age 10-20"] = average(total_10_20)
average_dict["age 20-30"] = average(total_20_30)
average_dict["age 30+"] = average(total_30)


print(average_dict)

