import emoji

print("Emojis disponíveis:")
print("❤️ - :red_heart:")
print("👍 - :thumbs_up:")
print("🤔 - :thinking_face:")
print("🥳 - :partying_face:")

frase = input("Digite uma frase e ela será emojizada: ")
frase_emojizada = emoji.emojize(frase, use_aliases=True)
print(f"Frase emojizada:\n{frase_emojizada}")
