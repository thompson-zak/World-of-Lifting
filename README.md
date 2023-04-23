# World of Lifting

### The goal of this website
The idea behind this website is to compile as much data as possible regarding all areas of fitness in order to provide people with a way to quantify how they stack up against their competition.
To begin this will only include powerlifting (i.e. squat, bench, deadlift) but I hope to expand it to other areas such as odd lifts (i.e zercher lifts, strongman, etc) and cardiovascular exercise (primarily running).

### Development timeline
1. Spin up site with OpenPowerlifting data and basic statistical analysis based on user input
2. Enhance statistical analysis and make graphs/data interactive
3. Expose APIs to allow for users to query data to see how performance is based on certain criteria
4. Enhance site to include running data
5. Enhance site to include odd lifts (exact lifts TBD)

### Running the website locally (Docker)
sudo docker-compose up -d --build  

### Running the website locally (Separate)
Important commands for each component  
  
Flask App:  
source env/bin/activate  
python app.py  
  
Vue App:  
npm run serve  
  
Postgres DB:  
sudo -i -u lifting  
psql  
<--Start DB Service-->  
sudo systemctl start postgresql.service  
<--DB Creation-->  
psql -U [username] -d [database] -a -f [db creation sql script]  