import subprocess
import os
import sys
import time


def sublist3r(domain):
# install from github   
    command1 = f"python3 ./Sublist3r/sublist3r.py -d {domain} -p 80,443,404 -t 50 -o ./result/{domain}/sublist3r.txt "  # | tee -a ./result/{domain}subfinder.txt
    p1=subprocess.run(command1, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, universal_newlines=True)
    if p1.returncode == 0:
        print('sublist3r Command : Success')
    else:
        print('sublist3r Command : Error')
    
    # output, error=p1.communicate()
    # print('output:{0}',format(output))
    # print('error:{0}',format(error))
    # if p1.communicate == 0:
   

def subfinder(domain):
# subfinder install with apt install subfinder
    command2 = f"subfinder -d {domain} -v -rL ./resolvers.txt -o ./result/{domain}/subfinder.txt" #  -v | tee -a ./result/subfinder.txt  -rL ./resolver.txt
    p2=subprocess.run(command2, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, universal_newlines=True ) 
    if p2.returncode == 0:
        print('subfinder Command : Success')
    else:
        print('subfinder Command : Error')

    # testing_command =subprocess.run(f"subfinder --version", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    # if testing_command.returncode != 0:
    #     os.system("apt install subfinder")

def amass(domain):
# amass install with github 
    command3 = f"amass enum -passive -d {domain} -rf ./resolvers.txt -o ./result/{domain}/amass.txt"
    p3=subprocess.run(command3, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, universal_newlines=True ) 
    if p3.returncode == 0:
        print('amass Command : Success')
    else:
        print('amass Command : Error')

def sorting_domains(domain):
    # command4=f"sort -u ./result/{domain}/subfinder.txt ./result/{domain}/sublist3r.txt | tee ./result/{domain}/sorted_subdomains.txt"
    command4=f"sort ./result/{domain}/sublist3r.txt ./result/{domain}/subfinder.txt | uniq >./result/{domain}/sorted_subdomains.txt"
    p4=subprocess.run(command4, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, universal_newlines=True ) 
    if p4.returncode == 0:
        print('sorting_domains Command : Success')
    else:
        print('sorting_domains Command : Error')

def httpx_live(domain):
# httpx install with github 
    command5=f"httpx -l ./result/{domain}/sorted_subdomains.txt -mc 200,301,302 | tee ./result/{domain}/httpx_live.txt"  # -sc
    p5=subprocess.run(command5, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, universal_newlines=True)
    if p5.returncode == 0:
        print('httpx_live Command : Success')
    else:
        print('httpx_live Command : Error')

def httpx_dead(domain):
# httpx install with github 
    command5=f"httpx -l ./result/{domain}/sorted_subdomains.txt -fc 404,403,401 | tee ./result/{domain}/httpx_dead.txt"  # -sc
    p5=subprocess.run(command5, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, universal_newlines=True)
    if p5.returncode == 0:
        print('httpx_dead Command : Success')
    else:
        print('httpx_dead Command : Error')

def paramspider(domain):
    command6=f"python3 ./ParamSpider/paramspider.py -d {domain} --level high -o ./result/{domain}/paramspider.txt"
    p6=subprocess.run(command6, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, universal_newlines=True)
    if p6.returncode == 0:
        print('paramspider Command : Success')
    else:
        print('paramspider Command : Error')

def nuclei(domain):
    command7=f"nuclei -l ./result/{domain}/sorted_subdomains.txt -s low,medium,high,critical -c 100 -o ./result/{domain}/nuclei.txt " #  | tee ./result/{domain}/nuclei.txt 
    p7=subprocess.run(command7, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, universal_newlines=True)
    if p7.returncode == 0:
        print('nuclei Command : Success')
    else:
        print('nuclei Command : Error')

def waybackurls(domain):
    command8=f"cat ./result/{domain}/sorted_subdomains.txt | waybackurls > ./result/{domain}/waybackurls.txt"
    p8=subprocess.run(command8, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, universal_newlines=True)
    if p8.returncode == 0:
        print('waybackurls Command : Success')
    else:
        print('waybackurls Command : Error')

