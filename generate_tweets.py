import re

hashtag = "#BellLetsTalk"
max_characters = 140
regex = r"(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s"

manifesto = open("./manifesto.txt").readlines()[0]
tweets = open("./tweets.txt", "w")

for sentence in re.split(regex, manifesto):
    if len(sentence) + len(hashtag) < max_characters:
        tweets.write(sentence + hashtag + "\n")
    else:
        i = 0
        while i < len(sentence):
            if i == 0:
                crop_length = max_characters - len(hashtag) - 3
                cropped = sentence[i:i+crop_length]
                new_sentence = cropped + "..." + hashtag
            else:
                crop_length = max_characters - len(hashtag) - 6
                cropped = sentence[i:i+crop_length]
                if i + crop_length < len(sentence):
                    new_sentence = ("..." + cropped + "..." + hashtag)
                else:
                    new_sentence = "..." + cropped + hashtag

            tweets.write(new_sentence + "\n")
            i += crop_length
