import sys

from zhipuai import ZhipuAI
import json

if __name__ == '__main__':
    args = sys.argv
    #api_key = args[1]
    with open("./target/generation_instruction.txt", "r", encoding="UTF-8") as file:
        content = file.readlines()

    file2 = open("./target/error_instruction.txt", "a", encoding="UTF-8")
    file3 = open("./target/car_data_QA.json", "a", encoding="UTF-8")
    index = 5037
    while index < len(content):
        instruction = content[index]
        try:
            client = ZhipuAI(api_key="e725cddeb96733573d6ad7f665137407.lNiXBXBRzumvSjgO")
            messages = [{"role": "user",
                         "content": f"你是一名汽车供应链领域的专家。请给下面的问题给出专业且合理的回答：\n{instruction}"}]
            response = client.chat.completions.create(
                model="glm-4",
                messages=messages,
            )
        except Exception as e:
            print(f"{index+1}   失败   {instruction}")
            print(e)
            file2.write(instruction)
        else:
            answer = response.choices[0].message.content
            QA_dict = {"instruction": instruction, "input": "", "output": answer}
            print(f"{index+1}   成功   {QA_dict}")
            file3.write(json.dumps(QA_dict, ensure_ascii=False) + ","+"\n")
        finally:
            index += 1
