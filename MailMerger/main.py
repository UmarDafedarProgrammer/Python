#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
INVITEES = "Input/Names/invited_names.txt"
EMAIL_FORMAT = "Input/Letters/starting_letter.txt"
OUTPUT_FOLDER = "Output/ReadyToSend"
PLACEHOLDER = "[name]"


##### Read the list of invitees
def read_invitees():
  with open(INVITEES, mode="r") as invitees:
    invitees_list = invitees.readlines()
    return invitees_list


##### Read the content of the letter
def email_content():
  print("*********Email Content!")
  with open(EMAIL_FORMAT) as letter:
    content = letter.read()
    return content


##### Generate mailers
def generate_mails():
  list = read_invitees()
  content = email_content()
  for invitee in list:
    file = open(f"{OUTPUT_FOLDER}/InvitationLetter_{invitee}.txt", mode="w")
    stripped_name = invitee.strip()
    new_content = content.replace(PLACEHOLDER, stripped_name)
    file.write(new_content)
    file.close()


generate_mails()
