module.exports = {
  apps: [{
    name: "sequental-etl-pipeline",
    script: "run_pipeline.py",
    interpreter: "python", // or path to your venv: "./venv/bin/python"
    
    // THE SCHEDULE
    cron_restart: "01 21 * * *", // Run every day at 2:00 AM
    
    // IMPORTANT SETTINGS FOR ETL
    autorestart: false, // Don't loop; wait for the next cron
    watch: false,
    
    // LOGGING
    out_file: "./logs/pipeline_out.log",
    error_file: "./logs/pipeline_err.log",
    merge_logs: true,
    log_date_format: "YYYY-MM-DD HH:mm:ss"
  }]
}