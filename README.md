# mailservice

Mailservice is an application developed in python using Django, able to send mail to any user and has support to cc and bcc along with subject and body. It also has support to parse CSV file which is list of email addresses, to whom the mail will be sent. I've used ELK stack for the log management, which also indexes the emails stored in DB along with the web requests. There is a periodic task running every 30 minutes, which curates the emails sent in that time period and sends the CSV export to the admins.

## Project setup

### 1. Essential package setup
- Python 3.6.7
- Django 2.0.7
- elasticsearch 6.6.0
- logstash 6.6.0
- kibana 6.6.0
- crontab 2.3.6
- celery 4.2.1
- redis 3.2.0

### 2. Commands to run
#### 1. Install python
- `sudo apt update`
- `sudo apt install python3.6`

#### 2. Install Django
pip is a package management system for python.

- `sudo apt install python3-pip -y`
- `pip install Django==2.0.7`

#### 3. Install virualenv
Virtualenv is a python environment builder. It is used to create isolated python environments.

- `pip install virtualenv`

Create virtual environment for your project directory followed by commands

- `mkdir dir_name`
- `cd dir_name`
- `virtualenv -p python3 .`
- `pip freeze`

start by `source bin/activate`

ends with `deactivate`


#### 4. Start with your Django project

Run migrations
- `python manage.py migrate`

Run your application in browser run the below command in your terminal and visit [localhost:8000](http://localhost:8000)

- `python manage.py runserver`

#### 5.  Build ELK stack with your application

#### - Elasticseacrh

Elasticsearch requires Java SDK 8 to be installed

- ` add-apt-repository ppa:webupd8team/java`
- ` apt install -y oracle-java8-set-default`

Elasticsearch is used to index data from database for quick search.

- ` wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-6.6.0.deb`
- `dpkg -i elasticsearch-6.3.2.deb`
- ` pip install django-elasticsearch-dsl`

After installing open **/etc/elasticsearch/elasticsearch.yml** and edit and uncomment the line below

- ` network.host: localhost`

Now start and run the Elasticsearch service by following commands and visit [localhost:9200](http://localhost:9200)

- `systemctl enable elasticsearch.service`
- `systemctl start elasticsearch.service`

#### - Logstash
logstash is used to collect, process, and forward events and log messages

- ` wget https://artifacts.elastic.co/downloads/logstash/logstash-6.6.0.deb`
- `dpkg -i logstash-6.6.0.deb`
- `pip install python3-logstash`

After installing open **/etc/logstash/logstash.yml** and change the line below

- `http.host: "localhost"`

Start and enable Logstash service

- `systemctl enable logstash.service`
- `systemctl start logstash.service`

#### - Kibana
Kibana is used to visualize all the events, data and logs

- ` wget https://artifacts.elastic.co/downloads/kibana/kibana-6.6.0.deb`
- `dpkg -i kibana-6.6.0.deb`
- `pip install python kibana`

Next, open **/etc/kibana/kibana.yml** and update below two lines

- ` server.host: "localhost"`
-  `elasticsearch.url: "http://localhost:9200"`

Start and enable Kibana service and visit [localhost:5601](http://localhost:5601) and configure an index pattern

- `systemctl enable kibana.service`
- `systemctl start kibana.service`


After configure ELK with your project run below command for logstash and let it run continous

- `sudo /usr/share/logstash/bin/logstash -f /path/to/logstash.conf`


#### 6. Scheduling jobs with pyhton

##### Celery

Celery is a scheduler, that hits off tasks at regular periods. It has worker and beat services. Celery requires redis as a broker

- `pip install celery redis`

Run worker and beat processes
- `celery -A mailservice worker -l info -B`
- `celery -A mailservice beat -l info -B`

## Workflow of mailservice

- Main landing page of the mailservice is [localhost:8000](http://localhost:8000).
- On [compose-mail](http://localhost:8000/email), you can send email to any user with support of cc and bcc.
- The fields `email to`, `cc`, and `bcc` supports comma separated list of emails and has validation in place.
- You can see records of emails in [Email model](http://localhost:8000/admin).
- Check [log records](http://localhost:5601), to see all request logs, and emails indexed from DB. Remember, you will have to create index pattern before that.
- Run `celery -A mailservice worker -l info -B` which will send email report every 30 minutes to admins.
- If no email found in last 30 minutes then it won't send report.





