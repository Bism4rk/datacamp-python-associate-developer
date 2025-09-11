# Complete the for loop with a regex to find dates

import re

sentiment_analysis = ["10 days ago", "5 hours ago", "Yesterday", "2 weeks ago", "3 months ago", "1 year ago", "Just now", "4 minutes ago", "8 days ago"]

for date in sentiment_analysis:
	print(re.findall(r"\d{1,2}\s\w+\sago", date))
	
# Complete the for loop with a regex to find dates
for date in sentiment_analysis:
	print(re.findall(r"\d{1,2}\w+\s\w+\s\d{4}", date))
	
# Complete the for loop with a regex to find dates
for date in sentiment_analysis:
	print(re.findall(r"\d{1,2}\w+\s\w+\s\d{4}\s\d{1,2}:\d{2}", date))