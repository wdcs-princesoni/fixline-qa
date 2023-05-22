import openai
import json



def get_openai_resp():
    response = openai.Completion.create(model="text-davinci-003",
                                        prompt="Tell me the betting question based on custom topic with two answer choices. Also, make sure that data should be in the json string format like key and value. Keys should be question, answer_one, answer_two respectively so it would be easy to extract the data.",
                                        max_tokens=50,
                                        temperature=1.0)
    return response.choices[0].text


op = get_openai_resp()
data = json.loads(op)
# print(op)
# data = json.loads(op)
question = data["question" or "Question"]
ans_one = data["answer_one" or "Answer_One"]
ans_two = data["answer_two" or "Answer_Two"]
# print(data,op, question, ans_two, ans_one)
one = ans_one
# print(one, "One")
two = ans_two
# print(two, "two")
ques = question
# print(ques, "ques")
