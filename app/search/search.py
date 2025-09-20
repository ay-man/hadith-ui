def search_query(query):
    # For now, mock data. Replace with actual search logic
    data = {
        "quran": ["Verse 1 related to {}".format(query), "Verse 2 related to {}".format(query)],
        "hadith": ["Hadith 1 related to {}".format(query), "Hadith 2 related to {}".format(query)],
    }
    return data

