import pandas as pd


def clean_data(file_path):
    # Load the CSV file
    df = pd.read_csv(file_path)

    # Fill missing values
    for column in df.columns:
        if df[column].dtype == 'float64' or df[column].dtype == 'int64':
            df[column].fillna(df[column].mean(), inplace=True)
        else:
            df[column].fillna(df[column].mode()[0], inplace=True)

    # Remove duplicate rows
    df.drop_duplicates(inplace=True)

    # Example filter: Remove rows where 'Id' is less than 2
    df = df[df['Id'] >= 2]

    # Save cleaned data to a new CSV file
    df.to_csv('cleaned_data.csv', index=False)
    print("Data cleaned and saved to 'cleaned_data.csv'.")


# Replace 'your_file.csv' with the path to your CSV file
clean_data('your_file.csv')
