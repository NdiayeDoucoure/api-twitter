import tweepy
from textblob import TextBlob

# Question 1:
"""L'analyse de sentiment (ou sentiment analysis en anglais) est le processus qui consiste
# à déterminer l'opinion, le jugement et l'émotion qui se cache derrière le langage naturel."""

# Quuestion 2:
"""L'analyse de sentiment se révèle redoutablement utile lorsque vous êtes face à un grand volume de données
textuelles et que vous devez en extraire des informations et les généraliser. En effet, si nos cerveaux
humains sont tout à fait capables de comprendre les sentiments qui se cachent derrière des énoncés, nous
ne sommes pas en mesure de traiter des masses importantes de commentaires venant de multiples sources en un temps raisonnable."""


# Stocker les clés dans des variables
API_KEY = "ZFII4cNVpIfoAH78O38obxZk0"
API_KEY_SECRET = "q2BahmIZbehBL5myAbK8JDSFOeEUzbvnPejlvyhwFtWj7rHmrX"
ACCESS_TOKEN = "1473316896661512193-JQyy6E5xYEaSbYjL7N0ZNvPl3LIuOh"
ACCESS_TOKEN_SECRET = "1Xhxiz6JzAeiJgXnAI3HNLwTDzGReeEVODipfg3ouiaEp"
BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAAFvGjgEAAAAAhQ5Wo3n8cjD7PWeXoh30wx838EE%3D1An9un8O84wQNy95bR8OEW5TpEqG73qr8RmELVCnkrUTKVkHfg"

# Initialiser une connexion à l'API de TWITTER
client = tweepy.Client(BEARER_TOKEN)
# Tester la connexion à l'API
try:
    print('Bakhna !')
except:
    print('Bakhoul dara !')

# Recuperer les tweets d'un utilisateur par son id
print("BILL GATES")
user_id = 50393960  # Bill Gates
response = client.get_users_tweets(user_id)

for tweet in response.data:
    print(tweet.id)
    print(tweet.text)

# Analyse sentimentale des 10 derniers tweets de Bill Gates
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    if analysis.sentiment[0] > 0:
        print("Tweet Positive")
    elif analysis.sentiment[0] < 0:
        print("Tweet Négative")
    else:
        print("Tweet Neutre")




