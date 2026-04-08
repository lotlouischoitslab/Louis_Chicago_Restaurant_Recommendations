import pandas as pd
import json

# 1. Load your Excel or CSV files
# If using the original Excel file, you can specify the sheet name
restaurants_df = pd.read_excel('../../02Chicago_Life/Recommended_Restaurants/Louis_Chicago_Restaurant_List.xlsx', sheet_name='Restaurants')
bakeries_df = pd.read_excel('../../02Chicago_Life/Recommended_Restaurants/Louis_Chicago_Restaurant_List.xlsx',sheet_name='Bakeries_Cafe')

# 2. Rename 'Bakery/Café' to 'Restaurants' so the keys match perfectly 
bakeries_df = bakeries_df.rename(columns={'Bakery/Café': 'Restaurants'})

# 3. Combine both dataframes into one list
combined_df = pd.concat([restaurants_df, bakeries_df], ignore_index=True)

# 4. Re-calculate the 'Index' to be sequential from 1 to the end
combined_df['Index'] = range(1, len(combined_df) + 1)

# 5. Ensure Price and Ratings are numeric for your website logic [cite: 35, 63]
combined_df['Price $'] = pd.to_numeric(combined_df['Price $'], errors='coerce').fillna(0)
combined_df['Ratings (/5)'] = pd.to_numeric(combined_df['Ratings (/5)'], errors='coerce').fillna(0)

# 6. Convert to the list of dictionaries (JSON)
final_json = combined_df.to_dict(orient='records')

# 7. Save to a file
with open('combined_restaurants.json', 'w', encoding='utf-8') as f:
    json.dump(final_json, f, indent=2, ensure_ascii=False)

print(f"Successfully combined {len(combined_df)} entries into combined_restaurants.json!")