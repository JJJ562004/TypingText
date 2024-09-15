import text
org_t_list = text.hard.split(' ')
type_t_list = 'Ephemeral vestiges'.split(' ')
print(org_t_list)
print(type_t_list)
result_list = [i2 for i1, i2 in zip(org_t_list, type_t_list) if i1 == i2]
print(result_list)