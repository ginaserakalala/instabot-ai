"""
Import Instapy module
"""
from instapy import InstaPy

from time import sleep
"""
Delay execution while instagram loads login page
"""

sleep(2)

"""
This feature allows the bot to run without the GUI of the browser.
This is super useful if you want to deploy your bot to a server where you may not have
or need the graphical interface. It’s also less CPU intensive, so it improves performance.
"""

session = InstaPy(username='username', password='password', headless_browser=True)
#session = InstaPy(username='datmemequeen42',password='keyaitaly')
session.login()

"""
Bot will only like posts based the specified tags below 
"""
#session.like_by_locations(['224442573/salton-sea/'], amount=100)
session.like_by_tags(["selfcare","waisttrainer","workout","gym"], amount = 50,media='Photo')
session.like_by_locations(['214345561','1018622046'], amount=50)
#session.like_by_locations(locations=['ZA/south-africa/'], amount=100, media='Photo')

"""
Set quota supervisor to prevent being banned by instagram
"""
session.set_quota_supervisor(enabled=True, sleep_after=['likes', 'comments_d', 'follows', 'unfollows', 'server_calls_h'], sleepyhead=True, stochastic_flow=True, notify_me=True,
                              peak_likes=(57, 585),
                               peak_comments=(21, 182),
                                peak_follows=(48, None),
                                 peak_unfollows=(35, 402),
                                  peak_server_calls=(None, 4700))

"""
This will close the browser, save the logs, 
and prepare a report that you can see in the console output
"""
session.end()
