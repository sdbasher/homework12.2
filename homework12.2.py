inputdata = ('Країна', 'шалаш', 'Летел', 'вертольот', 'УЧУ', 'мем', 'мова')

palindromes = filter(lambda word: word.lower() == word[::-1].lower(), inputdata)

print(list(palindromes))
