from configparser import ConfigParser as cfpr

config = cfpr()

# config['DATABASE'] = {
#     'login': 'root',
#     'pass': '12345',
#     'host': 'localhost',
#     'database': 'test_db'
# }
#
# with open('config.ini', 'w', encoding='utf8') as config_file:
#     config.write(config_file)

# config.read('config.ini')
# config.add_section('NEWLOGIN')
# config.set('NEWLOGIN', 'login', 'my_new_login')
# print(config['NEWLOGIN']['login'])
#
# with open('config.ini', 'w', encoding='utf8') as config_file:
#     config.write(config_file)