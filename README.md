# World of Lifting

### The goal of this website
The idea behind this website is to compile as much data as possible regarding all areas of fitness in order to provide people with a way to quantify how they stack up against their competition.
To begin this will only include powerlifting (i.e. squat, bench, deadlift) but I hope to expand it to other areas such as odd lifts (i.e zercher lifts, strongman, etc) and cardiovascular exercise (primarily running).
  
### Development timeline
  
#### Completed Items
1. Spin up site with OpenPowerlifting data and basic analysis based on user input
2. Make powerlifting graphs/data interactive
3. Dockerize application for future cloud hosting
  
#### Future Items
3. Create web scraper to pull running data and have basic anaylsis available
4. Build user facing page with interactive running data
5. Enhance site to include odd lifts
6. Deploy app to the cloud for public accessibility (Azure?)
  
### Running the website locally (Docker)
sudo docker-compose up -d --build  
  
<--Check logs-->
sudo docker ps
  
<--Kill container-->
sudo docker stop [container]
  
### Running the website locally (Separate)
Important commands for each component  
  
Flask App:  
source env/bin/activate  
flask --app 'app:create_app("dev")' run  
  
Vue App:  
npm install  
npm run serve  
  
Postgres DB:  
sudo -i -u lifting  
psql  
<--Start DB Service-->  
sudo systemctl start postgresql.service  
<--DB Creation-->  
psql -U [username] -d [database] -a -f [db creation sql script]  