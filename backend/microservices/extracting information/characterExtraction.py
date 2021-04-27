import nltk
from nltk.corpus import stopwords


def readText(file_path):
    """
    Reads the text from a text file.
    """
    with open(file_path, "rb") as f:
        text = f.read().decode('utf-8-sig')
    return text


def chunkSentences(text):
    """
    Parses text into parts of speech tagged with parts of speech labels.

    Used for reference: https://gist.github.com/onyxfish/322906
    """
    sentences = nltk.sent_tokenize(text)
    tokenizedSentences = [nltk.word_tokenize(sentence)
                          for sentence in sentences]
    taggedSentences = [nltk.pos_tag(sentence)
                       for sentence in tokenizedSentences]
    if nltk.__version__[0:2] == "2.":
        chunkedSentences = nltk.batch_ne_chunk(taggedSentences, binary=True)
    else:
        chunkedSentences = nltk.ne_chunk_sents(taggedSentences, binary=True)
    return chunkedSentences


def extractEntityNames(tree, _entityNames=None):
    """
    Creates a local list to hold nodes of tree passed through, extracting named
    entities from the chunked sentences.

    Used for reference: https://gist.github.com/onyxfish/322906
    """
    if _entityNames is None:
        _entityNames = []
    try:
        if nltk.__version__[0:2] == "2.":
            label = tree.node
        else:
            label = tree.label()
    except AttributeError:
        pass
    else:
        if label == 'NE':
            _entityNames.append(' '.join([child[0] for child in tree]))
        else:
            for child in tree:
                extractEntityNames(child, _entityNames=_entityNames)
    return _entityNames


def buildDict(chunkedSentences, _entityNames=None):
    """
    Uses the global entity list, creating a new dictionary with the properties
    extended by the local list, without overwriting.

    Used for reference: https://gist.github.com/onyxfish/322906
    """
    if _entityNames is None:
        _entityNames = []

    for tree in chunkedSentences:
        extractEntityNames(tree, _entityNames=_entityNames)

    return _entityNames


def removeStopwords(entityNames, customStopWords=None):
    """
    Brings in stopwords and custom stopwords to filter mismatches out.
    """
    # Memoize custom stop words
    customStopwords = "Street, Road, Bridge, Town, Park, Hill, Lane, CHAPTER, Chapter, CHAPTER I, CHAPTER II, CHAPTER III, CHAPTER IV, CHAPTER V, CHAPTER VI, CHAPTER VII, CHAPTER VIII, CHAPTER IX, CHAPTER X, CHAPTER XI, CHAPTER XII, CHAPTER XIII, CHAPTER XIV, CHAPTER XV, CHAPTER XVI, CHAPTER XVII, CHAPTER XVIII, CHAPTER XIX, CHAPTER XX, CHAPTER XXI, CHAPTER XXII, CHAPTER XXIII, CHAPTER XXIV, CHAPTER XXV, CHAPTER XXVI, CHAPTER XXVII, CHAPTER XXVIII, CHAPTER XXIX, CHAPTER XXX, CHAPTER XXXI, CHAPTER XXXII, CHAPTER XXXIII, CHAPTER XXXIV, CHAPTER XXXV, CHAPTER XXXVI, CHAPTER XXXVII, CHAPTER XXXVIII, CHAPTER XXXIX, CHAPTER XL, CHAPTER XLI, CHAPTER XLII, CHAPTER XLIII, CHAPTER XLIV, CHAPTER XLV, CHAPTER XLVI, CHAPTER XLVII, CHAPTER XLVIII, CHAPTER XLIX, CHAPTER L, CHAPTER LI, CHAPTER LII, CHAPTER LIII, CHAPTER LIV, CHAPTER LV, Chapter I, Chapter II, Chapter III, Chapter IV, Chapter V, Chapter VI, Chapter VII, Chapter VIII, Chapter IX,  Chapter X, Chapter XI, Chapter XII, Chapter XIII, Chapter XIV, Chapter XV, Chapter XVI, Chapter XVII, Chapter XVIII, Chapter XIX, Chapter XX, Chapter XXI, Chapter XXII, Chapter XXIII, Chapter XXIV, Chapter XXV, Chapter XXVI, Chapter XXVII, Chapter XXVIII, Chapter XXIX, Chapter XXX, Chapter XXXI, Chapter XXXII, Chapter XXXIII, Chapter XXXIV, Chapter XXXV, Chapter XXXVI, Chapter XXXVII, Chapter XXXVIII, Chapter XXXIX, Chapter XL, Chapter XLI, Chapter XLII, Chapter XLIII, Chapter XLIV, Chapter XLV, Chapter XLVI, Chapter XLVII, Chapter XLVIII, Chapter XLIX, Chapter L, Chapter LI, Chapter LII, Chapter LIII, Chapter LIV, Chapter LV, God, Lord, Heaven, Heavens, Come, Thank God, Poor, Tell, Well, Very, VERY, Meantime, No, Yes, Aye, Nor, Hark, Thou, Stand, Thank, French, German, English, Italian, Polish, Austrian, Russian, Pray, Certainly, Listen, Adieu, Mediterranean, Arabian, Hotel, Island, Ah, Oh, Please, Republic, Take, WHICH, Which, Certain, Alas, Ney, Woe, Life, Good, Death, Was, Latin, Nothing, Boulevard, Slang, Light, Greek, Place, Make, Such, Holy Sacrament, Night, Day, BOOK, Book, Great, Are, Guard, Wait, Him, Her, Look, Everything, Toward, Thy, Everyone, Every, Project, Project Gutenberg," \
        .split(', ')

    for name in entityNames:
        if name in stopwords.words('english') or name in customStopwords:
            entityNames.remove(name)


def getMajorCharacters(entityNames):
    """
    Adds names to the major character list if they appear frequently.
    """
    return {name for name in entityNames if entityNames.count(name) > 10}


def removeHonorifics(name):
    honorifics = ["Mr.", "mr.", "Mrs.", "mrs.", "Jr.", "jr.", "Dr.", "dr.",
                  "Prof.", "prof.", "Sr.", "sr.", "Lady.", "lady.", "Lord.", "Lord."]

    for title in honorifics:
        if name.lower().startswith(title.lower()):
            name = name[len(title):]
            name = name.strip()
            break
    return name


def removeTitles(names):
    """
    Split sentences on .?! "" and not on abbreviations of titles.
    Used for reference: http://stackoverflow.com/a/8466725
    """
    filtered_names = []
    for name in names:
        name = removeHonorifics(name)
        if len(name) > 0:
            filtered_names.append(name)

    return filtered_names


def characterExtraction(file_path):
    text = readText(file_path)
    chunkedSentences = chunkSentences(text)
    entityNames = buildDict(chunkedSentences)
    removeStopwords(entityNames)
    majorCharacters = getMajorCharacters(entityNames)
    majorCharacters = removeTitles(majorCharacters)
    majorCharacters.sort()
    print(majorCharacters)
    return majorCharacters


if __name__ == "__main__":
    characterExtraction("OlivarTwist.txt")
