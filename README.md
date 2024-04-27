# Laptop Price Prediction

This project aims to predict the price of laptops based on various features such as brand and various specifications. The dataset used for this project is sourced from Odin School and contains information about various laptops along with their prices.

### Project Questions to Explore

#### Which features have the most significant impact on laptop prices?

In analyzing the factors influencing laptop prices, several key features emerged as significant determinants:

- **Touchscreen and IPS Display:** Laptops equipped with Touchscreen functionality and IPS display technology tend to command higher prices. These features enhance user experience and visual quality, resulting in a price premium of approximately 20% compared to laptops without these features.

- **Storage Configuration:** The type and capacity of storage components, particularly SSDs (Solid State Drives), play a crucial role in pricing. Laptops with larger SSD capacities or high-speed SSDs are often priced higher due to their faster data access and improved system responsiveness.

#### Can the model accurately predict the prices of laptops from lesser-known brands?

After conducting predictions on laptops from lesser-known brands, the model achieved an accuracy rate of approximately 50%. While this accuracy level may seem moderate, it is important to consider the context of the analysis.

The limited availability of data for lesser-known brands poses a significant challenge to the model's predictive capabilities. With fewer observations to learn from, the model may struggle to generalize effectively to unseen instances from these brands. As a result, the achieved accuracy reflects the inherent difficulty in accurately predicting prices for laptops from lesser-known brands.

Moving forward, it is crucial for the organization to continue gathering data, particularly from lesser-known brands, to improve the model's performance. With a more extensive and diverse dataset, the model can better capture the nuances and variations in laptop prices across different brands, leading to enhanced predictive accuracy.

In conclusion, while the current accuracy rate may be modest, it serves as a starting point for further refinement and improvement. By prioritizing data collection efforts and continuously refining the modeling approach, the organization can strive towards achieving higher accuracy levels in predicting prices for laptops from lesser-known brands.

#### Does the brand of the laptop significantly influence its price?

Yes, the brand of a laptop can have a significant influence on its price. Brands with a strong reputation and brand equity, such as Apple, often command premium prices for their products. This price premium is primarily attributed to factors such as brand perception, reputation for quality, and consumer loyalty.

For example, laptops with similar specifications to those offered by Apple may be available at lower price points from other brands. However, despite comparable hardware specifications, Apple laptops tend to maintain higher price tags due to the brand's perceived value and status in the market.

#### How well does the model perform on laptops with high-end specifications compared to budget laptops?

The model demonstrates superior performance when predicting prices for laptops with high-end specifications compared to budget laptops. With an accuracy exceeding 87% on high-end laptops, the model showcases its effectiveness in accurately estimating prices for premium devices.

This higher accuracy can be attributed to several factors. High-end laptops typically feature advanced components, such as powerful processors, ample RAM, dedicated graphics cards, and larger SSD storage capacities. These specifications provide more distinct patterns and correlations in the data, enabling the model to make more precise predictions.

#### What are the limitations and challenges in predicting laptop prices accurately?

The accurate prediction of laptop prices poses several limitations and challenges for models. One of the primary limitations is the availability of data. Despite efforts to collect comprehensive datasets, the quantity and quality of available data may still be insufficient to capture the full range of factors influencing laptop prices. Limited data may result in model biases, reduced predictive accuracy, and challenges in generalizing to unseen instances.

#### How does the model perform when predicting the prices of newly released laptops not present in the training dataset?

To evaluate the model's performance on predicting prices for newly released laptops, we conducted tests on a recently launched laptop not present in the training dataset. The actual price of the laptop was ₹1,02,990, while the model predicted a price of ₹1,13,281.

This outcome demonstrates the model's ability to provide reasonably accurate price predictions for laptops not included in the training dataset. Despite not having prior exposure to the specific features and specifications of the newly released laptop, the model generated a prediction close to the actual price.

## Tools and Technologies Used

- Python
- Google Colab
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn

## Dataset

The dataset used for this project contains information about laptops, including their brand, specifications, and pricing. It consists of 1273 samples and 11 features. 
The columns in the dataset are:
1. Company
2. TypeName
3. Inches
4. ScreenResolution
5. Cpu
6. Ram
7. Memory
8. Gpu
9. OpSys
10. Weight
11. Price 

## Methodology

1. **Data Collection:** 
   - The laptop dataset was sourced from Odin school in a csv format.
   
2. **Data Preprocessing:**
   - Handling missing values
   - Encoding categorical variables
   - Feature scaling
   
3. **Exploratory Data Analysis (EDA):**
   - Data visualization to understand the distribution of features
   
4. **Feature Engineering:**

   - **Screen Resolution:** 
     - Engineered features from the `ScreenResolution` column to extract additional information:
       - **IPS Display:** Created a binary column indicating whether the laptop has an IPS display.
       - **Touchscreen:** Created a binary column indicating whether the laptop has touchscreen functionality.

   - **Inches:** 
     - Engineered the `Inches` column to create a new feature:
       - **PPI (Pixels Per Inch):** Calculated the pixel density per inch of the screen.

   - **Memory (RAM):** 
     - Extracted information from the `Memory` column to create new features:
       - **SSD Size:** Extracted the size of the Solid State Drive (SSD) from the `Memory` column.
       - **HDD Size:** Extracted the size of the Hard Disk Drive (HDD) from the `Memory` column.
       - **Flash Storage Size:** Extracted the size of the Flash Storage from the `Memory` column.
       - **Hybrid Size:** Extracted the size of the Hybrid Storage from the `Memory` column.

5. **Modeling:**

   - **Algorithms Used:** 
     - Linear Regression
     - Random Forest Regressor
     - Gradient Boosting Regressor

   - **Pipeline Formats:**

     - **Linear Regression:**
       - Defined a pipeline with necessary preprocessing steps like one-hot encoding and scaling, followed by linear regression.

     - **Random Forest:**
       - Created a pipeline with preprocessing and Random Forest Regressor. Hyperparameters were tuned for optimal performance.

   - **Hyperparameter Tuning:**
     - Tuned the Random Forest model's hyperparameters using `GridSearchCV`.

   - **Model Evaluation:**
     - Evaluated model performance using metrics such as R-squared, Mean Absolute Error (MAE), and Root Mean Squared Error (RMSE).

6. **Real-time Prediction:**

   - Collected real-time laptop data from online sources like Amazon for testing model predictions.

   - Created data dictionaries representing laptops from different brands and specifications.

   - Predicted prices for real-time data using the trained model.
