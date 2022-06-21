'''

@Code By Hikmat
Dilarang Keras Merecode Script Ini!! 
Anda Tidak Malu Kah? 
Saya Capek Buat Script Ini Bang:)
Hargai Author Yang Sudah Capek² Membuat Script
Emng Kontol Lu Yak Yang Jual Script Ane
Fb : HIKMAT XF
Coding : utf-8
python 3

'''


## [ Import Bahan² Penting ] ##

import bs4
import requests 
import rich as duid
import os
import sys
import random
import datetime
import time
import re
import json
import stdiomask
import threading
## [ Penginstallan Module Rich ] ##

try:
	import rich
except ImportError:
	print(" Anda belum menginstall module rich ")
	print(" Module rich sedang diinstall ")
	os.system("pip install rich")
	
## [ Penginstallan Module Requests ] ##

try:
	import requests
except ImportError:
	print(" Anda belum menginstall module requests ")
	print(" Module requests sedang diinstall ")
	os.system("pip install requests")
	
## [ Penginstallan Module Bs4 ] ##

try:
	import bs4
except ImportError:
	print(" Anda belum menginstall module bs4 ")
	print(" Module bs4 sedang diinstall ")
	os.system("pip install bs4")
	
## [ Penginstallan Module Mechanize ] ##

try:
	import mechanize
except ImportError:
	print(" Anda belum menginstall module mechanize ")
	print(" Module mechanize sedang diinstall ")
	os.system("pip install mechanize")
	
## [ Penginstallan Module Futures ] ##
	
try:
	import futures
except ImportError:
	print(" Anda belum menginstall module futures ")
	print(" Module futures sedang diinstall ")
	os.system("pip install futures")

## [ Penginstallan Module Stdiomask ] ##

try:
	import stdiomask
except ImportError:
	print(" Anda belum menginstall module stdiomask ")
	print(" Module stdiomask sedang diinstall ")
	os.system("pip install stdiomask")
	
	
## [ Penyatuan Bahan² Rich ] ##

from rich.table import Table as table
from rich.console import Console as console
from rich.console import Group as grup_rich
from rich.panel import Panel as panel
from rich.markdown import Markdown as mark
from rich.columns import Columns as columns
from rich.text import Text as text_rich
from rich import print as vprint
## [ Bahan² Disatukan ] ##

from random import randint
from concurrent.futures import ThreadPoolExecutor as tread
from bs4 import BeautifulSoup as biutipulsop

## [ Tanggal + Tahun + Bulan ] ##
komen = []
komengrup = []
FR = {'1':'Januari','2':'Februari','3':'Maret','4':'April','5':'Mei','6':'Juni','7':'Juli','8':'Agustus','9':'September','10':'Oktober','11':'November','12':'Desember'}
tgl = datetime.datetime.now().day
bln = FR[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
sekarang = "─>> "+str(tgl)+"-"+str(bln)+"-"+str(thn)

## [ Bahan² Header Cookie Dsb ] ##

m_fb = 'm.facebook.com'
url_businness = "https://business.facebook.com"
ua_business = "Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36"
web_fb = "https://www.facebook.com/"
m_feb = "https://m.facebook.com/"
mbasic = 'mbasic.facebook.com'
free_fb = 'free.facebook.com'
iphone = 'IPhone.facebook.com'
b_api = 'bapi.facebook.com'
touch = 'touch.facebook.com'
x_fb = 'x.facebook.com'
d_fb = 'd.facebook.com'
head_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]"}

def clear():
	os.system("clear")
def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e);sys.stdout.flush();time.sleep(0.01)

## [ Warna² Random ] ##

P = "\x1b[0;97m" # Putih
M = "\x1b[0;91m" # Merah
H = "\x1b[0;92m" # Hijau
K = "\x1b[0;93m" # Kuning
B = "\x1b[0;94m" # Biru
U = "\x1b[0;95m" # Ungu
O = "\x1b[0;96m" # Biru Muda
N = "\033[0m"    # Warna Mati
pink = "[deep_pink3]"

