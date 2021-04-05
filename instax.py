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


"""
Bot will only like posts based the specified tags below 
"""
session.like_by_tags(["memes","mzansi"], amount = 5)

"""
Set quota supervisor to prevent being banned by instagram
"""
session.set_quota_supervisor(enabled=True, peak_comments_daily=240, peak_comments_hourly=21)

"""
This will close the browser, save the logs, 
and prepare a report that you can see in the console output
"""
session.end()
