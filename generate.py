#!/usr/local/bin/python
import sys, csv

JOBS_LIST = "jobs.csv"
JENKINS_HOST = "https://jenkins-ci.org/"
EXTRA_OPTIONS = "" # use -noCertificateCheck option if needed
TEMPLATE = "TemplateJob.xml"

def generate_task(values):
    job_name = values.pop(0)
    if job_name.startswith("#"):
        return
    job_path = values.pop(0)

    template = [line for line in open(TEMPLATE)]
    job_filename = "data/" + job_name + ".xml"
    output = open(job_filename, "w")
    while len(template) > 0:
        line = template.pop(0)
        line = line.replace("$JOB_NAME$", job_name).replace("$JOB_PATH$", job_path)
        for value in values:
            k,v = value.split("=")
            line = line.replace("$"+k+"$", v)
        output.write(line)
    output.close()
    print("java -jar jenkins-cli.jar " + EXTRA_OPTIONS + " -s " + JENKINS_HOST + " update-job " + job_name + " < " + job_filename)

if len(sys.argv) == 1:
    for values in csv.reader(open(JOBS_LIST)):
        if len(values) >= 2:
            generate_task(values)
        else:
            print("")
else:
    print("to generate single job: python job-generator.py JOB_NAME SVN_PATH")
    print("to generate predefined jobs: python job-generator.py")
    print("modify " + JOBS_LIST + " to change the list of jobs")
    print("modify " + TEMPLATE + " to change the job template")
