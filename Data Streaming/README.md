# Capstone Project
# Model -1 (Baseline Linear Model)

# Step1-- Data Preprocessing
1> Creating array of DataFrames to store data of 14 different locations separately.
2> Adding TimeStamp column

# Step2-- Defining Schema and creating Stream File
1> Defining schema with feautures -- Timestamp, Occupancy, Capacity
2> Creating csv file for each location which will be used for demo-strraming

# Step3-- Creating tumbling window
1> Before creating tumbling window we have to add columns 't' and 'day'
2> Creating 'price' column in delta_window where previous price is base price.
3> Here I have taken previous price as base_price because taking exact previous price will the make the price monotonically increasing along the time.

# Step 4-- Creating price_plotter and running the stream
1> Creating a price_plotter which plots graph for dynamic pricing for each parking-lot
2> Pushing all the graph in dashboard
3> Finally running the stream using pw.run()


















# Model -2 (Demand Based Price Function)

# Step 1-- Data Preprocessing
1>Creating array of dataframes which contains data for all 14 different locations. 
2>Encoding the columns like 'VehiceType' and 'TrafficConditionNearby' into integer form using mapping dictionary
3>Creating a new column named 'Demand' -- which is linear function of columns like 'Occupancy','Capacity','QueueLength','TrafficConditionNearby','IsSpecialDay' and 'VehicleType'

# Step 2-- Creating Schema and making CSV files
1> Here the schema has two feautures named Timestamp and Demand
2> For each Lot ,a csv file is created(which will be later used for stream)

# Step 3-- Creating a demo replay data of each lot
1> data_locations is created from each CSV file
2> Then columns like 't'(for timestamp) , 'day_dt'(Date at Midnight) are created

# Step 4-- Creating a delta window
1> First daily_stats window is created for computing max_demand and min_demand for a day(for each location)
2> Then finally delta_window_locations is created which uses daily_stats to compute dynamic pricing

# Step 5-- Creating price_plotter and running the stream
1> Creating a price_plotter which plots graph for dynamic pricing for each parking-lot
2> Pushing all the graph in dashboard
3> Finally running the stream using pw.run()
