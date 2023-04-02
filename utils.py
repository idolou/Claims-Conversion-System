from constants import *
from collections import defaultdict
import os
import pandas as pd
from datetime import datetime, timedelta
import json


def dict_to_json(json_path, data, file_name, print_arg):
    """
    This function will convert a list of dictionaries to a JSON file

    
    Args:
        json_path (string): path to the output folder
        data (list): list of dictionaries
        file_name (string): name of the output file
        print_arg (string): used for printing the confirmation message
    
    Returns:
        None
    """
    # Construct path and create directories if they don't exist
    directory = os.path.join(json_path, file_name)
    os.makedirs(os.path.dirname(directory), exist_ok=True)

    # Write JSON data to file
    with open(directory, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    # Print confirmation message
    print(f"The converted {print_arg} JSON file is located at:\n{directory}")


def date_converter(string_date, date_format):
    """
    This function will convert a string date to a datetime object and add 3 days to it.
    It will then format the dates in 'YYYY-MM-DD' format and return them as a tuple.
    
    Args:
        string_date (string): date in string format
        date_format (string): date format

    Returns:
        tuple: formatted_date, processed_date
    """
    # Convert the string date to datetime object using the given date format
    datetime_obj = datetime.strptime(string_date, date_format)

    # Add 3 days to the date
    new_date = datetime_obj + timedelta(days=3)

    # Format the dates in 'YYYY-MM-DD' format
    formatted_date = datetime_obj.strftime("%Y-%m-%d")
    processed_date = new_date.strftime("%Y-%m-%d")

    return formatted_date, processed_date


def load_csv_to_dict(path, errDict=False):
    """
    this function will convert a csv file to a list of dictionaries
    Args:
        path (string): path to csv file
        reasonMap (bool, optional): _description_. Defaults to False - will use for the error dictionary

    Returns:
        2 lists of dictionaries: each dictionary is a row in the csv file
    """
    dict_data = {}
    dict_data_duplicates = {}
    dict_reason_code = {}
    with open(path, encoding="utf-8") as f:
        try:
            df = pd.read_csv(f)
            # Create dictionary mapping reason codes and processors to reason categories
            if errDict:
                for _, row in df.iterrows():
                    # change for abreaviation of AMEX for comapatibility with the other data
                    processor = (
                        "AMEX"
                        if row["Processor"] == "AMERICAN_EXPRESS"
                        else row["Processor"]
                    )
                    key = (row["OrderID"], processor)
                    dict_reason_code[key] = row[2]
                return dict_reason_code
            # Create two dictionaries for the data, one for regular orders and one for duplicates
            else:
                for _, row in df.iterrows():
                    key = row["OrderID"]
                    if key not in dict_data:
                        format_numeric_fields(key, dict_data, row)
                    else:
                        format_numeric_fields(key, dict_data_duplicates, row)
        except Exception as e:
            print(f"Error: {e}")
            return e

    return list(dict_data.values()), list(dict_data_duplicates.values())


def format_numeric_fields(key, dict_data, order):
    """
    Helper function for processing data read from the CSV file. It formats the data and adds it to the dictionary.

    Args:
        key (int): the orderID
        dict_data (dictionary): the data dictionary
        order (pandas.core.series.Series): a row in the dataframe
    
    Returns:
        None
    """
    data = defaultdict(int, order.to_dict())
    amount = data["Amount"]
    reason_code = data["ReasonCode"]

    # format reason code and amount
    data["ReasonCode"] = int(reason_code) if reason_code % 1 == 0 else reason_code
    data["Amount"] = int(amount) if amount % 1 == 0 else amount

    # add formatted data to the dictionary
    dict_data[key] = data


def fields_calc_and_formatting(data):
    """
     This function will calculate the new fields for the data
     such as: ReasonCategory, AmountUSD, ProcessingDate
    Args:
        data (list of dictionaries): list of dictionaries of the data
    
    Returns:
        None
    """
    # loop through the data, format all date formats and calculate the new fields
    for row in data:
        try:

            format_key = (row["MerchantName"], row["ProcessorName"])
            # get the date format and currency format for the current merchant and processor
            date_format, currency_format = data_formartting_dict[format_key]

            # format the DeliveryDate by the input formatting
            row["DeliveryDate"] = date_converter(row["DeliveryDate"], date_format)[0]

            # format the OrderDate by the input formatting and get the processing date by adding 3 days
            original_order_date, new_date = date_converter(
                row["OrderDate"], date_format
            )
            row["OrderDate"] = original_order_date

            # format the amount by the currency format
            format_amount = row["Amount"] * currency_format
            row["Amount"] = (
                int(format_amount) if format_amount % 1 == 0 else format_amount
            )

            # calculate the new fields
            row["ReasonCategory"] = error_dict[
                (row["ReasonCode"], row["ProcessorName"])
            ]
            new_amount = row["Amount"] / currency_rate_dict.get(row["Currency"], 1)
            row["AmountUSD:"] = int(new_amount) if new_amount % 1 == 0 else new_amount
            row["ProcessingDate"] = new_date
        except Exception as e:
            print(f"Error: {e}")
            return e
