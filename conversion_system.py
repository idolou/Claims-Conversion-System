from utils import *
import logging


def main():
    logging.basicConfig(
        filename="file_conversion.log",
        level=logging.INFO,
        format="%(levelname)s:%(asctime)s::%(message)s",
        datefmt="%m/%d/%Y %I:%M:%S %p",
    )
    logging.info("Conversion Started")

    # Get the current directory path
    dir_path = os.path.dirname(os.path.realpath(__file__))

    # Ask the user for the input file path
    print("Please enter a file path for conversation:")
    csv_path = input()

    # Extract the merchant name for creating the output folder directory
    try:
        if csv_path.startswith("/"):
            csv_path = csv_path[1:]
            marchant_name = csv_path.split("/")[3]
        else:
            marchant_name = csv_path.split("/")[2]

        # get the absolute path of the input file
        abs_csv_path = os.path.join(dir_path, csv_path)

        # Load the CSV data into dictionaries

        raw_data, raw_data_duplicates = load_csv_to_dict(abs_csv_path)
    except Exception as e:
        print(str(e) + " - maybe the file path you entered is not valid...")
        logging.info(str(e) + " please check the input file")
        return

    # Calculate the new fields and format the data
    try:
        fields_calc_and_formatting(raw_data)
        fields_calc_and_formatting(raw_data_duplicates)
    except Exception as e:
        print("calculating new fields caused an error, please check the input file!")
        logging.warning(str(e) + " please check the input file")
        return

        # Save the data to JSON files
    dict_to_json(
        os.path.join(dir_path, "conversion_system", "Outputs", marchant_name),
        raw_data,
        "file1.json",
        "Orders",
    )
    dict_to_json(
        os.path.join(dir_path, "conversion_system", "Outputs", marchant_name),
        raw_data_duplicates,
        "file1_duplicates.json",
        "Duplicate Orders",
    )

    logging.info("Conversion Finished!")


if __name__ == "__main__":
    main()
