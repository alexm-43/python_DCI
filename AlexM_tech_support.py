import sys

IT = {"crashed": "Are the device drivers up to date?",
      "blue": "Ah, the blue screen! And then what happened?",
      "hacked": "You should consider installing anti-virus software.",
      "bluetooth": "The solution is as simple as enabling it.",
      "windows": "Ah, I think I see your problem. What version?",
      "apple": "You do mean the computer kind of apple don't you?",
      "spam": "You should see if your mail client can filter  messages.",
      "connection": "Contact your internet provider."
      }

def query(message):
   message = message.lower()
   words = message.split()
   if 'quit' in words:
      sys.exit()
   for i in words:
      if i in IT:
         print(IT[i])
         new = str(input())
         query(new)
      else:
         continue
   print("Curious, tell me more.")
   new = str(input())
   query(new)
         
print("Welcome to the automated technical support  system. Please describe your problem:")
intro = str(input())
query(intro)
