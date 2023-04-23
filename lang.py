from lingua import Language, LanguageDetectorBuilder
languages = [Language.ENGLISH, Language.FRENCH, Language.GERMAN, Language.SPANISH]
detector = LanguageDetectorBuilder.from_languages(*languages).build()
text = input("Enter text in either english, german, french or spanish\n")
confidence_values = detector.compute_language_confidence_values(text)
for language, value in confidence_values:
     print(f"{language.name}: {value:.2f}")