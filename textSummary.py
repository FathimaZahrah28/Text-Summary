class text_summary:
    
    def __init__(self, text):
        self.text = text
    
    def word_tokenize(self):
        import spacy
        nlp = spacy.load('en_core_web_sm')
        doc = nlp(self.text)
        tokens = [token.text for token in doc]
        return tokens
    
    def text_cleaning(self):
        from spacy.lang.en.stop_words import STOP_WORDS
        from string import punctuation
        import spacy
        nlp = spacy.load('en_core_web_sm')
        doc = nlp(self.text)
        stopwords = list(STOP_WORDS)
        punctuation = punctuation + '\n'
        word_frequencies = {}
        for word in doc :
            if word.text.lower() not in stopwords:
                if word.text.lower() not in punctuation:
                    if word.text not in word_frequencies.keys():
                        word_frequencies[word.text] = 1
                    else:
                        word_frequencies[word.text] += 1
        
        return word_frequencies
    
    def word_frequency(self, word_frequencies):
        max_frequency = max(word_frequencies.values())
        for word in word_frequencies.keys():
            word_frequencies[word] = word_frequencies[word]/max_frequency
        
        return word_frequencies
    
    def sentence_token(self):
        import spacy
        nlp = spacy.load('en_core_web_sm')
        doc = nlp(self.text)
        sentence_tokens = [sent for sent in doc.sents]
        return sentence_tokens
    
    def sentence_score(self, sentence_tokens, word_frequencies):
        
        sentence_scores = {}
        for sent in sentence_tokens:
            for word in sent:
                if word.text.lower() in word_frequencies.keys():
                    if sent not in sentence_scores.keys():
                        sentence_scores[sent] = word_frequencies[word.text.lower()]
                    else:
                        sentence_scores[sent] += word_frequencies[word.text.lower()]
            
        from heapq  import nlargest
        select_length = int(len(sentence_tokens)*0.3)
        summary = nlargest(select_length, sentence_scores, key= sentence_scores.get)
        return summary
    
    def final_summary(self, summary):
        final_summary = [word.text for word in summary]
        summary = ' '.join(final_summary)
        return print(summary)
    
    def show_summary(self):
        w_token = self.word_tokenize()
        t_clean = self.text_cleaning()
        word_freq= self.word_frequency(t_clean)
        s_token = self.sentence_token()
        s_score = self.sentence_score(s_token, word_freq)
        f_summary = self.final_summary(s_score)
        return f_summary


      
      
