import requests, hashlib, string, random, uuid, time, calendar, re, json, urllib.parse, base64, pickle

class colors:

    ENDC     = '\33[0m'
    BOLD     = '\33[1m'
    ITALIC   = '\33[3m'
    URL      = '\33[4m'
    BLINK    = '\33[5m'
    BLINK2   = '\33[6m'
    SELECTED = '\33[7m'

    BLACK  = '\33[30m'
    RED    = '\33[31m'
    GREEN  = '\33[32m'
    YELLOW = '\33[33m'
    BLUE   = '\33[34m'
    VIOLET = '\33[35m'
    BEIGE  = '\33[36m'
    WHITE  = '\33[37m'

    BLACKBG  = '\33[40m'
    REDBG    = '\33[41m'
    GREENBG  = '\33[42m'
    YELLOWBG = '\33[43m'
    BLUEBG   = '\33[44m'
    VIOLETBG = '\33[45m'
    BEIGEBG  = '\33[46m'
    WHITEBG  = '\33[47m'

    GREY    = '\33[90m'
    RED2    = '\33[91m'
    GREEN2  = '\33[92m'
    YELLOW2 = '\33[93m'
    BLUE2   = '\33[94m'
    VIOLET2 = '\33[95m'
    BEIGE2  = '\33[96m'
    WHITE2  = '\33[97m'

    GREYBG    = '\33[100m'
    REDBG2    = '\33[101m'
    GREENBG2  = '\33[102m'
    YELLOWBG2 = '\33[103m'
    BLUEBG2   = '\33[104m'
    VIOLETBG2 = '\33[105m'
    BEIGEBG2  = '\33[106m'
    WHITEBG2  = '\33[107m'

def escape(string):
    return string.replace('/', '\\')
    
def printc(value, color='', nonewline=None, more=''):

    end = '\n'
    if nonewline: end = ''

    if color: print(color + value + colors.ENDC + more, end=end)
    else: print(value + more, end=end)

def inputc(value, color='', more=''):

    if color: return input(color + value + colors.ENDC + more)
    else: return input(value + more) 

def RandomString(n = 10):
    letters = string.ascii_lowercase + '1234567890'
    return ''.join(random.choice(letters) for i in range(n))

def RandomStringUpper(n = 10):
    letters = string.ascii_uppercase + '1234567890'
    return ''.join(random.choice(letters) for i in range(n))

def RandomStringChars(n = 10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(n))

def randomStringWithChar(stringLength=10):
    letters = string.ascii_lowercase + '1234567890'
    result = ''.join(random.choice(letters) for i in range(stringLength - 1))
    return RandomStringChars(1) + result

def printn(args): print(args, end='')
def ClearConsole(): printn("\033[H\033[2J")
def DeleteLine(): printn("\033[F"); print("\033[K")

