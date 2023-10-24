# data = "13432"
while True:
    data = input()
    file_name = "obs1.txt"
    with open(file_name, "w") as file:
        file.write(data)
    print(f"Data has been saved to {file_name}")
