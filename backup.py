#!/usr/local/bin/python
import sys, csv

JOBS_LIST = "jobs.csv"
JENKINS_HOST = "https://jenkins-ci.org/"
EXTRA_OPTIONS = "" # use -noCertificateCheck option if needed

for values in csv.reader(open(JOBS_LIST)):
    if len(values) == 2:
        job_name = values[0].replace("#", "")
        print("java -jar jenkins-cli.jar " + EXTRA_OPTIONS + " -s " + JENKINS_HOST + " get-job " + job_name + " > data/" + job_name + ".xml")
    else:
        print("")
