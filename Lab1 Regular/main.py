#Найдите анкеты людей, у которых указан номер телефона (в корректном формате).
#Выведите их количество на экран и сохраните найденные анкеты в новый файл.
import re
import argparse

#Находит все номера по заданному шаблону
def count_correct_numbers(text):
	pattern = r"(8|\+7)+[ (]*\d{3}[ )]*\d{3}[ -]*\d{2}[ -]*\d{2}"
	count = len(re.findall(pattern, text))
	return count

parser = argparse.ArgumentParser()
parser.add_argument("--file_name", "-f", type=str, help = "file name")
args = parser.parse_args()



with open(args.file_name, "r") as file:
	text = file.read()	

print(count_correct_numbers(text))