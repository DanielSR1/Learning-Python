from datetime import date, datetime
import instaloader
L=instaloader.Instaloader()
L.login('insira aqui seu login do instagram','insira sua senha')
posts=instaloader.Profile.from_username(L.context, "#insira aqui o nome do usuario para download").get_posts()
SINCE=datetime(2022, 3, 2)
UNTIL=datetime(2022, 3, 2)
for post in posts:
    if (post.date >= SINCE) and (post.date <= UNTIL):
        print(post.date)
        L.download_post(post, "insta-posts-downloads")

