"""
FILE SYSTEMS

'a' - append
'r' - read
'w' - write
'x' - create
# 'r+' read and write

"""

# file = open('text_files//lorem.txt', 'r', encoding='utf8')
# print(file.name)
# print(file.mode)
# print(file.closed)
# file.close()
# print(file.closed)
# some_text = input("Input some text: ")
# with open('text_files//test_file.txt', 'w', encoding='utf8') as file:
    # file_content = file.readlines()
    # for line in file_content:
    #     print(line.rstrip() + "...")
    # file_content = file.readline()
    # print(file_content, end='')
    # file_content2 = file.readline()
    # print(file_content2, end='')
    # print(file.read(3250))
    # file_content = file.read(100)
    # while len(file_content) > 0:
    #     file_content = file.read(100)
    #     print(file_content)
    # file.write(some_text)
# with open('text_files//test_file.txt', 'r', encoding='utf8') as file2:
#     print(file2.read(10))
#     print(file2.seek(0))
#     print(file2.read(10))

# with open('text_files//threemusketeer.txt', 'r', encoding='utf-8') as rfile:
#     with open('text_files//threemusketeerCopy.txt', 'w', encoding='utf8') as wfile:
#         file_content = rfile.read(100)
#         while len(file_content) == 100:
#             wfile.write(file_content)
#             file_content = rfile.read(100)

# with open('text_files//python.jpg', 'rb') as rfile:
#     with open('text_files//python_copy.jpg', 'wb') as wfile:
#         file_content = rfile.read(20)
#         while len(file_content) > 0:
#             wfile.write(file_content)
#             file_content = rfile.read(20)



