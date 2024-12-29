import requests, re, time, random, sys, pytz, os, json, uuid, string, urllib
from faker import Faker
from bs4 import BeautifulSoup as bs
from urllib.parse import quote
from datetime import datetime
from rich.console import Console
console = Console()
Ok, Cp, Fail = 0,0,0

P = '\033[0m'
K = '\x1b[1;93m'
H = "\033[32m"
M = '\x1b[1;91m'

POSTS, info = {'STATUS': None}, {}
	
class UserAgentGenerator:
	def __init__(self):
		self.fb_versions = ["486.0.0.66.70", "443.0.0.23.229"]
		self.fbbv_versions = ["480086166", "543547945"]
		self.densities = [2.75, 2.0, 3.0, 2.5, 3.5]
		self.screen_resolutions = [{"width": 1080, "height": 2216}, {"width": 720, "height": 2400}, {"width": 1440, "height": 2280}, {"width": 1280, "height": 1920}]
		self.locales = ["id_ID"]
		self.devices = [
            {"manufacturer": "Xiaomi", "brand": "xiaomi", "model": "Redmi Note 8", "os_version": "9"},
            {"manufacturer": "Xiaomi", "brand": "xiaomi", "model": "2106118C", "os_version": "12"},
            {"manufacturer": "Samsung", "brand": "samsung", "model": "Galaxy S10", "os_version": "12"},
            {"manufacturer": "Samsung", "brand": "samsung", "model": "Galaxy A52", "os_version": "11"},
            {"manufacturer": "Realme", "brand": "Realme", "model": "RMX3868", "os_version": "14"},
            {"manufacturer": "Realme", "brand": "Realme", "model": "RMX2121", "os_version": "11"},
            {"manufacturer": "OPPO", "brand": "OPPO", "model": "CPH2083", "os_version": "9"},
            {"manufacturer": "OPPO", "brand": "OPPO", "model": "A54", "os_version": "11"},
            {"manufacturer": "LGE", "brand": "lge", "model": "LM-V600", "os_version": "10"},
            {"manufacturer": "LGE", "brand": "lge", "model": "LM-G900N", "os_version": "10"},
            {"manufacturer": "Huawei", "brand": "HUAWEI", "model": "P30 Pro", "os_version": "10"},
            {"manufacturer": "Huawei", "brand": "HUAWEI", "model": "Mate 40", "os_version": "11"},
            {"manufacturer": "Apple", "brand": "apple", "model": "iPhone 11", "os_version": "14"},
            {"manufacturer": "Apple", "brand": "apple", "model": "iPhone 12", "os_version": "15"},
            {"manufacturer": "Google", "brand": "google", "model": "Pixel 5", "os_version": "11"},
            {"manufacturer": "Google", "brand": "google", "model": "Pixel 6 Pro", "os_version": "12"},
            {"manufacturer": "Sony", "brand": "sony", "model": "Xperia 1 III", "os_version": "12"},
            {"manufacturer": "Sony", "brand": "sony", "model": "Xperia 5 II", "os_version": "11"},
            {"manufacturer": "Motorola", "brand": "motorola", "model": "Moto G Power", "os_version": "11"},
            {"manufacturer": "Motorola", "brand": "motorola", "model": "Moto G Stylus", "os_version": "10"},
            {"manufacturer": "Nokia", "brand": "nokia", "model": "Nokia 5.3", "os_version": "11"},
            {"manufacturer": "Nokia", "brand": "nokia", "model": "Nokia 7.2", "os_version": "12"},
            {"manufacturer": "Asus", "brand": "asus", "model": "ROG Phone 5", "os_version": "11"},
            {"manufacturer": "Asus", "brand": "asus", "model": "Zenfone 8", "os_version": "12"},
            {"manufacturer": "Vivo", "brand": "vivo", "model": "V21", "os_version": "11"},
            {"manufacturer": "Vivo", "brand": "vivo", "model": "X60 Pro", "os_version": "12"},
            {"manufacturer": "OnePlus", "brand": "oneplus", "model": "9 Pro", "os_version": "12"},
            {"manufacturer": "OnePlus", "brand": "oneplus", "model": "Nord 2", "os_version": "11"},
            {"manufacturer": "Lenovo", "brand": "lenovo", "model": "Legion Duel", "os_version": "11"},
            {"manufacturer": "Lenovo", "brand": "lenovo", "model": "K12 Note", "os_version": "10"},
            {"manufacturer": "Xiaomi", "brand": "xiaomi", "model": "Redmi Note 9", "os_version": "10"},
            {"manufacturer": "Samsung", "brand": "samsung", "model": "Galaxy A72", "os_version": "12"},
            {"manufacturer": "Realme", "brand": "Realme", "model": "RMX3390", "os_version": "12"},
            {"manufacturer": "OPPO", "brand": "OPPO", "model": "Find X3", "os_version": "12"},
            {"manufacturer": "Huawei", "brand": "HUAWEI", "model": "Mate 50", "os_version": "13"},
            {"manufacturer": "Apple", "brand": "apple", "model": "iPhone 13", "os_version": "15"},
            {"manufacturer": "Google", "brand": "google", "model": "Pixel 7", "os_version": "13"},
            {"manufacturer": "Motorola", "brand": "motorola", "model": "Edge 20", "os_version": "12"},
            {"manufacturer": "Sony", "brand": "sony", "model": "Xperia 10 III", "os_version": "11"},
            {"manufacturer": "Asus", "brand": "asus", "model": "Zenfone 9", "os_version": "13"},
            {"manufacturer": "Vivo", "brand": "vivo", "model": "X70 Pro", "os_version": "12"},
            {"manufacturer": "OnePlus", "brand": "oneplus", "model": "8T", "os_version": "12"},
            {"manufacturer": "Lenovo", "brand": "lenovo", "model": "ThinkPad X1", "os_version": "13"},
            {"manufacturer": "Xiaomi", "brand": "xiaomi", "model": "Mi 11", "os_version": "12"},
            {"manufacturer": "Samsung", "brand": "samsung", "model": "Galaxy Z Fold 3", "os_version": "12"},
            {"manufacturer": "Huawei", "brand": "HUAWEI", "model": "P40 Pro", "os_version": "10"},
            {"manufacturer": "Apple", "brand": "apple", "model": "iPhone SE", "os_version": "13"},
            {"manufacturer": "Google", "brand": "google", "model": "Pixel 4a", "os_version": "11"},
            {"manufacturer": "Motorola", "brand": "motorola", "model": "Moto Edge", "os_version": "12"},
            {"manufacturer": "Sony", "brand": "sony", "model": "Xperia 1 II", "os_version": "11"},
            {"manufacturer": "Asus", "brand": "asus", "model": "Zenfone 7 Pro", "os_version": "11"},
            {"manufacturer": "Vivo", "brand": "vivo", "model": "V19", "os_version": "10"},
            {"manufacturer": "OnePlus", "brand": "oneplus", "model": "OnePlus 7T", "os_version": "10"},
            {"manufacturer": "Lenovo", "brand": "lenovo", "model": "Z6 Pro", "os_version": "10"},
            {"manufacturer": "Xiaomi", "brand": "xiaomi", "model": "Redmi 9A", "os_version": "10"}
		]
	
	def _generate_facebook_user_agent(self):
		device = random.choice(self.devices)
		resolution = random.choice(self.screen_resolutions)
		user_agent = (f"[FBAN/FB4A;FBAV/486.0.0.66.70;"f"FBBV/653066364;"f"FBDM/{{density={random.choice(self.densities)},"f"width={resolution['width']}," f"height={resolution['height']}}};"f"FBLC/{random.choice(self.locales)};FBRV/0;FBCR/XL;"f"FBMF/{device['manufacturer']};FBBD/{device['brand']};"f"FBPN/com.facebook.mahos;FBDV/{device['model']};"f"FBSV/{device['os_version']};FBOP/1;FBCA/arm64-v8a:]")
		return user_agent
        
