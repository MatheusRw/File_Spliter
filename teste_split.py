import pandas as pd

def split_excel_file(input_file, output_dir):
    df = pd.read_excel(input_file,sheet_name='TEUM')
    for i in range(0, df.shape[0], 1000):
        chunk = df[i:i+1000]
        output_file = os.path.join(output_dir, f"{i}.csv")
        chunk.to_excel(output_file)

if __name__ == "__main__":
    input_file = input("Enter the input Excel file: ")
    output_dir = input("Enter the output directory: ")
    split_excel_file(input_file, output_dir)
