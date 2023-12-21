#!/bin/python3
import pyfiglet

text = "KAWAII IP FETCHER"
ascii_art = pyfiglet.figlet_format(text)
print(ascii_art)




import urllib.request

external_ip = urllib.request.urlopen('https://ipv4.icanhazip.com/').read().decode('utf8')
def nl(): print('\n')


matrix = "Follow the white rabbit"
ascii1 = """ (\ /) """
ascii2 = """ ( . .) """
ascii3 = """C(")(") """
print(matrix)
nl()
print(ascii1)
print(ascii2)
print(ascii3)
nl()
print("Your ip address is : " + format(external_ip))


