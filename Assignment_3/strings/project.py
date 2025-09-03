"""
Interview-Style String Challenges
=================================
Author: Waqar Ali
Purpose: Dynamic practice hub for advanced string manipulation + interview Qs
"""

# ---------------------------
# Section F: String Challenges
# ---------------------------

def remove_duplicates():
    s = input("👉 Enter string: ")
    result = ""
    for ch in s:
        if ch not in result:
            result += ch
    print("✅ Without duplicates:", result)


def first_non_repeated():
    s = input("👉 Enter string: ")
    for ch in s:
        if s.count(ch) == 1:
            print("✅ First non-repeated:", ch)
            return
    print("❌ No non-repeated character found.")


def rotate_left():
    s = input("👉 Enter string: ")
    k = int(input("👉 Enter rotate by (default=1): ") or 1)
    print("✅ Rotated:", s[k:] + s[:k])


def compress_string():
    s = input("👉 Enter string: ")
    if not s:
        print("❌ Empty string.")
        return
    result, count = "", 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            result += s[i - 1] + str(count)
            count = 1
    result += s[-1] + str(count)
    print("✅ Compressed:", result)


def reverse_words():
    sentence = input("👉 Enter sentence: ")
    words = sentence.split()
    result = []
    for i in range(len(words) - 1, -1, -1):
        result.append(words[i])
    print("✅ Reversed words:", " ".join(result))


def count_case():
    s = input("👉 Enter text: ")
    upper = sum(1 for ch in s if ch.isupper())
    lower = sum(1 for ch in s if ch.islower())
    print(f"✅ Uppercase: {upper}, Lowercase: {lower}")


def validate_password():
    pw = input("👉 Enter password: ")
    valid = len(pw) >= 8 and any(ch.isdigit() for ch in pw)
    print("✅ Password valid?" if valid else "❌ Invalid password.")


def find_duplicate_words():
    text = input("👉 Enter paragraph: ").lower().split()
    duplicates = []
    for word in text:
        if text.count(word) > 1 and word not in duplicates:
            duplicates.append(word)
    print("✅ Duplicate words:", duplicates if duplicates else "None")


def vowel_frequency():
    s = input("👉 Enter string: ").lower()
    vowels = "aeiou"
    freq = {v: s.count(v) for v in vowels}
    print("✅ Vowel frequency:", freq)


def are_anagrams():
    s1 = input("👉 Enter first string: ").lower()
    s2 = input("👉 Enter second string: ").lower()
    print("✅ Are anagrams?" if sorted(s1) == sorted(s2) else "❌ Not anagrams.")


def interview_qs():
    print("\n💡 Interview Insights:")
    print("69. Difference between Immutable vs Mutable?")
    print("   - Immutable: str, tuple (cannot be changed once created).")
    print("   - Mutable: list, dict (can be modified in place).\n")
    print("70. Why are strings immutable?")
    print("   - Memory efficiency via interning.")
    print("   - Hashability (usable as dict keys).")
    print("   - Thread-safety & reliability (no accidental changes).")


# ---------------------------
# Main Menu Runner (Dynamic)
# ---------------------------

def main():
    options = {
        "59": ("Remove duplicate characters", remove_duplicates),
        "60": ("First non-repeated character", first_non_repeated),
        "61": ("Rotate string left", rotate_left),
        "62": ("Compress string", compress_string),
        "63": ("Reverse words in sentence", reverse_words),
        "64": ("Count uppercase vs lowercase", count_case),
        "65": ("Validate password", validate_password),
        "66": ("Find duplicate words in paragraph", find_duplicate_words),
        "67": ("Count frequency of vowels", vowel_frequency),
        "68": ("Check if two strings are anagrams", are_anagrams),
        "69-70": ("Interview Questions", interview_qs),
        "all": ("Run All Challenges", None),
    }

    while True:
        print("\n🚀 Interview-Style String Challenges 🚀")
        for key, (desc, _) in options.items():
            print(f"{key}. {desc}")
        print("0. Exit")

        choice = input("\n👉 Choose an option (e.g., 59, 63, all): ").strip()

        if choice == "0":
            print("👋 Exiting project. Goodbye!")
            break
        elif choice == "all":
            for _, func in options.values():
                if func:
                    func()
        elif choice in options:
            func = options[choice][1]
            if func:
                func()
        else:
            print("❌ Invalid choice, please try again.")


if __name__ == "__main__":
    main()
