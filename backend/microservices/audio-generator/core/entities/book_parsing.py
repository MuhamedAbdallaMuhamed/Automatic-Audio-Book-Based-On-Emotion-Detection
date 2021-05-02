def parse_book(text):
    import nltk
    import re
    import spacy
    import neuralcoref
    from nltk.corpus import stopwords
    from collections import defaultdict

    DELIMITER = " $@$ "
    DISTANCE_LIMIT = 20
    KEYWORD_LIMIT = 5
    dialogue_index = int()

    # Load SpaCy
    nlp = spacy.load('en')
    # Add neural coref to SpaCy's pipe
    neuralcoref.add_to_pipe(nlp)

    def coref_resolution(text):
        """Function that executes coreference resolution on a given text"""
        doc = nlp(text)
        return doc._.coref_resolved

    def isValid(char, prev):
        return 'A' <= char <= 'Z' and not ('a' <= prev <= 'z' or 'A' <= prev <= 'Z')

    def isGood(char):
        good = ".", " ", ",", "$", "@"
        return 'A' <= char <= 'Z' or 'a' <= char <= 'z' or char in good

    def cleanDialogues(text):
        dialogues = list()
        new_text = str()
        i = 0
        while i < len(text):
            if text[i] == "'" and isValid(text[i + 1], text[i - 1]):
                start = i + 1
                end = text.find("' ", i + 1)
                if end == -1:
                    end = text.find("'\n", i + 1)
                if start <= end:
                    dialogues.append(text[start:end])
                    i = end + 1
                new_text += "'' "
            else:
                if isGood(text[i]):
                    new_text += text[i]
            i += 1
        return dialogues, new_text

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

    def splitIntoSentences(text):
        """
        Split sentences on .?! "" and not on abbreviations of titles.
        Used for reference: http://stackoverflow.com/a/8466725
        """
        sentenceEnders = re.compile(r"""
        # Split sentences on whitespace between them.
        (?:               # Group for two positive lookbehinds.
          (?<=[.!?])      # Either an end of sentence punct,
        | (?<=[.!?]['"])  # or end of sentence punct and quote.
        )                 # End group of two positive lookbehinds.
        (?<!  Mr\.   )    # Don't end sentence on "Mr."
        (?<!  Mrs\.  )    # Don't end sentence on "Mrs."
        (?<!  Ms\.   )    # Don't end sentence on "Ms."
        (?<!  Jr\.   )    # Don't end sentence on "Jr."
        (?<!  Dr\.   )    # Don't end sentence on "Dr."
        (?<!  Prof\. )    # Don't end sentence on "Prof."
        (?<!  Sr\.   )    # Don't end sentence on "Sr."
        \s+               # Split on whitespace between sentences.
        """, re.IGNORECASE | re.VERBOSE)
        return sentenceEnders.split(text)

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

    def removeStopwords(entityNames, is_sentence=False):
        """
        Brings in stopwords and custom stopwords to filter mismatches out.
        """
        # Memoize custom stop words
        customStopwords = "Street, Road, Bridge, Town, Park, Hill, Lane, CHAPTER, Chapter, CHAPTER I, " \
                          "CHAPTER II, CHAPTER III, CHAPTER IV, CHAPTER V, CHAPTER VI, CHAPTER VII, " \
                          "CHAPTER VIII, CHAPTER IX, CHAPTER X, CHAPTER XI, CHAPTER XII, CHAPTER XIII, " \
                          "CHAPTER XIV, CHAPTER XV, CHAPTER XVI, CHAPTER XVII, CHAPTER XVIII, CHAPTER XIX, " \
                          "CHAPTER XX, CHAPTER XXI, CHAPTER XXII, CHAPTER XXIII, CHAPTER XXIV, " \
                          "CHAPTER XXV, CHAPTER XXVI, CHAPTER XXVII, CHAPTER XXVIII, CHAPTER XXIX, " \
                          "CHAPTER XXX, CHAPTER XXXI, CHAPTER XXXII, CHAPTER XXXIII, CHAPTER XXXIV, " \
                          "CHAPTER XXXV, CHAPTER XXXVI, CHAPTER XXXVII, CHAPTER XXXVIII, CHAPTER XXXIX, " \
                          "CHAPTER XL, CHAPTER XLI, CHAPTER XLII, CHAPTER XLIII, CHAPTER XLIV, " \
                          "CHAPTER XLV, CHAPTER XLVI, CHAPTER XLVII, CHAPTER XLVIII, CHAPTER XLIX, " \
                          "CHAPTER L, CHAPTER LI, CHAPTER LII, CHAPTER LIII, CHAPTER LIV, CHAPTER LV, " \
                          "Chapter I, Chapter II, Chapter III, Chapter IV, Chapter V, Chapter VI, " \
                          "Chapter VII, Chapter VIII, Chapter IX,  Chapter X, Chapter XI, Chapter XII, " \
                          "Chapter XIII, Chapter XIV, Chapter XV, Chapter XVI, Chapter XVII, " \
                          "Chapter XVIII, Chapter XIX, Chapter XX, Chapter XXI, Chapter XXII, " \
                          "Chapter XXIII, Chapter XXIV, Chapter XXV, Chapter XXVI, Chapter XXVII, " \
                          "Chapter XXVIII, Chapter XXIX, Chapter XXX, Chapter XXXI, Chapter XXXII, " \
                          "Chapter XXXIII, Chapter XXXIV, Chapter XXXV, Chapter XXXVI, Chapter XXXVII, " \
                          "Chapter XXXVIII, Chapter XXXIX, Chapter XL, Chapter XLI, Chapter XLII, " \
                          "Chapter XLIII, Chapter XLIV, Chapter XLV, Chapter XLVI, Chapter XLVII, " \
                          "Chapter XLVIII, Chapter XLIX, Chapter L, Chapter LI, Chapter LII, Chapter LIII, " \
                          "Chapter LIV, Chapter LV, God, Lord, Heaven, Heavens, Come, Thank God, Poor, " \
                          "Tell, Well, Very, VERY, Meantime, No, Yes, Aye, Nor, Hark, Thou, Stand, Thank, " \
                          "French, German, English, Italian, Polish, Austrian, Russian, Pray, Certainly, " \
                          "Listen, Adieu, Mediterranean, Arabian, Hotel, Island, Ah, Oh, Please, Republic, " \
                          "Take, WHICH, Which, Certain, Alas, Ney, Woe, Life, Good, Death, Was, Latin, " \
                          "Nothing, Boulevard, Slang, Light, Greek, Place, Make, Such, Holy Sacrament, " \
                          "Night, Day, BOOK, Book, Great, Are, Guard, Wait, Him, Her, Look, Everything, " \
                          "Toward, Thy, Everyone, Every, Project, Project Gutenberg," \
            .split(', ')
        stopCharacters = "\n", "-", "", ":", ";"

        for name in entityNames:
            if name in stopwords.words('english') or name in customStopwords or name in stopCharacters:
                entityNames.remove(name)
        if not is_sentence:
            return entityNames

        replace_words_space = "(", ")", "-"
        useless_words = "?", "!", "#", "$", "%", "^", "&", "*", "_", "+", "-", "/", ":", ";"

        if not entityNames:
            return []

        for j in range(len(entityNames)):
            for i in useless_words:
                entityNames[j] = entityNames[j].replace(i, '')
            for i in replace_words_space:
                entityNames[j] = entityNames[j].replace(i, ' ')
            tmp_str = str()
            for i in range(len(entityNames[j])):
                if i + 1 < len(entityNames[j]) and i - 1 >= 0 and \
                        entityNames[j][i] == "'" and not (isValid(entityNames[j][i + 1], entityNames[j][i - 1])):
                    continue
                else:
                    tmp_str += entityNames[j][i]
            entityNames[j] = tmp_str
            entityNames[j] = entityNames[j].replace("  ", " ")
        return entityNames

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

    def getParagraphs(text):
        paragraph = text.split("\n\n")
        return paragraph

    def cleanCharactersList(characters):
        persons = list()
        vis = {}
        for i in characters:
            vis[i] = False
        for i in range(len(characters)):
            for j in range(i + 1, len(characters)):
                if characters[j].startswith(characters[i]) and characters[i] != characters[j]:
                    vis[characters[j]] = True
        for i in characters:
            if not vis[i]:
                end = i.find(" ")
                if end == -1:
                    persons.append(i)
                else:
                    persons.append(i[end + 1:-1])
                vis[i] = True
        return persons

    def discoverRightCharacter(characters, text, index):
        word_count = 0
        while word_count < DISTANCE_LIMIT:
            end = text.find(" ", index)
            if end == -1:
                end = text.find("\n", index)
                if end == -1:
                    return None
            word = text[index:end]
            for i in characters:
                if word.startswith(i):
                    return i
            index = end + 1
            word_count += 1
        return None

    def getLeftSpace(index, text):
        while index >= 0:
            if text[index] == " " or text[index] == '\n':
                return index
            index -= 1
        return -1

    def discoverLeftCharacter(characters, text, index):
        word_count = 0
        while word_count < DISTANCE_LIMIT:
            start = getLeftSpace(index, text)
            if start == -1:
                return None
            word = text[start + 1:index]
            for i in characters:
                if word.startswith(i):
                    return i
            index = start - 1
            word_count += 1
        return None

    def hasKeyWord(text, index):
        keyWords = "spoke said replied observed inquired interposed added repeated urged stammered continued acquiesced " \
                   "rejoined exclaimed sobbed cried".split(" ")
        word_count = 0
        while word_count < KEYWORD_LIMIT:
            end = text.find(" ", index)
            word = text[index:end]
            if word in keyWords:
                return True
            word_count += 1
            index = end + 1
        return False

    def extractCharacterScripts(text, characters, dialogues, scripts):
        global dialogue_index
        if dialogue_index >= len(dialogues):
            return
        prev_character = None
        i = 0
        while i < len(text):
            if i + 2 < len(text) and text[i] == "'" and text[i + 1] == "'" \
                    and (i == 0 or isValid('A', text[i - 1])) and (text[i + 2] == ' ' or text[i + 2] == '\n'):
                right_character = discoverRightCharacter(characters, text, i + 2)
                left_character = discoverLeftCharacter(characters, text, i - 1)
                if right_character and left_character:
                    if hasKeyWord(text, i + 2):
                        scripts[right_character].append((dialogues[dialogue_index], dialogue_index))
                        prev_character = right_character
                    else:
                        scripts[left_character].append((dialogues[dialogue_index], dialogue_index))
                        prev_character = left_character
                elif right_character:
                    scripts[right_character].append((dialogues[dialogue_index], dialogue_index))
                    prev_character = right_character
                elif left_character:
                    scripts[left_character].append((dialogues[dialogue_index], dialogue_index))
                    prev_character = left_character
                else:
                    if prev_character is not None:
                        scripts[prev_character].append((dialogues[dialogue_index], dialogue_index))
                dialogue_index += 1
                i += 1
            i += 1

    def characterExtraction():
        chunkedSentences = chunkSentences(text)
        entityNames = buildDict(chunkedSentences)
        entityNames = removeStopwords(entityNames, False)
        majorCharacters = getMajorCharacters(entityNames)
        majorCharacters = removeTitles(majorCharacters)
        majorCharacters.sort(key=len)
        majorCharacters = cleanCharactersList(majorCharacters)
        paragraph = getParagraphs(text)
        sentences = list()
        for sentence in paragraph:
            split_text = splitIntoSentences(sentence)
            new_text = removeStopwords(split_text, True)
            if new_text:
                sentences.append(new_text)
        tmp = str()
        for i in sentences:
            tmp += " ".join(i)
            tmp += DELIMITER
        tmp += ' '
        tmp = tmp.replace('\n', ' ')
        dialogues, tmp = cleanDialogues(tmp)
        for i in range(len(dialogues)):
            dialogues[i] = dialogues[i].replace("$@$", "")
        cleaned_paragraphs = tmp.split("$@$")
        for i in range(len(cleaned_paragraphs)):
            cleaned_paragraphs[i] = coref_resolution(cleaned_paragraphs[i])
            cleaned_paragraphs[i] += '\n'
        scripts = defaultdict(list)
        global dialogue_index
        dialogue_index = 0
        for i in cleaned_paragraphs:
            extractCharacterScripts(i, majorCharacters, dialogues, scripts)
        return sentences, majorCharacters, scripts

    return characterExtraction()

    '''
    El H5a Techniques (made with love by MM):
        1- character found in right of sentence then right done
        2- character found in left of sentence then left done
        3- character not found then done
            3.1- last sentence in the same paragraph then it belongs to the same character
            3.2- else the default character
        4- character found in both directions then done 
            4.1- search for key word in right 
                4.1.1- found then it belongs to right
                4.1.2- not found then it belongs to left
        DISTANCE= 20*words
    '''
    '''
        muhamed said "" done
        sentences, { character name: [list_sentences]} done
        tmp_sentences -> done
        [amin is kaka] -> done
    '''
