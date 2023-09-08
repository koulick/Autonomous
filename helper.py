import subprocess
import os



BLUE, RED, WHITE, YELLOW, MAGENTA, GREEN, END = '\33[94m', '\033[91m', '\33[97m', '\33[93m', '\033[1;35m', '\033[1;32m', '\033[0m'

def install_golang():
    result = subprocess.run("go version", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
    if result.returncode != 0:
        # printWarning(f"golang is not installed. {GREEN}Installing...{WHITE}")
        # Installing package
        os.system("sudo apt install -y golang")

        # Then adding the following to your .bashrc
        os.system("export GOROOT=/usr/lib/go")
        os.system("export GOPATH=$HOME/go")
        os.system("export PATH=$GOPATH/bin:$GOROOT/bin:$PATH")
        
        # Reloading your .bashrc              
        os.system("source .bashrc")

def sublist3r():
    result = subprocess.run("python3 sublist3r.py", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
    if result.returncode != 0:
        os.system("cd ./Sublist3r;sudo chmod 777 *;pip install -r requirements.txt")  #  pip freeze > requirements.txt

def subfinder():
    result = subprocess.run("subfinder -h", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
    if result.returncode != 0:
        os.system("sudo apt install subfinder")

def amass():
    result = subprocess.run("amass -h", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
    if result.returncode != 0:
        os.system("git clone https://github.com/owasp-amass/amass.git;cd ./amass/cmd/amass; go build;sudo mv amass /usr/local/bin")

def install_httpx():
    result = subprocess.run("httpx -version", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
    if result.returncode != 0:
        # printWarning(f"httpx is not installed. {GREEN}Installing...{WHITE}")
        os.system("git clone https://github.com/projectdiscovery/httpx.git; cd httpx/cmd/httpx; go build;sudo  mv httpx /usr/local/bin/")

def pramspider():
    result = subprocess.run("python3 paramspider.py -h", shell= True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
    if result.returncode !=0:
        os.system("cd ./ParamSpider;sudo chmod 777 *;pip install -r requirements.txt") # pip freeze > requirements.txt

def waybackurls():
    result = subprocess.run("waybackurls -h", shell= True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
    if result.returncode !=0:
        os.system("git clone https://github.com/tomnomnom/waybackurls.git ;cd waybackurls; go build;sudo mv waybackurls /usr/local/bin")

def nuclei():
    result = subprocess.run("nuclei -h", shell= True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
    if result.returncode !=0:
        os.system("sudo apt install nuclei")

def dirsearch():
    result = subprocess.run("dirsearch -h", shell= True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
    if result.returncode !=0:
        os.system("git clone https://github.com/maurosoria/dirsearch.git", shell= True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
        print(result.returncode)


# # subprocess.run("sudo su", shell= True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
install_golang()
sublist3r()
subfinder()
amass()
install_httpx()
pramspider()
waybackurls()
nuclei()
dirsearch()
