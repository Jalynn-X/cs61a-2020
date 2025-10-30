"""Typing test implementation"""

from utils import lower, split, remove_punctuation, lines_from_file
from ucb import main, interact, trace
from datetime import datetime


###########
# Phase 1 #
###########


def choose(paragraphs, select, k):
    """Return the Kth paragraph from PARAGRAPHS for which SELECT called on the
    paragraph returns true. If there are fewer than K such paragraphs, return
    the empty string.
    """
    # BEGIN PROBLEM 1
    "*** YOUR CODE HERE ***"
    para_can_be_selected = [x for x in paragraphs if select(x) is True]
    if len(para_can_be_selected) < k + 1:
        return ""
    else:
        return para_can_be_selected[k]
    # END PROBLEM 1



def about(topic):
    """Return a select function that returns whether a paragraph contains one
    of the words in TOPIC.

    >>> about_dogs = about(['dog', 'dogs', 'pup', 'puppy'])
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup!'], about_dogs, 0)
    'Cute Dog!'
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup.'], about_dogs, 1)
    'Nice pup.'
    """
    assert all([lower(x) == x for x in topic]), 'topics should be lowercase.'
    # BEGIN PROBLEM 2
    "*** YOUR CODE HERE ***"
    def select(para):
        para_list = split(lower(remove_punctuation(para)))
        for one_topic in topic:
            if one_topic in para_list:
                return True
        return False
    return select
    # END PROBLEM 2
# 这里要尤其注意return False的缩进，我之前写的是：
# for one_topic in topic:
#   if one_topic in para_list:
#       return True
#   else:
#       return False
# 这就导致当执行for循环的时候，如果第一个元素不满足True, 那么就会返回False，不会判断第二个元素了
# 但是，如果return False的缩进和for在同一层级，如果没有满足条件的item，第一个return没有执行，才会执行第二个return

def accuracy(typed, reference):
    """Return the accuracy (percentage of words typed correctly) of TYPED
    when compared to the prefix of REFERENCE that was typed.

    >>> accuracy('Cute Dog!', 'Cute Dog.')
    50.0
    >>> accuracy('A Cute Dog!', 'Cute Dog.')
    0.0
    >>> accuracy('cute Dog.', 'Cute Dog.')
    50.0
    >>> accuracy('Cute Dog. I say!', 'Cute Dog.')
    50.0
    >>> accuracy('Cute', 'Cute Dog.')
    100.0
    >>> accuracy('', 'Cute Dog.')
    0.0
    """
    typed_words = split(typed)
    reference_words = split(reference)
    # BEGIN PROBLEM 3
    "*** YOUR CODE HERE ***"
    num, denum, num_reference = 0, len(typed_words), len(reference_words)
    if len(typed_words) == 0:
        return 0.0
    else:
        for i in range(min(denum, num_reference)):
            if typed_words[i] == reference_words[i]:
                num += 1
    return (num / denum) * 100
    # END PROBLEM 3


def wpm(typed, elapsed):
    """Return the words-per-minute (WPM) of the TYPED string."""
    assert elapsed > 0, 'Elapsed time must be positive'
    # BEGIN PROBLEM 4
    "*** YOUR CODE HERE ***"
    words = len(typed) / 5
    return words/(elapsed/60)
    # END PROBLEM 4


def autocorrect(user_word, valid_words, diff_function, limit):
    """Returns the element of VALID_WORDS that has the smallest difference
    from USER_WORD. Instead returns USER_WORD if that difference is greater
    than LIMIT.
    """
    # BEGIN PROBLEM 5
    "*** YOUR CODE HERE ***"
    if user_word in valid_words:
        return user_word
    else:
        word_plus_diff = []
        for valid_word in valid_words:
            diff = diff_function(user_word, valid_word, limit)
            word_plus_diff.append([valid_word, diff])
        min_num = min([x[1] for x in word_plus_diff])
        if min_num <= limit:
            words = [word[0] for word in word_plus_diff if word[1] == min_num]
            return words[0]
        else:
            return user_word
    # END PROBLEM 5
        
# 虽然感觉用字典储存valid:diff会更好，但是字典是无序的吧？用字典如何实现取第一个呢？
# hint介绍了一个比较list其中一个元素的方法，我在上面是通过提取每一个sub list里的元素进行比较
# min(word_plus_diff, key = lambda item: item[1])
# >>> min([[1,5], [2,6], [3,4]], key=lambda item: item[0]) --- [1, 5]

def shifty_shifts(start, goal, limit):
    """A diff function for autocorrect that determines how many letters
    in START need to be substituted to create GOAL, then adds the difference in
    their lengths.
    """
    # BEGIN PROBLEM 6
    def helper(start, goal, limit, diff_len=0):
        min_len = min(len(start), len(goal))
        if diff_len > limit:
            return limit + 1
        else:
            if len(start) == 0 and len(goal) == 0:
                return diff_len
            elif len(start) != len(goal):
                diff_len = abs(len(start) - len(goal))
                return helper(start[:min_len], goal[:min_len], limit, diff_len)
            else:
                if start[0] != goal[0]:
                    diff_len += 1
                return helper(start[1:min_len], goal[1:min_len], limit, diff_len)
    return helper(start, goal, limit)
    # END PROBLEM 6


