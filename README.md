# jenkins-job-manager
Create a jenkins job from template and backup existing job using [Jenkins CLI](https://icejenkins.cern.ch/cli/)

## How to create a job
1. Add your project to the jobs.csv file (format - job_name,path_in_svn)
2. Define JENKINS_HOST in generate.py scripts.
3. Run generate.py script to generate a jenkins job's xml file (name : job_name.xml)  
```
    python generate.py
```
4. Login to Jenkins CLI
```
    java -jar jenkins-cli.jar -s JENKINS_HOST login --username YOUR_ACCOUNT_LOGIN
```
5. Copy/paste the output of generate.py script to the console to manage the corresponding job.   
By default script prints _create-job_ instruction, replace it with _update-job_ to overwrite existing job.
```
    java -jar jenkins-cli.jar -s JENKINS_HOST create-job MYJOB < MYJOB.xml
    java -jar jenkins-cli.jar -s JENKINS_HOST update-job MYJOB < MYJOB.xml
```

## How to backup a job
1. Add your project to the jobs.csv file (format - job_name,path_in_svn)
2. Define JENKINS_HOST in backup.py scripts.
3. Run backup.py script to get the instructions
```
    python backup.py
```
4. Copy/paste the output of backup.py script to the console to manage the corresponding job.   
```
java -jar jenkins-cli.jar -s JENKINS_HOST get-job MYJOB > data/MYJOB.xml

```

## Known issues
1. Option -noCertificateCheck can be useful to avoid issues with specific certificates.
2. Please ignore following warning, it seems not affecting the process:  
> Skipping HTTPS certificate checks altogether. Note that this is not secure at all.
> [WARN] Failed to authenticate with your SSH keys. Proceeding as anonymous

