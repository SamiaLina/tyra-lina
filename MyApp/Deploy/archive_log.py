import os
import time
import tarfile

# Use Windows-compatible paths
log_dir = os.path.join(os.path.expanduser("~"), "Documents", "Code", "Python", "Deploy", "logs")
backup_dir = os.path.join(os.path.expanduser("~"), "Documents", "Code", "Python", "Deploy", "logs_backup")

def archive_logs():
    # Create backup directory if it doesn't exist
    os.makedirs(backup_dir, exist_ok=True)
    
    # Generate archive name with timestamp
    current_time = time.strftime('%Y%m%d-%H%M%S')
    archive_name = f'logs_backup_{current_time}.tar.gz'
    archive_path = os.path.join(backup_dir, archive_name)
    
    # Create tar.gz archive
    with tarfile.open(archive_path, "w:gz") as tar:
        # Change to log_dir to avoid including full path in archive
        os.chdir(log_dir)
        for log_file in os.listdir(log_dir):
            if log_file.endswith(".log"):  # Archive only .log files (adjust as needed)
                tar.add(log_file)

if __name__ == "__main__":
    # Ensure log_dir exists
    os.makedirs(log_dir, exist_ok=True)
    archive_logs()