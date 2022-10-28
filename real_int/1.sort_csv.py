import unittest

def sort_csv_columns(csv_data: str) -> str:
    mapper = {}
    counter = 0
    name_columns = csv_data.split('\n')[0].split(',')
    for columns in csv_data.split('\n'):
        mapper[counter] = csv_data.split('\n')[counter].split(',')
        counter += 1

    #     name_columns = csv_data.split('\n')[0].split(',')
    #     other_values = csv_data.split('\n')[1].split(',')
    #     other_values_1 = csv_data.split('\n')[2].split(',')

    mapper_holder = []

    for key in mapper.keys():
        if key == 0:
            continue

        mapper_holder.append(dict(zip(name_columns, mapper[key])))

    #     dict_map_name_other =  dict(zip(name_columns, other_values))
    #     dict_map_name_other_1 = dict(zip(name_columns, other_values_1))
    sorted_names = sorted(name_columns)
    final_csv = ",".join(sorted_names) + "\n"

    for item in mapper_holder:
        item_builder = []
        for name in sorted_names:
            item_builder.append(item.get(name))
        sorted_values_final = ",".join(item_builder) + "\n"
        final_csv = final_csv + sorted_values_final

    return final_csv[:-1]


def sort_csv_columns_test(csv_data: str) -> str:
    name_columns = csv_data.split('\n')[0].split(',')
    other_values = csv_data.split('\n')[1].split(',')
    other_values_1 = csv_data.split('\n')[2].split(',')

    dict_map_name_other = dict(zip(name_columns, other_values))
    dict_map_name_other_1 = dict(zip(name_columns, other_values_1))

    sorted_names = sorted(name_columns)
    final_csv = ",".join(sorted_names) + "\n"

    sorted_values = []
    for name in sorted_names:
        value = dict_map_name_other.get(name)
        sorted_values.append(value)

    sorted_values_final = ",".join(sorted_values) + "\n"

    sorted_values_1 = []
    for name in sorted_names:
        value = dict_map_name_other_1.get(name)
        sorted_values_1.append(value)

    sorted_values_final_1 = ",".join(sorted_values_1)

    return final_csv + sorted_values_final + sorted_values_final_1

# class TestExampleTests(unittest.TestCase):
#     def test_should_handle_the_example(self):
#         self.assertEqual(
#             sort_csv_columns("Beth,Charles,Danielle,Adam,Eric\n17945,10091,10088,3907,10132\n2,12,13,48,11"),
#             "Adam,Beth,Charles,Danielle,Eric\n3907,17945,10091,10088,10132\n48,2,12,13,11")



if __name__=="__main__":
    print(sort_csv_columns("Beth,Charles,Danielle,Adam,Eric\n17945,10091,10088,3907,10132\n2,12,13,48,11")==
          "Adam,Beth,Charles,Danielle,Eric\n3907,17945,10091,10088,10132\n48,2,12,13,11")




