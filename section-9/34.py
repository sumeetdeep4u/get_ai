# Import required libraries
import streamlit as st                     # Streamlit for web UI components
import pandas as pd                        # Pandas for data manipulation
from sklearn import datasets               # To load sample datasets (like Iris)
from sklearn.ensemble import RandomForestClassifier  # ML algorithm for classification

# ---------------------------------------------------------
# Function to load and cache the Iris dataset
# ---------------------------------------------------------
@st.cache_data  # Caches data to avoid reloading it every time the app reruns
def load_data():
    iris = datasets.load_iris()  # Load the built-in Iris dataset from sklearn
    # Convert the data into a pandas DataFrame for easier manipulation
    df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    # Create a pandas Series for target labels (species)
    target = pd.Series(iris.target)
    # Return features (df), target labels, and target names (species names)
    return df, target, iris.target_names

# Load the cached dataset
df, target, target_names = load_data()

# ---------------------------------------------------------
# Train the Random Forest model
# ---------------------------------------------------------
# Initialize the RandomForestClassifier with default parameters
model = RandomForestClassifier()
# Fit (train) the model using all the data
model.fit(df, target)

# ---------------------------------------------------------
# Streamlit App UI Components
# ---------------------------------------------------------
st.title("🌼 Iris Flower Prediction App (Streamlit + ML)")  # Title at the top of the app
st.write("Adjust the sliders below to predict the Iris flower species using a trained Random Forest model.")

# Sidebar section for user input
st.sidebar.header("Input Features")  # Sidebar title

# ---------------------------------------------------------
# Create interactive sliders for user input (each feature)
# ---------------------------------------------------------
# Each slider lets the user choose a value within the dataset's min/max range
sepal_length = st.sidebar.slider(
    'Sepal Length (cm)',
    float(df['sepal length (cm)'].min()),  # Minimum slider value
    float(df['sepal length (cm)'].max())   # Maximum slider value
)

sepal_width = st.sidebar.slider(
    'Sepal Width (cm)',
    float(df['sepal width (cm)'].min()),
    float(df['sepal width (cm)'].max())
)

petal_length = st.sidebar.slider(
    'Petal Length (cm)',
    float(df['petal length (cm)'].min()),
    float(df['petal length (cm)'].max())
)

petal_width = st.sidebar.slider(
    'Petal Width (cm)',
    float(df['petal width (cm)'].min()),
    float(df['petal width (cm)'].max())
)

# Combine user-selected values into a list for prediction
input_features = [[sepal_length, sepal_width, petal_length, petal_width]]

# ---------------------------------------------------------
# Make a prediction using the trained model
# ---------------------------------------------------------
prediction = model.predict(input_features)          # Predicts numeric class (0, 1, or 2)
predicted_species = target_names[prediction[0]]     # Maps numeric prediction to species name

# ---------------------------------------------------------
# Display prediction results in the app
# ---------------------------------------------------------
st.subheader("🔍 Predicted Iris Species")            # Subheader for clarity
st.success(f"**{predicted_species}**")              # Display the predicted species in a green box

# Show the numeric feature values entered by the user
st.write("### Input Feature Values:")
# Display them in a formatted table using pandas DataFrame
st.dataframe(pd.DataFrame(input_features, columns=df.columns))


# --------------------------------------------
# Footer Notes
# --------------------------------------------
st.markdown("""
---
**Notes:**
- Uses `@st.cache_data` for optimized data loading.
- Demonstrates an end-to-end machine learning app using Streamlit.
- Random Forest Classifier predicts the Iris species in real-time.
""")
