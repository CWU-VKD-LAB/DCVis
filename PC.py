import numpy as np
import DATASET


def compute_positions(data, df_name, section_array):
    x_coord = np.tile(section_array, reps=len(df_name.index))
    y_coord = df_name.to_numpy()
    y_coord = y_coord.ravel()
    pos_array = np.column_stack((x_coord, y_coord))
    return pos_array


def compute_axis_positions(data, section_array):
    axis_vertex_array = [[-1, -1], [-1, 1]]
    for idx in range(1, data.vertex_count):
        axis_vertex_array.append([section_array[idx], 1])
        axis_vertex_array.append([section_array[idx], -1])
    return axis_vertex_array


class PC:
    def __init__(self, data: DATASET.Dataset):
        # Normalization using the DATASET class function
        data.dataframe = data.normalize_data(range=(-1, 1))

        # Create section_array based on vertex_count
        section_array = np.linspace(start=-1, stop=1, num=data.vertex_count)

        # Compute positions for each class and store in data.positions
        data.positions = []
        for class_name in data.class_names:
            df_name = data.dataframe[data.dataframe['class'] == class_name]
            df_name = df_name.drop(columns='class', axis=1)
            pos_array = compute_positions(data, df_name, section_array)
            data.positions.append(pos_array)

        # Compute axis positions
        data.axis_positions = compute_axis_positions(data, section_array)
        data.axis_count = data.vertex_count

        print('PC BASED GCA COMPLETE')
