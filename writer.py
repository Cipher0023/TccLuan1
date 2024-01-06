import pandas as pd

def write_results_to_csv(
    case_name,
    v_values,
    tc_values,
    t1_values,
    t2_values,
    tt_values,
    c1_values,
    c2_values,
    c3_values,
    kp_values
):
    df = pd.DataFrame({
        'v_values':v_values,
        'tc_values':tc_values,
        't1_values':t1_values,
        't2_values':t2_values,
        'tt_values':tt_values,
        'c1_values':c1_values,
        'c2_values':c2_values,
        'c3_values':c3_values,
        'kp_values':kp_values,
    })
    df.to_csv(f'outputs/{case_name}.csv')
    return df    