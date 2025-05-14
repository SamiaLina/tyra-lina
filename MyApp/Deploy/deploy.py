import subprocess
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def deploy_application():
   try:
       logging.info("Starting deployment process...")

       # Pull from Git
       result = subprocess.run(['git', 'pull'], capture_output=True, text=True)
       if result.returncode != 0:
           logging.error(f"Git pull failed: {result.stderr}")
           return

       # Run Docker Compose
       result = subprocess.run(['docker-compose', 'up', '-d'], capture_output=True, text=True)
       if result.returncode != 0:
           logging.error(f"Docker deployment failed: {result.stderr}")
           return

       logging.info("Deployment completed successfully.")
   except Exception as e:
       logging.error(f"Error: {e}")

if __name__ == "__main__":
   deploy_application()
