# word2vec_google_news_demo.py
# ---------------------------------------------
# Example using pretrained Google News Word2Vec (300D)
# via gensim.downloader
# ---------------------------------------------

import gensim.downloader as api

# ---------------------------------------------------
# Step 1: Load Pretrained Model
# ---------------------------------------------------
print("Loading pre-trained 'word2vec-google-news-300' model... (may take a few minutes)")
model = api.load('word2vec-google-news-300')
print("✅ Model loaded successfully!\n")

# ---------------------------------------------------
# Step 2: Find similar words
# ---------------------------------------------------
print("Top 5 words similar to 'king':")
print(model.most_similar('king', topn=5))
print()

print("Top 5 words similar to 'computer':")
print(model.most_similar('computer', topn=5))
print()

# ---------------------------------------------------
# Step 3: Analogy examples
# ---------------------------------------------------
print("Analogy example: king - man + woman = ?")
result = model.most_similar(positive=['king', 'woman'], negative=['man'], topn=5)
for word, score in result:
    print(f"{word}: {score:.3f}")
print()

# ---------------------------------------------------
# Step 4: Word similarity scores
# ---------------------------------------------------
print("Similarity between 'car' and 'bus':", model.similarity('car', 'bus'))
print("Similarity between 'car' and 'apple':", model.similarity('car', 'apple'))
print()

# ---------------------------------------------------
# Step 5: Odd one out
# ---------------------------------------------------
words = ['apple', 'banana', 'mango', 'car', 'grape']
outlier = model.doesnt_match(words)
print(f"Outlier in {words} → {outlier}")
