with open("tambol_deta.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

sorted_numbers = sorted((int(line.split()[0]) for line in lines), reverse=True)

with open("a_list.txt", "w", encoding="utf-8") as output_file:
    for number in sorted_numbers:
        output_file.write(f"{number}\n")

print("Big to small a_list.")