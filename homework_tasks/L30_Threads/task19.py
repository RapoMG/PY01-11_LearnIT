'''
AI: Równoległa analiza sentymentu (symulacja)
Stwórz listę 20 przykładowych zdań (opinii o produkcie). Napisz funkcję
analizuj_sentyment(zdanie), która symuluje zapytanie do API AI przez
time.sleep(random.uniform(0.5, 2.0)) i zwraca losowo "Pozytywny", "Negatywny" lub
"Neutralny". Użyj puli wątków (concurrent.futures.ThreadPoolExecutor), aby przeanalizować
wszystkie zdania i zebrać wyniki. Zmierz czas wykonania.
'''

import concurrent.futures
import random
import time


def analyze_sentiment(sentence):
    time.sleep(random.uniform(0.5, 2.0))
    return random.choice(['Positive', 'Negative', 'Neutral'])   


if __name__ == "__main__":
    sentences = [
        "This product is great!",
        "I love this product!",
        "The product is okay.",
        "I don't like this product.",
        "This product is amazing!",
        "The product is not good.",
        "I really like this product.",
        "This product is awesome!",
        "The product is not bad.",
        "I really love this product.",
        "This product is so-so.",
        "The product is not good.",
        "I really like this product.",
        "This product is awesome!",
        "The product is not bad.",
        "I really love this product.",
        "This product is so-so.",
        "The product is not good.",
        "I really like this product.",
        "This product is awesome!",
    ]

    start_time = time.time()
    with concurrent.futures.ThreadPoolExecutor() as executor:    
        results = list(executor.map(analyze_sentiment, sentences))

    end_time = time.time()
    print(f"Time taken: {end_time - start_time}")

    print(results)