def dirsearch(domain):
    k=input("Do you want to Bruteforce Subdomain? (y/n)")
    if(k=='y' or k=='Y'):
        command9=f"python3 ./dirsearch/dirsearch.py -l ./result/{domain}/sorted_subdomains.txt -w password.txt -r -t 50 -o ./result/{domain}/dirsearch.txt"  #-o ./result/{domain}/dirsearch.txt   | tee ./result/{domain}/dirsearch.txt
        p9=subprocess.run(command9, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, universal_newlines=True)
        if p9.returncode == 0:
            print('dirsearch Command : Success')
        else:
            print('dirsearch Command : Error')    







def banner():
    # Rainbow color codes
    rainbow_colors = [
       "\033[31m",  # Red
        "\033[33m",  # Yellow
        "\033[32m",  # Green
        "\033[36m",  # Cyan
        "\033[34m",  # Blue
        "\033[35m",  # Purple
    ]

    text = '''
     ▄▄▄       █    ██ ▄▄▄█████▓ ▒█████   ███▄    █  ▒█████   ███▄ ▄███▓ ▒█████   █    ██   ██████ 
    ▒████▄     ██  ▓██▒▓  ██▒ ▓▒▒██▒  ██▒ ██ ▀█   █ ▒██▒  ██▒▓██▒▀█▀ ██▒▒██▒  ██▒ ██  ▓██▒▒██    ▒ 
    ▒██  ▀█▄  ▓██  ▒██░▒ ▓██░ ▒░▒██░  ██▒▓██  ▀█ ██▒▒██░  ██▒▓██    ▓██░▒██░  ██▒▓██  ▒██░░ ▓██▄   
    ░██▄▄▄▄██ ▓▓█  ░██░░ ▓██▓ ░ ▒██   ██░▓██▒  ▐▌██▒▒██   ██░▒██    ▒██ ▒██   ██░▓▓█  ░██░  ▒   ██▒
     ▓█   ▓██▒▒▒█████▓   ▒██▒ ░ ░ ████▓▒░▒██░   ▓██░░ ████▓▒░▒██▒   ░██▒░ ████▓▒░▒▒█████▓ ▒██████▒▒
     ▒▒   ▓▒█░░▒▓▒ ▒ ▒   ▒ ░░   ░ ▒░▒░▒░ ░ ▒░   ▒ ▒ ░ ▒░▒░▒░ ░ ▒░   ░  ░░ ▒░▒░▒░ ░▒▓▒ ▒ ▒ ▒ ▒▓▒ ▒ ░
      ▒   ▒▒ ░░░▒░ ░ ░     ░      ░ ▒ ▒░ ░ ░░   ░ ▒░  ░ ▒ ▒░ ░  ░      ░  ░ ▒ ▒░ ░░▒░ ░ ░ ░ ░▒  ░ ░
      ░   ▒    ░░░ ░ ░   ░      ░ ░ ░ ▒     ░   ░ ░ ░ ░ ░ ▒  ░      ░   ░ ░ ░ ▒   ░░░ ░ ░ ░  ░  ░  
          ░  ░   ░                  ░ ░           ░     ░ ░         ░       ░ ░     ░           ░  
    '''

    # Split the text into lines and print with rainbow colors
    lines = text.split('\n')

    for i, line in enumerate(lines):
        if i < len(rainbow_colors):
            sys.stdout.write(rainbow_colors[i])
        else:
            # Cycle through rainbow_colors if text has more lines than colors
            sys.stdout.write(rainbow_colors[i % len(rainbow_colors)])
        sys.stdout.write(line + '\n')
        sys.stdout.write('\033[0m')  # Reset color
        time.sleep(0.2)  # Pause to control the speed of printing

    sys.stdout.write('\033[0m')  # Reset color at the end
    print('''\t\t\t\t\t\t\t\t\t\u001b[32m - coded by Koulick\u001b[0m''')
    print('''      
                                          httpx(error)
                                               ^
                      --> sublist3r }-\        |            /--> nuclei
    result/{domain} --> subfinder   }-> sorted_subdomain --/-> paramspider
                      --> amass     }-/        |     \    /--> waybackurls
                                               v      \\
                                          httpx(live)  \--y/n-> directory_bruteforce
      
        ''')


banner()
domain=input("Enter domain:- ")
os.mkdir(f"./result/{domain}")
sublist3r(domain)
subfinder(domain)
amass(domain)
sorting_domains(domain)
httpx_live(domain)
httpx_dead(domain)
paramspider(domain)
nuclei(domain)
waybackurls(domain)
dirsearch(domain)

#i have to learn all error code from book
