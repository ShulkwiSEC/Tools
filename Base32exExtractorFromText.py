import re

def extract_base32(filename):
  """
  This function attempts to extract Base32 encoded data from a file.

  Args:
      filename: The path to the file containing potentially encoded data.

  Returns:
      A list of strings containing the extracted Base32 data (may include false positives).
  """
  base32_pattern = r"[A-Z2-7=_]+"  # Regex pattern for Base32 characters
  extracted_data = []

  try:
    with open(filename, 'r') as file:
      for line in file:
        matches = re.findall(base32_pattern, line)
        extracted_data.extend(matches)
  except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")
    return []

  return extracted_data

if __name__ == "__main__":
  # Get filename from user input
  filename = input("Enter the file name: ")
  
  # Extract and print Base32 data
  extracted_data = extract_base32(filename)
  if extracted_data:
    print("Extracted Base32 data:")
    for item in extracted_data:
      print(item)
  else:
    print("No Base32 data found in the file.")

