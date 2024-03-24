import tweepy

auth = tweepy.OAuth1UserHandler(
    'ZZoExY8utr3LD3O1WMO9LrkrD', 'OQMbelV6bLlQeZpQ0AoqZ4oy5o8OmJxCqgQf7cxJv6hfVoUOng', '1674428657501368320-v2mUE67NBRpdZKMy8ovcWvNpsbyrKZ', 'ONiOQ5XrOrD5x0NdxLAT4uF1lJ7Dn16KBYtoz4w5i5yO5'
)

api = tweepy.API(auth)
user = api.get_user()
print(user.name)