## [ Logo Script BFH ] ##
def logo():
	print(f"""
  {P}_______    {H}_______   {M}___ ___ 
 {P}|   _   \  {H}|   _   | {M}|   Y   |
 {P}|.  1   /  {H}|.  1___| {M}|.  1   |
 {P}|.  _   \  {H}|.  __)   {M}|.  _   |
 {P}|:  1    \ {H}|:  |     {M}|:  |   |
 {P}|::.. .  / {H}|::.|     {M}|::.|:. |
 {P}`-------'  {H}`---'     {M}`--- ---' 
{K}Moga aja cookie nya awet coy {P}[ {H}Versi 0.3.1 {P}]""")

## [ Garis² Untuk Memperindah:v ] ##

maling_pangsit = " "+P+"("+H+"•"+K+"•"+M+"•"+P+")"

## [ Cek Login Cookie ] ##

def cek_login():
		try:
			token  = open('token.txt','r').read()
			cookie = {'cookie':open('cookie.txt','r').read()}
			#cookie.append(cookie)
			try:
				token  = open('token.txt','r').read()
				cookie = {'cookie':open('cookie.txt','r').read()}
				get  = requests.Session().get('https://graph.facebook.com/me?fields=name,id&access_token=%s'%(token),cookies=cookie)
				menu()
			except (KeyError):
				jalan(maling_pangsit+" Cookie kadaluarsa")
				os.system('rm -rf cookie.txt')
				os.system('rm -rf token.txt')
				login()
			except requests.exceptions.ConnectionError:
				jalan(maling_pangsit+" Koneksi Internet Bermasalah")
				exit()
		except IOError:
			login()

## [ Fitur Login Dsb ] ##
def login():
	logo()
	jalan(maling_pangsit+" Selamat datang di sc "+H+"Zmbf")
	print(P+" ["+O+"01"+P+"] Login with"+H+" cookie")
	print(P+" ["+O+"02"+P+"] Cara menggunakan script"+H+" Zmbf")
	print(P+" ["+M+"00"+P+"] Exit")
	gk_nanya = input(maling_pangsit+" Pilih :"+H+" ")
	if gk_nanya in ["1","01","a"]:
		login_cookie()
	elif gk_nanya in ["2","02","b"]:
		cara_menggunakan()
	elif gk_nanya in ["0","00","c"]:
		print(maling_pangsit+P+" Anda yakin ingin keluar"+P+"("+H+"y"+P+"/"+M+"t"+P+")?")
		tanya_balek = input(maling_pangsit+" Pilih :"+H+" ")
		if tanya_balek in ["y","Y","ya","Yes","yes"]:
			jalan(maling_pangsit+" Terimakasih sudah menggunakan sc "+H+"Zmbf")
			input(maling_pangsit+" Enter untuk keluar")
			exit()
		elif tanya_balek in ["2","02","b"]:
			input(maling_pangsit+" Enter untuk kembali")
			login()
		else:
			jalan(maling_pangsit+" Isi yang benar")
			login()
	else:
		jalan(maling_pangsit+" Isi yang benar")
		login()
	
## [ Cara Menggunakan ] ##
	
def cara_menggunakan():
	jalan(maling_pangsit+" Cara menggunakan script"+H+" Zmbf"+P)
	cui = "Pertama kamu harus login untuk ke menu fitur BFH\nLogin nya ada fitur login cookie.. Pilihlah salah satu fitur login itu..\nKalo mau ambil cookie ada extension nya\nExtension cookie ─> Cookiedough\nTapi kamu harus donwload aplikasi ─> Kiwi Browser ada di playstore\nMau ambil extension cookie cari aja di Chrome Web Store di Kiwi Browser"
	arghh = panel(cui, style='white')
	vprint(panel(arghh, title='[bold yellow]Cara menggunakan[/bold yellow]'))
	cuy = "Masih belum paham? ketik ─> Chat untuk ngechat author untuk pahami lebih lanjut tentang script BFH dan script lainnya..\nAtau ketik ─> Kembali untuk kembali ke menu login"
	arghh = panel(cuy, style='white')
	vprint(panel(arghh, title='[bold red]Chat author[/bold red]'))
	cok = input(maling_pangsit+" Masukan pilihan :"+H+" ")
	if cok in ["chat","Chat","CHAT"]:
		jalan(maling_pangsit+" Ini nomor whastapp admin ─> "+H+"+62 821-1541-3282\n"+P+"Chat aja kalo ada kepentingan atau mau ditanyakan ke author"+H+" BFH")
		input(maling_pangsit+" Enter untuk kembali")
		login()
	elif cok in ["kembali","Kembali","KEMBALI"]:
		login()
	else:
		jalan(maling_pangsit+" Isi Yang Benar")
		login()
	
