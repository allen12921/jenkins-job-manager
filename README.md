# jenkins-job-manager
Create a jenkins job from template and backup existing job using Jenkins CLI

To add a job modify jobs.csv - add a new line in a format JOBS_NAME,SVN_PATH

To generate the jobs run following command which creates job's configs and prints out further instructions:
    python generate.py

To access jenkins api, you first should login:
    java -jar jenkins-cli.jar JENKINS_HOST login --username YOUR_ACCOUNT_LOGIN

To update existing job execute following command:
    java -jar jenkins-cli.jar JENKINS_HOST update-job MYJOB < MYJOB.xml

If job doesn't exist execute following command:
    java -jar jenkins-cli.jar JENKINS_HOST create-job MYJOB < MYJOB.xml

Define JENKINS_HOST in generate.py and backup.py scripts.
