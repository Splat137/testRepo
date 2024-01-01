import os
import json
import requests
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--resultlog', dest='logPath', default=None)
args = parser.parse_args()
logPath = args.logPath

if logPath:
    if os.path.exists(logPath):
        with open(logPath, 'r') as logFile:
            logContent = logFile.read()
            
        webhookUrl = os.getenv('WEBHOOK_URL')
        if webhookUrl:
            testResults = json.dumps({'results' : logContent})
            requests.post(webhookUrl, json=testResults)
        else:
            print("WEBHOOK_URL environment variable not set.")
    else:
        print(f"Log file not found at: {log_path}")
else:
    print("--resultlog option not specified.")
