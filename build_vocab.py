# -*- coding: utf-8 -*-

# Các ký tự đầu vào
_pad = "$"
_punctuation = '«»“”;:,.!?¡¿—…" '
_letters = '()1234567*\u0361\u0306LMNOPQRSTUVWXYăabcdefghijklmnopqrstuvwxyz'
_letters_ipa = "ɑɐɒæɓʙβɔɕçɗɖðʤəɘɚɛɜɝɞɟʄɡɠɢʛɦɧħɥʜɨɪʝɭɬɫɮʟɱɯɰŋɳɲɴøɵɸθœɶʘɹɺɾɻʀʁɽʂʃʈʧʉʊʋⱱʌɣɤʍχʎʏʑʐʒʔʡʕʢǀǁǂǃˈˌːˑʼʴʰʱʲʷˠˤ˞↓↑→↗↘̩'ᵻ"
vocab_chars = list(dict.fromkeys(_pad + _punctuation + _letters + _letters_ipa))

# Các token đặc biệt
vocab_list = [
]

# Gộp danh sách cuối cùng: token đặc biệt + ký tự
vocab_list += [" " if c.strip() == "" else c for c in vocab_chars]

# Ghi ra file text
with open("word_index_dict.txt", "w", encoding="utf-8") as f:
    for idx, token in enumerate(vocab_list):
        f.write(f'"{token}",{idx}\n')

symbols = [_pad] + list(_punctuation) + list(_letters) + list(_letters_ipa)
print(len(symbols))
print(len(vocab_list))