## [ Login Cookie ] ##

def login_cookie():
	jalan(maling_pangsit+ " Jangan pake akun pribadi!! harus pake akun tumbal untuk ambil cookie")
	cookie = str(input(maling_pangsit+" Masukkan cookie :"+H+" "))
	with requests.Session() as xyz:
		try:
			get_tok = xyz.get(url_businness+'/business_locations',headers = {"user-agent":ua_business,"referer": web_fb,"host": "business.facebook.com","origin": url_businness,"upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","content-type":"text/html; charset=utf-8"},cookies = {"cookie":cookie})
			token = re.search("(EAAG\w+)", get_tok.text).group(1)
			open('cookie.txt','w').write(cookie) 
			open('token.txt','w').write(token)
			jalan(maling_pangsit+" Login sukses "+H+"√")
			input(maling_pangsit+" Enter untuk melanjutkan ke menu ")
			menu()
		except requests.exceptions.ConnectionError:
			jalan(maling_pangsit+"\n Tidak ada koneksi internet ")
			exit()
		except (KeyError,IOError):
			jalan(maling_pangsit+"\n Cookie [ %s%s%s ] %sInvalid"%(H,cookie,P,M))
			os.system("rm -rf cookie.txt")
			os.system("rm -rf token.txt")
			login()

## [ Fitur Menu Dsb ] ##

def menu():
	os.system("clear")
	logo()
	token  = open('token.txt','r').read()
	cookie = {'cookie':open('cookie.txt','r').read()}
	cookie2 = open('cookie.txt','r').read()
	get  = requests.Session().get('https://graph.facebook.com/me?fields=name,id&access_token=%s'%(token),cookies=cookie)
	jsx = json.loads(get.text)
	nama = jsx["name"]
	tumbal_id = jsx["id"]
	xn = requests.Session().get('https://graph.facebook.com/me?access_token=%s'%(token),cookies=cookie)
	x = json.loads(xn.text)
	lis = x["link"]
	try:co = x["email"]
	except (KeyError,IOError):
		co = M+"-"+P
	try:pko = x["birthday"]
	except (KeyError,IOError):
		pko = M+"-"+P
	try:lok = x["locale"]
	except (KeyError,IOError):
		lok = M+"-"+P
	jalan(maling_pangsit+" Selamat datang [ " +H+nama+P+" ]")
	print(maling_pangsit+" Link facebook [ %s%s%s ]"%(H,lis,P))
	print(maling_pangsit+" Email facebook [ %s%s%s ]"%(H,co,P))
	print(maling_pangsit+" Lokasi facebook [ %s%s%s ]"%(H,lok,P))
	print(maling_pangsit+" Tanggal facebook [ %s%s%s ]"%(H,pko,P))
	print(maling_pangsit+" ID [ "+H+tumbal_id+P+" ]")
	#print(maling_pangsit+" Cookie [ %s%s%s ]"%(H,cookie2,P))
	#print(maling_pangsit+" Token  [ %s%s%s ]"%(H,token,P))
	print(maling_pangsit+" Jam [ "+H+datetime.datetime.now().strftime('%H:%M:%S')+P+" ]")
	print(maling_pangsit+" Tanggal [ "+H+sekarang+P+" ]") 
	print(maling_pangsit+" Status login  : Cookie"+H+" active")
	print("")
	jalan(maling_pangsit+" Mohon bersabar karena script ini sedang tahap pengembangan. Klo ada yang error mohon dimaklumi:) ")
	print(P+" ["+O+"01"+P+"] Bot share public ")
	print(P+" ["+O+"02"+P+"] Bot komen public ")
	print(P+" ["+O+"03"+P+"] Bot komen profil ")
	print(P+" ["+O+"04"+P+"] Bot komen grup ")
	#print(P+" ["+O+"05"+P+"] Bot komen public ")
	print(P+" ["+O+"05"+P+"] Bot likes public")
	mattzy = input(maling_pangsit+" Pilih :"+H+" ") 
	if mattzy in ["1","01"]:
		share()
	elif mattzy in ["2","02"]:
		komen_public()
	elif mattzy in ["3","03"]:
		komen_profil()
	elif mattzy in ["4","04"]:
		komen_grup()
	elif mattzy in ["5","05"]:
		jalan(maling_pangsit+" Fitur ini sedang tahap pengembangan mohon pakai fitur lainnya yakk")
		input(maling_pangsit+" Enter untuk kembali")
		menu()
	else:
		jalan(maling_pangsit+" Isi yang benar")
		menu()

