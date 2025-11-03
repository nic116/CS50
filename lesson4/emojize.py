

import emoji

def main():
    emo = get_emoji(input("Input: "))
    print(emo)

def get_emoji(prompt):
    
    emo_out = emoji.emojize(f"Output: {prompt}", language='alias')
    return emo_out


main()