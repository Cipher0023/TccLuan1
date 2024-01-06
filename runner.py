import pandas as pd
from app import run_main_from_str
            
def run_from_csv(csv_file):
    df = pd.read_csv(csv_file)
    i = 0
    for ele, row in df.iterrows():
        input_str = "{}".format(str(row['x1']),)
        run_main_from_str(input_str)
        i+=1
        print(f"Runned {i} cases")
            
        if __name__ == "__main__":
            run_from_csv('inputs.csv')
