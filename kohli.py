import os
import time
import subprocess
import argparse


def main():
    parser = argparse.ArgumentParser(description="Additional recon after subdomain enumeration")
    parser.add_argument("-c", type=str, help="Company name")
    parser.add_argument("-u", type=str, help="Single url to gather further info")
    parser.add_argument("-f", type=str, help="File containing a list of domains to gather information")
    args = parser.parse_args()
    file_name = f"/Users/karthikeyan/recon/{args.c}/{args.f}"
    folder_path = f"/Users/karthikeyan/recon/{args.c}" 
    if args.f:
        run_recon(args.c, args.f, args)
    else:
       run_recon(args.c, args.u, args)


def run_recon(company, domain, args):
    j = 5

    folder_path = f"/Users/karthikeyan/recon/{company}" 
 

    
    print("Directory bruteforcing starts..")
    dir_bruteforcing(args)
    print("Directory bruteforcing ends successfully")

    print(f"Recon completed!! - check recon data here:{folder_path}")

def param_spider(args):
    j=5
    folder_path = f"/Users/karthikeyan/recon/{args.c}" 
    path = f"{folder_path}/subdomains.txt"
    with open(path, "r") as file:
         domains = file.read().splitlines()
    for domain in domains:
        param_cmd = f"python3 /Users/karthikeyan/tools/pentesting/ParamSpider/paramspider.py -d {domain} -o {folder_path}/paramspider.txt "
        try:
            subprocess.run(param_cmd, shell=True, check=True)
            for i in range(j):
                print(".")
                time.sleep(0.5)
        except subprocess.CalledProcessError as e:
            print(".")
            print(".")
            print(".")
            print(f"ParamSpider failed with error: {e}")

def pattern_match(args):
    j=5
    folder_path = f"/Users/karthikeyan/recon/{args.c}" 
    path = f"/Users/karthikeyan/tools/patterns.txt"
    patt = f"{folder_path}/patterns"
    os.mkdir(patt)
    with open(path, "r") as file:
         domains = file.read().splitlines()
    for domain in domains:
        pattern_cmd = f"cat {folder_path}/paramspider.txt | gf {domain} > {patt}/{domain}.txt"
        print(pattern_cmd)
        try:
            subprocess.run(pattern_cmd, shell=True, check=True)
            for i in range(j):
                print(".")
                time.sleep(0.5)
        except subprocess.CalledProcessError as e:
            print(".")
            print(".")
            print(".")
            print(f"ParamSpider failed with error: {e}")

def dir_bruteforcing(args):
    j = 5
    folder_path = f"/Users/karthikeyan/recon/{args.c}" 
    path = f"{folder_path}/live.txt"
    dir_path = f"{folder_path}/directory"
    
    # Create the directory if it doesn't exist
    os.makedirs(dir_path, exist_ok=True)
    
    with open(path, "r") as file:
        domains = file.read().splitlines()
        line_count = sum(1 for _ in file)

    for k, domain in enumerate(domains, start=1):
        dir_cmd = f"python3 /Users/karthikeyan/tools/pentesting/dirsearch/dirsearch.py -u {domain} -e php,asp,aspx,net,js,cs,php2,php3,php4,php5,php6,php7,jsp,java,python,yaml,yml,config,conf,htaccess,htpasswd,shtml -o {dir_path}/{k}.txt"
        try:
            subprocess.run(dir_cmd, shell=True, check=True)
            for i in range(j):
                print(".")
                time.sleep(0.5)
        except subprocess.CalledProcessError as e:
            print(".")
            print(".")
            print(".")
            print(f"Dirsearch failed with error: {e}")

if __name__ == "__main__":
    print(" .-----------------------------.            ")
    print(" |  Recon hunter               |            ")
    print(" |  Author : @cyber_karthi     |            ")
    print(" |           Hacker            |            ")
    print(" '-----------------------------'            ")
    print("                 ^      (\_/)    ")
    print("                 '----- (o.o)    ")
    print("                        (> <)    ")
    print("   ")
    main()
