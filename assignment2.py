
def get_messages():
    n = int(input("Enter the number of messages: "))
    messages = []
    for _ in range(n):
        msg = input()
        messages.append(msg)
    return messages

def parse_messages(messages):
    data = []
    for msg in messages:
        if ": " in msg:
            name, text = msg.split(": ", 1)
            data.append((name.strip(), text.strip()))
    return data



def option_1_total_messages(messages):
    print("Total messages:", len(messages))

def option_2_unique_users(data):
    users = []
    for name, _ in data:
        if name not in users:
            users.append(name)
    print("Unique users in the chat:", set(users))

def option_3_total_words(data):
    count = 0
    for _, msg in data:
        count += len(msg.split())
    print("Total words in the chat:", count)

def option_4_avg_words_per_message(data):
    if len(data) == 0:
        print("No data available.")
        return
    total = 0
    for _, msg in data:
        total += len(msg.split())
    avg = total / len(data)
    print("Average words per message:", round(avg, 2))

def option_5_longest_message(messages):
    longest = ""
    for msg in messages:
        if len(msg) > len(longest):
            longest = msg
    print("Longest message:", '"' + longest + '"')

def option_6_most_active_user(data):
    counts = {}
    for user, _ in data:
        if user in counts:
            counts[user] += 1
        else:
            counts[user] = 1
    max_user = ""
    max_count = 0
    for user in counts:
        if counts[user] > max_count:
            max_user = user
            max_count = counts[user]
    print("Most active user:", max_user, f"({max_count} messages)")

def option_7_message_count_for_user(data):
    name = input("Enter user name: ")
    count = 0
    for user, _ in data:
        if user == name:
            count += 1
    print("Messages sent by", name + ":", count)

def option_8_most_frequent_word_by_user(data):
    name = input("Enter user name: ")
    word_count = {}
    for user, msg in data:
        if user == name:
            words = msg.lower().split()
            for word in words:
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1
    if len(word_count) == 0:
        print("No messages by", name)
        return
    max_word = ""
    max_count = 0
    for word in word_count:
        if word_count[word] > max_count:
            max_word = word
            max_count = word_count[word]
    print("Most frequent word used by", name + ':', '"' + max_word + '"')

def option_9_first_last_by_user(data):
    name = input("Enter user name: ")
    user_msgs = []
    for user, msg in data:
        if user == name:
            user_msgs.append(user + ": " + msg)
    if len(user_msgs) == 0:
        print("No messages by", name)
    else:
        print("First message by", name + ":", '"' + user_msgs[0] + '"')
        print("Last message by", name + ":", '"' + user_msgs[-1] + '"')

def option_10_check_user_present(data):
    name = input("Enter user name to check: ")
    found = False
    for user, _ in data:
        if user == name:
            found = True
            break
    if found:
        print("User '" + name + "' found in the chat.")
    else:
        print("User '" + name + "' not found in the chat.")

def option_11_common_repeated_words(data):
    word_count = {}
    for _, msg in data:
        for word in msg.lower().split():
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1
    repeated = []
    for word in word_count:
        if word_count[word] > 1:
            repeated.append(word)
    print("Common repeated words:", set(repeated))

def option_13_longest_avg_message_user(data):
    user_words = {}
    user_counts = {}
    for user, msg in data:
        words = len(msg.split())
        if user in user_words:
            user_words[user] += words
            user_counts[user] += 1
        else:
            user_words[user] = words
            user_counts[user] = 1
    max_user = ""
    max_avg = 0
    for user in user_words:
        avg = user_words[user] / user_counts[user]
        if avg > max_avg:
            max_avg = avg
            max_user = user
    print("User with longest average message:", max_user, f"(avg {round(max_avg, 2)} words)")

def option_14_messages_mentioning_user(data):
    name = input("Enter name to check mentions: ").lower()
    count = 0
    for _, msg in data:
        if name in msg.lower():
            count += 1
    print("Messages mentioning '" + name + "':", count)

def option_15_remove_duplicate_messages(messages):
    unique = []
    for msg in messages:
        if msg not in unique:
            unique.append(msg)
    print("Unique messages count:", len(unique))
    for msg in sorted(unique):
        print(msg)

def option_16_sort_messages(messages):
    sorted_msgs = sorted(messages)
    print("Messages sorted A-Z:")
    for msg in sorted_msgs:
        print(msg)

def option_17_extract_questions(data):
    print("Questions in the chat:")
    for user, msg in data:
        if "?" in msg:
            print(user + ": " + msg)

def option_18_reply_ratio_between_users(data):
    user1 = input("Enter first user (sender): ")
    user2 = input("Enter second user (replier): ")
    replies = 0
    for i in range(1, len(data)):
        prev_user, _ = data[i - 1]
        curr_user, _ = data[i]
        if prev_user == user1 and curr_user == user2:
            replies += 1
    print("Reply ratio from", user2, "to", user1 + ":", replies, "replies")

def option_19_check_deleted_messages(data):
    count = 0
    for _, msg in data:
        if msg == "This message was deleted":
            count += 1
    print("Deleted messages found:", count)


def show_menu():
    print("\nChoose an analysis option (0 to exit):")
    print("1. Count total number of messages")
    print("2. Identify unique users in the chat")
    print("3. Count total words in the chat")
    print("4. Calculate average words per message")
    print("5. Find the longest message sent")
    print("6. Find the most active user")
    print("7. Get message count for a specific user")
    print("8. Find the most frequently used word by a specific user")
    print("9. Retrieve the first and last message sent by a user")
    print("10. Check if a user is present in the chat")
    print("11. Find commonly repeated words")
    print("12. Identify the user with the longest average message length")
    print("13. Count how many messages mention a specific user")
    print("14. Remove duplicate messages")
    print("15. Sort messages alphabetically")
    print("16. Extract all questions asked in the chat")
    print("17. Calculate the reply ratio between two users")
    print("18. Check for deleted messages")


def main():
    messages = get_messages()
    data = parse_messages(messages)

    while True:
        show_menu()
        choice = input("Enter your option: ")
        if choice == "0":
            break
        elif choice == "1":
            option_1_total_messages(messages)
        elif choice == "2":
            option_2_unique_users(data)
        elif choice == "3":
            option_3_total_words(data)
        elif choice == "4":
            option_4_avg_words_per_message(data)
        elif choice == "5":
            option_5_longest_message(messages)
        elif choice == "6":
            option_6_most_active_user(data)
        elif choice == "7":
            option_7_message_count_for_user(data)
        elif choice == "8":
            option_8_most_frequent_word_by_user(data)
        elif choice == "9":
            option_9_first_last_by_user(data)
        elif choice == "10":
            option_10_check_user_present(data)
        elif choice == "11":
            option_11_common_repeated_words(data)
        elif choice == "12":
            option_13_longest_avg_message_user(data)
        elif choice == "13":
            option_14_messages_mentioning_user(data)
        elif choice == "14":
            option_15_remove_duplicate_messages(messages)
        elif choice == "15":
            option_16_sort_messages(messages)
        elif choice == "16":
            option_17_extract_questions(data)
        elif choice == "17":
            option_18_reply_ratio_between_users(data)
        elif choice == "18":
            option_19_check_deleted_messages(data)
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
