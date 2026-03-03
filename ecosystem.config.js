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