def run(link, cookie):
	token = open('token.txt','r').read()
	cookie = open('cookie.txt','r').read()
	coki = {"cookie":cookie}
	while True:
		headers = {'authority': 'graph.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?0','user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.66 Safari/537.36',}
		try:
			response = requests.post('https://graph.facebook.com/me/feed?link=%s&published=0&access_token=%s'%(link,token),cookies=coki, headers=headers)
			print(response.text)
			if "Kami membatasi seberapa sering Anda dapat memposting, berkomentar, atau melakukan hal-hal lain dalam jumlah waktu tertentu guna membantu melindungi komunitas dari spam. Anda bisa mencoba lagi nanti. Pelajari Selengkapnya" in response.text:
				clear()
				print(maling_pangsit+" Anda terkena spam!! mode pesawat 5 detik atau diemin 1 hari jangan maksain!!")
		except:
			sys.exit()

def share():
	#token = open('token.txt','r').read()
	#cookie = open('cookie.txt','r').read()
	#coki = {"cookie":cookie}
	cookie = str(input(maling_pangsit+" Masukkan cookie :"+H+" "))
	with requests.Session() as xyz:
		try:
			get_tok = xyz.get(url_businness+'/business_locations',headers = {"user-agent":ua_business,"referer": web_fb,"host": "business.facebook.com","origin": url_businness,"upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","content-type":"text/html; charset=utf-8"},cookies = {"cookie":cookie}) 
			token = re.search("(EAAG\w+)", get_tok.text).group(1)
			open('cookie.txt','w').write(cookie)
			open('token.txt','w').write(token)
		except (KeyError,IOError):
			jalan(maling_pangsit+"\n Cookie [ %s%s%s ] %sInvalid"%(H,cookie,P,M))
			os.system("rm -rf cookie.txt")
			os.system("rm -rf token.txt")
			login()
	link = input(maling_pangsit+" Link postingan public :"+H+" ")
	print(maling_pangsit+" Minimal"+H+" 2")
	number_thread = int(input(maling_pangsit+" Mau berapa yang mau dishare :"+H+" "))
	for i in range(number_thread):
		thread = threading.Thread(target=run, args=(link, cookie))
		thread.start()
		
def komen_profil():
	try:
		token = open('token.txt','r').read()
		cookie = open('cookie.txt','r').read()
		coki = {"cookie":cookie}
	except IOError:
		jalan(maling_pangsit+" Cookie kadaluarsa")
		os.system('rm -rf cookie.txt')
		os.system('rm -rf token.txt')
		login()
	print(maling_pangsit+" Harap gunakan '<>' untuk membuat garis baru")
	ide = input(maling_pangsit+' ID target   :'+H+' ')
	km = input(maling_pangsit+' Komentar    :'+H+' ')
	limit = input(maling_pangsit+" Limit       :"+H+' ')
	km=km.replace('<>','\n')
	try:
		p = requests.get("https://graph.facebook.com/%s?fields=feed.limit(%s)&access_token=%s"%(ide,limit,token),cookies=coki)
		a = json.loads(p.text)
		jalan(maling_pangsit+"\n Komentar anda sedang di proses...\n")
		for s in a['feed']['data']:
			f = s['id']
			komen.append(f)
			requests.post("https://graph.facebook.com/%s/comments?message=%s&access_token=%s"%(f,km,token),cookies=coki)
			print(maling_pangsit+' Komentar '+H+''+km.replace('\n',' ')+''+P+' terkirim')
		print(maling_pangsit+"\r Komentar selesai "+str(len(komen)))
		input(maling_pangsit+"\n Tekan enter untuk kembali ke menu ")
		menu()
	except KeyError:
		print(maling_pangsit+" ID tidak ditemukan!")
		input(maling_pangsit+"\n Tekan enter untuk kembali ke menu ")
		menu()
		

