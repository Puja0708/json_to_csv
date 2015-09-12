from crontab import CronTab
#init cron
cron   = CronTab()

#add new cron job
job  = cron.new(command='python /home/puja/Documents/sportskeeda-assignment/storeCSV.py')

#job settings
job.minute.every(5)