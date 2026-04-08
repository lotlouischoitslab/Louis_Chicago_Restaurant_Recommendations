import pandas as pd
import json


# 1. Load your Excel file
# Suggestion: If the script is in the same folder as the Excel, just use the filename
file_path = '../../02Chicago_Life/Recommended_Restaurants/Louis_Chicago_Restaurant_List.xlsx'
restaurants_df = pd.read_excel(file_path, sheet_name='Restaurants')
bakeries_df = pd.read_excel(file_path, sheet_name='Bakeries_Cafe')

# 2. Rename 'Bakery/Café' to 'Restaurants' so the keys match perfectly 
bakeries_df = bakeries_df.rename(columns={'Bakery/Café': 'Restaurants'})

# 3. Combine both dataframes into one list
combined_df = pd.concat([restaurants_df, bakeries_df], ignore_index=True)

# 4. Re-calculate the 'Index' to be sequential from 1 to the end
combined_df['Index'] = range(1, len(combined_df) + 1)

# 5. Clean numeric columns (This handles your "NA" values)
combined_df['Price $'] = pd.to_numeric(combined_df['Price $'], errors='coerce').fillna(0)
combined_df['Ratings (/5)'] = pd.to_numeric(combined_df['Ratings (/5)'], errors='coerce').fillna(0)

# 6. ADD THIS LINE: Fill all other empty cells with an empty string ""
# Without this, empty cells become "NaN", which will break your Javascript
combined_df = combined_df.fillna('')

# 7. Convert to the list of dictionaries (JSON)
final_json = combined_df.to_dict(orient='records')

# 8. Save to a file
with open('combined_restaurants.json', 'w', encoding='utf-8') as f:
    json.dump(final_json, f, indent=2, ensure_ascii=False)

print(f"Successfully combined {len(combined_df)} entries into combined_restaurants.json!")