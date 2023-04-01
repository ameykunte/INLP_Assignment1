#wittenbell
def witten_bell_smoothing(corpus, sentence):
    n = 4 # n-gram order
    # Compute n-gram counts
    ngram_counts = {}
    for doc in corpus:
        for i in range(len(doc) - n + 1):
            ngram = tuple(doc[i:i+n])
            if ngram not in ngram_counts:
                ngram_counts[ngram] = 1
            else:
                ngram_counts[ngram] += 1

    # Compute vocabulary size
    vocabulary = set([word for doc in corpus for word in doc])
    V = len(vocabulary)

    # Compute unigram counts
    unigram_counts = {}
    for ngram in ngram_counts:
        if len(ngram) == 1:
            unigram_counts[ngram] = ngram_counts[ngram]
    # Compute context counts and probabilities
    context_counts = {}
    context_probs = {}
    for ngram in ngram_counts:
        if len(ngram) == n:
            context = ngram[:-1]
            if context in context_counts:
                context_counts[context] += 1
            else:
                context_counts[context] = 1
    for context in context_counts:
        denominator = sum([ngram_counts[ngram] for ngram in ngram_counts if ngram[:-1] == context])
        context_probs[context] = 1 - (context_counts[context] / (context_counts[context] + denominator))

    # Compute probabilities 
    sentence = ["<s>"] * (n-1) + sentence.split() + ["</s>"]
    sentence_prob = 1.0
    for i in range(n-1, len(sentence)):
        context = tuple(sentence[i-n+1:i-1])
        word = sentence[i]
        if context in context_probs:
            total_count = sum([ngram_counts[ngram] for ngram in ngram_counts if ngram[:-1] == context])
            if (context + (word,)) in ngram_counts:
                word_count = ngram_counts[context+(word,)]
            else:
                word_count = 0
            word_prob = (context_probs[context] * word_count / total_count) + ((1 - context_probs[context]) * unigram_counts.get((word,), 0) / V)
            sentence_prob *= word_prob
        else:
            # If the context is unseen, use a uniform distribution over the vocabulary
            sentence_prob *= 1 / V**(n-1)

    return sentence_prob

#kneser-ney
def kneser_ney_smoothing(corpus, sentence):

    n = 4  # n-gram order
    discount = 0.75

    # Compute n-gram counts
    ngram_counts = {}
    for doc in corpus:
        for i in range(len(doc) - n + 1):
            ngram = tuple(doc[i:i+n])
            if ngram not in ngram_counts:
                ngram_counts[ngram] = 1
            else:
                ngram_counts[ngram] += 1

    # Compute vocab size
    vocabulary = set([word for doc in corpus for word in doc])
    V = len(vocabulary)

    # Compute unigram counts
    unigram_counts = {}
    for ngram in ngram_counts:
        if len(ngram) == 1:
            unigram_counts[ngram] = ngram_counts[ngram]

    # Compute context counts
    context_counts = {}
    for ngram in ngram_counts:
        if len(ngram) == n:
            context = ngram[:-1]
            if context in context_counts:
                context_counts[context] += 1
            else:
                context_counts[context] = 1

    # Compute backoff weights and probabilities
    backoff_weights = {}
    backoff_probs = {}
    for context in context_counts:
        counts = [ngram_counts[ngram] for ngram in ngram_counts if ngram[:-1] == context]
        backoff_weights[context] = max(sum(counts) - discount, 0) / sum(counts)
    for ngram in ngram_counts:
        if len(ngram) == n-1:
            context = ngram
            total_count = sum([ngram_counts[ngram] for ngram in ngram_counts if ngram[:-1] == context])
            backoff_probs[context] = max((total_count - discount) / total_count, 0)

    # Compute probabilities
    sentence = ["<s>"] * (n-1) + sentence.split() + ["</s>"]
    sentence_prob = 1.0
    for i in range(n-1, len(sentence)):
        context = tuple(sentence[i-n+1:i-1])
        word = sentence[i]
        if context in backoff_weights:
            total_count = sum([ngram_counts[ngram] for ngram in ngram_counts if ngram[:-1] == context])
            if (context + (word,)) in ngram_counts:
                word_count = ngram_counts[context+(word,)]
            else:
                word_count = 0
            word_prob = (max(word_count - discount, 0) / total_count) + (backoff_weights[context] * backoff_probs.get(word, 0))
            sentence_prob *= word_prob
        else:
            # If the context is unseen, use a uniform distribution over the vocabulary
            sentence_prob *= 1 / V**(n-1)

    return sentence_prob
