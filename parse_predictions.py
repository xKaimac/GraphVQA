import json

# Load JSON file
with open('./sceneGraphs/predictions.json', 'r') as file:
    data = json.load(file)

# The predictions are stored in a list under the key 'predictions'
predictions = data['predictions']

# Sort predictions by confidence score in descending order
sorted_predictions = sorted(predictions, key=lambda x: x['confidence'], reverse=True)

# Select top N predictions
top_n = 20  # ish
top_predictions = sorted_predictions[:top_n]

# Create new JSON structure
new_data = {"predictions": top_predictions}

# Save the updated JSON to a new file
with open('./sceneGraphs/test_sceneGraphs.json', 'w') as file:
    json.dump(new_data, file, indent=4)