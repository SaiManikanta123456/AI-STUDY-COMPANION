# import nltk
# from textblob import TextBlob
# from nltk.tokenize import sent_tokenize, word_tokenize
# from nltk.corpus import words
#
# nltk.download('punkt')
# nltk.download('words')
# nltk.download('cmudict')
#
# def calculate_features(text):
#     # Tokenize the text into words and sentences
#     words_list = word_tokenize(text)
#     sentences = sent_tokenize(text)
#
#     # Total number of words
#     word_count = len(words_list)
#
#     # Total number of sentences
#     sentence_count = len(sentences)
#
#     # Average sentence length
#     avg_sentence_length = word_count / sentence_count
#
#     # Percentage of complex words (words with more than two syllables)
#     syllable_count = 0
#     complex_word_count = 0
#
#     for word in words_list:
#         if word.lower() in words.words():
#             syllable_count += nltk.corpus.cmudict.dict()[word.lower()][0][-1]
#
#         if syllable_count > 2:
#             complex_word_count += 1
#
#     percentage_complex_words = (complex_word_count / word_count) * 100
#
#     # FOG Index
#     fog_index = 0.4 * (avg_sentence_length + percentage_complex_words)
#
#     # Average number of words per sentence
#     avg_words_per_sentence = word_count / sentence_count
#
#     # Syllables per word
#     syllables_per_word = syllable_count / word_count
#
#     # Personal pronouns (he, she, I, me, etc.)
#     personal_pronouns = sum(1 for word in words_list if word.lower() in ['i', 'me', 'my', 'mine', 'we', 'us', 'our', 'ours'])
#
#     # Average word length
#     avg_word_length = sum(len(word) for word in words_list) / word_count
#
#     # Sentiment analysis
#     polarity, subjectivity = TextBlob(text).sentiment
#
#     return {
#         'Positive Score': polarity if polarity > 0 else 0,
#         'Negative Score': -polarity if polarity < 0 else 0,
#         'Polarity Score': polarity,
#         'Subjectivity Score': subjectivity,
#         'Avg Sentence Length': avg_sentence_length,
#         'Percentage of Complex Words': percentage_complex_words,
#         'FOG Index': fog_index,
#         'Avg Number of Words per Sentence': avg_words_per_sentence,
#         'Complex Word Count': complex_word_count,
#         'Word Count': word_count,
#         'Syllables per Word': syllables_per_word,
#         'Personal Pronouns': personal_pronouns,
#         'Avg Word Length': avg_word_length
#     }
#
# # Sample text for demonstration
# sample_text = "This is a sample text. It has multiple sentences. Some words are complex."
#
# # Calculate features for the sample text
# features = calculate_features(sample_text)
# print("Text Features:")
# for feature, value in features.items():
#     print(f"{feature}: {value}")
import nltk
from textblob import TextBlob
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import words

nltk.download('punkt')
nltk.download('words')
nltk.download('cmudict')
def calculate_features(text):
    # Tokenize the text into words and sentences
    words_list = word_tokenize(text)
    sentences = sent_tokenize(text)

    # Total number of words
    word_count = len(words_list)

    # Total number of sentences
    sentence_count = len(sentences)

    # Average sentence length
    avg_sentence_length = word_count / sentence_count

    # Percentage of complex words (words with more than two syllables)
    syllable_count = 0
    complex_word_count = 0

    for word in words_list:
        if word.lower() in words.words():
            # Calculate the number of syllables
            syllables = [char for char in nltk.corpus.cmudict.dict()[word.lower()][0] if char[-1].isdigit()]
            syllable_count += len(syllables)

        if syllable_count > 2:
            complex_word_count += 1

    percentage_complex_words = (complex_word_count / word_count) * 100

    # FOG Index
    fog_index = 0.4 * (avg_sentence_length + percentage_complex_words)

    # Average number of words per sentence
    avg_words_per_sentence = word_count / sentence_count

    # Syllables per word
    syllables_per_word = syllable_count / word_count

    # Personal pronouns (he, she, I, me, etc.)
    personal_pronouns = sum(1 for word in words_list if word.lower() in ['i', 'me', 'my', 'mine', 'we', 'us', 'our', 'ours'])

    # Average word length
    avg_word_length = sum(len(word) for word in words_list) / word_count

    # Sentiment analysis
    polarity, subjectivity = TextBlob(text).sentiment

    return {
        'Positive Score': polarity if polarity > 0 else 0,
        'Negative Score': -polarity if polarity < 0 else 0,
        'Polarity Score': polarity,
        'Subjectivity Score': subjectivity,
        'Avg Sentence Length': avg_sentence_length,
        'Percentage of Complex Words': percentage_complex_words,
        'FOG Index': fog_index,
        'Avg Number of Words per Sentence': avg_words_per_sentence,
        'Complex Word Count': complex_word_count,
        'Word Count': word_count,
        'Syllables per Word': syllables_per_word,
        'Personal Pronouns': personal_pronouns,
        'Avg Word Length': avg_word_length
    }

# Sample text for demonstration
sample_text = "Telemedicine, the use of technology to diagnose and treat patients remotely, has been rising in recent years. With the advent of high-speed internet and improved video conferencing tools, healthcare providers are increasingly turning to telemedicine to provide care to patients in remote or underserved areas."

# Calculate features for the sample text
features = calculate_features(sample_text)
print("Text Features:")
for feature, value in features.items():
    print(f"{feature}: {value}")

