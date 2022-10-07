# file = open('dict/sampleData.tt')
# while opening with invalid extension it will trigger => FileNotFoundError: [Errno 2] No such file or directory: 'dict/sampleData.tt'

try:
    file = open('dict/sampleData.txt')
    print(file.name)
    if file.name == 'dict/sampleData.txt':
        raise Exception  # manually raise the exception, and it goes and print the content under exception block
except FileNotFoundError as error:
    print("Sorry! This file is not exists",
          error)  # Will trigger error if file is not opened with any errors and pass to the next line of logic
except Exception as error:
    print("Something went wrong!", error)  # Will handle the errors instead specifically catch error on file not found
else:
    print(file.read())
    file.close()
finally:
    print(
        "!!!!!!!!Executing Finally!!!!!!!!")  # Will execute at the end of the statements even successful or caught error
