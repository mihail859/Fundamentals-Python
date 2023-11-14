# C:\Internal\training-internal\Template.pptx
input_path = input().split("\\")
needed_information = input_path[-1]
file_name, extension = needed_information.split(".")
print(f"File name: {file_name}")
print("File extension: {}".format(extension))