import subprocess
import multiprocessing

# Define the names of the files you want to run
file1 = "udpserver.py"
file2 = "player_entry_screen.py"

# Define functions to run the files
def run_script1():
    try:
        subprocess.run(["python3", file1], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running {file1}: {e}")

def run_script2():
    try:
        subprocess.run(["python3", file2], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running {file2}: {e}")

# Create two processes to run the scripts concurrently
if __name__ == "__main__":
    process1 = multiprocessing.Process(target=run_script1)
    process2 = multiprocessing.Process(target=run_script2)

    # Start both processes
    process1.start()
    process2.start()

    # Wait for both processes to finish
    process1.join()
    process2.join()