#### BOT KOMEN TARGET ####
def komen_public():
	try:
		token = open('token.txt','r').read()
		cookie = open('cookie.txt','r').read()
		coki = {"cookie":cookie}
	except IOError:
		jalan(maling_pangsit+" Cookie kadaluarsa")
		os.system('rm -rf cookie.txt')
		os.system('rm -rf token.txt')
		login()
	print(maling_pangsit+" Harap gunakan '<>' untuk membuat garis baru")
	ide = input(maling_pangsit+" ID target :"+H+" ")
	idp = input(maling_pangsit+" ID postingan :"+H+" ")
	km = input(maling_pangsit+" Komentar :"+H+" ")
	limit = input(maling_pangsit+" Limit :"+H+" ")
	km=km.replace('<>','\n')
	try:
		p = requests.get("https://graph.facebook.com/%s?fields=feed.limit(%s)&access_token=%s"%(ide,limit,token),cookies=coki)
		a = json.loads(p.text)
		print(maling_pangsit+"\n Komentar anda sedang di proses...\n")
		for s in a['feed']['data']:
			f = s['id']
			komen.append(idp)
			requests.post("https://graph.facebook.com/%s/comments?message=%s&access_token=%s"%(idp,km,token),cookies=coki)
			print(maling_pangsit+' Komentar '+H+''+km.replace('\n',' ')+''+P+' terkirim')
		print(maling_pangsit+"\r Komentar selesai "+str(len(komen)))
		input(maling_pangsit+"\n Tekan enter untuk kembali ke menu ")
		menu()
	except KeyError:
		print(maling_pangsit+" ID tidak ditemukan!")
		input(maling_pangsit+" Tekan enter untuk kembali ke menu ")
		menu()

#### BOT KOMEN GRUP ####
def komen_grup():
	try:
		token = open('token.txt','r').read()
		cookie = open('cookie.txt','r').read()
		coki = {"cookie":cookie}
	except IOError:
		jalan(maling_pangsit+" Cookie kadaluarsa")
		os.system('rm -rf cookie.txt')
		os.system('rm -rf token.txt')
		login()
	print(maling_pangsit+" Harap gunakan '<>' untuk membuat garis baru")
	ide = input(maling_pangsit+' ID grup     :'+H+' ')
	km = input(maling_pangsit+' Komentar    :'+H+' ')
	limit = raw_input(maling_pangsit+" Limit       :"+H+' ')
	km=km.replace('<>','\n')
	try:
		r=requests.get('https://graph.facebook.com/group/?id=%s&access_token=%s'%(ide,token),cookies=coki)
		asw=json.loads(r.text)
	except KeyError:
		print(maling_pangsit+" Grup tidak ditemukan!")
		input(maling_pangsit+"\n Tekan enter untuk kembali ke menu ")
		menu()
	try:
		p = requests.get("https://graph.facebook.com/v3.0/%s?fields=feed.limit(%s)&access_token=%s"%(ide,limit,token),cookies=coki)
		a = json.loads(p.text)
		jalan(maling_pangsit+"\n Komentar anda sedang di proses...\n")
		for s in a['feed']['data']:
			f = s['id']
			komengrup.append(f)
			requests.post("https://graph.facebook.com/%s/comments?message=%s&access_token=%s"%(f,km,token),cookies=coki)
			print(maling_pangsit+' Komentar '+H+''+km.replace('\n',' ')+''+P+' terkirim')
		print(maling_pangsit+"\r Komentar selesai "+str(len(komengrup)))
		input(maling_pangsit+"\n Tekan enter untuk kembali ke menu ")
		menu()
	except KeyError:
		print(maling_pangsit+" Grup tidak ditemukan!")
		input(maling_pangsit+"\n Tekan enter untuk kembali ke menu ")
		menu()

cek_login()