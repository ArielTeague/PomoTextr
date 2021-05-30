import argparse
import pomoCycle

#
# For super base: replace number and body with desired number and body
# Next goals: run from CLI, taking in number and message from there are
# After that, Pomo logic for single loop. Pause? Research Methods
# Add method for deciding loops
# Add method to cancel
# Set up multiple timer methods and allow person to choose
# Set up web access version to allow person to trigger/cancel from website?
# --
# Create parser and add argument(s)
parser = argparse.ArgumentParser(description='Setup A Round of Pomodoro Texted To Your Phone')
parser.add_argument('Phone',
                    metavar='phone',
                    type=str,
                    help=' Ten Digit Phone number without formatting.')
# Execute parse_args and assign to object
args = parser.parse_args()

# Pull Phone Number And Format (Only US for first run)
phoneNumberInput = args.Phone
# Add check to confirm correct formatting
formattedPhoneNumber = '+1{0}'.format(phoneNumberInput)

# Send to the pomodoro manager
pomoCycle.startSingleClassicCycle(formattedPhoneNumber)

# send_sms.send_message(formattedPhoneNumber, '***body***')
