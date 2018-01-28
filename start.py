import time

from instapy import InstaPy
from insta_config import config
from insta_config import runs

while True:
    for run in runs:
        session = InstaPy(username=config['username'], password=config['password'], nogui=config['nogui'])
        session.login()

        # read the global config and do the set_XXX methods

        if 'lower_follower_count' in config and config['lower_follower_count']:
            session.set_lower_follower_count(limit=config['lower_follower_count'])

        if 'upper_follower_count' in config and config['upper_follower_count']:
            session.set_upper_follower_count(limit=config['upper_follower_count'])

        if 'dont_include' in config and config['dont_include']:
            session.set_dont_include(config['dont_include'])

        if 'do_follow' in config and config['do_follow'] is True:
            session.set_do_follow(enabled=True, percentage=config['do_follow_percentage'], times=config['do_follow_times'])

        if 'inclusion' in run and run['inclusion'] is True:
            # run the like_by_tags
            session.like_by_tags_with_inclusion(
                main_tag=run['main_tag'],
                include_tags=run['include_tags'],
                amount=run['amount']
            )
        else:
            session.like_by_tags(
                tags=run['include_tags'],
                amount=run['amount']
            )

        # do an unfollow?
        if 'do_unfollow' in config and config['do_unfollow'] is True:
            session.unfollow_users(
                amount=config['do_unfollow_amount'],
                onlyInstapyFollowed=config['do_unfollow_only_ig'],
                onlyNotFollowMe=config['do_unfollow_only_not_followed'],
                sleep_delay=config['do_unfollow_delay']
            )

        # end session and sleep
        session.end()
        time.sleep(config['sleep_time'])
