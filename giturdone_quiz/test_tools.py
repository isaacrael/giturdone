import os
import django

#  you have to set the correct path to you settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "giturdone.settings")
django.setup()


from giturdone_quiz.models import Question, Answer


def run():
    # do the work
    wrong_answers_ordered = Answer.objects.order_by('total_wrong_answers')
    count = 0
    for answer in wrong_answers_ordered:
       count = count + 1
#       print(count)
    total = count
    print(total)
#    print(count)
    # first element in range
    last_element_in_range = total
    first_element_in_range = last_element_in_range - 6
    print(first_element_in_range)
    print(last_element_in_range)
    wrong_answers_ordered = Answer.objects.order_by('total_wrong_answers')
    wrong_answers_ordered = wrong_answers_ordered.values()
    wrong_answers_ordered = wrong_answers_ordered.order_by("total_wrong_answers")
    index = first_element_in_range
    context = {}
    for values in range(first_element_in_range,last_element_in_range):
        wrong_answers_ordered = Answer.objects.order_by('total_wrong_answers')
        wrong_answers_ordered = wrong_answers_ordered.values()
        my_dict = wrong_answers_ordered[index]
        print(my_dict)
        id = my_dict["question_id"]
        q = Question.objects.get(id=id)
        print(q)
        print my_dict["answer_text"]
        print my_dict["total_wrong_answers"]
        if index == first_element_in_range:
            question1 = Question.objects.get(pk=id)
            question1_total_wrong_answers = my_dict["total_wrong_answers"]
            print(question1)
            print(question1_total_wrong_answers)
            context["question1"] = question1
            context["question1_total_wrong_answers"] = question1_total_wrong_answers
            print context["question1"]
            print context["question1_total_wrong_answers"]
            print(context)
        elif index == first_element_in_range + 1:
            question2 = Question.objects.get(pk=id)
            question2_total_wrong_answers = my_dict["total_wrong_answers"]
            context["question2"] = question2
            context["question2_total_wrong_answers"] = question2_total_wrong_answers
            print context["question2"]
            print context["question2_total_wrong_answers"]
            print(context)
            print(question2)
            print(question2_total_wrong_answers)
        elif index == first_element_in_range + 2:
            question3 = Question.objects.get(pk=id)
            question3_total_wrong_answers = my_dict["total_wrong_answers"]
            context["question3"] = question3
            context["question3_total_wrong_answers"] = question3_total_wrong_answers
            print context["question3"]
            print context["question3_total_wrong_answers"]
            print(context)
            print(question3)
            print(question3_total_wrong_answers)
        elif index == first_element_in_range + 3:
            question4 = Question.objects.get(pk=id)
            question4_total_wrong_answers = my_dict["total_wrong_answers"]
            context["question4"] = question4
            context["question4_total_wrong_answers"] = question4_total_wrong_answers
            print context["question4"]
            print context["question4_total_wrong_answers"]
            print(context)
            print(question4)
            print(question4_total_wrong_answers)
        elif index == first_element_in_range + 4:
            question5 = Question.objects.get(pk=id)
            question5_total_wrong_answers = my_dict["total_wrong_answers"]
            context["question5"] = question5
            context["question5_total_wrong_answers"] = question5_total_wrong_answers
            print context["question5"]
            print context["question5_total_wrong_answers"]
            print(context)
            print(question5)
            print(question5_total_wrong_answers)

        print(index)
        if index != first_element_in_range + 5:
            index = index + 1
        print(context)




if __name__ == '__main__':
    run()