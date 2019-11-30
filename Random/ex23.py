#Exercise 20:



def count_name(text):
  names_count =0
  names_count = len(text.splitlines())
  return names_count

def read_from_file():
  with open( 'nameslist.txt', 'r') as open_file:
    return open_file.read()

if __name__ == "__main__":
    text = read_from_file()
    name_count = count_name(text)
    print(str(name_count) + " names in files")