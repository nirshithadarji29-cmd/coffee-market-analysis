import os

print("Current Working Directory:")
print(os.getcwd())

print("\nFiles in current directory:")
print(os.listdir())

data_path = os.path.join(os.getcwd(), "data")

print("\nData folder exists:", os.path.exists(data_path))

if os.path.exists(data_path):
    print("\nFiles inside data:")
    print(os.listdir(data_path))