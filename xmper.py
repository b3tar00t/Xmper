from faker import Faker

import os

import dumper

os.system("clear")

print("\033[1;33;40m")

os.system("figlet X M P E R ")

print("\033[1;34;40m[\033[1;31;40m+\033[1;34;40m] \033[1;31;40mAuthor : b3tar00t")

print(" ")

print("\033[1;34;40m[\033[1;31;40m+\033[1;34;40m] \033[1;31;40mInstagram : @b3ta_r00t")

print(" ")

print("\033[1;34;40m[\033[1;31;40m+\033[1;34;40m] \033[1;31;40mGithub : https://github.com/b3tar00t")

print(" ")

faker = Faker()

print('\033[1;36;40m ================================================= ')

print(' ')

print(" \033[1;32;40mMale Profile : ")

maleprofile = faker.simple_profile('M')

dumper.dump(maleprofile)

print(' ')

print(' \033[1;36;40m================================================= ')

print(' ')

print(" \033[1;32;40mFemale Profile : ")

femaleprofile = faker.simple_profile('F')

dumper.dump(femaleprofile)

print(' ')
print(" \033[1;32;40mPhone Number : ")
print(f' Phone Number : {faker.phone_number()}')
print(' ')
print(' \033[1;36;40m================================================== ')
print(' ')
print(" \033[1;32;40mCompany Detail : ")
print(f' Company Email : {faker.company_email()}')
print(' ')
print(' \033[1;36;40m================================================== ')
print(' ')
print(" \033[1;32;40mInternet Addresses : ")
print(f' IPv4: {faker.ipv4()}')
print(f' IPv6: {faker.ipv6()}')
print(f' MAC address: {faker.mac_address()}')
print(' ')
print(' \033[1;36;40m=================================================== ')
print(' ')
print(" \033[1;32;40mCurrency :")
print(f' Curreny Name : {faker.currency_name()}')
print(' ')
print(' \033[1;36;40m=================================================== ')
print(' ')
print(" \033[1;32;40mJobs list: ")
print(' ')
for _ in range(5):
   print(faker.job())
   print(' ')
   continue
   print(' \033[1;36;40m=============================================== ')

print(" ")
print(" ")
print(" \033[1;35;40m*Dear user Thank You for using my Tool! If you like it then please follow me on Github and Instagram. ")
print(" ")
print(" ")
