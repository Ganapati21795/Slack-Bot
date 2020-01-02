import os
import time
import re
from slackclient import SlackClient



# instantiate the slack client
slack_client = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))
# starterbot's user id in slack:value is assigned after the bot starts up.
starterbot_id = None


# constants
RTM_READ_DELAY = 1 # 1 second delay between reading from the RTM
EXAMPLE_COMMAND = "do"
PERF_NOTIFY = "notify 300"
MENTION_REGEX = "^<@(|[WU].+?)>(.*)"


def parse_bot_commands(slack_events):
    """
    parses the list of events coming from the RTM API to find the bot commands.
    if the bot command not found this function returns the tuple of command and channel.
    if this is not found this function returns None and None
    """
    for event in slack_events:
        if event["type"] == "message" and not "subtype" in event:
            user_id, message = parse_direct_mention(event["text"])
            if user_id == starterbot_id:
                return message, event["channel"]
    return None, None

def parse_direct_mention(message_text):
    """
    Finds a direct mention (a mention that is at the beggining) in a message text
    and returns the user id which is mentioned. If there is no direct mention returns None.
    """
    matches = re.search(MENTION_REGEX, message_text)
    # the first group contains a username and the second group contains remaining message.
    return (matches.group(1), matches.group(2).strip()) if matches else (None, None)
    


def handle_command(command, channel):
    """
    executes the command if the command is known
    """
    # default response is help to text for the user.
    default_response = "Not sure what you mean. Try *{}*.".format(EXAMPLE_COMMAND)
    
    # finds and executes the given command. filling in response.
    response = None
    # start to implement the more command
    if command.startswith(EXAMPLE_COMMAND):
        response = "sure write some more code then i can do that"
    if command.startswith(300_PERF_NOTIFY")
	"""
        get the response of the 300 perf results of the to json or xml document
        then send the response to the perticular channel
        """
        response = "getting the results of performance testing"

    # sends the response back to the channel.
    slack_client.api_call(
        "chat.postMessage",
        channel=channel,
        text= response or default_response
    )


if __name__ == "__main__":
    if slack_client.rtm_connect(with_team_state = False):
        print("starter bot is connected and running")
        # read a bot's user id by calling the Web API method 'auth.test'
        starterbot_id = slack_client.api_call("auth.test")["user_id"]
	while True:
            command, channel = parse_bot_commands(slack_client.rtm_read())
            if command:
                handle_command(command, channel)
            time.sleep(RTM_READ_DELAY)
    else:
        print("connection failed !!!")
   

