def answer_puzzle():
    """
    This function randomly asks a question and captures the user answer from the input.
    Then the answer is compared against the solution.
    The function returns 1 if the answer and solution matches and 0 otherwise.
    The questions and the corresponding solutions are define in a form of keys/pairs within a dictionary.
    """

    import random
    enigmas = {
    "I have four legs, a back, but no head. What am I?":"chair",
    "I can fall off a building and live, but put me in water I will die. What am I?":"paper",
    "I have keys, but no locks and no rooms. You can enter, but you can’t go outside. What am I?":"keyboard",
    "You answer me, but I never ask you questions. What am I?":"telephone",
    "You change me every month, no matter how much you use me. What am I?":"calendar",
    "If you break me, I’ll not stop working.If you can touch me, my work is done.If you lose me, you must find me with a ring soon after.What am I?":"heart",
    "What goes on four legs in the morning, on two legs at noon, and on three legs in the evening?":"man",
    "I have teeth, but cannot chew. What am I?":"comb",
    "I’m excellent to taste, but horrible to smell. What am I?":"tongue",
    "I am made of water, but I’m not wet. What am I?":"cloud",
    "I have a ring but no finger. What am I?":"telephone",
    "I’m full of keys but I can’t open any door. What am I?":"piano",
    "I’m tall when I’m young and I’m short when I’m old. What am I?":"candle",
    "I have a single eye but cannot see. What am I?":"needle",
    "I have a face but no eyes, hands but no arms. What am I?":"clock",
    "I sit in a corner while travelling around the world. What am I?":"stamp",
    "I always run but never walk, often murmur but never talk, have a bed but never sleep, have a mouth but never eat. What am I?":"river"
          }
    questions = [k for k,v in enigmas.items()]
    i = random.randint(0, len(enigmas.keys()) - 1)

    if enigmas[questions[i]] in input(questions[i]).lower().split(): result = 1
    else:
      play_sound(failed)
      result = 0

    return result

def christmas_tree(x):
    print("\n".join([f"{'*'*(2* n + 1):^{2*x+1}}" for n in (*range(x), 0, 0)]))

def play_sound(file_path):
    pygame.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    time.sleep(2)
    pygame.quit()
