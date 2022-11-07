#! user/bin/python3
import sys, signal
from git import Repo
import re 
import time

repo_dir = './skale-manager'
key_words = ['credentials','password','key'] 

def control_c(signal, frame):
    print('\n [!] Se termina la ejecución del programa [!] \n')
    sys.exit()
signal.signal(signal.SIGINT, control_c)

def extract(repo_dir):
    repo = Repo(repo_dir)
    commits = list(repo.iter_commits('develop'))
    return commits

def transform(commits):
    leaks = []
    for commit in commits:
        for word in key_words:
            if re.search(word, commit.message, re.IGNORECASE):
                leaks.append(commit)
    return leaks

def load(leaks): 
    for leak in leaks:
        print(f'Commit: {leak.hexsha} -> {leak.message}')

if __name__ == '__main__':
    commits = extract(repo_dir)
    leaks = transform(commits)
    load(leaks)
    
                
                

    
