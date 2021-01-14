from dotenv import load_dotenv
import datetime
import json
import logging
import os


load_dotenv()

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

logger = logging.getLogger(__name__)


TOKEN = os.environ.get("TELEGRAM_TOKEN")

def main():
  # Create Updater object and attach dispatcher to it
  updater = Updater(token=TOKEN)
  j = updater.job_queue
  dispatcher = updater.dispatcher
  # Add command handler to dispatcher

  # Start
  start_handler = CommandHandler('start', start)
  dispatcher.add_handler(start_handler)

  # List
  list_handler = CommandHandler('list', list_reminds, pass_args=True)
  dispatcher.add_handler(list_handler)

  # Jobs
  j.run_repeating(remind, interval=60,  first=0)
  j.run_repeating(remind_1, interval=60,  first=0)
  j.run_repeating(remind_2, interval=60,  first=0)
  j.run_repeating(check_expired, interval=60,  first=0)
  

  # Feedback
  feedback_remind_handler = CommandHandler('feedback', feedback, pass_args=True)
  dispatcher.add_handler(feedback_remind_handler)
  
  # Help
  help_remind_handler = CommandHandler('help', help_remind)
  dispatcher.add_handler(help_remind_handler)
  
  # About
  about_remind_handler = CommandHandler('about', about)
  dispatcher.add_handler(about_remind_handler)
  
  #Callback for menu
  updater.dispatcher.add_handler(CallbackQueryHandler(button))

  # Always should be last
  unknown_handler = MessageHandler(Filters.command, unknown)
  dispatcher.add_handler(unknown_handler)

  # Start the bot
  updater.start_polling()

  # Run the bot until you press Ctrl-C
  updater.idle()


if __name__ == '__main__':
  main()