def pawssible_patches(start, goal, limit):
    """A diff function that computes the edit distance from START to GOAL."""
    def patches_helper(start, goal, limit, diff=0):
        if diff > limit:
            return limit + 1
        else:
            if start == goal:
                return diff
            elif len(start) == 0 or len(goal) == 0:
                return diff + abs(len(start) - len(goal))
            else:
                if start[0] != goal[0]:
                    add = patches_helper(start, goal[1:], limit, diff+1)
                    substitute = patches_helper(start[1:], goal[1:], limit, diff+1)
                    #substituting "hello" and "mello" equivales distracting h, m and comparing the other letters 
                    remove = patches_helper(start[1:], goal, limit, diff+1)
                    return min(add, substitute, remove)
                else:
                    if len(start) > 1 and len(goal) > 1:
                        return patches_helper(start[1:], goal[1:], limit, diff)
                    elif (len(start) == 1 and len(goal) > 1) or (len(start) > 1 and len(goal) == 1):
                        return diff + abs(len(goal) - len(start))
                    elif len(start) <= 1 and len(goal) <= 1:
                        return diff
    return patches_helper(start, goal, limit)

# 以下注释都是我尝试question07的过程。刚开始尝试自己比较在什么情况下用哪种方法会带来更小的数值，也就是说我想通过穷举来代替min这个功能
# 后来发现不现实，很难把所有情况都进行列举。所以参考了hint视频的提示做出来了，但是代码很长...需要看看是否能够精简
#                 if start[i] not in goal:
#                     diff += 1
#                     start = start[0:i] + start[i+1:]
#                 return patches_helper(start, goal, limit, diff)
#             for i in range(0, len(goal)):
#                 if goal[i] not in start:
#                     diff += 1
#                     start = start[0:i] + goal[i] + start[i + 1:]
#                 return patches_helper(start, goal, limit, diff)
#             for i in range(0,len(start)):
#                 if start[i] != goal[i]:
#                     new_index = start.index(goal[i])
#                     diff += 1
#                     start = start[0, min(i, new_index)] + start[min(i, new_index)] + start[min(i, new_index)+1, max(i, new_index)] + start[max(i, new_index)] + start[max(i, new_index):]
#                 return patches_helper(start, goal, limit, diff)
# return patches_helper(start, goal, limit)

#             for letter in start:
#                 s_index, g_index = start.index(letter), goal.index(letter)
#                 if letter not in goal:
#                     diff += 1
#                     start = start[0:s_index] + start[s_index:]
#                 elif letter not in start:
#                     diff += 1
#                     start = start[0:g_index] + letter + start[g_index:]
#                 elif s_index != g_index:
#                     diff += 1
#                     start = start[0:min(s_index, g_index)] + start[min(s_index, g_index)] + start[min(s_index, g_index):max(s_index, g_index)] + start[max(s_index, g_index):]
#                 return patches_helper(start, goal, limit, diff)
# return patches_helper(start, goal, limit)

# if goal[0] in start:
#     change_index = start.index(goal[0])
#     start = start[change_index] + start
#     diff += 1 #substitute
#     return patches_helper(start[1:], goal[1:], limit, diff)
# elif start[0] not in goal:
#     diff += 1 #remove
#     return patches_helper(start[1:], goal, limit, diff)
# elif goal[0] not in start:

def final_diff(start, goal, limit):
    """A diff function. If you implement this function, it will be used."""
    assert False, 'Remove this line to use your final_diff function'


###########
# Phase 3 #
###########


def report_progress(typed, prompt, user_id, send):
    """Send a report of your id and progress so far to the multiplayer server."""
    # BEGIN PROBLEM 8
    "*** YOUR CODE HERE ***"
    index, count_right, dictionary = 0, 0, {}
    while index < len(typed):
        if typed[index] != prompt[index]:
            break
        else:
            count_right += 1
        index += 1
    percentage = count_right / len(prompt)
    dictionary['id'] = user_id
    dictionary['progress'] = percentage
    send(dictionary)
    return percentage
    # END PROBLEM 8


def fastest_words_report(times_per_player, words):
    """Return a text description of the fastest words typed by each player."""
    game = time_per_word(times_per_player, words)
    fastest = fastest_words(game)
    report = ''
    for i in range(len(fastest)):
        words = ','.join(fastest[i])
        report += 'Player {} typed these fastest: {}\n'.format(i + 1, words)
    return report


def time_per_word(times_per_player, words):
    """Given timing data, return a game data abstraction, which contains a list
    of words and the amount of time each player took to type each word.

    Arguments:
        times_per_player: A list of lists of timestamps including the time
                          the player started typing, followed by the time
                          the player finished typing each word.
        words: a list of words, in the order they are typed.
    """
    # BEGIN PROBLEM 9
    "*** YOUR CODE HERE ***"
    time_lists = []
    for t_p_y in times_per_player:
        index_tpy = len(t_p_y)
        per_list = [] # 注意这个列表不能放在第一个for之前，否则会把所有的数值都储存在一起，导致数量不一致
        for i in range(1, index_tpy): #注意这里的range范围，我写错了好多次
            per_list.append(t_p_y[i] - t_p_y[i-1])
        time_lists.append(per_list)
    return game(words, time_lists)
    # END PROBLEM 9


