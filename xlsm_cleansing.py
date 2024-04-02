import pandas as pd

def clean_xlsm_data(file_path, output_path):
    # Load the XLSM file
    df = pd.read_excel(file_path, engine='openpyxl')

    # Fill missing values
    # For numerical columns, fill with the mean. For categorical, fill with the mode.
    for column in df.columns:
        if df[column].dtype == 'float64' or df[column].dtype == 'int64':
            df[column].fillna(df[column].mean(), inplace=True)
        else:
            df[column].fillna(df[column].mode()[0], inplace=True)

    # Remove duplicate rows
    df.drop_duplicates(inplace=True)

    # Save cleaned data to a new XLSM file
    with pd.ExcelWriter(output_path, engine='openpyxl') as writer:
        df.to_excel(writer, index=False)

    print(f"Data cleaned and saved to '{output_path}'.")


# Example usage
clean_xlsm_data('your_data.xlsm', 'cleaned_data.xlsm')