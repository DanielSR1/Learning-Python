from datetime import date, datetime
import instaloader
L=instaloader.Instaloader()
#fazer login na sua conta do instagram#
L.login('insira aqui seu login do instagram','insira sua senha')
#carregar todos os posts do perfil escolhido#
posts=instaloader.Profile.from_username(L.context, "insira aqui o nome do usuario para download").get_posts()
#periodo que deseja baixar os posts#
SINCE=datetime(2022, 3, 2)
UNTIL=datetime(2022, 3, 2)
#percorre os posts e baixa apenas os que estão na data desejada#
for post in posts:
    if (post.date >= SINCE) and (post.date <= UNTIL):
        print(post.date)
        L.download_post(post, "insta-posts-downloads")

