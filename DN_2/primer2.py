our_list = [1,2,3,4,5,6,7]
our_dict = {
    "a": 2,
    "b": 5,
    "c": 8,
    "d": 12,
    "e": 357,
    "f": 12
}
our_tuple = (357, 12, 12, 8, 5, 2, 2)

# Odstranjevanje vrednosti iz our_list in spreminjanje our_dict
our_dict["d"] = our_list.pop(4)

print(our_list)
print(our_dict)
 
# Zapisovanje vrednosti our_dict v novi tuple
new_tuple = tuple(our_dict.values())

# Primerjava tuple-ov
print("\nPrimerjava:")
print(new_tuple)
print(our_tuple)

if new_tuple == our_tuple:
    print("Tuple-a sta enaka")
else:
    print("Tuple-a nista enaka")