import nltk
text="In very brief summary, you have passed something that is being interpreted as a string of bytes to something that needs to decode it into Unicode characters, but the default codec (ascii) is failing. This is the classic unicode issue. I believe that explaining this is beyond the scope of a StackOverflow answer to completely explain what is happening. This is the classic unicode issue. I believe that explaining this is beyond the scope of a StackOverflow answer to completely explain what is happening."

num = len(text)
print(num)

sentences = nltk.sent_tokenize(text)
tokenized_sentences = [nltk.word_tokenize(sentence) for sentence in sentences]
tagged_sentences = [nltk.pos_tag(sentence) for sentence in tokenized_sentences]
chunked_sentences = nltk.ne_chunk_sents(tagged_sentences, binary=True)

def extract_entity_names(t):
    entity_names = []

    if hasattr(t, 'label') and t.label:
        if t.label() == 'NE':
            entity_names.append(' '.join([child[0] for child in t]))
        else:
            for child in t:
                entity_names.extend(extract_entity_names(child))

    return entity_names

entity_names = []
for tree in chunked_sentences:
    #print results per sentence
    #print extract_entity_names(tree)

    entity_names.extend(extract_entity_names(tree))

#print all entity_names
#print entity_names

#print unique entity names
print set(entity_names)