def fastest_words(game):
    """Return a list of lists of which words each player typed fastest.

    Arguments:
        game: a game data abstraction as returned by time_per_word.
    Returns:
        a list of lists containing which words each player typed fastest
    """
    player_indices = range(len(all_times(game)))  # contains an *index* for each player
    word_indices = range(len(all_words(game)))    # contains an *index* for each word
    # 注意这里的range是可以直接使用的。作为参考，以后对于这种len(list)作为range范围的，其实不需要写range(0, len)
    # BEGIN PROBLEM 10
    "*** YOUR CODE HERE ***"  
    player_fastest_words = []
    for player_index in player_indices:
        fastest_word = []
        player_fastest_words.append(fastest_word)
    for num_index in word_indices:
        min_time = min(time[num_index] for time in all_times(game))
        for player_index in player_indices:
            if time(game, player_index, num_index) == min_time:
                player_fastest_words[player_index].append(word_at(game, num_index))
                break 
    return player_fastest_words
    # END PROBLEM 10

# 真的服了....我写的好复杂啊啊啊啊，要先去看一下hint视频，然后参考下别人的答案
#     for num_index in range(0, num_of_words):
#         if time(game, player_index, num_index) == fastest_player[num_index] and pla:
#             fastest_word.append(word_at(game, num_index))
#     fastest_words.append(fastest_word)
# return fastest_words

# 看了hint视频，我原来也考虑过先建立一个大的列表，然后每个player都建立一个空列表，再逐个往里面添加。但是后来没想好怎么实现
# 以下是我最开始绞尽脑汁写的代码.....好啰嗦
# fastest_player = {}
# for num_index in word_indices:
#     all_player_time = []
#     for player_index in player_indices:
#         all_player_time.append(time(game, player_index, num_index))
#     fastest_player_index = [all_player_time.index(time) for time in all_player_time if time == min(all_player_time)][0]
#     fastest_player[num_index] = fastest_player_index
# player_fastest_words = []
# for player_index in player_indices:
#     fastest_word = []
#     for i in word_indices:
#         if fastest_player[i] == player_index:
#             fastest_word.append(word_at(game, i))
#     player_fastest_words.append(fastest_word)
# return player_fastest_words




def game(words, times):
    """A data abstraction containing all words typed and their times."""
    assert all([type(w) == str for w in words]), 'words should be a list of strings'
    assert all([type(t) == list for t in times]), 'times should be a list of lists'
    assert all([isinstance(i, (int, float)) for t in times for i in t]), 'times lists should contain numbers'
    assert all([len(t) == len(words) for t in times]), 'There should be one word per time.'
    return [words, times]


def word_at(game, word_index):
    """A selector function that gets the word with index word_index"""
    assert 0 <= word_index < len(game[0]), "word_index out of range of words"
    return game[0][word_index]


def all_words(game):
    """A selector function for all the words in the game"""
    return game[0]


def all_times(game):
    """A selector function for all typing times for all players"""
    return game[1]


def time(game, player_num, word_index):
    """A selector function for the time it took player_num to type the word at word_index"""
    assert word_index < len(game[0]), "word_index out of range of words"
    assert player_num < len(game[1]), "player_num out of range of players"
    return game[1][player_num][word_index]


def game_string(game):
    """A helper function that takes in a game object and returns a string representation of it"""
    return "game(%s, %s)" % (game[0], game[1])

enable_multiplayer = False  # Change to True when you're ready to race.

##########################
# Command Line Interface #
##########################


def run_typing_test(topics):
    """Measure typing speed and accuracy on the command line."""
    paragraphs = lines_from_file('data/sample_paragraphs.txt')
    select = lambda p: True
    if topics:
        select = about(topics)
    i = 0
    while True:
        reference = choose(paragraphs, select, i)
        if not reference:
            print('No more paragraphs about', topics, 'are available.')
            return
        print('Type the following paragraph and then press enter/return.')
        print('If you only type part of it, you will be scored only on that part.\n')
        print(reference)
        print()

        start = datetime.now()
        typed = input()
        if not typed:
            print('Goodbye.')
            return
        print()

        elapsed = (datetime.now() - start).total_seconds()
        print("Nice work!")
        print('Words per minute:', wpm(typed, elapsed))
        print('Accuracy:        ', accuracy(typed, reference))

        print('\nPress enter/return for the next paragraph or type q to quit.')
        if input().strip() == 'q':
            return
        i += 1


@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions."""
    import argparse
    parser = argparse.ArgumentParser(description="Typing Test")
    parser.add_argument('topic', help="Topic word", nargs='*')
    parser.add_argument('-t', help="Run typing test", action='store_true')

    args = parser.parse_args()
    if args.t:
        run_typing_test(args.topic)