class asset:
	def __init__(self):
		self.useragent = UserAgentGenerator()._generate_facebook_user_agent()
	
	def data_graphql(self, req, id):
		return {'av': id,'__aaid': "0",'__user': id,'__a': "1",'__req': "x",'__hs': re.search('"haste_session":"(.*?)"', str(req)).group(1),'dpr': "3",'__ccg': "EXCELLENT",'__rev': re.search('"__spin_r":(.*?)', str(req)).group(1),'__s': "gj8z5g:6nupeb:1xcz9j",'__hsi': re.search(r'"hsi":"(.*?)"',str(req)).group(1),'__dyn': "",'__csr': "",'__comet_req': "15",'fb_dtsg': re.search(r'"DTSGInitialData",\[\],{"token":"(.*?)"}',str(req)).group(1),'jazoest': re.search(r'jazoest=(.*?)"',str(req)).group(1),'lsd': re.search('"LSD",\\[\\],{"token":"(.*?)"}', str(req)).group(1),'__spin_r': re.search('"__spin_r":(.*?)', str(req)).group(1),'__spin_b': "trunk",'__spin_t': re.search('"__spin_t":(.*?)', str(req)).group(1),}
	
	def temp_headers(self):
		return {'host': 'api.internal.temp-mail.io','application-name': 'web','sec-ch-ua-platform': '"Android"','application-version': '2.4.2','sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"','sec-ch-ua-mobile': '?1','user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Mobile Safari/537.36','accept': 'application/json, text/plain, */*','content-type': 'application/json;charset=UTF-8','origin': 'https://temp-mail.io','sec-fetch-site': 'same-site','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://temp-mail.io/','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
	
	def get_data(self):
		return {"method": "post","pretty": "false","format": "json", "server_timestamps": "true","locale": "id_ID","purpose": "fetch","fb_api_caller_class": "graphservice","client_doc_id": "119940804214876861379510865434",}
	
	def get_headers(self):
		return {'host': 'b-graph.facebook.com','x-fb-ta-logging-ids': 'graphql:720a2e70-7733-4c08-b6a4-638be8ae3102','x-fb-net-hni': '51011','x-fb-request-analytics-tags': '{"network_tags":{"product":"350685531728","purpose":"fetch","request_category":"graphql","retry_attempt":"0"},"application_tags":"graphservice"}','x-graphql-client-library': 'graphservice','authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32','x-fb-privacy-context': '3643298472347298','content-type': 'application/x-www-form-urlencoded','x-graphql-request-purpose': 'fetch','x-fb-sim-hni': '51011','user-agent': '[FBAN/FB4A;FBAV/486.0.0.66.70;FBBV/653066364;FBDM/{density=2.75,width=1080,height=2130};FBLC/id_ID;FBRV/0;FBCR/XL;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.mahos;FBDV/Redmi Note 8;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]','x-fb-connection-type': 'MOBILE.LTE','x-fb-device-group': '6980','x-tigon-is-retry': 'False','x-fb-http-engine': 'Liger','x-fb-client-ip': 'True','x-fb-server-cluster': 'True'}
	
	def kode(self, a):
		for sleep in range(int(a), 0, -1):
			console.print(f' [bold green]#[bold white] Lagi nunggu codenya bos {sleep}{" "*10}', end='\r')
			time.sleep(1)
			
	def delayy(self, a):
		for sleep in range(int(a), 0, -1):
			console.print(f' [bold green]#[bold white] Bentar ya bos {sleep}{" "*10}', end='\r')
			time.sleep(1)
		
class AccountCreator:
	
	def banner(self):
		console.print(f"""
[italic bold sky_blue1][bold grey37] [italic bold sky_blue1]

____________    ___             _____                _             
|  ___| ___ \  / _ \           /  __ \              | |            
| |_  | |_/ / / /_\ \ ___ ___  | /  \/_ __ ___  __ _| |_ ___  _ __ 
|  _| | ___ \ |  _  |/ __/ __| | |   | '__/ _ \/ _` | __/ _ \| '__|
| |   | |_/ / | | | | (_| (__  | \__/\ | |  __/ (_| | || (_) | |   
\_|   \____/  \_| |_/\___\___|  \____/_|  \___|\__,_|\__\___/|_|   
                                                                   
                                                                   
______        ______                 _                             
| ___ \       | ___ \               | |                            
| |_/ /_   _  | |_/ /_   _  ___ ___ | |                            
| ___ \ | | | | ___ \ | | |/ __/ _ \| |                            
| |_/ / |_| | | |_/ / |_| | (_| (_) | |                            
\____/ \__, | \____/ \__,_|\___\___/|_|                            
        __/ |                                                      
       |___/                                                       

Version 1.0
Re-modified by Colsss[/][bold cyan3][bold white]
		""")
	
	def menu(self):
		self.banner()
		console.print("""
 [bold green]1[bold blue]) Create Akun FB
 [bold green]2[bold blue]) Cek Akun
 [bold green]3[bold blue]) Ambatukam
		""")
		userInput = console.input(" [bold green]#[bold white] pilih 1-3: ")
		if userInput in ['1', '01']:
			self.create()
		elif userInput in ['2', '02']:
			self.cek_account() 
		elif userInput in ['3', '03']:
			exit()
		elif userInput in ['4', '04']:
			pass # coming soon
		elif userInput in ['5', '05']:
			pass # coming soon
	
	def cek_account(self):
		with open('Results/FBNewAkun.json', 'r') as file:
			json_data = json.load(file)
		for i, data in enumerate(json_data, start=1):
			name = data.get("Name")
			userID = data.get("Userid")
			email = data.get("Email")
			password = data.get("Password")
			cookies = data.get("Cookies")
			token = data.get("Token")
			tanggal_lahir = data.get("Tanggal lahir")
			
			print(f"""\n
  Account ke {i}
  Name         : {name}
  UserID       : {userID}
  Email        : {email}
  Password     : {password}
  Cookies      : {cookies}
  Token        : {token}
  Tanggal Lahir: {tanggal_lahir}""")
			
			
	def create(self):
		try:
			total = int(console.input('\n [bold green]#[bold white] Mau berapa akun bos?: ') or 5)
			delay = int(console.input(" [bold green]#[bold white] Delaynya brp detik bos?: ") or 60)
##			console.print(" [bold green]#[bold white] Apakah kamu ingin langsung membuat postingan pertama (skip=enter)")
			konten_postingan = console.input(" [bold green]#[bold white] Caption buat post: ")
			if konten_postingan:
				POSTS.update({'STATUS': f'{konten_postingan}'})
			else:
				POSTS.update({'STATUS': None})
				
		except ValueError:
			total = 5
			delay = 60
		
		for acc in range(total):
			AccountCreation()
			self.looping(delay)

	def looping(self, delay):
		for sleep in range(int(delay), 0, -1):
			console.print(f' [green]#[white] Delay bos: {sleep} Sukses: [green]{Ok}[white] Gagal: [red]{Fail}[white] CP: [yellow]{Cp}[white] ', end='\r')
			time.sleep(1)

class AccountCreation:
	def __init__(self):
		self.data = asset().get_data()
		self.headers = asset().get_headers()
		self.data_collection()
		self.name_signup()
	
	def data_collection(self):
		self.nama_depan, self.nama_belakang = self.generate_username()
		self.email, self.ses_email, self.coki = self.get_email_temp_mail()
		self.tgl_lahir = self.generate_birthday()
		self.password = self.nama_belakang.lower()+"321@"
	
	def generate_username(self):
		fake = Faker("id_ID")
		first_name = fake.first_name_female()
		last_name = fake.last_name_female()
		name = f"{first_name} {last_name}"
		return first_name, last_name
	
	def generate_birthday(self):
		year = random.randint(1995, 2003)
		month = random.randint(1, 12)
		day = random.randint(1, 27)
		return str(f'{day:02d}-{month:02d}-{year}')
		
	def get_email_temp_mail(self):
		with requests.Session() as mail:
			headers = asset().temp_headers()
			payload = json.dumps({"min_name_length": 10,"max_name_length": 10})
			headers.update({'content-length': str(len(payload))})
			req = mail.post('https://api.internal.temp-mail.io/api/v3/email/new', data=payload, headers=headers).json()
			email = req['email']
			cookie = '; '.join([f"{x}={y}" for x, y in mail.cookies.get_dict().items()])
			return email, mail, cookie
	
	def get_code_temp_mail(self, email):
		headers = asset().temp_headers()
		response = self.ses_email.get(f'https://api.internal.temp-mail.io/api/v3/email/{email}/messages', cookies = {'cookie': self.coki}, headers=headers)
		open('Data/CodeCekTemp.json', 'w').write(str(response.text))
		if response.status_code == 200:
			req = response.json()
			if req and isinstance(req, list):
				subject = req[0].get('subject', '')
				kode = re.search(r'(\d{5})', subject)
				code = kode.group(1) if kode else 'Kode tidak ditemukan'
				return code
			else:
				return 'Respon tidak valid'
		return None
		
	def name_signup(self):
		global Fail
		try:
			with requests.Session() as r:
				self.headers.update({"x-fb-friendly-name": "FbBloksActionRootQuery-com.bloks.www.bloks.caa.reg.name.async"})
				self.data.update({
					"fb_api_req_friendly_name": "FbBloksActionRootQuery-com.bloks.www.bloks.caa.reg.name.async",
					"variables": "{\"params\":{\"params\":\"{\\\"params\\\":\\\"{\\\\\\\"client_input_params\\\\\\\":{\\\\\\\"lois_settings\\\\\\\":{\\\\\\\"lois_token\\\\\\\":\\\\\\\"\\\\\\\",\\\\\\\"lara_override\\\\\\\":\\\\\\\"\\\\\\\"},\\\\\\\"firstname\\\\\\\":\\\\\\\""+self.nama_depan+"\\\\\\\",\\\\\\\"lastname\\\\\\\":\\\\\\\""+self.nama_belakang+"\\\\\\\"},\\\\\\\"server_params\\\\\\\":{\\\\\\\"event_request_id\\\\\\\":\\\\\\\"fc6d2935-c10a-43b3-a8a2-bad6e3fffefe\\\\\\\",\\\\\\\"is_from_logged_out\\\\\\\":0,\\\\\\\"layered_homepage_experiment_group\\\\\\\":null,\\\\\\\"device_id\\\\\\\":\\\\\\\"463f7aa2-87c0-4345-a3fb-bce0adc35308\\\\\\\",\\\\\\\"waterfall_id\\\\\\\":\\\\\\\"89e9a4d6-fe66-4e33-b40e-8150b5c4d224\\\\\\\",\\\\\\\"INTERNAL__latency_qpl_instance_id\\\\\\\":1.27385225300171E14,\\\\\\\"flow_info\\\\\\\":\\\\\\\"{\\\\\\\\\\\\\\\"flow_name\\\\\\\\\\\\\\\":\\\\\\\\\\\\\\\"new_to_family_fb_default\\\\\\\\\\\\\\\",\\\\\\\\\\\\\\\"flow_type\\\\\\\\\\\\\\\":\\\\\\\\\\\\\\\"ntf\\\\\\\\\\\\\\\"}\\\\\\\",\\\\\\\"is_platform_login\\\\\\\":0,\\\\\\\"INTERNAL__latency_qpl_marker_id\\\\\\\":36707139,\\\\\\\"reg_info\\\\\\\":\\\\\\\"{\\\\\\\\\\\\\\\"first_name\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"last_name\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"full_name\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"contactpoint\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"ar_contactpoint\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"contactpoint_type\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"is_using_unified_cp\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"unified_cp_screen_variant\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"is_cp_auto_confirmed\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"is_cp_auto_confirmable\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"confirmation_code\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"birthday\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"did_use_age\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"gender\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"use_custom_gender\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"custom_gender\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"encrypted_password\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"username\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"username_prefill\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"fb_conf_source\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"device_id\\\\\\\\\\\\\\\":\\\\\\\\\\\\\\\"463f7aa2-87c0-4345-a3fb-bce0adc35308\\\\\\\\\\\\\\\",\\\\\\\\\\\\\\\"ig4a_qe_device_id\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"family_device_id\\\\\\\\\\\\\\\":\\\\\\\\\\\\\\\"463f7aa2-87c0-4345-a3fb-bce0adc35308\\\\\\\\\\\\\\\",\\\\\\\\\\\\\\\"nta_eligibility_reason\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"ig_nta_test_group\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"user_id\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"safetynet_token\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"safetynet_response\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"machine_id\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"profile_photo\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"profile_photo_id\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"profile_photo_upload_id\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"avatar\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"email_oauth_token_no_contact_perm\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"email_oauth_token\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"email_oauth_tokens\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"should_skip_two_step_conf\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"openid_tokens_for_testing\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"encrypted_msisdn\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"encrypted_msisdn_for_safetynet\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"cached_headers_safetynet_info\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"should_skip_headers_safetynet\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"headers_last_infra_flow_id\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"headers_last_infra_flow_id_safetynet\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"headers_flow_id\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"was_headers_prefill_available\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"sso_enabled\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"existing_accounts\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"used_ig_birthday\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"sync_info\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"create_new_to_app_account\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"skip_session_info\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"ck_error\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"ck_id\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"ck_nonce\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"should_save_password\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"horizon_synced_username\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"fb_access_token\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"horizon_synced_profile_pic\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"is_identity_synced\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"is_msplit_reg\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"user_id_of_msplit_creator\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"dma_data_combination_consent_given\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"xapp_accounts\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"fb_device_id\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"fb_machine_id\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"ig_device_id\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"ig_machine_id\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"should_skip_nta_upsell\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"big_blue_token\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"skip_sync_step_nta\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"caa_reg_flow_source\\\\\\\\\\\\\\\":\\\\\\\\\\\\\\\"login_home_native_integration_point\\\\\\\\\\\\\\\",\\\\\\\\\\\\\\\"ig_authorization_token\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"full_sheet_flow\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"crypted_user_id\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"is_caa_perf_enabled\\\\\\\\\\\\\\\":true,\\\\\\\\\\\\\\\"is_preform\\\\\\\\\\\\\\\":true,\\\\\\\\\\\\\\\"ignore_suma_check\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"ignore_existing_login\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"ignore_existing_login_from_suma\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"ignore_existing_login_after_errors\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"suggested_first_name\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"suggested_last_name\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"suggested_full_name\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"replace_id_sync_variant\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"is_redirect_from_nta_replace_id_sync_variant\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"frl_authorization_token\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"post_form_errors\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"skip_step_without_errors\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"existing_account_exact_match_checked\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"existing_account_fuzzy_match_checked\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"email_oauth_exists\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"confirmation_code_send_error\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"is_too_young\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"source_account_type\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"whatsapp_installed_on_client\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"confirmation_medium\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"source_credentials_type\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"source_cuid\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"source_account_reg_info\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"soap_creation_source\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"source_account_type_to_reg_info\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"registration_flow_id\\\\\\\\\\\\\\\":\\\\\\\\\\\\\\\"bf85b3e7-ce6a-4abf-962b-2c528167c7e9\\\\\\\\\\\\\\\",\\\\\\\\\\\\\\\"should_skip_youth_tos\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"is_youth_regulation_flow_complete\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"is_on_cold_start\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"email_prefilled\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"cp_confirmed_by_auto_conf\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"auto_conf_info\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"in_sowa_experiment\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"youth_regulation_config\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"conf_allow_back_nav_after_change_cp\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"conf_bouncing_cliff_screen_type\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"conf_show_bouncing_cliff\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"eligible_to_flash_call_in_ig4a\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"flash_call_permissions_status\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"attestation_result\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"request_data_and_challenge_nonce_string\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"confirmed_cp_and_code\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"notification_callback_id\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"reg_suma_state\\\\\\\\\\\\\\\":0,\\\\\\\\\\\\\\\"is_msplit_neutral_choice\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"msg_previous_cp\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"ntp_import_source_info\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"youth_consent_decision_time\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"username_screen_experience\\\\\\\\\\\\\\\":\\\\\\\\\\\\\\\"control\\\\\\\\\\\\\\\",\\\\\\\\\\\\\\\"reduced_tos_test_group\\\\\\\\\\\\\\\":\\\\\\\\\\\\\\\"control\\\\\\\\\\\\\\\",\\\\\\\\\\\\\\\"should_show_spi_before_conf\\\\\\\\\\\\\\\":true,\\\\\\\\\\\\\\\"google_oauth_account\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"is_reg_request_from_ig_suma\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"is_igios_spc_reg\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"device_emails\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"is_toa_reg\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"is_threads_public\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"spc_import_flow\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"caa_play_integrity_attestation_result\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"flash_call_provider\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"name_prefill_variant\\\\\\\\\\\\\\\":\\\\\\\\\\\\\\\"control\\\\\\\\\\\\\\\",\\\\\\\\\\\\\\\"spc_birthday_input\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"failed_birthday_year_count\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"user_presented_medium_source\\\\\\\\\\\\\\\":null}\\\\\\\",\\\\\\\"family_device_id\\\\\\\":\\\\\\\"463f7aa2-87c0-4345-a3fb-bce0adc35308\\\\\\\",\\\\\\\"offline_experiment_group\\\\\\\":\\\\\\\"caa_iteration_v6_perf_fb_2\\\\\\\",\\\\\\\"INTERNAL_INFRA_THEME\\\\\\\":\\\\\\\"harm_f,default,default,harm_f\\\\\\\",\\\\\\\"access_flow_version\\\\\\\":\\\\\\\"F2_FLOW\\\\\\\",\\\\\\\"is_from_logged_in_switcher\\\\\\\":0,\\\\\\\"current_step\\\\\\\":1}}\\\"}\",\"bloks_versioning_id\":\"3711cb070fe0ab5acd59ae663b1ae4dc75db6f0c463d26a232fd9d72a63fb3e5\",\"app_id\":\"com.bloks.www.bloks.caa.reg.name.async\"},\"scale\":\"3\",\"nt_context\":{\"using_white_navbar\":true,\"styles_id\":\"cfe75e13b386d5c54b1de2dcca1bee5a\",\"pixel_ratio\":3,\"is_push_on\":true,\"debug_tooling_metadata_token\":null,\"is_flipper_enabled\":false,\"theme_params\":[],\"bloks_version\":\"3711cb070fe0ab5acd59ae663b1ae4dc75db6f0c463d26a232fd9d72a63fb3e5\"}}",
					"fb_api_analytics_tags": "[\"GraphServices\"]",
					"client_trace_id": str(uuid.uuid4())
				})
				post = r.post('https://b-graph.facebook.com/graphql', data=self.data,  headers=self.headers)
				if "Kapan tanggal lahir Anda?" in post.text:
					self.birthday()
				else:
					Fail+=1
		except Exception as e:print(e)	
	
	def birthday(self):
		global Fail
		with requests.Session() as r:
			self.headers.update({"x-fb-friendly-name": "FbBloksActionRootQuery-com.bloks.www.bloks.caa.reg.birthday.async"})
			self.data.update({
				"fb_api_req_friendly_name": "FbBloksActionRootQuery-com.bloks.www.bloks.caa.reg.birthday.async",
				"variables": "{\"params\":{\"params\":\"{\\\"params\\\":\\\"{\\\\\\\"client_input_params\\\\\\\":{\\\\\\\"should_skip_youth_tos\\\\\\\":0,\\\\\\\"is_youth_regulation_flow_complete\\\\\\\":0,\\\\\\\"client_timezone\\\\\\\":\\\\\\\"Asia\\\\/Jakarta\\\\\\\",\\\\\\\"birthday_or_current_date_string\\\\\\\":\\\\\\\""+self.tgl_lahir+"\\\\\\\",\\\\\\\"birthday_timestamp\\\\\\\":"+str(int(time.time()))+",\\\\\\\"lois_settings\\\\\\\":{\\\\\\\"lois_token\\\\\\\":\\\\\\\"\\\\\\\",\\\\\\\"lara_override\\\\\\\":\\\\\\\"\\\\\\\"}},\\\\\\\"server_params\\\\\\\":{\\\\\\\"is_from_logged_out\\\\\\\":0,\\\\\\\"layered_homepage_experiment_group\\\\\\\":null,\\\\\\\"device_id\\\\\\\":\\\\\\\"463f7aa2-87c0-4345-a3fb-bce0adc35308\\\\\\\",\\\\\\\"waterfall_id\\\\\\\":\\\\\\\"89e9a4d6-fe66-4e33-b40e-8150b5c4d224\\\\\\\",\\\\\\\"INTERNAL__latency_qpl_instance_id\\\\\\\":1.27432008400228E14,\\\\\\\"flow_info\\\\\\\":\\\\\\\"{\\\\\\\\\\\\\\\"flow_name\\\\\\\\\\\\\\\":\\\\\\\\\\\\\\\"new_to_family_fb_default\\\\\\\\\\\\\\\",\\\\\\\\\\\\\\\"flow_type\\\\\\\\\\\\\\\":\\\\\\\\\\\\\\\"ntf\\\\\\\\\\\\\\\"}\\\\\\\",\\\\\\\"is_platform_login\\\\\\\":0,\\\\\\\"INTERNAL__latency_qpl_marker_id\\\\\\\":36707139,\\\\\\\"reg_info\\\\\\\":\\\\\\\"{\\\\\\\\\\\\\\\"first_name\\\\\\\\\\\\\\\":\\\\\\\\\\\\\\\""+self.nama_depan+"\\\\\\\\\\\\\\\",\\\\\\\\\\\\\\\"last_name\\\\\\\\\\\\\\\":\\\\\\\\\\\\\\\""+self.nama_belakang+"\\\\\\\\\\\\\\\",\\\\\\\\\\\\\\\"full_name\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"contactpoint\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"ar_contactpoint\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"contactpoint_type\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"is_using_unified_cp\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"unified_cp_screen_variant\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"is_cp_auto_confirmed\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"is_cp_auto_confirmable\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"confirmation_code\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"birthday\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"did_use_age\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"gender\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"use_custom_gender\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"custom_gender\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"encrypted_password\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"username\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"username_prefill\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"fb_conf_source\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"device_id\\\\\\\\\\\\\\\":\\\\\\\\\\\\\\\"463f7aa2-87c0-4345-a3fb-bce0adc35308\\\\\\\\\\\\\\\",\\\\\\\\\\\\\\\"ig4a_qe_device_id\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"family_device_id\\\\\\\\\\\\\\\":\\\\\\\\\\\\\\\"463f7aa2-87c0-4345-a3fb-bce0adc35308\\\\\\\\\\\\\\\",\\\\\\\\\\\\\\\"nta_eligibility_reason\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"ig_nta_test_group\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"user_id\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"safetynet_token\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"safetynet_response\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"machine_id\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"profile_photo\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"profile_photo_id\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"profile_photo_upload_id\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"avatar\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"email_oauth_token_no_contact_perm\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"email_oauth_token\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"email_oauth_tokens\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"should_skip_two_step_conf\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"openid_tokens_for_testing\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"encrypted_msisdn\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"encrypted_msisdn_for_safetynet\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"cached_headers_safetynet_info\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"should_skip_headers_safetynet\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"headers_last_infra_flow_id\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"headers_last_infra_flow_id_safetynet\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"headers_flow_id\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"was_headers_prefill_available\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"sso_enabled\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"existing_accounts\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"used_ig_birthday\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"sync_info\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"create_new_to_app_account\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"skip_session_info\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"ck_error\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"ck_id\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"ck_nonce\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"should_save_password\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"horizon_synced_username\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"fb_access_token\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"horizon_synced_profile_pic\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"is_identity_synced\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"is_msplit_reg\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"user_id_of_msplit_creator\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"dma_data_combination_consent_given\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"xapp_accounts\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"fb_device_id\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"fb_machine_id\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"ig_device_id\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"ig_machine_id\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"should_skip_nta_upsell\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"big_blue_token\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"skip_sync_step_nta\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"caa_reg_flow_source\\\\\\\\\\\\\\\":\\\\\\\\\\\\\\\"login_home_native_integration_point\\\\\\\\\\\\\\\",\\\\\\\\\\\\\\\"ig_authorization_token\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"full_sheet_flow\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"crypted_user_id\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"is_caa_perf_enabled\\\\\\\\\\\\\\\":true,\\\\\\\\\\\\\\\"is_preform\\\\\\\\\\\\\\\":true,\\\\\\\\\\\\\\\"ignore_suma_check\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"ignore_existing_login\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"ignore_existing_login_from_suma\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"ignore_existing_login_after_errors\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"suggested_first_name\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"suggested_last_name\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"suggested_full_name\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"replace_id_sync_variant\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"is_redirect_from_nta_replace_id_sync_variant\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"frl_authorization_token\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"post_form_errors\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"skip_step_without_errors\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"existing_account_exact_match_checked\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"existing_account_fuzzy_match_checked\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"email_oauth_exists\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"confirmation_code_send_error\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"is_too_young\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"source_account_type\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"whatsapp_installed_on_client\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"confirmation_medium\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"source_credentials_type\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"source_cuid\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"source_account_reg_info\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"soap_creation_source\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"source_account_type_to_reg_info\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"registration_flow_id\\\\\\\\\\\\\\\":\\\\\\\\\\\\\\\"bf85b3e7-ce6a-4abf-962b-2c528167c7e9\\\\\\\\\\\\\\\",\\\\\\\\\\\\\\\"should_skip_youth_tos\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"is_youth_regulation_flow_complete\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"is_on_cold_start\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"email_prefilled\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"cp_confirmed_by_auto_conf\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"auto_conf_info\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"in_sowa_experiment\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"youth_regulation_config\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"conf_allow_back_nav_after_change_cp\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"conf_bouncing_cliff_screen_type\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"conf_show_bouncing_cliff\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"eligible_to_flash_call_in_ig4a\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"flash_call_permissions_status\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"attestation_result\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"request_data_and_challenge_nonce_string\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"confirmed_cp_and_code\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"notification_callback_id\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"reg_suma_state\\\\\\\\\\\\\\\":0,\\\\\\\\\\\\\\\"is_msplit_neutral_choice\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"msg_previous_cp\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"ntp_import_source_info\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"youth_consent_decision_time\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"username_screen_experience\\\\\\\\\\\\\\\":\\\\\\\\\\\\\\\"control\\\\\\\\\\\\\\\",\\\\\\\\\\\\\\\"reduced_tos_test_group\\\\\\\\\\\\\\\":\\\\\\\\\\\\\\\"control\\\\\\\\\\\\\\\",\\\\\\\\\\\\\\\"should_show_spi_before_conf\\\\\\\\\\\\\\\":true,\\\\\\\\\\\\\\\"google_oauth_account\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"is_reg_request_from_ig_suma\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"is_igios_spc_reg\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"device_emails\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"is_toa_reg\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"is_threads_public\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"spc_import_flow\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"caa_play_integrity_attestation_result\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"flash_call_provider\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"name_prefill_variant\\\\\\\\\\\\\\\":\\\\\\\\\\\\\\\"control\\\\\\\\\\\\\\\",\\\\\\\\\\\\\\\"spc_birthday_input\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"failed_birthday_year_count\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"user_presented_medium_source\\\\\\\\\\\\\\\":null}\\\\\\\",\\\\\\\"family_device_id\\\\\\\":\\\\\\\"463f7aa2-87c0-4345-a3fb-bce0adc35308\\\\\\\",\\\\\\\"offline_experiment_group\\\\\\\":\\\\\\\"caa_iteration_v6_perf_fb_2\\\\\\\",\\\\\\\"INTERNAL_INFRA_THEME\\\\\\\":\\\\\\\"harm_f,default,default,harm_f\\\\\\\",\\\\\\\"access_flow_version\\\\\\\":\\\\\\\"F2_FLOW\\\\\\\",\\\\\\\"is_from_logged_in_switcher\\\\\\\":0,\\\\\\\"current_step\\\\\\\":2}}\\\"}\",\"bloks_versioning_id\":\"3711cb070fe0ab5acd59ae663b1ae4dc75db6f0c463d26a232fd9d72a63fb3e5\",\"app_id\":\"com.bloks.www.bloks.caa.reg.birthday.async\"},\"scale\":\"3\",\"nt_context\":{\"using_white_navbar\":true,\"styles_id\":\"cfe75e13b386d5c54b1de2dcca1bee5a\",\"pixel_ratio\":3,\"is_push_on\":true,\"debug_tooling_metadata_token\":null,\"is_flipper_enabled\":false,\"theme_params\":[],\"bloks_version\":\"3711cb070fe0ab5acd59ae663b1ae4dc75db6f0c463d26a232fd9d72a63fb3e5\"}}",
				"fb_api_analytics_tags": "[\"GraphServices\"]",
				"client_trace_id": str(uuid.uuid4())
			})
			post = r.post('https://b-graph.facebook.com/graphql', data=self.data,  headers=self.headers)
			if "Apa jenis kelamin Anda?" in post.text:
				self.gender()
			else:
				Fail+=1
	
	def gender(self):
		global Fail
		with requests.Session() as r:
			self.headers.update({"x-fb-friendly-name": "FbBloksActionRootQuery-com.bloks.www.bloks.caa.reg.gender.async"})
			self.data.update({
				"fb_api_req_friendly_name": "FbBloksActionRootQuery-com.bloks.www.bloks.caa.reg.gender.async",
				"variables": "{\"params\":{\"params\":\"{\\\"params\\\":\\\"{\\\\\\\"client_input_params\\\\\\\":{\\\\\\\"device_phone_numbers\\\\\\\":[],\\\\\\\"gender\\\\\\\":1,\\\\\\\"pronoun\\\\\\\":0,\\\\\\\"lois_settings\\\\\\\":{\\\\\\\"lois_token\\\\\\\":\\\\\\\"\\\\\\\",\\\\\\\"lara_override\\\\\\\":\\\\\\\"\\\\\\\"},\\\\\\\"custom_gender\\\\\\\":\\\\\\\"\\\\\\\"},\\\\\\\"server_params\\\\\\\":{\\\\\\\"is_from_logged_out\\\\\\\":0,\\\\\\\"layered_homepage_experiment_group\\\\\\\":null,\\\\\\\"device_id\\\\\\\":\\\\\\\"463f7aa2-87c0-4345-a3fb-bce0adc35308\\\\\\\",\\\\\\\"waterfall_id\\\\\\\":\\\\\\\"89e9a4d6-fe66-4e33-b40e-8150b5c4d224\\\\\\\",\\\\\\\"INTERNAL__latency_qpl_instance_id\\\\\\\":1.27453352400107E14,\\\\\\\"flow_info\\\\\\\":\\\\\\\"{\\\\\\\\\\\\\\\"flow_name\\\\\\\\\\\\\\\":\\\\\\\\\\\\\\\"new_to_family_fb_default\\\\\\\\\\\\\\\",\\\\\\\\\\\\\\\"flow_type\\\\\\\\\\\\\\\":\\\\\\\\\\\\\\\"ntf\\\\\\\\\\\\\\\"}\\\\\\\",\\\\\\\"is_platform_login\\\\\\\":0,\\\\\\\"INTERNAL__latency_qpl_marker_id\\\\\\\":36707139,\\\\\\\"reg_info\\\\\\\":\\\\\\\"{\\\\\\\\\\\\\\\"first_name\\\\\\\\\\\\\\\":\\\\\\\\\\\\\\\""+self.nama_depan+"\\\\\\\\\\\\\\\",\\\\\\\\\\\\\\\"last_name\\\\\\\\\\\\\\\":\\\\\\\\\\\\\\\""+self.nama_belakang+"\\\\\\\\\\\\\\\",\\\\\\\\\\\\\\\"full_name\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"contactpoint\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"ar_contactpoint\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"contactpoint_type\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"is_using_unified_cp\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"unified_cp_screen_variant\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"is_cp_auto_confirmed\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"is_cp_auto_confirmable\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"confirmation_code\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"birthday\\\\\\\\\\\\\\\":\\\\\\\\\\\\\\\""+self.tgl_lahir+"\\\\\\\\\\\\\\\",\\\\\\\\\\\\\\\"did_use_age\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"gender\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"use_custom_gender\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"custom_gender\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"encrypted_password\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"username\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"username_prefill\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"fb_conf_source\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"device_id\\\\\\\\\\\\\\\":\\\\\\\\\\\\\\\"463f7aa2-87c0-4345-a3fb-bce0adc35308\\\\\\\\\\\\\\\",\\\\\\\\\\\\\\\"ig4a_qe_device_id\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"family_device_id\\\\\\\\\\\\\\\":\\\\\\\\\\\\\\\"463f7aa2-87c0-4345-a3fb-bce0adc35308\\\\\\\\\\\\\\\",\\\\\\\\\\\\\\\"nta_eligibility_reason\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"ig_nta_test_group\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"user_id\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"safetynet_token\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"safetynet_response\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"machine_id\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"profile_photo\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"profile_photo_id\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"profile_photo_upload_id\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"avatar\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"email_oauth_token_no_contact_perm\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"email_oauth_token\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"email_oauth_tokens\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"should_skip_two_step_conf\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"openid_tokens_for_testing\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"encrypted_msisdn\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"encrypted_msisdn_for_safetynet\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"cached_headers_safetynet_info\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"should_skip_headers_safetynet\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"headers_last_infra_flow_id\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"headers_last_infra_flow_id_safetynet\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"headers_flow_id\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"was_headers_prefill_available\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"sso_enabled\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"existing_accounts\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"used_ig_birthday\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"sync_info\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"create_new_to_app_account\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"skip_session_info\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"ck_error\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"ck_id\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"ck_nonce\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"should_save_password\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"horizon_synced_username\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"fb_access_token\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"horizon_synced_profile_pic\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"is_identity_synced\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"is_msplit_reg\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"user_id_of_msplit_creator\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"dma_data_combination_consent_given\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"xapp_accounts\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"fb_device_id\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"fb_machine_id\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"ig_device_id\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"ig_machine_id\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"should_skip_nta_upsell\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"big_blue_token\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"skip_sync_step_nta\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"caa_reg_flow_source\\\\\\\\\\\\\\\":\\\\\\\\\\\\\\\"login_home_native_integration_point\\\\\\\\\\\\\\\",\\\\\\\\\\\\\\\"ig_authorization_token\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"full_sheet_flow\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"crypted_user_id\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"is_caa_perf_enabled\\\\\\\\\\\\\\\":true,\\\\\\\\\\\\\\\"is_preform\\\\\\\\\\\\\\\":true,\\\\\\\\\\\\\\\"ignore_suma_check\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"ignore_existing_login\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"ignore_existing_login_from_suma\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"ignore_existing_login_after_errors\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"suggested_first_name\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"suggested_last_name\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"suggested_full_name\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"replace_id_sync_variant\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"is_redirect_from_nta_replace_id_sync_variant\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"frl_authorization_token\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"post_form_errors\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"skip_step_without_errors\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"existing_account_exact_match_checked\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"existing_account_fuzzy_match_checked\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"email_oauth_exists\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"confirmation_code_send_error\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"is_too_young\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"source_account_type\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"whatsapp_installed_on_client\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"confirmation_medium\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"source_credentials_type\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"source_cuid\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"source_account_reg_info\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"soap_creation_source\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"source_account_type_to_reg_info\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"registration_flow_id\\\\\\\\\\\\\\\":\\\\\\\\\\\\\\\"bf85b3e7-ce6a-4abf-962b-2c528167c7e9\\\\\\\\\\\\\\\",\\\\\\\\\\\\\\\"should_skip_youth_tos\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"is_youth_regulation_flow_complete\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"is_on_cold_start\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"email_prefilled\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"cp_confirmed_by_auto_conf\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"auto_conf_info\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"in_sowa_experiment\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"youth_regulation_config\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"conf_allow_back_nav_after_change_cp\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"conf_bouncing_cliff_screen_type\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"conf_show_bouncing_cliff\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"eligible_to_flash_call_in_ig4a\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"flash_call_permissions_status\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"attestation_result\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"request_data_and_challenge_nonce_string\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"confirmed_cp_and_code\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"notification_callback_id\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"reg_suma_state\\\\\\\\\\\\\\\":0,\\\\\\\\\\\\\\\"is_msplit_neutral_choice\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"msg_previous_cp\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"ntp_import_source_info\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"youth_consent_decision_time\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"username_screen_experience\\\\\\\\\\\\\\\":\\\\\\\\\\\\\\\"control\\\\\\\\\\\\\\\",\\\\\\\\\\\\\\\"reduced_tos_test_group\\\\\\\\\\\\\\\":\\\\\\\\\\\\\\\"control\\\\\\\\\\\\\\\",\\\\\\\\\\\\\\\"should_show_spi_before_conf\\\\\\\\\\\\\\\":true,\\\\\\\\\\\\\\\"google_oauth_account\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"is_reg_request_from_ig_suma\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"is_igios_spc_reg\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"device_emails\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"is_toa_reg\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"is_threads_public\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"spc_import_flow\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"caa_play_integrity_attestation_result\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"flash_call_provider\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"name_prefill_variant\\\\\\\\\\\\\\\":\\\\\\\\\\\\\\\"control\\\\\\\\\\\\\\\",\\\\\\\\\\\\\\\"spc_birthday_input\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"failed_birthday_year_count\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"user_presented_medium_source\\\\\\\\\\\\\\\":null}\\\\\\\",\\\\\\\"family_device_id\\\\\\\":\\\\\\\"463f7aa2-87c0-4345-a3fb-bce0adc35308\\\\\\\",\\\\\\\"offline_experiment_group\\\\\\\":\\\\\\\"caa_iteration_v6_perf_fb_2\\\\\\\",\\\\\\\"INTERNAL_INFRA_THEME\\\\\\\":\\\\\\\"harm_f,default,default,harm_f\\\\\\\",\\\\\\\"access_flow_version\\\\\\\":\\\\\\\"F2_FLOW\\\\\\\",\\\\\\\"is_from_logged_in_switcher\\\\\\\":0,\\\\\\\"current_step\\\\\\\":3}}\\\"}\",\"bloks_versioning_id\":\"3711cb070fe0ab5acd59ae663b1ae4dc75db6f0c463d26a232fd9d72a63fb3e5\",\"app_id\":\"com.bloks.www.bloks.caa.reg.gender.async\"},\"scale\":\"3\",\"nt_context\":{\"using_white_navbar\":true,\"styles_id\":\"cfe75e13b386d5c54b1de2dcca1bee5a\",\"pixel_ratio\":3,\"is_push_on\":true,\"debug_tooling_metadata_token\":null,\"is_flipper_enabled\":false,\"theme_params\":[],\"bloks_version\":\"3711cb070fe0ab5acd59ae663b1ae4dc75db6f0c463d26a232fd9d72a63fb3e5\"}}",
				"fb_api_analytics_tags": "[\"GraphServices\"]",
				"client_trace_id": str(uuid.uuid4())
			})
			post = r.post('https://b-graph.facebook.com/graphql', data=self.data,  headers=self.headers)
			if "Masukkan email" in post.text:
				self.contac_mail()
			else:
				Fail+=1
				
	def contac_mail(self):
		global Fail
		console.print(f" [bold green]#[bold white] email: [green]{self.email}[white]{' '*10}", end = '\r')
		time.sleep(1.5)
		with requests.Session() as r:
			self.headers.update({"x-fb-friendly-name": "FbBloksActionRootQuery-com.bloks.www.bloks.caa.reg.async.contactpoint_email.async"})
			self.data.update({
				"fb_api_req_friendly_name": "FbBloksActionRootQuery-com.bloks.www.bloks.caa.reg.async.contactpoint_email.async",
				"variables": "{\"params\":{\"params\":\"{\\\"params\\\":\\\"{\\\\\\\"client_input_params\\\\\\\":{\\\\\\\"accounts_list\\\\\\\":[],\\\\\\\"email_prefilled\\\\\\\":0,\\\\\\\"confirmed_cp_and_code\\\\\\\":{},\\\\\\\"family_device_id\\\\\\\":\\\\\\\"463f7aa2-87c0-4345-a3fb-bce0adc35308\\\\\\\",\\\\\\\"fb_ig_device_id\\\\\\\":[],\\\\\\\"device_id\\\\\\\":\\\\\\\"463f7aa2-87c0-4345-a3fb-bce0adc35308\\\\\\\",\\\\\\\"lois_settings\\\\\\\":{\\\\\\\"lois_token\\\\\\\":\\\\\\\"\\\\\\\",\\\\\\\"lara_override\\\\\\\":\\\\\\\"\\\\\\\"},\\\\\\\"msg_previous_cp\\\\\\\":\\\\\\\"\\\\\\\",\\\\\\\"is_from_device_emails\\\\\\\":0,\\\\\\\"switch_cp_first_time_loading\\\\\\\":1,\\\\\\\"email\\\\\\\":\\\\\\\""+self.email+"\\\\\\\",\\\\\\\"switch_cp_have_seen_suma\\\\\\\":0},\\\\\\\"server_params\\\\\\\":{\\\\\\\"event_request_id\\\\\\\":\\\\\\\"05d555f2-6eb8-4e6c-9a71-d2c099d5434e\\\\\\\",\\\\\\\"is_from_logged_out\\\\\\\":0,\\\\\\\"text_input_id\\\\\\\":127474623800072,\\\\\\\"layered_homepage_experiment_group\\\\\\\":null,\\\\\\\"device_id\\\\\\\":\\\\\\\"463f7aa2-87c0-4345-a3fb-bce0adc35308\\\\\\\",\\\\\\\"waterfall_id\\\\\\\":\\\\\\\"89e9a4d6-fe66-4e33-b40e-8150b5c4d224\\\\\\\",\\\\\\\"INTERNAL__latency_qpl_instance_id\\\\\\\":1.274746238001E14,\\\\\\\"flow_info\\\\\\\":\\\\\\\"{\\\\\\\\\\\\\\\"flow_name\\\\\\\\\\\\\\\":\\\\\\\\\\\\\\\"new_to_family_fb_default\\\\\\\\\\\\\\\",\\\\\\\\\\\\\\\"flow_type\\\\\\\\\\\\\\\":\\\\\\\\\\\\\\\"ntf\\\\\\\\\\\\\\\"}\\\\\\\",\\\\\\\"is_platform_login\\\\\\\":0,\\\\\\\"INTERNAL__latency_qpl_marker_id\\\\\\\":36707139,\\\\\\\"reg_info\\\\\\\":\\\\\\\"{\\\\\\\\\\\\\\\"first_name\\\\\\\\\\\\\\\":\\\\\\\\\\\\\\\""+self.nama_depan+"\\\\\\\\\\\\\\\",\\\\\\\\\\\\\\\"last_name\\\\\\\\\\\\\\\":\\\\\\\\\\\\\\\""+self.nama_belakang+"\\\\\\\\\\\\\\\",\\\\\\\\\\\\\\\"full_name\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"contactpoint\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"ar_contactpoint\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"contactpoint_type\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"is_using_unified_cp\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"unified_cp_screen_variant\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"is_cp_auto_confirmed\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"is_cp_auto_confirmable\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"confirmation_code\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"birthday\\\\\\\\\\\\\\\":\\\\\\\\\\\\\\\""+self.tgl_lahir+"\\\\\\\\\\\\\\\",\\\\\\\\\\\\\\\"did_use_age\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"gender\\\\\\\\\\\\\\\":1,\\\\\\\\\\\\\\\"use_custom_gender\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"custom_gender\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"encrypted_password\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"username\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"username_prefill\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"fb_conf_source\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"device_id\\\\\\\\\\\\\\\":\\\\\\\\\\\\\\\"463f7aa2-87c0-4345-a3fb-bce0adc35308\\\\\\\\\\\\\\\",\\\\\\\\\\\\\\\"ig4a_qe_device_id\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"family_device_id\\\\\\\\\\\\\\\":\\\\\\\\\\\\\\\"463f7aa2-87c0-4345-a3fb-bce0adc35308\\\\\\\\\\\\\\\",\\\\\\\\\\\\\\\"nta_eligibility_reason\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"ig_nta_test_group\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"user_id\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"safetynet_token\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"safetynet_response\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"machine_id\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"profile_photo\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"profile_photo_id\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"profile_photo_upload_id\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"avatar\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"email_oauth_token_no_contact_perm\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"email_oauth_token\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"email_oauth_tokens\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"should_skip_two_step_conf\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"openid_tokens_for_testing\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"encrypted_msisdn\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"encrypted_msisdn_for_safetynet\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"cached_headers_safetynet_info\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"should_skip_headers_safetynet\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"headers_last_infra_flow_id\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"headers_last_infra_flow_id_safetynet\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"headers_flow_id\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"was_headers_prefill_available\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"sso_enabled\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"existing_accounts\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"used_ig_birthday\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"sync_info\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"create_new_to_app_account\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"skip_session_info\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"ck_error\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"ck_id\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"ck_nonce\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"should_save_password\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"horizon_synced_username\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"fb_access_token\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"horizon_synced_profile_pic\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"is_identity_synced\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"is_msplit_reg\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"user_id_of_msplit_creator\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"dma_data_combination_consent_given\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"xapp_accounts\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"fb_device_id\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"fb_machine_id\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"ig_device_id\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"ig_machine_id\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"should_skip_nta_upsell\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"big_blue_token\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"skip_sync_step_nta\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"caa_reg_flow_source\\\\\\\\\\\\\\\":\\\\\\\\\\\\\\\"login_home_native_integration_point\\\\\\\\\\\\\\\",\\\\\\\\\\\\\\\"ig_authorization_token\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"full_sheet_flow\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"crypted_user_id\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"is_caa_perf_enabled\\\\\\\\\\\\\\\":true,\\\\\\\\\\\\\\\"is_preform\\\\\\\\\\\\\\\":true,\\\\\\\\\\\\\\\"ignore_suma_check\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"ignore_existing_login\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"ignore_existing_login_from_suma\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"ignore_existing_login_after_errors\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"suggested_first_name\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"suggested_last_name\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"suggested_full_name\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"replace_id_sync_variant\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"is_redirect_from_nta_replace_id_sync_variant\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"frl_authorization_token\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"post_form_errors\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"skip_step_without_errors\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"existing_account_exact_match_checked\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"existing_account_fuzzy_match_checked\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"email_oauth_exists\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"confirmation_code_send_error\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"is_too_young\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"source_account_type\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"whatsapp_installed_on_client\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"confirmation_medium\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"source_credentials_type\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"source_cuid\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"source_account_reg_info\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"soap_creation_source\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"source_account_type_to_reg_info\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"registration_flow_id\\\\\\\\\\\\\\\":\\\\\\\\\\\\\\\"bf85b3e7-ce6a-4abf-962b-2c528167c7e9\\\\\\\\\\\\\\\",\\\\\\\\\\\\\\\"should_skip_youth_tos\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"is_youth_regulation_flow_complete\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"is_on_cold_start\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"email_prefilled\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"cp_confirmed_by_auto_conf\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"auto_conf_info\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"in_sowa_experiment\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"youth_regulation_config\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"conf_allow_back_nav_after_change_cp\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"conf_bouncing_cliff_screen_type\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"conf_show_bouncing_cliff\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"eligible_to_flash_call_in_ig4a\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"flash_call_permissions_status\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"attestation_result\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"request_data_and_challenge_nonce_string\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"confirmed_cp_and_code\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"notification_callback_id\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"reg_suma_state\\\\\\\\\\\\\\\":0,\\\\\\\\\\\\\\\"is_msplit_neutral_choice\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"msg_previous_cp\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"ntp_import_source_info\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"youth_consent_decision_time\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"username_screen_experience\\\\\\\\\\\\\\\":\\\\\\\\\\\\\\\"control\\\\\\\\\\\\\\\",\\\\\\\\\\\\\\\"reduced_tos_test_group\\\\\\\\\\\\\\\":\\\\\\\\\\\\\\\"control\\\\\\\\\\\\\\\",\\\\\\\\\\\\\\\"should_show_spi_before_conf\\\\\\\\\\\\\\\":true,\\\\\\\\\\\\\\\"google_oauth_account\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"is_reg_request_from_ig_suma\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"is_igios_spc_reg\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"device_emails\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"is_toa_reg\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"is_threads_public\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"spc_import_flow\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"caa_play_integrity_attestation_result\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"flash_call_provider\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"name_prefill_variant\\\\\\\\\\\\\\\":\\\\\\\\\\\\\\\"control\\\\\\\\\\\\\\\",\\\\\\\\\\\\\\\"spc_birthday_input\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"failed_birthday_year_count\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"user_presented_medium_source\\\\\\\\\\\\\\\":null}\\\\\\\",\\\\\\\"family_device_id\\\\\\\":\\\\\\\"463f7aa2-87c0-4345-a3fb-bce0adc35308\\\\\\\",\\\\\\\"offline_experiment_group\\\\\\\":\\\\\\\"caa_iteration_v6_perf_fb_2\\\\\\\",\\\\\\\"cp_funnel\\\\\\\":0,\\\\\\\"INTERNAL_INFRA_THEME\\\\\\\":\\\\\\\"harm_f,default,default,harm_f\\\\\\\",\\\\\\\"cp_source\\\\\\\":0,\\\\\\\"access_flow_version\\\\\\\":\\\\\\\"F2_FLOW\\\\\\\",\\\\\\\"is_from_logged_in_switcher\\\\\\\":0,\\\\\\\"current_step\\\\\\\":4}}\\\"}\",\"bloks_versioning_id\":\"3711cb070fe0ab5acd59ae663b1ae4dc75db6f0c463d26a232fd9d72a63fb3e5\",\"app_id\":\"com.bloks.www.bloks.caa.reg.async.contactpoint_email.async\"},\"scale\":\"3\",\"nt_context\":{\"using_white_navbar\":true,\"styles_id\":\"cfe75e13b386d5c54b1de2dcca1bee5a\",\"pixel_ratio\":3,\"is_push_on\":true,\"debug_tooling_metadata_token\":null,\"is_flipper_enabled\":false,\"theme_params\":[],\"bloks_version\":\"3711cb070fe0ab5acd59ae663b1ae4dc75db6f0c463d26a232fd9d72a63fb3e5\"}}",
				"fb_api_analytics_tags": "[\"GraphServices\"]",
				"client_trace_id": str(uuid.uuid4())
			})
			post = r.post('https://b-graph.facebook.com/graphql', data=self.data,  headers=self.headers)
			if "Buat kata sandi" in post.text:
				self.createpassword()
			else:
				Fail+=1
	
	def createpassword(self):
		global Fail
		self.enpas = '#PWD_FB4A:0:{}:{}'.format(int(time.time()), self.password)
		with requests.Session() as r:
			self.headers.update({"x-fb-friendly-name": "FbBloksActionRootQuery-com.bloks.www.bloks.caa.reg.password.async"})
			self.data.update({
				"fb_api_req_friendly_name": "FbBloksActionRootQuery-com.bloks.www.bloks.caa.reg.password.async",
				"variables": "{\"params\":{\"params\":\"{\\\"params\\\":\\\"{\\\\\\\"client_input_params\\\\\\\":{\\\\\\\"safetynet_response\\\\\\\":\\\\\\\"\\\\\\\",\\\\\\\"caa_play_integrity_attestation_result\\\\\\\":\\\\\\\"\\\\\\\",\\\\\\\"flash_call_permissions_status\\\\\\\":{\\\\\\\"READ_PHONE_STATE\\\\\\\":\\\\\\\"DENIED\\\\\\\",\\\\\\\"READ_CALL_LOG\\\\\\\":\\\\\\\"DENIED\\\\\\\",\\\\\\\"ANSWER_PHONE_CALLS\\\\\\\":\\\\\\\"DENIED\\\\\\\"},\\\\\\\"safetynet_token\\\\\\\":\\\\\\\"dW5rbm93bnwxNzI5NDg4OTc5fLUi\\\\/TyV+hEA7n2lK9cKnUlWQODIJQmBjQ==\\\\\\\",\\\\\\\"whatsapp_installed_on_client\\\\\\\":1,\\\\\\\"attestation_result\\\\\\\":{\\\\\\\"data\\\\\\\":\\\\\\\"eyJjaGFsbGVuZ2Vfbm9uY2UiOiIvM0RzUldLNTQwZEQrSG5SQmRMVnhqYjN3WEZBcG90QzRWZVZDSkswODlvPSIsInVzZXJuYW1lIjoic293aGF0aHVlQGFkZHJpbi51ayJ9\\\\\\\",\\\\\\\"signature\\\\\\\":\\\\\\\"MEQCIGEcdEAj4GE+A+pY6wcdyK8CHPJIsAtLEr8d1LMHz6bmAiB1t1riuFEJl1gOESyMY4gzYfnyRrtDUwjJHsjlP+\\\\/kAQ==\\\\\\\",\\\\\\\"keyHash\\\\\\\":\\\\\\\"41a027e5e1fd23df7c15035d2477f1749786ff8bc73176bf2d1670489404be6e\\\\\\\"},\\\\\\\"machine_id\\\\\\\":\\\\\\\"\\\\\\\",\\\\\\\"headers_last_infra_flow_id_safetynet\\\\\\\":\\\\\\\"03a6d253-1759-4995-9a1b-cfb7330ec49a\\\\\\\",\\\\\\\"system_permissions_status\\\\\\\":{\\\\\\\"READ_CONTACTS\\\\\\\":\\\\\\\"DENIED\\\\\\\",\\\\\\\"GET_ACCOUNTS\\\\\\\":\\\\\\\"DENIED\\\\\\\",\\\\\\\"READ_PHONE_STATE\\\\\\\":\\\\\\\"DENIED\\\\\\\",\\\\\\\"READ_PHONE_NUMBERS\\\\\\\":\\\\\\\"DENIED\\\\\\\"},\\\\\\\"email_oauth_token_map\\\\\\\":{},\\\\\\\"fb_ig_device_id\\\\\\\":[],\\\\\\\"request_data_and_challenge_nonce_string\\\\\\\":\\\\\\\"{\\\\\\\\\\\\\\\"challenge_nonce\\\\\\\\\\\\\\\":\\\\\\\\\\\\\\\"\\\\/3DsRWK540dD+HnRBdLVxjb3wXFApotC4VeVCJK089o=\\\\\\\\\\\\\\\",\\\\\\\\\\\\\\\"username\\\\\\\\\\\\\\\":\\\\\\\\\\\\\\\""+self.email+"\\\\\\\\\\\\\\\"}\\\\\\\",\\\\\\\"encrypted_msisdn_for_safetynet\\\\\\\":\\\\\\\"\\\\\\\",\\\\\\\"lois_settings\\\\\\\":{\\\\\\\"lois_token\\\\\\\":\\\\\\\"\\\\\\\",\\\\\\\"lara_override\\\\\\\":\\\\\\\"\\\\\\\"},\\\\\\\"encrypted_password\\\\\\\":\\\\\\\""+self.enpas+"\\\\\\\"},\\\\\\\"server_params\\\\\\\":{\\\\\\\"event_request_id\\\\\\\":\\\\\\\"32d01e6c-aabb-47f5-a518-ac8096cf8e77\\\\\\\",\\\\\\\"is_from_logged_out\\\\\\\":0,\\\\\\\"layered_homepage_experiment_group\\\\\\\":null,\\\\\\\"device_id\\\\\\\":\\\\\\\"463f7aa2-87c0-4345-a3fb-bce0adc35308\\\\\\\",\\\\\\\"waterfall_id\\\\\\\":\\\\\\\"89e9a4d6-fe66-4e33-b40e-8150b5c4d224\\\\\\\",\\\\\\\"INTERNAL__latency_qpl_instance_id\\\\\\\":1.27488520500354E14,\\\\\\\"flow_info\\\\\\\":\\\\\\\"{\\\\\\\\\\\\\\\"flow_name\\\\\\\\\\\\\\\":\\\\\\\\\\\\\\\"new_to_family_fb_default\\\\\\\\\\\\\\\",\\\\\\\\\\\\\\\"flow_type\\\\\\\\\\\\\\\":\\\\\\\\\\\\\\\"ntf\\\\\\\\\\\\\\\"}\\\\\\\",\\\\\\\"is_platform_login\\\\\\\":0,\\\\\\\"INTERNAL__latency_qpl_marker_id\\\\\\\":36707139,\\\\\\\"reg_info\\\\\\\":\\\\\\\"{\\\\\\\\\\\\\\\"first_name\\\\\\\\\\\\\\\":\\\\\\\\\\\\\\\""+self.nama_depan+"\\\\\\\\\\\\\\\",\\\\\\\\\\\\\\\"last_name\\\\\\\\\\\\\\\":\\\\\\\\\\\\\\\""+self.nama_belakang+"\\\\\\\\\\\\\\\",\\\\\\\\\\\\\\\"full_name\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"contactpoint\\\\\\\\\\\\\\\":\\\\\\\\\\\\\\\""+self.email+"\\\\\\\\\\\\\\\",\\\\\\\\\\\\\\\"ar_contactpoint\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"contactpoint_type\\\\\\\\\\\\\\\":\\\\\\\\\\\\\\\"email\\\\\\\\\\\\\\\",\\\\\\\\\\\\\\\"is_using_unified_cp\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"unified_cp_screen_variant\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"is_cp_auto_confirmed\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"is_cp_auto_confirmable\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"confirmation_code\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"birthday\\\\\\\\\\\\\\\":\\\\\\\\\\\\\\\""+self.tgl_lahir+"\\\\\\\\\\\\\\\",\\\\\\\\\\\\\\\"did_use_age\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"gender\\\\\\\\\\\\\\\":1,\\\\\\\\\\\\\\\"use_custom_gender\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"custom_gender\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"encrypted_password\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"username\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"username_prefill\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"fb_conf_source\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"device_id\\\\\\\\\\\\\\\":\\\\\\\\\\\\\\\"463f7aa2-87c0-4345-a3fb-bce0adc35308\\\\\\\\\\\\\\\",\\\\\\\\\\\\\\\"ig4a_qe_device_id\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"family_device_id\\\\\\\\\\\\\\\":\\\\\\\\\\\\\\\"463f7aa2-87c0-4345-a3fb-bce0adc35308\\\\\\\\\\\\\\\",\\\\\\\\\\\\\\\"nta_eligibility_reason\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"ig_nta_test_group\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"user_id\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"safetynet_token\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"safetynet_response\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"machine_id\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"profile_photo\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"profile_photo_id\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"profile_photo_upload_id\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"avatar\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"email_oauth_token_no_contact_perm\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"email_oauth_token\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"email_oauth_tokens\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"should_skip_two_step_conf\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"openid_tokens_for_testing\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"encrypted_msisdn\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"encrypted_msisdn_for_safetynet\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"cached_headers_safetynet_info\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"should_skip_headers_safetynet\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"headers_last_infra_flow_id\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"headers_last_infra_flow_id_safetynet\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"headers_flow_id\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"was_headers_prefill_available\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"sso_enabled\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"existing_accounts\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"used_ig_birthday\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"sync_info\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"create_new_to_app_account\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"skip_session_info\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"ck_error\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"ck_id\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"ck_nonce\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"should_save_password\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"horizon_synced_username\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"fb_access_token\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"horizon_synced_profile_pic\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"is_identity_synced\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"is_msplit_reg\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"user_id_of_msplit_creator\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"dma_data_combination_consent_given\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"xapp_accounts\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"fb_device_id\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"fb_machine_id\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"ig_device_id\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"ig_machine_id\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"should_skip_nta_upsell\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"big_blue_token\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"skip_sync_step_nta\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"caa_reg_flow_source\\\\\\\\\\\\\\\":\\\\\\\\\\\\\\\"login_home_native_integration_point\\\\\\\\\\\\\\\",\\\\\\\\\\\\\\\"ig_authorization_token\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"full_sheet_flow\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"crypted_user_id\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"is_caa_perf_enabled\\\\\\\\\\\\\\\":true,\\\\\\\\\\\\\\\"is_preform\\\\\\\\\\\\\\\":true,\\\\\\\\\\\\\\\"ignore_suma_check\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"ignore_existing_login\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"ignore_existing_login_from_suma\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"ignore_existing_login_after_errors\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"suggested_first_name\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"suggested_last_name\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"suggested_full_name\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"replace_id_sync_variant\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"is_redirect_from_nta_replace_id_sync_variant\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"frl_authorization_token\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"post_form_errors\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"skip_step_without_errors\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"existing_account_exact_match_checked\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"existing_account_fuzzy_match_checked\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"email_oauth_exists\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"confirmation_code_send_error\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"is_too_young\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"source_account_type\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"whatsapp_installed_on_client\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"confirmation_medium\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"source_credentials_type\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"source_cuid\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"source_account_reg_info\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"soap_creation_source\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"source_account_type_to_reg_info\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"registration_flow_id\\\\\\\\\\\\\\\":\\\\\\\\\\\\\\\"bf85b3e7-ce6a-4abf-962b-2c528167c7e9\\\\\\\\\\\\\\\",\\\\\\\\\\\\\\\"should_skip_youth_tos\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"is_youth_regulation_flow_complete\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"is_on_cold_start\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"email_prefilled\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"cp_confirmed_by_auto_conf\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"auto_conf_info\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"in_sowa_experiment\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"youth_regulation_config\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"conf_allow_back_nav_after_change_cp\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"conf_bouncing_cliff_screen_type\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"conf_show_bouncing_cliff\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"eligible_to_flash_call_in_ig4a\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"flash_call_permissions_status\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"attestation_result\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"request_data_and_challenge_nonce_string\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"confirmed_cp_and_code\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"notification_callback_id\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"reg_suma_state\\\\\\\\\\\\\\\":0,\\\\\\\\\\\\\\\"is_msplit_neutral_choice\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"msg_previous_cp\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"ntp_import_source_info\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"youth_consent_decision_time\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"username_screen_experience\\\\\\\\\\\\\\\":\\\\\\\\\\\\\\\"control\\\\\\\\\\\\\\\",\\\\\\\\\\\\\\\"reduced_tos_test_group\\\\\\\\\\\\\\\":\\\\\\\\\\\\\\\"control\\\\\\\\\\\\\\\",\\\\\\\\\\\\\\\"should_show_spi_before_conf\\\\\\\\\\\\\\\":true,\\\\\\\\\\\\\\\"google_oauth_account\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"is_reg_request_from_ig_suma\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"is_igios_spc_reg\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"device_emails\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"is_toa_reg\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"is_threads_public\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"spc_import_flow\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"caa_play_integrity_attestation_result\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"flash_call_provider\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"name_prefill_variant\\\\\\\\\\\\\\\":\\\\\\\\\\\\\\\"control\\\\\\\\\\\\\\\",\\\\\\\\\\\\\\\"spc_birthday_input\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"failed_birthday_year_count\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"user_presented_medium_source\\\\\\\\\\\\\\\":null}\\\\\\\",\\\\\\\"family_device_id\\\\\\\":\\\\\\\"463f7aa2-87c0-4345-a3fb-bce0adc35308\\\\\\\",\\\\\\\"offline_experiment_group\\\\\\\":\\\\\\\"caa_iteration_v6_perf_fb_2\\\\\\\",\\\\\\\"INTERNAL_INFRA_THEME\\\\\\\":\\\\\\\"harm_f,default,default,harm_f\\\\\\\",\\\\\\\"access_flow_version\\\\\\\":\\\\\\\"F2_FLOW\\\\\\\",\\\\\\\"is_from_logged_in_switcher\\\\\\\":0,\\\\\\\"current_step\\\\\\\":5}}\\\"}\",\"bloks_versioning_id\":\"3711cb070fe0ab5acd59ae663b1ae4dc75db6f0c463d26a232fd9d72a63fb3e5\",\"app_id\":\"com.bloks.www.bloks.caa.reg.password.async\"},\"scale\":\"3\",\"nt_context\":{\"using_white_navbar\":true,\"styles_id\":\"cfe75e13b386d5c54b1de2dcca1bee5a\",\"pixel_ratio\":3,\"is_push_on\":true,\"debug_tooling_metadata_token\":null,\"is_flipper_enabled\":false,\"theme_params\":[],\"bloks_version\":\"3711cb070fe0ab5acd59ae663b1ae4dc75db6f0c463d26a232fd9d72a63fb3e5\"}}",
				"fb_api_analytics_tags": "[\"GraphServices\"]",
				"client_trace_id": str(uuid.uuid4())
			})
			post = r.post('https://b-graph.facebook.com/graphql', data=self.data,  headers=self.headers)
			if "Setujui ketentuan dan kebijakan Facebook" in post.text:
				self.create_account()
			else:
				Fail+=1

	def create_account(self):
		global Cp, Fail
		with requests.Session() as r:
			self.headers.update({"x-fb-friendly-name": "FbBloksActionRootQuery-com.bloks.www.bloks.caa.reg.create.account.async"})
			self.data.update({
				"fb_api_req_friendly_name": "FbBloksActionRootQuery-com.bloks.www.bloks.caa.reg.create.account.async",
				"variables": "{\"params\":{\"params\":\"{\\\"params\\\":\\\"{\\\\\\\"client_input_params\\\\\\\":{\\\\\\\"ck_error\\\\\\\":\\\\\\\"\\\\\\\",\\\\\\\"device_id\\\\\\\":\\\\\\\"463f7aa2-87c0-4345-a3fb-bce0adc35308\\\\\\\",\\\\\\\"waterfall_id\\\\\\\":\\\\\\\"89e9a4d6-fe66-4e33-b40e-8150b5c4d224\\\\\\\",\\\\\\\"failed_birthday_year_count\\\\\\\":\\\\\\\"\\\\\\\",\\\\\\\"headers_last_infra_flow_id\\\\\\\":\\\\\\\"03a6d253-1759-4995-9a1b-cfb7330ec49a\\\\\\\",\\\\\\\"machine_id\\\\\\\":\\\\\\\"\\\\\\\",\\\\\\\"should_ignore_existing_login\\\\\\\":0,\\\\\\\"reached_from_tos_screen\\\\\\\":1,\\\\\\\"ck_nonce\\\\\\\":\\\\\\\"\\\\\\\",\\\\\\\"lois_settings\\\\\\\":{\\\\\\\"lois_token\\\\\\\":\\\\\\\"\\\\\\\",\\\\\\\"lara_override\\\\\\\":\\\\\\\"\\\\\\\"},\\\\\\\"ck_id\\\\\\\":\\\\\\\"\\\\\\\",\\\\\\\"no_contact_perm_email_oauth_token\\\\\\\":\\\\\\\"\\\\\\\",\\\\\\\"encrypted_msisdn\\\\\\\":\\\\\\\"\\\\\\\"},\\\\\\\"server_params\\\\\\\":{\\\\\\\"event_request_id\\\\\\\":\\\\\\\"8fe1dbc4-ae4a-4572-9f64-593e4593e5b0\\\\\\\",\\\\\\\"is_from_logged_out\\\\\\\":0,\\\\\\\"layered_homepage_experiment_group\\\\\\\":null,\\\\\\\"device_id\\\\\\\":\\\\\\\"463f7aa2-87c0-4345-a3fb-bce0adc35308\\\\\\\",\\\\\\\"waterfall_id\\\\\\\":\\\\\\\"686c7c49-633c-49b9-90be-de3e03b50751\\\\\\\",\\\\\\\"INTERNAL__latency_qpl_instance_id\\\\\\\":1.2752005070024E14,\\\\\\\"flow_info\\\\\\\":\\\\\\\"{\\\\\\\\\\\\\\\"flow_name\\\\\\\\\\\\\\\":\\\\\\\\\\\\\\\"new_to_family_fb_default\\\\\\\\\\\\\\\",\\\\\\\\\\\\\\\"flow_type\\\\\\\\\\\\\\\":\\\\\\\\\\\\\\\"ntf\\\\\\\\\\\\\\\"}\\\\\\\",\\\\\\\"is_platform_login\\\\\\\":0,\\\\\\\"INTERNAL__latency_qpl_marker_id\\\\\\\":36707139,\\\\\\\"reg_info\\\\\\\":\\\\\\\"{\\\\\\\\\\\\\\\"first_name\\\\\\\\\\\\\\\":\\\\\\\\\\\\\\\""+self.nama_depan+"\\\\\\\\\\\\\\\",\\\\\\\\\\\\\\\"last_name\\\\\\\\\\\\\\\":\\\\\\\\\\\\\\\""+self.nama_belakang+"\\\\\\\\\\\\\\\",\\\\\\\\\\\\\\\"full_name\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"contactpoint\\\\\\\\\\\\\\\":\\\\\\\\\\\\\\\""+self.email+"\\\\\\\\\\\\\\\",\\\\\\\\\\\\\\\"ar_contactpoint\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"contactpoint_type\\\\\\\\\\\\\\\":\\\\\\\\\\\\\\\"email\\\\\\\\\\\\\\\",\\\\\\\\\\\\\\\"is_using_unified_cp\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"unified_cp_screen_variant\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"is_cp_auto_confirmed\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"is_cp_auto_confirmable\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"confirmation_code\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"birthday\\\\\\\\\\\\\\\":\\\\\\\\\\\\\\\""+self.tgl_lahir+"\\\\\\\\\\\\\\\",\\\\\\\\\\\\\\\"did_use_age\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"gender\\\\\\\\\\\\\\\":1,\\\\\\\\\\\\\\\"use_custom_gender\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"custom_gender\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"encrypted_password\\\\\\\\\\\\\\\":\\\\\\\\\\\\\\\""+self.enpas+"\\\\\\\\\\\\\\\",\\\\\\\\\\\\\\\"username\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"username_prefill\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"fb_conf_source\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"device_id\\\\\\\\\\\\\\\":\\\\\\\\\\\\\\\"463f7aa2-87c0-4345-a3fb-bce0adc35308\\\\\\\\\\\\\\\",\\\\\\\\\\\\\\\"ig4a_qe_device_id\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"family_device_id\\\\\\\\\\\\\\\":\\\\\\\\\\\\\\\"463f7aa2-87c0-4345-a3fb-bce0adc35308\\\\\\\\\\\\\\\",\\\\\\\\\\\\\\\"nta_eligibility_reason\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"ig_nta_test_group\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"user_id\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"safetynet_token\\\\\\\\\\\\\\\":\\\\\\\\\\\\\\\"dW5rbm93bnwxNzI5NDg4OTc5fLUi\\\\\\\\\\\\\\\\\\\\/TyV+hEA7n2lK9cKnUlWQODIJQmBjQ==\\\\\\\\\\\\\\\",\\\\\\\\\\\\\\\"safetynet_response\\\\\\\\\\\\\\\":\\\\\\\\\\\\\\\"\\\\\\\\\\\\\\\",\\\\\\\\\\\\\\\"machine_id\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"profile_photo\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"profile_photo_id\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"profile_photo_upload_id\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"avatar\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"email_oauth_token_no_contact_perm\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"email_oauth_token\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"email_oauth_tokens\\\\\\\\\\\\\\\":[],\\\\\\\\\\\\\\\"should_skip_two_step_conf\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"openid_tokens_for_testing\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"encrypted_msisdn\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"encrypted_msisdn_for_safetynet\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"cached_headers_safetynet_info\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"should_skip_headers_safetynet\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"headers_last_infra_flow_id\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"headers_last_infra_flow_id_safetynet\\\\\\\\\\\\\\\":\\\\\\\\\\\\\\\"03a6d253-1759-4995-9a1b-cfb7330ec49a\\\\\\\\\\\\\\\",\\\\\\\\\\\\\\\"headers_flow_id\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"was_headers_prefill_available\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"sso_enabled\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"existing_accounts\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"used_ig_birthday\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"sync_info\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"create_new_to_app_account\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"skip_session_info\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"ck_error\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"ck_id\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"ck_nonce\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"should_save_password\\\\\\\\\\\\\\\":true,\\\\\\\\\\\\\\\"horizon_synced_username\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"fb_access_token\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"horizon_synced_profile_pic\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"is_identity_synced\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"is_msplit_reg\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"user_id_of_msplit_creator\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"dma_data_combination_consent_given\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"xapp_accounts\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"fb_device_id\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"fb_machine_id\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"ig_device_id\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"ig_machine_id\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"should_skip_nta_upsell\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"big_blue_token\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"skip_sync_step_nta\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"caa_reg_flow_source\\\\\\\\\\\\\\\":\\\\\\\\\\\\\\\"login_home_native_integration_point\\\\\\\\\\\\\\\",\\\\\\\\\\\\\\\"ig_authorization_token\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"full_sheet_flow\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"crypted_user_id\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"is_caa_perf_enabled\\\\\\\\\\\\\\\":true,\\\\\\\\\\\\\\\"is_preform\\\\\\\\\\\\\\\":true,\\\\\\\\\\\\\\\"ignore_suma_check\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"ignore_existing_login\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"ignore_existing_login_from_suma\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"ignore_existing_login_after_errors\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"suggested_first_name\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"suggested_last_name\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"suggested_full_name\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"replace_id_sync_variant\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"is_redirect_from_nta_replace_id_sync_variant\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"frl_authorization_token\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"post_form_errors\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"skip_step_without_errors\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"existing_account_exact_match_checked\\\\\\\\\\\\\\\":true,\\\\\\\\\\\\\\\"existing_account_fuzzy_match_checked\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"email_oauth_exists\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"confirmation_code_send_error\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"is_too_young\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"source_account_type\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"whatsapp_installed_on_client\\\\\\\\\\\\\\\":true,\\\\\\\\\\\\\\\"confirmation_medium\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"source_credentials_type\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"source_cuid\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"source_account_reg_info\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"soap_creation_source\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"source_account_type_to_reg_info\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"registration_flow_id\\\\\\\\\\\\\\\":\\\\\\\\\\\\\\\"bf85b3e7-ce6a-4abf-962b-2c528167c7e9\\\\\\\\\\\\\\\",\\\\\\\\\\\\\\\"should_skip_youth_tos\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"is_youth_regulation_flow_complete\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"is_on_cold_start\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"email_prefilled\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"cp_confirmed_by_auto_conf\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"auto_conf_info\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"in_sowa_experiment\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"youth_regulation_config\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"conf_allow_back_nav_after_change_cp\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"conf_bouncing_cliff_screen_type\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"conf_show_bouncing_cliff\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"eligible_to_flash_call_in_ig4a\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"flash_call_permissions_status\\\\\\\\\\\\\\\":{\\\\\\\\\\\\\\\"READ_PHONE_STATE\\\\\\\\\\\\\\\":\\\\\\\\\\\\\\\"DENIED\\\\\\\\\\\\\\\",\\\\\\\\\\\\\\\"READ_CALL_LOG\\\\\\\\\\\\\\\":\\\\\\\\\\\\\\\"DENIED\\\\\\\\\\\\\\\",\\\\\\\\\\\\\\\"ANSWER_PHONE_CALLS\\\\\\\\\\\\\\\":\\\\\\\\\\\\\\\"DENIED\\\\\\\\\\\\\\\"},\\\\\\\\\\\\\\\"attestation_result\\\\\\\\\\\\\\\":{\\\\\\\\\\\\\\\"data\\\\\\\\\\\\\\\":\\\\\\\\\\\\\\\"eyJjaGFsbGVuZ2Vfbm9uY2UiOiIvM0RzUldLNTQwZEQrSG5SQmRMVnhqYjN3WEZBcG90QzRWZVZDSkswODlvPSIsInVzZXJuYW1lIjoic293aGF0aHVlQGFkZHJpbi51ayJ9\\\\\\\\\\\\\\\",\\\\\\\\\\\\\\\"signature\\\\\\\\\\\\\\\":\\\\\\\\\\\\\\\"MEQCIGEcdEAj4GE+A+pY6wcdyK8CHPJIsAtLEr8d1LMHz6bmAiB1t1riuFEJl1gOESyMY4gzYfnyRrtDUwjJHsjlP+\\\\\\\\\\\\\\\\\\\\/kAQ==\\\\\\\\\\\\\\\",\\\\\\\\\\\\\\\"keyHash\\\\\\\\\\\\\\\":\\\\\\\\\\\\\\\"41a027e5e1fd23df7c15035d2477f1749786ff8bc73176bf2d1670489404be6e\\\\\\\\\\\\\\\"},\\\\\\\\\\\\\\\"request_data_and_challenge_nonce_string\\\\\\\\\\\\\\\":\\\\\\\\\\\\\\\"{\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\"challenge_nonce\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\":\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\"\\\\\\\\\\\\\\\\\\\\/3DsRWK540dD+HnRBdLVxjb3wXFApotC4VeVCJK089o=\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\",\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\"username\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\":\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\"sowhathue\\\\\\\\\\\\\\\\u0040addrin.uk\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\"}\\\\\\\\\\\\\\\",\\\\\\\\\\\\\\\"confirmed_cp_and_code\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"notification_callback_id\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"reg_suma_state\\\\\\\\\\\\\\\":0,\\\\\\\\\\\\\\\"is_msplit_neutral_choice\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"msg_previous_cp\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"ntp_import_source_info\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"youth_consent_decision_time\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"username_screen_experience\\\\\\\\\\\\\\\":\\\\\\\\\\\\\\\"control\\\\\\\\\\\\\\\",\\\\\\\\\\\\\\\"reduced_tos_test_group\\\\\\\\\\\\\\\":\\\\\\\\\\\\\\\"control\\\\\\\\\\\\\\\",\\\\\\\\\\\\\\\"should_show_spi_before_conf\\\\\\\\\\\\\\\":true,\\\\\\\\\\\\\\\"google_oauth_account\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"is_reg_request_from_ig_suma\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"is_igios_spc_reg\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"device_emails\\\\\\\\\\\\\\\":[],\\\\\\\\\\\\\\\"is_toa_reg\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"is_threads_public\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"spc_import_flow\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"caa_play_integrity_attestation_result\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"flash_call_provider\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"name_prefill_variant\\\\\\\\\\\\\\\":\\\\\\\\\\\\\\\"control\\\\\\\\\\\\\\\",\\\\\\\\\\\\\\\"spc_birthday_input\\\\\\\\\\\\\\\":false,\\\\\\\\\\\\\\\"failed_birthday_year_count\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"user_presented_medium_source\\\\\\\\\\\\\\\":null}\\\\\\\",\\\\\\\"family_device_id\\\\\\\":\\\\\\\"463f7aa2-87c0-4345-a3fb-bce0adc35308\\\\\\\",\\\\\\\"offline_experiment_group\\\\\\\":\\\\\\\"caa_iteration_v6_perf_fb_2\\\\\\\",\\\\\\\"INTERNAL_INFRA_THEME\\\\\\\":\\\\\\\"harm_f,default,default,harm_f\\\\\\\",\\\\\\\"access_flow_version\\\\\\\":\\\\\\\"F2_FLOW\\\\\\\",\\\\\\\"app_id\\\\\\\":0,\\\\\\\"is_from_logged_in_switcher\\\\\\\":0,\\\\\\\"current_step\\\\\\\":8}}\\\"}\",\"bloks_versioning_id\":\"3711cb070fe0ab5acd59ae663b1ae4dc75db6f0c463d26a232fd9d72a63fb3e5\",\"app_id\":\"com.bloks.www.bloks.caa.reg.create.account.async\"},\"scale\":\"3\",\"nt_context\":{\"using_white_navbar\":true,\"styles_id\":\"cfe75e13b386d5c54b1de2dcca1bee5a\",\"pixel_ratio\":3,\"is_push_on\":true,\"debug_tooling_metadata_token\":null,\"is_flipper_enabled\":false,\"theme_params\":[],\"bloks_version\":\"3711cb070fe0ab5acd59ae663b1ae4dc75db6f0c463d26a232fd9d72a63fb3e5\"}}",
				"fb_api_analytics_tags": "[\"GraphServices\"]",
				"client_trace_id": str(uuid.uuid4())
			})
			post = r.post('https://b-graph.facebook.com/graphql', data=self.data, headers=self.headers).text.replace('\\', '')
			mek = post
			open('Data/Cekacc.json', 'w').write(str(mek))
			if "session_key" in mek or 'access_token' in mek:
				
				token = re.search('"access_token":"(.*?)"', mek)
				id = re.search('"uid":(\\d+)', mek)
				self.tokenku = token.group(1) if token else None
				self.userid = id.group(1) if id else None
					
				try:
					coki = {"datr": re.search('"name":"datr","value":"(.*?)"', mek).group(1),"fr": re.search('"name":"fr","value":"(.*?)"', mek).group(1),"c_user": re.search('"name":"c_user","value":"(\\d+)"', mek).group(1),"xs": re.search('"name":"xs","value":"(.*?)"', mek).group(1),"ps_l": "1","ps_n": "1","wd": "1035x2039"}
				except AttributeError:
					coki = None
					
				if coki:
					self.cookie = ';'.join(f'{key}={value}' for key, value in coki.items())
				else:
					self.cookie = None
				
				asset().kode(20)
				self.code = self.get_code_temp_mail(self.email)
				self.confirm_code(self.code)
			
			elif "Kami Tidak Bisa Membuat Akun untuk Anda" in mek:
				console.print(f" [bold red]# Maaf bos gagal buat akunnya{' '*10}\r")
			elif "Nama pengguna atau kata sandi tidak valid" in mek:
					Cp += 1
					print(f"""\r{' ' * 76}
{{
  {M}Status{P}: {M}Failed{P}
  {M}details{P}: {{
    {M}name{P}: {K}{self.nama_depan}{P},
    {M}email{P}: {K}{self.email}{P},
    {M}password{P}: {K}{self.password}{P},
    {M}birthday{P}: {H}{self.tgl_lahir}{P}
  }}
}}""")
			else:
				Fail+=1

	def confirm_code(self, code):
		global Ok, Cp
		with requests.Session() as r:
			console.print(f"\r [bold green]#[bold white] verification code > {code}{' ' *10}", end = '')
			time.sleep(2.5)
			self.headers.update({"x-fb-friendly-name": "FbBloksActionRootQuery-com.bloks.www.bloks.caa.reg.confirmation.async", "authorization":  f"OAuth {self.tokenku}"})
			self.data.update({
				"fb_api_req_friendly_name": "FbBloksActionRootQuery-com.bloks.www.bloks.caa.reg.confirmation.async",
				"variables": "{\"params\":{\"params\":\"{\\\"params\\\":\\\"{\\\\\\\"client_input_params\\\\\\\":{\\\\\\\"confirmed_cp_and_code\\\\\\\":{},\\\\\\\"code\\\\\\\":\\\\\\\""+self.code+"\\\\\\\",\\\\\\\"fb_ig_device_id\\\\\\\":[],\\\\\\\"device_id\\\\\\\":\\\\\\\"463f7aa2-87c0-4345-a3fb-bce0adc35308\\\\\\\",\\\\\\\"lois_settings\\\\\\\":{\\\\\\\"lois_token\\\\\\\":\\\\\\\"\\\\\\\",\\\\\\\"lara_override\\\\\\\":\\\\\\\"\\\\\\\"}},\\\\\\\"server_params\\\\\\\":{\\\\\\\"event_request_id\\\\\\\":\\\\\\\"7839acd2-baeb-4e2c-9436-85410f63d0c6\\\\\\\",\\\\\\\"is_from_logged_out\\\\\\\":0,\\\\\\\"text_input_id\\\\\\\":127581505000056,\\\\\\\"layered_homepage_experiment_group\\\\\\\":null,\\\\\\\"device_id\\\\\\\":\\\\\\\"463f7aa2-87c0-4345-a3fb-bce0adc35308\\\\\\\",\\\\\\\"waterfall_id\\\\\\\":\\\\\\\"2b514462-5c56-4431-82bb-da7c92f8bad5\\\\\\\",\\\\\\\"wa_timer_id\\\\\\\":\\\\\\\"wa_retriever\\\\\\\",\\\\\\\"INTERNAL__latency_qpl_instance_id\\\\\\\":1.27581505000092E14,\\\\\\\"flow_info\\\\\\\":\\\\\\\"{\\\\\\\\\\\\\\\"flow_name\\\\\\\\\\\\\\\":\\\\\\\\\\\\\\\"new_to_family_fb_default\\\\\\\\\\\\\\\",\\\\\\\\\\\\\\\"flow_type\\\\\\\\\\\\\\\":\\\\\\\\\\\\\\\"ntf\\\\\\\\\\\\\\\"}\\\\\\\",\\\\\\\"is_platform_login\\\\\\\":0,\\\\\\\"sms_retriever_started_prior_step\\\\\\\":0,\\\\\\\"INTERNAL__latency_qpl_marker_id\\\\\\\":36707139,\\\\\\\"reg_info\\\\\\\":\\\\\\\"{\\\\\\\\\\\\\\\"contactpoint\\\\\\\\\\\\\\\":\\\\\\\\\\\\\\\""+self.email+"\\\\\\\\\\\\\\\",\\\\\\\\\\\\\\\"contactpoint_type\\\\\\\\\\\\\\\":\\\\\\\\\\\\\\\"email\\\\\\\\\\\\\\\",\\\\\\\\\\\\\\\"encrypted_msisdn\\\\\\\\\\\\\\\":\\\\\\\\\\\\\\\"\\\\\\\\\\\\\\\",\\\\\\\\\\\\\\\"headers_last_infra_flow_id\\\\\\\\\\\\\\\":\\\\\\\\\\\\\\\"03a6d253-1759-4995-9a1b-cfb7330ec49a\\\\\\\\\\\\\\\",\\\\\\\\\\\\\\\"flash_call_permissions_status\\\\\\\\\\\\\\\":{\\\\\\\\\\\\\\\"READ_PHONE_STATE\\\\\\\\\\\\\\\":\\\\\\\\\\\\\\\"DENIED\\\\\\\\\\\\\\\",\\\\\\\\\\\\\\\"CALL_PHONE\\\\\\\\\\\\\\\":\\\\\\\\\\\\\\\"DENIED\\\\\\\\\\\\\\\",\\\\\\\\\\\\\\\"READ_CALL_LOG\\\\\\\\\\\\\\\":\\\\\\\\\\\\\\\"DENIED\\\\\\\\\\\\\\\",\\\\\\\\\\\\\\\"ANSWER_PHONE_CALLS\\\\\\\\\\\\\\\":\\\\\\\\\\\\\\\"DENIED\\\\\\\\\\\\\\\"},\\\\\\\\\\\\\\\"first_name\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"last_name\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"full_name\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"ar_contactpoint\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"is_using_unified_cp\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"unified_cp_screen_variant\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"is_cp_auto_confirmed\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"is_cp_auto_confirmable\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"confirmation_code\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"birthday\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"did_use_age\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"gender\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"use_custom_gender\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"custom_gender\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"encrypted_password\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"username\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"username_prefill\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"fb_conf_source\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"device_id\\\\\\\\\\\\\\\":\\\\\\\\\\\\\\\"463f7aa2-87c0-4345-a3fb-bce0adc35308\\\\\\\\\\\\\\\",\\\\\\\\\\\\\\\"ig4a_qe_device_id\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"ig_nta_test_group\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"family_device_id\\\\\\\\\\\\\\\":\\\\\\\\\\\\\\\"463f7aa2-87c0-4345-a3fb-bce0adc35308\\\\\\\\\\\\\\\",\\\\\\\\\\\\\\\"nta_eligibility_reason\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"youth_consent_decision_time\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"username_screen_experience\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"user_id\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"safetynet_token\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"safetynet_response\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"machine_id\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"profile_photo\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"profile_photo_id\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"profile_photo_upload_id\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"avatar\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"email_oauth_token_no_contact_perm\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"email_oauth_token\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"email_oauth_tokens\\\\\\\\\\\\\\\":[],\\\\\\\\\\\\\\\"should_skip_two_step_conf\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"openid_tokens_for_testing\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"encrypted_msisdn_for_safetynet\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"cached_headers_safetynet_info\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"should_skip_headers_safetynet\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"headers_last_infra_flow_id_safetynet\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"headers_flow_id\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"was_headers_prefill_available\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"sso_enabled\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"existing_accounts\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"used_ig_birthday\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"sync_info\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"create_new_to_app_account\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"skip_session_info\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"ck_error\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"ck_id\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"ck_nonce\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"should_save_password\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"horizon_synced_username\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"fb_access_token\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"horizon_synced_profile_pic\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"is_identity_synced\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"is_msplit_reg\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"user_id_of_msplit_creator\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"dma_data_combination_consent_given\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"xapp_accounts\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"fb_device_id\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"fb_machine_id\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"ig_device_id\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"ig_machine_id\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"should_skip_nta_upsell\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"big_blue_token\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"skip_sync_step_nta\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"caa_reg_flow_source\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"ig_authorization_token\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"full_sheet_flow\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"crypted_user_id\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"is_caa_perf_enabled\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"is_preform\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"ignore_suma_check\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"ignore_existing_login\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"ignore_existing_login_from_suma\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"ignore_existing_login_after_errors\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"suggested_first_name\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"suggested_last_name\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"suggested_full_name\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"replace_id_sync_variant\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"is_redirect_from_nta_replace_id_sync_variant\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"frl_authorization_token\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"post_form_errors\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"skip_step_without_errors\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"existing_account_exact_match_checked\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"existing_account_fuzzy_match_checked\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"email_oauth_exists\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"confirmation_code_send_error\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"is_too_young\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"source_account_type\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"whatsapp_installed_on_client\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"confirmation_medium\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"source_credentials_type\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"source_cuid\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"source_account_reg_info\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"soap_creation_source\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"source_account_type_to_reg_info\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"registration_flow_id\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"should_skip_youth_tos\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"is_youth_regulation_flow_complete\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"is_on_cold_start\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"email_prefilled\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"cp_confirmed_by_auto_conf\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"auto_conf_info\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"in_sowa_experiment\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"eligible_to_flash_call_in_ig4a\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"youth_regulation_config\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"conf_allow_back_nav_after_change_cp\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"conf_bouncing_cliff_screen_type\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"conf_show_bouncing_cliff\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"is_msplit_neutral_choice\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"msg_previous_cp\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"ntp_import_source_info\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"attestation_result\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"request_data_and_challenge_nonce_string\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"confirmed_cp_and_code\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"notification_callback_id\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"reg_suma_state\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"reduced_tos_test_group\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"should_show_spi_before_conf\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"google_oauth_account\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"is_reg_request_from_ig_suma\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"is_igios_spc_reg\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"device_emails\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"is_toa_reg\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"is_threads_public\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"spc_import_flow\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"caa_play_integrity_attestation_result\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"flash_call_provider\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"name_prefill_variant\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"spc_birthday_input\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"failed_birthday_year_count\\\\\\\\\\\\\\\":null,\\\\\\\\\\\\\\\"user_presented_medium_source\\\\\\\\\\\\\\\":null}\\\\\\\",\\\\\\\"family_device_id\\\\\\\":\\\\\\\"463f7aa2-87c0-4345-a3fb-bce0adc35308\\\\\\\",\\\\\\\"offline_experiment_group\\\\\\\":\\\\\\\"caa_iteration_v6_perf_fb_2\\\\\\\",\\\\\\\"INTERNAL_INFRA_THEME\\\\\\\":\\\\\\\"harm_f\\\\\\\",\\\\\\\"access_flow_version\\\\\\\":\\\\\\\"F2_FLOW\\\\\\\",\\\\\\\"is_from_logged_in_switcher\\\\\\\":0,\\\\\\\"current_step\\\\\\\":10}}\\\"}\",\"bloks_versioning_id\":\"3711cb070fe0ab5acd59ae663b1ae4dc75db6f0c463d26a232fd9d72a63fb3e5\",\"app_id\":\"com.bloks.www.bloks.caa.reg.confirmation.async\"},\"scale\":\"3\",\"nt_context\":{\"using_white_navbar\":true,\"styles_id\":\"cfe75e13b386d5c54b1de2dcca1bee5a\",\"pixel_ratio\":3,\"is_push_on\":true,\"debug_tooling_metadata_token\":null,\"is_flipper_enabled\":false,\"theme_params\":[],\"bloks_version\":\"3711cb070fe0ab5acd59ae663b1ae4dc75db6f0c463d26a232fd9d72a63fb3e5\"}}",
				"fb_api_analytics_tags": "[\"GraphServices\"]",
				"client_trace_id": str(uuid.uuid4())
			})
			post = r.post('https://z-m-graph.facebook.com/graphql', data=self.data,  headers=self.headers).text.replace('\\', '')
			if "confirmation_success" in post:
				waktu = datetime.now(pytz.timezone('Asia/Jakarta')).strftime("%d-%m-%Y %H:%M:%S")
				Ok+=1
				AutentikasiTwoFactor().tahap_pertama(self.cookie, self.email)
				asset().delayy(20)
				start = Pic_Profile(self.cookie)
				hasil = start.post()
				posx = Edit_profile()
				posx.intro_profile(self.cookie)
				if POSTS["STATUS"] is not None:
					texz = posx.posting(self.cookie)
					print(f"""\r{' ' * 76}
{{
  {M}Status{P}: {H}Success{P}
  {M}Timestamp{P}: {H}{waktu}{P},
  {M}details{P}: {{
    {M}name{P}: {H}{self.nama_depan} {self.nama_belakang}{P},
    {M}userID{P}: {H}{self.userid}{P},
    {M}token{P}: {H}{self.tokenku}{P},
    {M}cookies{P}: {H}{self.cookie}{P},
    {M}profile{P}: {hasil},
    {M}posting{P}: {texz},
    {M}email{P}: {H}{self.email}{P},
    {M}password{P}: {H}{self.password}{P},
    {M}birthday{P}: {H}{self.tgl_lahir}{P}
  }}
}}""")
				else:
					print(f"""\r{' ' * 76}
{{
  {M}Status{P}: {H}Success{P}
  {M}Timestamp{P}: {H}{waktu}{P},
  {M}details{P}: {{
    {M}name{P}: {H}{self.nama_depan} {self.nama_belakang}{P},
    {M}userID{P}: {H}{self.userid}{P},
    {M}token{P}: {H}{self.tokenku}{P},
    {M}cookies{P}: {H}{self.cookie}{P},
    {M}profile{P}: {hasil},
    {M}email{P}: {H}{self.email}{P},
    {M}password{P}: {H}{self.password}{P},
    {M}birthday{P}: {H}{self.tgl_lahir}{P}
  }}
}}""")
				json_ = {
					'Name': f'{self.nama_depan} {self.nama_belakang}',
					'Userid': f'{self.userid}',
					'Email': f'{self.email}',
					'Password': f'{self.password}',
					'Tanggal lahir': f'{self.tgl_lahir}',
					'Cookies': f'{self.cookie}',
					'Token': f'{self.tokenku}'
				}
				file_path = 'Results/AkunFbNew.json'
				os.makedirs(os.path.dirname(file_path), exist_ok=True)
				if os.path.exists(file_path):
					with open(file_path, 'r') as file:
						try:
							data = json.load(file)
						except json.JSONDecodeError:
							data = []
				else:
					data = []
				data.append(json_)
				with open(file_path, 'w') as file:
					json.dump(data, file, indent=4)
			else:
				Cp+=1


class Pic_Profile:
	def __init__(self, cookie):
		self.cookie = cookie
		self.path = 'Data/pinterest.txt'
			
	def post(self):
		img = open('Data/pinterest.txt', 'r').read().splitlines()
		image_url = random.choice(img)
		try:
			with requests.Session() as r:
				id = re.search('c_user=(\\d+)', str(self.cookie)).group(1)
				req = r.get(f'https://web.facebook.com/profile.php?id={id}', cookies={'cookie': self.cookie}).text
				params = asset().data_graphql(req, id)
				params.update({
					'profile_id': id,
					'photo_source': "57",
				})
				files = {'file':('image.jpg',urllib.request.urlopen(image_url).read())}
				pos = r.post("https://web.facebook.com/profile/picture/upload/", cookies={'cookie': self.cookie}, params=params,  files=files).text
				fbid = re.search('"fbid":"(\d+)"', str(pos)).group(1)
				data = asset().data_graphql(req, id)
				data.update({
					"fb_api_caller_class": "RelayModern",
					"fb_api_req_friendly_name": "ProfileCometProfilePictureSetMutation",
					"variables": json.dumps({"input":{"attribution_id_v2":"ProfileCometTimelineListViewRoot.react,comet.profile.timeline.list,via_cold_start,1729674295794,691444,190055527696468,,","caption":"","existing_photo_id":fbid,"expiration_time":None,"profile_id":id,"profile_pic_method":"EXISTING","profile_pic_source":"TIMELINE","scaled_crop_rect":{"height":1,"width":1,"x":0,"y":0},"skip_cropping": True,"actor_id":id,"client_mutation_id":"2"},"isPage":False,"isProfile":True,"sectionToken":"UNKNOWN","collectionToken":"UNKNOWN","scale":3,"__relay_internal__pv__ProfileGeminiIsCoinFlipEnabledrelayprovider":False}),
					"server_timestamps": "true",
					"doc_id": "28132579203008372"
				})
				post = r.post('https://web.facebook.com/api/graphql/', data=data, cookies = {'cookie':self.cookie})
				if 'profilePhoto' in post.text:
					return f"{H}Foto profile berhasil dirubah bos{P}"
				else:
					return f"{M}Foto profile gagal dirubah bos{P}"
					
		except Exception as e:
			return f"{M}Foto profile gagal dirubah bos{P}"

class Edit_profile:
	def __init__(self) -> None:
		pass
	
	def intro_profile(self, cookie):
		try:
			with requests.Session() as r:
				id = re.search('c_user=(\\d+)', str(cookie)).group(1)
				response = r.get(f'https://web.facebook.com/profile.php?id={id}&sk=about_work_and_education', cookies={'cookie': cookie}).text
				
				cltk = re.search(r'"collectionToken":"(.*?)"', str(response))
				sectoken = re.search(r'"sectionToken":"(.*?)"', str(response))
				collectionToken = cltk.group(1) if cltk else None
				sectionToken = sectoken.group(1) if sectoken else None
				
				data = asset().data_graphql(response, id)
				data.update({
					"fb_api_caller_class": "RelayModern",
					"fb_api_req_friendly_name": "ComposerStoryCreateMutation",
					"variables": json.dumps({"collectionToken":collectionToken,"input":{"description":None,"employer_id":"1953170501618069","employer_name":None,"end_date":{},"is_current":True,"location_id":"102173726491792","mutation_surface":"PROFILE","position_id":"186213662204063","position_name":None,"privacy":{"allow":[],"base_state":"EVERYONE","deny":[],"tag_expansion_state":"UNSPECIFIED"},"start_date":{"day":int(random.randint(1,28)),"month":int(random.randint(1,12)),"year":int(random.randint(1980,2024))},"actor_id":id,"client_mutation_id":"5"},"scale":3,"sectionToken":sectionToken,"useDefaultActor":False}),
					"server_timestamps": "true",
					"doc_id": "8496075440505870"
				})
				post = r.post('https://web.facebook.com/api/graphql/', data=data, cookies = {'cookie':cookie})
				if 'entity' in post.text:
					pass
				else:
					pass
					
		except Exception as e:
			pass
			
	def posting(self, cookie):
		try:
			with requests.Session() as r:
				id = re.search('c_user=(\\d+)', str(cookie)).group(1)
				req = r.get(f'https://web.facebook.com/profile.php?id={id}', cookies={'cookie': cookie}).text
				data = asset().data_graphql(req, id)
				data.update({
					"fb_api_caller_class": "RelayModern",
					"fb_api_req_friendly_name": "ComposerStoryCreateMutation",
					"variables": json.dumps({"input":{"composer_entry_point":"inline_composer","composer_source_surface":"timeline","idempotence_token":"437cba73-b0e3-4655-aada-38dfd789008e_FEED","source":"WWW","attachments":[],"audience":{"privacy":{"allow":[],"base_state":"EVERYONE","deny":[],"tag_expansion_state":"UNSPECIFIED"}},"message":{"ranges":[],"text":POSTS['STATUS']},"with_tags_ids":None,"inline_activities":[],"text_format_preset_id":"0","publishing_flow":{"supported_flows":["ASYNC_SILENT","ASYNC_NOTIF","FALLBACK"]},"logging":{"composer_session_id":"437cba73-b0e3-4655-aada-38dfd789008e"},"navigation_data":{"attribution_id_v2":"ProfileCometTimelineListViewRoot.react,comet.profile.timeline.list,unexpected,1730202783968,840602,190055527696468,,;CometErrorRoot.react,comet.error,via_cold_start,1730202779383,997568,,,"},"tracking":[None],"event_share_metadata":{"surface":"timeline"},"actor_id":id,"client_mutation_id":"3"},"feedLocation":"TIMELINE","feedbackSource":0,"focusCommentID":None,"gridMediaWidth":230,"groupID":None,"scale":3,"privacySelectorRenderLocation":"COMET_STREAM","checkPhotosToReelsUpsellEligibility":True,"renderLocation":"timeline","useDefaultActor":False,"inviteShortLinkKey":None,"isFeed":False,"isFundraiser":False,"isFunFactPost":False,"isGroup":False,"isEvent":False,"isTimeline":True,"isSocialLearning":False,"isPageNewsFeed":False,"isProfileReviews":False,"isWorkSharedDraft":False,"hashtag":None,"canUserManageOffers":False,"__relay_internal__pv__CometUFIShareActionMigrationrelayprovider":True,"__relay_internal__pv__GHLShouldChangeSponsoredDataFieldNamerelayprovider":False,"__relay_internal__pv__GHLShouldChangeAdIdFieldNamerelayprovider":False,"__relay_internal__pv__IncludeCommentWithAttachmentrelayprovider":True,"__relay_internal__pv__CometUFIReactionsEnableShortNamerelayprovider":False,"__relay_internal__pv__CometImmersivePhotoCanUserDisable3DMotionrelayprovider":False,"__relay_internal__pv__IsWorkUserrelayprovider":False,"__relay_internal__pv__IsMergQAPollsrelayprovider":False,"__relay_internal__pv__FBReelsMediaFooter_comet_enable_reels_ads_gkrelayprovider":True,"__relay_internal__pv__StoriesArmadilloReplyEnabledrelayprovider":False,"__relay_internal__pv__EventCometCardImage_prefetchEventImagerelayprovider":False,"__relay_internal__pv__GHLShouldChangeSponsoredAuctionDistanceFieldNamerelayprovider":True}),
					"server_timestamps": "true",
					"doc_id": "8941629622565537"
				})
				post = r.post('https://web.facebook.com/api/graphql/', data=data, cookies = {'cookie':cookie})
				if "story_create" in post.text:
					return f"{H}berhasil posting {POSTS['STATUS']}{P}"
				else:
					return f"{M}gagal posting {POSTS['STATUS']}{P}"
		except Exception as e:
			return f"{M}gagal posting {POSTS['STATUS']}{P}"
			
class AutentikasiTwoFactor:
	def __init__(self):
		pass
	
	def tahap_pertama(self, cookie, email):
		try:
			with requests.Session() as r:
				username, domain = email.split('@')
				masked_username = f"{username[0]}****{username[-1]}"
				masked_domain = f"{domain[0]}*****{domain[-3:]}"
				mail = f"{masked_username}@{masked_domain}"
				print(mail)
				id = re.search('c_user=(\\d+)', str(cookie)).group(1)
				response = r.get('https://accountscenter.facebook.com/password_and_security/two_factor', cookies = {'cookie': cookie}).text
				data = asset().data_graphql(response, id)
				data.update({
					"fb_api_caller_class": "RelayModern",
					"fb_api_req_friendly_name": "useTwoStepVerificationSendCodeMutation",
					'variables': json.dumps({"encryptedContext":"","challenge":"EMAIL","maskedContactPoint":mail}),
					"server_timestamps": "true",
					"doc_id": "7767429506681192"
				})
				post = r.post('https://accountscenter.facebook.com/api/graphql/', data=data, cookies = {'cookie':cookie})
				open('Data/Post.txt', 'w').write(str(post.text))
				if '"is_success": true' in post.text:
					asset().kode(20)
					code = self.get_code_temp_mail(email)
					print(code)
					exit()
				elif '"is_success": false' in post.text:
					exit()
		except Exception as e:
			raise e
if __name__ == '__main__':
	if os.path.exists("Results") == False:
		os.mkdir("Results")
	os.system('clear')
	AccountCreator().menu()