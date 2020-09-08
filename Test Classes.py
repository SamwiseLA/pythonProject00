from Question import Question

# This way, you do not need to do anything but add to the list and the module will handle adding the question

l_question_prompts = [
    ["What color are Apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n", "a"],
    ["What color are Bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n", "c"],
    ["What color are Strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n", "b"],
    ["What color are Lemons?\n(a) Yellow\n(b) Red\n(c) Blue\n\n", "a"],
    ["What color are Pears?\n(a) Yellow\n(b) Green\n(c) Blue\n\n", "b"]
]

l_questions = []
lc_questions = []

print("")

for i in l_question_prompts:
    # Classless List - access items using relative location 0 through len() - 1
    l_questions.append(i)
    # Class List - access items by row and label from class "Question" from app27Question
    lc_questions.append(Question(i[0], i[1]))

# print("") # For Debugging


def f_run_testl(pl_questions):
    i_score = 0
    for il_question in pl_questions:
        l_valid_answers = ["a", "b", "c"]
        s_answer = "x"
        while s_answer not in l_valid_answers:
            s_answer = input(il_question[0])
            if s_answer not in l_valid_answers:
                print("*** Invalid Choice***\nPlease enter -> \"a\", \"b\" or \"c\":")
        if s_answer == il_question[1]:
            i_score += 1

    return i_score, len(pl_questions)


def f_run_testlc(plc_questions):
    i_score = 0
    for il_question in plc_questions:
        l_valid_answers = ["a", "b", "c"]
        s_answer = "x"
        while s_answer not in l_valid_answers:
            s_answer = input(il_question.s_prompt)
            if s_answer not in l_valid_answers:
                print("*** Invalid Choice***\nPlease enter -> \"a\", \"b\" or \"c\":")
        if s_answer == il_question.s_answer:
            i_score += 1

    return i_score, len(plc_questions)

Bold = "\033[1m"
Reg = "\033[0m"
print(Bold + "--- Using Relative Locations---\n" + Reg)
l_result = f_run_testl(l_questions)
print("\n*******************************\nYou got {0} Correct out of {1}!".format(l_result[0], l_result[1]))
print("\n*******************************\n")


print(Bold + "--- Using Class Labels ---\n" + Reg)
l_result = f_run_testlc(lc_questions)
print("\n*******************************\nYou got {0} Correct out of {1}!".format(l_result[0], l_result[1]))
