import subprocess
import os

current_os = os.name


def ping_website(site_list, sistema, count):
    for i in site_list:
        result = subprocess.run(['ping', sistema, count, i], stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                encoding="CP866")

        if result.returncode == 0:
            print(result.stdout)
            print("----------------")
        else:
            print(result.stderr)


sites = ["www.google.com.ua", "duckduckgo.com"]

if current_os == "nt":

    ping_website(sites, "-n", "3")

elif current_os == "posix":

    ping_website(sites, "-c", "3")
