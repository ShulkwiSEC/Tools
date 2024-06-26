import subprocess
import time

def run_dynamicy(guess):
  """Runs Dynamicy.exe with the given guess, parses the response, and excludes initial prompts."""
  try:
    # Replace with the actual paths
    process = subprocess.Popen(["/etc/alternatives/wine", "/home/m4x/Downloads/flagyard/Yet/Dynamicy.exe"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    process.stdin.write(str(guess).encode())
    process.stdin.flush()
    time.sleep(0.1)  # Add a brief delay for potential communication issues

    # Capture output and split into lines
    output_lines = process.communicate()[0].decode("utf-8").splitlines()

    # Extract the last line as the response (assuming dynamic feedback)
    last_line = output_lines[-1].strip()
    return last_line
  except Exception as e:
    print(f"Error running Dynamicy.exe: {e}")
    return None

def brute_force_4_digit():
  for guess in range(1000, 10000):
    response = run_dynamicy(guess)
    if response != "Try Harder ...":
      print(f"Found a response! Guess: {guess}, Response: {response}")
      return

brute_force_4_digit()
