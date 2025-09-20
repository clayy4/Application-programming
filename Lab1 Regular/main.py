#Найдите анкеты людей, у которых указан номер телефона (в корректном формате).
#Выведите их количество на экран и сохраните найденные анкеты в новый файл.
import re
import argparse

#Находит все номера по заданному шаблону
def correct_numbers(text):
	pattern = r"[8|\+7]+[ (]*\d{3}[ )]*\d{3}[ -]*\d{2}[ -]*\d{2}"
	return re.findall(pattern, text)

parser = argparse.ArgumentParser()
parser.add_argument("--read_file", "-rf", type=str, help = "file read name")
parser.add_argument("--write_file", "-wf", type=str, help = "file write name")
args = parser.parse_args()

phone_numbers = []

if args.read_file is not None:
	with open(args.read_file, "r") as file:
		text = file.read()	
	phone_numbers = correct_numbers(text)
	print("\nКоличество корректных номеров среди анкет: ",len(phone_numbers))

if args.write_file is not None:
	with open(args.write_file, "w") as file:
		for cur_number in phone_numbers:
			file.write(cur_number + "\n")
		print(f"Все номера успешно записаны в \"{args.write_file}\"\n")	

