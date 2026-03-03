## INSTALLATION
npm install pm2@latest -g

## CONFIGURATION
- Python script
- ecosystem.config.js

module.exports = {
  apps: [{
    name: "etl-test-job",
    script: "test-pmt.py",
    interpreter: "python3", // Use "python" or path to your venv bin
    cron_restart: "*/2 * * * *", // Runs every 2 minutes
    autorestart: false,
    watch: false,
    log_date_format: "YYYY-MM-DD HH:mm:ss",
    error_file: "logs/etl-error.log",
    out_file: "logs/etl-out.log",
  }]
}

## Start an app

$ pm2 start ecosystem.config.js ()
$ pm2 start python-app.py --watch

## Management

$ pm2 restart app_name
$ pm2 reload app_name
$ pm2 stop app_name
$ pm2 delete app_name

## List managed applications

$ pm2 [list|ls|status]


## Display logs

To display logs in realtime:

$ pm2 logs
To dig in older logs:

$ pm2 logs --lines 200


## Terminal Based Dashboard
Here is a realtime dashboard that fits directly into your terminal:

$ pm2 monit


## pm2.io: Monitoring & Diagnostic Web Interface
Web based dashboard, cross servers with diagnostic system:

$ pm2 plus

## Chron
┌─────────── minute (0 - 59)
 │ ┌───────── hour (0 - 23)
 │ │ ┌─────── day of month (1 - 31)
 │ │ │ ┌───── month (1 - 12)
 │ │ │ │ ┌─── day of week (0 - 6) (0 is Sunday)
 │ │ │ │ │
 * * * * *

  Common examples:

Goal	Cron Syntax
Every Minute	* * * * *
Every 30 Mins	*/30 * * * *
Every Hour	0 * * * *
Every Morning (6 AM)	0 6 * * *
Every Sunday Midnight	0 0 * * 0
Every 1st of the Month	0 0 1 * *


* (Any/Every): "Every minute," "Every day," etc.
, (And): To list specific times. 1,15,30 means at the 1st, 15th, and 30th minute.
- (Range): 1-5 in the Day of Week slot means Monday through Friday.
/ (Interval): */15 in the Minute slot means "every 15 minutes."


