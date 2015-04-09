import sys
import os
import time
import webbrowser
import re # regular expression
import dropbox # C:\Python34>python -m pip install dropbox
 
print ('Number of arguments:', len(sys.argv), 'arguments.')
print ('Argument List:', str(sys.argv))
 
 
# Getting started with Dropbox in Python: https://www.dropbox.com/developers/core/start/python
 
app_key = 'xmi@@@@@@@'
app_secret = 'i2cnfc@@@@@@@@'
 
flow = dropbox.client.DropboxOAuth2FlowNoRedirect(app_key, app_secret)
 
# Occhio è importante che l'access token venga conservato in modo sicuro.
token_file = "./access_token.txt" #file che contiene l'access token
if os.path.isfile(token_file):
    f2=open(token_file, 'r')
    access_token = f2.read()
    f2.close()
 
else:
    f2=open(token_file, 'w+')
    # Have the user sign in and authorize this token
    authorize_url = flow.start()
    print('1. Go to: ' + authorize_url)
    webbrowser.open(authorize_url) # apriamo nel browser automaticamente l'URL.
    print('2. Click "Allow" (you might have to log in first)')
    print('3. Copy the authorization code.')
    code = input("Enter the authorization code here: ").strip()
 
    # This will fail if the user enters an invalid authorization code
    access_token, user_id = flow.finish(code)
 
    f2.write(access_token) # scriviamo l'access token nel file
    f2.close()
 
client = dropbox.client.DropboxClient(access_token)
print('linked account: ', client.account_info())
 
 
def ripulisci(stringa):
 
    stringa = stringa.strip()
    stringa = stringa.lower()
    words_to_filter = ["dvdrip", "bdrip", "satrip", "hdrip", "divx", "xvid", "bluray", "ld", "ac3", "mp4", "x264", "mkv", "1080p", "480p"]
 
    for x in words_to_filter:
        stringa = stringa.replace(x, "").strip()
        stringa = re.sub(r'\s+', ' ', stringa) # rimuoviamo spazi bianchi all'interno della stringa
 
    return stringa
 
if len(sys.argv) > 1:
    titolo = ""
    sys.argv.pop(0) # rimuoviamo nome script py
    for x in sys.argv:
        if x != "##":
            titolo = titolo + x + " "
        else:
            break
 
    titolo = ripulisci(titolo)
 
    print(titolo)
 
    # salviamo il titolo in append al file su dropbox...
 
    try:
        # file gia' presente, aggiorniamo:
        f, metadata = client.get_file_and_metadata('/downloaded_files.txt')
        out = open('./downloaded_files.txt', 'wb') # scarichiamo file aggiornato
        out.write(f.read())
        out.close()
        f2 = open('./downloaded_files.txt', 'a+')
        print(titolo, file=f2) # aggiungiamo nuovo titolo
        f2.close()
        f2 = open('./downloaded_files.txt', 'rb')
        response = client.put_file('/downloaded_files.txt', f2, overwrite=True) # upload file aggiornato
        print('Uploaded: ', response)
        f2.close()
        f.close()
        while True:
            try:
                os.remove('./downloaded_files.txt') # rimuoviamo file locale
                break
            except:
                print(sys.exc_info()[0])
                time.sleep(3) # se non ci riusciamo potrebbe essere ancora in upload, aspettiamo.
 
    except dropbox.rest.ErrorResponse:
        # file non trovato lo creiamo.
        f = open('downloaded_files.txt', 'a+')
        print(titolo, file=f)
        f.close()
        f = open('downloaded_files.txt', 'rb')
        response = client.put_file('/downloaded_files.txt', f)
        print('Uploaded: ', response)
        f2.close()
        f.close()
        while True:
            try:
                os.remove('./downloaded_files.txt') # rimuoviamo file locale
                break
            except:
                print(sys.exc_info()[0])
                time.sleep(3) # se non ci riusciamo potrebbe essere ancora in upload, aspettiamo.
 
else:
    print("No parameters...")