class account:

    def __init__(self, username: str, password: str):
        self.fheaders = self.fetch_headers()
        self.username = username
        self.password = password
        self.cookies = dict()
        self.csrftoken = self.fheaders['csrftoken']
        self.mid = self.fheaders['mid']
        self.DeviceID = self.generate_device_id(self.hex_digest(username, password))
        self.guid1 = str(uuid.uuid4())
        self.guid2 = str(uuid.uuid4())
        self.guid3 = str(uuid.uuid4())
        self.checkpoint = bool()
        self.loggedIn = bool()
        self.ds_user_id = str()
        self.proxies = []
        self.proxiesIndex = 0
        self.proxyInNeed = bool()
        self.proxy = str()
        self.kickmeout = bool()

        TimeStamp = calendar.timegm(time.gmtime())

        headers = {}
        headers['User-Agent'] = self.UserAgent()
        headers['Host'] = 'i.instagram.com'
        headers['x-ig-app-locale'] = 'en_SA'
        headers['x-ig-device-locale'] = 'en_SA' 
        headers['x-ig-mapped-locale'] = 'en_US'
        headers['x-pigeon-session-id'] = self.guid()
        headers['x-pigeon-rawclienttime'] = f'{TimeStamp}'
        headers['x-ig-connection-speed'] = '643kbps'
        headers['x-ig-bandwidth-speed-kbps'] = '1236.889'
        headers['x-ig-bandwidth-totalbytes-b'] = '6672937'
        headers['x-ig-bandwidth-totaltime-ms'] = '7015'
        headers['x-ig-app-startup-country'] = 'SA'
        headers['x-bloks-version-id'] = '85e371bf185c688d008ad58d18c84943f3e6d568c4eecd561eb4b0677b1e4c55'
        headers['x-ig-www-claim'] = '0'
        headers['x-bloks-is-layout-rtl'] = 'false'
        headers['x-ig-device-id'] = self.guid()
        headers['x-ig-android-id'] = self.DeviceID
        headers['x-ig-connection-type'] = 'WIFI'
        headers['x-ig-capabilities'] = '3brTvw8='
        headers['x-ig-app-id'] = '567067343352427'
        headers['accept-language'] = 'en-SA, en-US'
        headers['x-mid'] = self.mid
        headers['content-type'] = 'application/x-www-form-urlencoded; charset=UTF-8' 
        headers['accept-encoding'] = 'gzip, deflate'
        headers['x-fb-http-engine'] = 'Liger'
        headers['Connection'] = 'close'
        self.headers = headers
        self.login()

    def UserAgent(self): # "user-agent"
        version = f'{random.randint(3, 138)}.{random.randint(5, 10)}.{random.randint(0, 10)}'
        if random.randint(0, 1):
            version = f'{random.randint(4, 138)}.{random.randint(0, 10)}.{random.randint(0, 10)}'
        if random.randint(0, 1):
            version = '155.0.0.37.107' #last version

        return self.randDevice().replace('(VERSION)', version)

    def guid(self): return str(uuid.uuid4()) # "phone_id", "guid", "adid"

    def fetch_headers(self) -> dict:
        url = 'https://i.instagram.com/api/v1/si/fetch_headers/'

        headers = {}
        headers['Host'] = 'i.instagram.com'
        headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:80.0) Gecko/20100101 Firefox/80.0'
        headers['Accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
        headers['Accept-Language'] = 'ar,en-US;q=0.7,en;q=0.3'
        headers['Accept-Encoding'] = 'gzip, deflate, br'
        headers['Connection'] = 'close'

        return requests.get(url, headers=headers).cookies.get_dict()

    def hex_digest(self, *args):
        m = hashlib.md5()
        m.update(b''.join([arg.encode('utf-8') for arg in args]))
        return m.hexdigest()

    def generate_device_id(self, seed):
        volatile_seed = "12345"
        m = hashlib.md5()
        m.update(seed.encode('utf-8') + volatile_seed.encode('utf-8'))
        return 'android-' + m.hexdigest()[:16]

    def randDevice(self) -> str:

        dpi = [
        '480', '320', '640', '515', '120', '160', '240', '800'
        ]
        manufacturer = [
            'HUAWEI', 'Xiaomi', 'samsung', 'OnePlus', 'LGE/lge', 'ZTE', 'HTC',
            'LENOVO', 'MOTOROLA', 'NOKIA', 'OPPO', 'SONY', 'VIVO', 'LAVA'
        ]
        
        randResolution = random.randrange(2, 9) * 180
        lowerResolution = randResolution - 180

        DEVICE = {
            'android_version': random.randrange(18, 25),
            'android_release': f'{random.randrange(1, 7)}.{random.randrange(0, 7)}',
            'dpi': f'{random.choice(dpi)}dpi',
            'resolution': f'{lowerResolution}x{randResolution}',
            'manufacturer': random.choice(manufacturer),
            'device': f'{random.choice(manufacturer)}-{RandomStringUpper(5)}',
            'model': f'{randomStringWithChar(4)}',
            'cpu': f'{RandomStringChars(2)}{random.randrange(1000, 9999)}'
        }

        if random.randrange(0, 2):
            DEVICE['android_release'] = f'{random.randrange(1, 7)}.{random.randrange(0, 7)}.{random.randrange(1, 7)}'

        USER_AGENT_BASE = (
            'Instagram (VERSION) '
            'Android ({android_version}/{android_release}; '
            '{dpi}; {resolution}; {manufacturer}; '
            '{device}; {model}; {cpu}; en_US)'
        )

        return USER_AGENT_BASE.format(**DEVICE)

    def sendCode(self, url, security_code):
        postData = {}
        guid = str(uuid.uuid4())

        postData['security_code'] = security_code
        postData['guid'] = self.guid1
        postData['_csrftoken'] = self.cookies['csrftoken']
        postData['device_id'] = self.DeviceID
        
        payload = {}
        payload['signed_body'] = f'SIGNATURE.{json.dumps(postData)}'

        response = requests.post(url, headers=self.headers, cookies=self.cookies, data=payload, verify=True)
        return response

    def sendMethod(self, url, choice):
        postData = {}
        guid = str(uuid.uuid4())

        postData['choice'] = choice # (Phone number = 0, email = 1)
        postData['guid'] = self.guid1
        postData['_csrftoken'] = self.cookies['csrftoken']
        postData['device_id'] = self.DeviceID

        payload = {}
        payload['signed_body'] = f'SIGNATURE.{json.dumps(postData)}'

        return requests.post(url, headers=self.headers, cookies=self.cookies, data=payload, verify=True)

    def login(self):

        TimeStamp = calendar.timegm(time.gmtime())

        data = {}
        data['jazoest'] = '22713'
        data['phone_id'] = self.guid1
        data['enc_password'] = f'#PWD_INSTAGRAM_BROWSER:0:{TimeStamp}:{self.password}'
        data['_csrftoken'] = self.csrftoken
        data['username'] = self.username
        data['adid'] = self.guid2
        data['guid'] = self.guid3
        data['device_id'] = self.DeviceID
        data['google_tokens'] = '[]'
        data['login_attempt_count'] = '0'

        payload = {}
        payload['signed_body'] = f'SIGNATURE.{json.dumps(data)}'

        response = requests.post('https://i.instagram.com/api/v1/accounts/login/', headers=self.headers, cookies=self.fheaders, data=payload, verify=True)
        if 'logged_in_user' in response.text:
            self.loggedIn = True
            self.cookies = response.cookies.get_dict()
            self.csrftoken = self.cookies['csrftoken']
            self.ds_user_id = self.cookies['ds_user_id']
            printc(f'Logged In @{self.username} Successfully', colors.GREEN2)
            #printc('SessionID: ', colors.GREEN2, more=self.cookies['sessionid'])
        elif 'challenge_required' in response.text:
            printc(f'@{self.username} Challenge is required', colors.RED)
            return
            self.checkpoint = True
            self.cookies = response.cookies.get_dict()

            checkpoint_path = re.findall(r'"api_path": "(.*?)"', response.text)[0]
            challenge_url = f'https://i.instagram.com/api/v1{checkpoint_path}'

            getMethods = requests.get(challenge_url, headers=self.headers, cookies=self.cookies)

            phone = bool()
            email = bool()
            try:
                step_name = getMethods.json()['step_name'] 
            except Exception as ex:
                printc('Error, @ctpe', colors.RED)
                print(getMethods.text)
                exit()
           
            if step_name == "select_verify_method":
                if "phone_number" in getMethods.text:
                    phone = True
                if "email" in getMethods.text:
                    email = True
            elif step_name == "delta_login_review":
                choice = 0
            else:
                print(f'Strange step_name: {step_name}\n Send me this {insta}')
                choice = 0

            printc('Challenge is required', colors.RED)
            if email:
                printc('1', colors.YELLOW, more=') email')
            if phone:
                printc('0', colors.YELLOW, more=') phone number')
            choice = inputc('Choose a method to unlock your account: ', colors.YELLOW)
            
            res = self.sendMethod(challenge_url, choice)
            sendto = res.json()['step_data']['contact_point']
            print(f'A code has been sent to {sendto}')
            
            code = inputc('Enter code: ', colors.YELLOW)
            response = self.sendCode(challenge_url, code)
            if 'logged_in_user' in response.text:
                self.loggedIn = True
                self.cookies = response.cookies.get_dict()
                self.csrftoken = self.cookies['csrftoken']
                self.ds_user_id = self.cookies['ds_user_id']
                printc('Logged In Successfully', colors.GREEN2)
                printc('SessionID: ', colors.GREEN2, more=self.cookies['sessionid'])
            else: printc('Login failure, try again', colors.GREEN2); exit()

        elif "Incorrect Username" in response.text:
            printc(f'@{self.username} doesn\'t not exist', colors.RED)
        elif 'Incorrect password' in response.text:
            printc(f'@{self.username} wrong password', colors.RED)
        elif 'inactive user' in response.text:
            printc(f'@{self.username} banned account', colors.RED)
        else:
            printc(f'@{self.username} unknown response\n{response.text}\n', colors.RED)

    #id_to_shortcode = lambda instagram_id: base64.b64encode(instagram_id.to_bytes(9, 'big'), b'-_').decode().replace('A', ' ').lstrip().replace(' ', 'A')

    def shortcodeToID(self, shortcode):
        code = ('A' * (12-len(shortcode)))+shortcode
        return int.from_bytes(base64.b64decode(code.encode(), b'-_'), 'big')

    def getID(self, us):
        headers = {}
        headers["User-Agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:78.0) Gecko/20100101 Firefox/78.0"
        headers["Host"] = "www.instagram.com"
        headers["Accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
        headers["Accept-Language"] = "ar,en-US;q=0.7,en;q=0.3"
        headers["Accept-Encoding"] = "gzip, deflate, br"
        headers["Connection"] = "keep-alive"

        res = requests.get(f'https://www.instagram.com/{us}/?__a=1', headers=headers, cookies=self.cookies)
        return res.json()['graphql']['user']['id'] 

    def sendComment(self, shortcode, comment, postID=None):
        url = f'https://i.instagram.com/api/v1/media/{self.shortcodeToID(shortcode)}/comment/'

        if postID:
            url = f'https://i.instagram.com/api/v1/media/{postID}/comment/'

        data = {
            "delivery_class":"organic",
            "idempotence_token":f'{self.guid()}',
            "carousel_index":"0",
            "_csrftoken":f"{self.csrftoken}",
            "radio_type":"wifi-none",
            "_uid":f'{self.ds_user_id}',
            "_uuid":f'{self.guid()}',
            "comment_text":f'{comment}',
            "is_carousel_bumped_post":"false",
            "feed_position":"0"
        }

        payload = {}
        payload['signed_body'] = f'SIGNATURE.{json.dumps(data)}'

        if self.proxies:
            if self.proxyInNeed:
                self.proxy = self.proxiesIndex
                if self.proxiesIndex == len(self.proxies) - 1:
                    self.proxiesIndex = 0
                else: self.proxiesIndex += 1

            try:
                if self.proxy:
                    proxies = {'http': self.proxy, 'https': self.proxy}
                    response = requests.post(url, headers=self.headers, cookies=self.cookies, data=payload, verify=True, proxies=proxies)
                else:
                    response = requests.post(url, headers=self.headers, cookies=self.cookies, data=payload, verify=True)
            except Exception:
                if self.proxyInNeed:
                    self.proxy = self.proxiesIndex
                    if self.proxiesIndex == len(self.proxies) - 1:
                        self.proxiesIndex = 0
                    else: self.proxiesIndex += 1
            else:
                if response.json()['status'] == 'ok':
                    printc(f'Sent Successfully by @{self.username}', color=colors.GREEN)
                    self.proxyInNeed = False
                elif 'Commenting is Off' in response.text:
                    printc(f'You can\'t comment in the target post, cause commenting is Off', color=colors.RED2)
                    exit(1)
                elif 'feedback_required' in response.text or 'repute/report_problem/instagram_comment/' in response.text:
                    printc(f'@{self.username} Got comment\'s block', color=colors.RED2)
                    self.kickmeout = True
                else: self.proxyInNeed = True
        else:
            response = requests.post(url, headers=self.headers, cookies=self.cookies, data=payload, verify=True)
            print(response.text)
            if response.json()['status'] == 'ok':
                printc(f'Sent Successfully by @{self.username}: ', color=colors.GREEN)
            elif 'feedback_required' in response.text or 'repute/report_problem/instagram_comment/' in response.text:
                printc(f'@{self.username} Got comment\'s block', color=colors.RED2)
                self.kickmeout = True
            else: self.kickmeout = True

ClearConsole()
printc('''
  _____                          __  ___       __ 
 / ___/__  __ _  __ _  ___ ___  / /_/ _ )___  / /_
/ /__/ _ \/  ' \/  ' \/ -_) _ \/ __/ _  / _ \/ __/
\___/\___/_/_/_/_/_/_/\__/_//_/\__/____/\___/\__/  

''', colors.BLUE)

printc(f'By Hades, inst: @0xhades', colors.BLUE2)
print()

pickled = bool()

target = str()
usernames = []
passwords = []
accounts = []
proxies = []
mentions = []
comments = []
mention = bool()
loop = bool()
eloop = 0
wloop = 0
sleep = int()


target = inputc('Enter the Post ID (example: CFMFOeijE-v): ', colors.YELLOW)
sleep = int(inputc('sleep (milliseconds, best: 500, no? = 0): ', colors.YELLOW))

choice = inputc('Multi accounts(M) or single(S)? or saved sessions(Pickle)(P) [M/S/P]: ', colors.YELLOW)

if choice.lower() == 'm':
    choice = inputc('Combo list(C) or (usernames+password)(T) [C/T]: ', colors.YELLOW)
    if choice.lower() == 'c':
        combos = open(escape(inputc('Enter the combo list: ', colors.BLUE)) , 'r').read().splitlines()
        for combo in combos:
            usernames.append(combo.split(':')[0])
            passwords.append(combo.split(':')[1])
    else:
        usernames = open(escape(inputc('Enter the usernames list: ', colors.BLUE)) , 'r').read().splitlines()
        passwords = open(escape(inputc('Enter the passwords list: ', colors.BLUE)) , 'r').read().splitlines()

elif choice.lower() == 'p':
    with open(escape(inputc('Enter the path to the sessions: ', colors.BLUE)), 'rb') as f:
        accounts = pickle.load(f)
    pickled = True

else:
    usernames.append(inputc('Username: ', colors.YELLOW))
    passwords.append(inputc('Password: ', colors.YELLOW))

if len(usernames) != len(passwords): printc(f'Usernames list and passwords are not equal', colors.RED); exit(1)

if not pickled:
    for i in range(len(usernames)):
        acc = account(usernames[i], passwords[i])
        time.sleep(sleep / 1000)
        if acc.loggedIn:
            accounts.append(acc)

    choice = inputc('Want to save the sessions (cookies)? [Y\\N]: ', colors.YELLOW)
    if choice.lower() == 'y':
        with open(escape(inputc('Enter the path to a file: ', colors.BLUE)), 'wb') as f:
            pickle.dump(accounts, f)

unloggedIn = 0
for i in accounts:
    if not i.loggedIn: unloggedIn += 1

if unloggedIn == len(accounts): exit(1); printc('Bad Accounts', colors.RED)

choice = inputc('Want to use proxies? [Y\\N]: ', colors.YELLOW)
if choice.lower() == 'y':
    proxies = open(escape(inputc('Enter the proxies list: ', colors.BLUE)) , 'r').read().splitlines()
    for i in accounts:
        i.proxies = proxies

choice = inputc('Want to use mentions Bot? [Y\\N]: ', colors.YELLOW)
if choice.lower() == 'y':
    mention = True
    choice = inputc('Want to load the usernames here(T) or from an extend file(F) ? [T\F]: ', colors.YELLOW)
    if choice.lower() == 'f':
        targets = open(escape(inputc('Enter the path to the usernames file: ', colors.BLUE)) , 'r').read().splitlines()
        mentions_per_comment = int(inputc('how many mentions per comment?: ', colors.YELLOW))
        
        users = len(targets)
        comment_limit = mentions_per_comment
        comments_count = 0
        if users > comment_limit:
            temp = ''
            for i in range(users):
                if i != 0 and i % comment_limit == 0:
                    comments_count += 1
                    comments.append(temp)
                    temp = ''
                    if (users - (comments_count * comment_limit)) < comment_limit: break 
                temp += f'@{targets[i]} '
            left = (users - (comments_count * comment_limit))
            temp = ''
            for user in targets[-left:]:
                temp += f'@{targets[i]} '
            comments.append(temp)
            comments_count += 1

        else:

            for user in targets:
                temp += f' @{targets[i]} '
            comments.append(temp)
            comments_count += 1

    else:
        comments.append(inputc('Enter usernames, please use @ before every username:\n', colors.YELLOW))
else:
    choice = inputc('Want to load the comments here(T) or from an extend file(F) ? [T\F]: ', colors.YELLOW)
    if choice.lower() == 'f':
        comments = open(escape(inputc('Enter the path to the comments file: ', colors.BLUE)) , 'r').read().splitlines()
    else:
        comments.append(inputc('Enter text:\n', colors.YELLOW))

choice = inputc('Do want to repeat the comment (loop)? (Y/N): ', colors.YELLOW)
if choice.lower() == 'y':
    loop = True
    eloop = int(inputc('Enter the number of loops for each comment (no = 1): ', colors.YELLOW))
    wloop = int(inputc('Enter the number of loops for the whole comments (no = 1): ', colors.YELLOW))

for i in accounts:
    if i.loggedIn:

        def run(i):
            if loop:
                for lap in range(wloop):
                    for comment in comments:
                        for _lap in range(eloop):
                            if i.kickmeout: return
                            i.sendComment(target, comment)
                            time.sleep(sleep / 1000)
            else:
                for comment in comments:
                    if i.kickmeout: return
                    i.sendComment(target, comment)
                    time.sleep(sleep / 1000)
    
    run(i)
