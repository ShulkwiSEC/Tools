import unicodedata
import platform

def char_to_ref(char):
  """
  Converts a character to its decimal character reference.

  Args:
      char: A single Unicode character.

  Returns:
      The decimal character reference (NCR) for the character.
  """
  codepoint = ord(char)
  if unicodedata.category(char) == "Cs":
    # Control characters don't have NCRs
    return None
  return f"&#{codepoint};"

def main():
  """
  Reads input from the user and converts it to character references for different browsers.
  """
  user_input = input("Enter your text: ")
  converted_text_firefox = "".join(char_to_ref(char) or char for char in user_input)
  converted_text_chrome = converted_text_firefox.replace("&", "&amp;")

  # Adapt Safari conversion based on Safari's specific entity handling (might require further research)
  converted_text_safari = converted_text_firefox.replace("<", "&lt;")
  space = " "
  print(f"Converted text (Firefox): {converted_text_firefox}")
  print(space)
  print(f"Converted text (Chrome): {converted_text_chrome}")
  print(space)
  print(f"Converted text (Safari): {converted_text_safari}")
  print(space)
  print(f"Your Input: {user_input}")

if __name__ == "__main__":
  main()
