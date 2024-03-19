import app.io.input as inp
import app.io.output as out


def main():
    # from console:
    text_from_console = inp.input_text_from_console()

    out.output_text_to_console("\n\tText from console:\n" + text_from_console)
    out.write_to_file_using_py("data/output_file.txt", text_from_console)

    # from file py:
    text_from_file = inp.read_from_file_using_py("data/input_file.txt")

    out.output_text_to_console("\n\tText from file:\n" + text_from_file)
    out.write_to_file_using_py("data/output_file_2.txt", text_from_file)

    # from file pandas:
    data_frame_pandas = inp.read_from_file_using_pandas("data/pandas_data.csv").to_string()

    out.output_text_to_console("\n\tText from pandas file:\n" + data_frame_pandas)
    out.write_to_file_using_py("data/output_file_3.txt", data_frame_pandas)


if __name__ == "__main__":
    main()
