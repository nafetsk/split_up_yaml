import pandas as pd
import yaml

def split_yaml(input_file_name):
    """Split a YAML file into multiple YAML files."""
    
    # Load YAML data
    with open(input_file_name, 'r') as file:
        data = yaml.safe_load(file)

    # Convert data to DataFrames
    provided_df = pd.DataFrame(data['inputs']['provided'])
    assumed_df = pd.DataFrame(data['inputs']['assumed'])
    output_df = pd.DataFrame(data['outputs'])

    # Split DataFrames into five separate DataFrames
    provided_dfs = [provided_df.iloc[i:i+1] for i in range(len(provided_df))]
    assumed_dfs = [assumed_df.iloc[i:i+1] for i in range(len(assumed_df))]
    output_dfs = [output_df.iloc[i:i+1] for i in range(len(output_df))]

    # Save each set of DataFrames as separate YAML files
    for i, (provided_split, assumed_split, output_split) in enumerate(zip(provided_dfs, assumed_dfs, output_dfs)):
        output_data = {
            'inputs': {'provided': provided_split.to_dict(orient='list'), 'assumed': assumed_split.to_dict(orient='list')},
            'outputs': output_split.to_dict(orient='list')
        }
        output_file_name = f'{input_file_name} output_{i + 1}.yaml'

        with open(output_file_name, 'w') as output_file:
            yaml.dump(output_data, output_file, default_flow_style=False)

