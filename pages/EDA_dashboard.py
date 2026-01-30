import streamlit as st
from PIL import Image
from pathlib import Path

# --------------------------------------------------
# Page config
# --------------------------------------------------
st.set_page_config(
    page_title="EDA Dashboard",
    layout="wide"
)

# --------------------------------------------------
# Paths
# --------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent
OUTPUTS_DIR = BASE_DIR / "outputs"

# --------------------------------------------------
# Helper
# --------------------------------------------------
def show_image(title, filename, insight=None):
    img_path = OUTPUTS_DIR / filename

    st.markdown(f"### {title}")

    if img_path.exists():
        st.image(Image.open(img_path))
    else:
        st.error(f"Image not found: {filename}")

    if insight:
        st.info(insight)

    st.markdown("---")

# --------------------------------------------------
# Header
# --------------------------------------------------
st.title("📊 Exploratory Data Analysis")
st.caption("Visual insights derived from the car insurance dataset")
st.markdown("---")

# --------------------------------------------------
# Target Variable
# --------------------------------------------------
st.markdown("## 🎯 Target Variable: Insurance Claim")

col1, col2 = st.columns(2)

with col1:
    show_image(
        "Count of Insurance Claims",
        "output.png",
        "The dataset is highly imbalanced, with far fewer claims compared to non-claims."
    )

with col2:
    show_image(
        "Percentage Distribution of Insurance Claims",
        "output1.png",
        "Only a small percentage of policyholders file insurance claims."
    )

# --------------------------------------------------
# Categorical EDA
# --------------------------------------------------
st.markdown("## 🧩 Categorical Feature Analysis")

show_image(
    "Car Segment Distribution & Claim Rate",
    "output2.png",
    "Certain car segments show a higher claim rate despite lower representation."
)

# --------------------------------------------------
# Numerical EDA
# --------------------------------------------------
st.markdown("## 📈 Numerical Feature Analysis")

col3, col4 = st.columns(2)

with col3:
    show_image(
        "NCAP Rating vs Insurance Claim",
        "output3.png",
        "Lower NCAP ratings are associated with a slightly higher claim tendency."
    )

    show_image(
        "Gross Weight vs Insurance Claim",
        "output4.png",
        "Heavier vehicles show marginal differences in claim behavior."
    )

    show_image(
        "Turning Radius vs Insurance Claim",
        "output5.png",
        "Turning radius shows limited direct separation between claim classes."
    )

with col4:
    show_image(
        "Engine Displacement vs Insurance Claim",
        "output6.png",
        "Mid-range engine displacement vehicles appear more frequently in claims."
    )

    show_image(
        "Population Density vs Insurance Claim",
        "output7.png",
        "Higher population density regions tend to show increased claim activity."
    )

    show_image(
        "Age of Car vs Insurance Claim",
        "output8.png",
        "Older cars show slightly higher variability in claim occurrence."
    )

show_image(
    "Age of Policyholder vs Insurance Claim",
    "output9.png",
    "Policyholder age shows overlap between claim and non-claim cases."
)

# --------------------------------------------------
# Safety Features
# --------------------------------------------------
st.markdown("## 🛡️ Safety & Assistance Features")

col5, col6 = st.columns(2)

with col5:
    show_image(
        "Brake Assist Presence",
        "output11.png",
        "Vehicles with brake assist show marginally higher claim rates, possibly due to exposure."
    )

    show_image(
        "TPMS Presence",
        "output12.png",
        "TPMS presence does not strongly differentiate claim behavior."
    )

with col6:
    show_image(
        "ESC Presence",
        "output13.png",
        "ESC-equipped vehicles still show claims, indicating multi-factor risk."
    )

    show_image(
        "Number of Airbags",
        "output14.png",
        "More airbags do not necessarily imply lower claim frequency."
    )

# --------------------------------------------------
# Geography & Mechanics
# --------------------------------------------------
st.markdown("## 🌍 Geography & Vehicle Mechanics")

show_image(
    "Area Cluster Distribution & Claim Rate",
    "output15.png",
    "Certain geographic clusters exhibit significantly higher claim rates."
)

col7, col8 = st.columns(2)

with col7:
    show_image(
        "Rear Brakes Type",
        "output16.png",
        "Rear brake type shows minimal influence on claim likelihood."
    )

with col8:
    show_image(
        "Transmission Type",
        "output17.png",
        "Transmission type shows near-identical claim rates."
    )

show_image(
    "Fuel Type Distribution & Claim Rate",
    "output18.png",
    "Fuel type shows mild variation in claim rates across categories."
)

# --------------------------------------------------
# Correlation
# --------------------------------------------------
st.markdown("## 🔗 Correlation Analysis")

show_image(
    "Correlation Heatmap (Numerical Features)",
    "output10.png",
    "Strong correlations exist among vehicle size-related features."
)
