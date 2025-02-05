# aligntextstamp.py

import difflib

def align_text_with_timestamps(original_text, transcribed_words):
    """
    Orijinal metni ve transkribe edilmiş kelimeleri zaman damgalarıyla hizalar.

    Args:
        original_text (str): Orijinal metin.
        transcribed_words (list): Transkribe edilmiş kelimelerin ve zaman damgalarının listesi.

    Returns:
        list: Hizalanmış kelimelerin ve zaman damgalarının listesi.
    """
    # Orijinal metni kelimelere bölün
    original_words = original_text.strip().split()
    original_word_texts = [w.strip() for w in original_words]
    transcribed_word_texts = [w['word'] for w in transcribed_words]

    # Hizalama yapalım
    matcher = difflib.SequenceMatcher(None, original_word_texts, transcribed_word_texts)
    alignment = matcher.get_opcodes()

    # Orijinal kelimelere zaman damgalarını atayalım
    aligned_words = []
    for tag, i1, i2, j1, j2 in alignment:
        if tag == 'equal':
            # Kelimeler eşleşiyorsa, zaman damgalarını atayın
            for idx in range(i2 - i1):
                original_idx = i1 + idx
                transcribed_idx = j1 + idx
                word = original_word_texts[original_idx]
                timestamp = transcribed_words[transcribed_idx]
                aligned_words.append({'word': word, 'start': timestamp['start'], 'end': timestamp['end']})
        elif tag == 'replace':
            # Değiştirme durumunda, mümkünse zaman damgalarını atayın
            for idx in range(i2 - i1):
                original_idx = i1 + idx
                if j1 + idx < len(transcribed_words):
                    transcribed_idx = j1 + idx
                    word = original_word_texts[original_idx]
                    timestamp = transcribed_words[transcribed_idx]
                    aligned_words.append({'word': word, 'start': timestamp['start'], 'end': timestamp['end']})
                else:
                    word = original_word_texts[original_idx]
                    aligned_words.append({'word': word, 'start': None, 'end': None})
        elif tag == 'delete':
            # Orijinal metinde olup transkripsiyonda olmayan kelimeler
            for idx in range(i2 - i1):
                original_idx = i1 + idx
                word = original_word_texts[original_idx]
                aligned_words.append({'word': word, 'start': None, 'end': None})
        elif tag == 'insert':
            # Transkripsiyonda olup orijinal metinde olmayan kelimeler
            pass

    return aligned_words