# Import re module
import re

sentiment_analysis = ["@user1 I love this! http://example.com", "Check this out @user2 http://example.org", "No links or mentions here", "@user3 visit http://example.net", "Another tweet without special content", "@user4 http://example.com/page"]

for tweet in sentiment_analysis:
	# Write regex to match http links and print out result
	print(re.findall(r"http\S+", tweet))

	# Write regex to match user mentions and print out result
	print(re.findall(r"@\w+", tweet))