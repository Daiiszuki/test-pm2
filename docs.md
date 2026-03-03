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
*    *    *    *    *    *
  ┬    ┬    ┬    ┬    ┬    ┬
  │    │    │    │    │    └─ day of week (0 - 7) (0 or 7 is Sun)
  │    │    │    │    └────── month (1 - 12)
  │    │    │    └─────────── day of month (1 - 31)
  │    │    └──────────────── hour (0 - 23)
  │    └───────────────────── minute (0 - 59)
  └────────────────────────── second (0 - 59, optional)

  Common examples:
*/15 * * * * : Every 15 minutes.
0 * * * * : Every hour (at the top of the hour).
30 2 * * * : Every day at 2:30 AM.
0 0 * * 1 : Every Monday at midnight.
0 22 * * 1-5 : 10:00 PM every weekday (Mon-Fri).


