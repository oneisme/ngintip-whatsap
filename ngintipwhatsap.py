
#coding: utf-8
# Developer: godeyes
# Version: 1.0
from selenium import webdriver
import os, time

driver = webdriver.Firefox()

if driver:
	driver.get('https://web.whatsapp.com/')
	flag = True
else:
	print('\n\033[01;31m[!]\033[00;00m Erro ao encontrar o webdriver em seu Firefox!\n\033[01;32m[*]\033[00;00m Versão recomendada: \033[01;32m52.6\033[00;00m\n\033[01;31m[!]\033[00;00m Sua versão: \033[01;31m{}\033[00;00m'.format(android.system('firefox --version')))
	flag = False

try:
	if flag == True:
		def main():
			os.system('clear')
print('''\033[01;32m
================\
╦ ╦┬ ┬┌─┐┌┬┐    \
║║║├─┤├─┤ │      \
╚╩╝┴ ┴┴ ┴ ┴       \
╦ ╦┬ ┬┌─┐┌┬┐      /
║║║├─┤├─┤ │      /
╚╩╝┴ ┴┴ ┴ ┴     /
================/
    \033[01;31m by godeyes v1.0
		\033[00;00m''')
			time.sleep(0.5)

			print('\033[01;32m[*]\033[00;00m Leia o QRCode')

			naza_gai = input('\033[01;34m[+]\033[00;00m Nomere koncomu utowo group: ')
			lawliet_viad = input('\033[01;34m[+]\033[00;00m Pesene piye: ')
			ian_tetud = int(input('\033[01;34m[+]\033[00;00m Piro sih pesen sing meh dikirim: '))

			try:
				user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(naza_gai))
				user.click()

				for i in range(ian_tetud):
					msg_box = driver.find_element_by_class_name('input-container')
					msg_box.send_keys(lawliet_viad)
					botao = driver.find_element_by_class_name('compose-btn-send')
					botao.click()

					print('\033[01;32m[*]\033[00;00m Pesenmu wis sukses terkirim!')

				input("\033[01;35m[*]\033[00;00m Pressione \033[01;33m[ENTER]\033[00;00m selanjutnya...")
				main()
			except:
				print('\033[01;31m[!]\033[00;00m Obrolan whatsap!')
				input("\033[01;35m[*]\033[00;00m Pressione \033[01;33m[ENTER]\033[00;00m selanjutnya...")
				main()

		main()
	else:
		exit(1)
except KeyboardInterrupt:
	print("\n\033[01;31m[!]\033[00;00m Você decidiu sair!")
