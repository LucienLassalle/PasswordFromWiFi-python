import subprocess
data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode("latin").split('\n')
profiles = [i.split(":")[1][1:-1] for i in data if ("Profil Tous les utilisateurs" in i) or ("All User Profile" in i)]
for i in profiles:
    try:
        results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('latin').split('\n')
        results = [b.split(":")[1][1:-1] for b in results if ("Contenu " in b) or ("Content " in b)]
        try:
            print ("{:<30}|  {:<}".format(i, results[0]))
        except IndexError:
            print ("{:<30}|  {:<}".format(i, ""))
    except subprocess.CalledProcessError:
        print ("{:<30}|  {:<}".format(i, "ENCODAGE NON SUPPORTÉ"))

input("Press any key to continue...")