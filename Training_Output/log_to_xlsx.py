import pandas as pd
import json
import matplotlib.pyplot as plt  # Import matplotlib for plotting
import os

def convert_log_to_xlsx(log_file_path, xlsx_file_path, plot_graphs=False):
    """
    Converts a log file in JSON format to an XLSX file using pandas, and optionally plots graphs.

    Args:
        log_file_path (str): The path to the log file.
        xlsx_file_path (str): The path to the output XLSX file.
        plot_graphs (bool, optional): Whether to plot graphs. Defaults to False.
    """
    try:
        # Read the log file
        with open(log_file_path, 'r') as f:
            log_data = f.readlines()  # Read each line

        # Parse each line as JSON and store in a list
        data = []
        for line in log_data:
            try:
                data.append(json.loads(line))
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON: {e}, for line: {line.strip()}")
                #  Skip the invalid line
                continue

        # Create a pandas DataFrame from the list of dictionaries
        df = pd.DataFrame(data)

        # Write the DataFrame to an XLSX file
        # df.to_excel(xlsx_file_path, index=False, engine='openpyxl')

        # print(f"Successfully converted log file to XLSX: {xlsx_file_path}")

        if plot_graphs:
            # Ensure the output directory exists
            output_dir = os.path.dirname(xlsx_file_path)
            if output_dir and not os.path.exists(output_dir):
                os.makedirs(output_dir)

            # Plotting
            plt.figure(figsize=(10, 6))  # Adjust figure size as needed
            plt.plot(df['epoch'], df['train_predict_loss'], marker='.', linestyle='-', color='blue')
            plt.title('Epoch vs. Train Predict Loss')
            plt.xlabel('Epoch')
            plt.ylabel('Train Predict Loss')
            plt.grid(True)
            plt.tight_layout()  # Adjust layout to prevent labels from overlapping
            plt.savefig(os.path.join(output_dir, 'epoch_vs_train_predict_loss.png'))  # Save the plot
            plt.close() # Close to prevent display issues in some environments

            plt.figure(figsize=(10, 6))
            plt.plot(df['epoch'], df['train_edge_loss'], marker='.', linestyle='-', color='red')
            plt.title('Epoch vs. Train Edge Loss')
            plt.xlabel('Epoch')
            plt.ylabel('Train Edge Loss')
            plt.grid(True)
            plt.tight_layout()
            plt.savefig(os.path.join(output_dir, 'epoch_vs_train_edge_loss.png'))
            plt.close()

            # # Example of plotting 'epoch' against 'test_average_f1' if it exists
            # if 'test_average_f1' in df.columns:
            #     plt.figure(figsize=(10, 6))
            #     plt.plot(df['epoch'], df['test_average_f1'], marker='', linestyle='-', color='green')
            #     plt.title('Epoch vs. Test Average F1')
            #     plt.xlabel('Epoch')
            #     plt.ylabel('Test Average F1')
            #     plt.grid(True)
            #     plt.tight_layout()
            #     plt.savefig(os.path.join(output_dir, 'epoch_vs_test_average_f1.png'))
            #     plt.close()
            # print("Graphs saved to the same directory as the XLSX file.")

    except FileNotFoundError:
        print(f"Error: Log file not found at {log_file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Specify the paths
    log_file_path = "output_dir/log.txt"  # Replace with your log file
    xlsx_file_path = "Training_Output/training.xlsx"  # Replace with your desired XLSX file name
    plot_graphs = True # Set this to True to generate graphs

    convert_log_to_xlsx(log_file_path, xlsx_file_path, plot_graphs)


# import pandas as pd
# import matplotlib.pyplot as plt
# import io
# import base64

# def generate_graph_from_xlsx(file_content, output_format='png'):
#     """
#     Generates a line graph from an XLSX file, with 'epochs' on the x-axis
#     and other columns on the y-axis.  Saves the graph to a file.

#     Args:
#         file_content (bytes): The content of the XLSX file.
#         output_format (str, optional):  The format to save the graph.
#             Defaults to 'png'.  Other options are 'jpg', 'jpeg', 'svg', etc.
#             See https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.savefig.html
#             for a complete list.

#     Returns:
#         str:  The filename the graph was saved to, or an error message.
#     """
#     try:
#         # Read the XLSX file from the provided bytes
#         df = pd.read_excel(io.BytesIO(file_content))

#         # Lowercase all column names for case-insensitivity
#         df.columns = df.columns.str.lower()

#         # Check if 'epochs' column exists
#         if 'epoch' not in df.columns:
#             return "Error: Column 'epochs' not found. Please make sure your XLSX file has a column named 'epochs'."

#         # Set 'epochs' as the x-axis
#         x = df['epoch']

#         # Create the plot
#         plt.figure(figsize=(10, 6))  # Adjust figure size
#         plt.xlabel('Epochs')
#         plt.ylabel('Values')
#         plt.title('Data from XLSX File')

#         # Plot each column (except 'epochs') as a separate line
#         for column in df.columns:
#             if column != 'epoch':
#                 plt.plot(x, df[column], label=column)

#         plt.legend()
#         plt.grid(True)

#         # Save the plot to a file
#         filename = f"graph_from_xlsx.{output_format.lower()}"
#         plt.savefig(filename, format=output_format.lower())
#         plt.close()
#         return filename

#     except Exception as e:
#         return f"Error: An error occurred while processing the file: {str(e)}"

# if __name__ == "__main__":
#     # Example usage:
#     # 1.  Read the XLSX file.
#     # 2.  Call the function to generate and save the graph.
#     # 3.  Print the filename.

#     # Replace 'your_file.xlsx' with the actual path to your XLSX file.
#     try:
#         with open('Training_Output/training.xlsx', 'rb') as f:
#             file_content = f.read()
#     except FileNotFoundError:
#         print("Error: Please make sure you have a file named 'your_file.xlsx' in the same directory as this script, or change the filename in the script.")
#         exit()

#     # Generate and save as PNG (default)
#     output_file_png = generate_graph_from_xlsx(file_content)
#     if "Error:" in output_file_png:
#         print(output_file_png)
#     else:
#         print(f"Graph saved as: {output_file_png}")

#     # Generate and save as JPG
#     output_file_jpg = generate_graph_from_xlsx(file_content, output_format='jpg')
#     if "Error:" in output_file_jpg:
#         print(output_file_jpg)
#     else:
#         print(f"Graph saved as: {output_file_jpg}")

