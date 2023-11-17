import subprocess
import multiprocessing

# Define the names of the files you want to run

file1 = "udpserver.py"
file2 = "player_entry_screen.py"
file3 = "Splash.py"

# Define functions to run the files

def run_scriptSplash():
    try:
        subprocess.run(["python3", file3], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running {file3}: {e}")

def run_script2():
    try:
        subprocess.run(["python3", file2], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running {file2}: {e}")

def run_script1():
    try:
        subprocess.run(["python3", file1], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running {file1}: {e}")

# Create two processes to run the scripts concurrently
if __name__ == "__main__":
    processSplash = multiprocessing.Process(target=run_scriptSplash)
    process1 = multiprocessing.Process(target=run_script1)
    process2 = multiprocessing.Process(target=run_script2)
    

    # Start both processes
    processSplash.start()
    process2.start()
    process1.start()
    
    

    # Wait for both processes to finish
    processSplash.join()
    process2.join()
    process1.join()
   
    



