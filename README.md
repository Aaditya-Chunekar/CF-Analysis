# Codeforces Analysis App

A Streamlit web application that analyzes Codeforces competitive programming ratings and identifies "valleys" in a user's rating progression.

## Features

- **Rating Visualization**: View your rating progression over contests with interactive charts
- **Valley Detection**: Automatically identifies rating "valleys" - drops followed by recoveries
- **Comeback Analysis**: Calculates your comeback ratio to see how well you recover from rating drops
- **Dual Chart View**: Compare rating trends and rating-to-contest ratios side by side

## What are Rating Valleys?

A "valley" occurs when:
1. Your rating drops in one contest (oldRating > newRating)
2. Your rating rises in the next contest (oldRating < newRating)

The app highlights valleys in two colors:
- 🟩 **Green**: Good valleys where you gained more than you lost (Rise > Fall)
- 🟥 **Red**: Bad valleys where you lost more than you gained (Fall > Rise)

## Installation

1. Clone this repository
2. Install required dependencies:
```bash
pip install streamlit requests pandas
```

## Usage

1. Run the Streamlit app:
```bash
streamlit run app.py
```

2. Enter your Codeforces username in the text input field
3. View your rating analysis including:
   - Rating progression chart
   - Rating/Contest number ratio chart
   - Detected valleys table with comeback statistics

## Requirements

- Python 3.7+
- streamlit
- requests
- pandas

## Data Source

The app fetches data from the official Codeforces API:
- Endpoint: `https://codeforces.com/api/user.rating?handle={username}`
- Requires at least 3 contest participations for analysis

## Features Breakdown

### Charts
- **Ratings Over Contests**: Shows your rating progression across all contests
- **Rating/Contest Number**: Shows the ratio of your rating to contest number, useful for tracking improvement efficiency

### Valley Analysis Table
- **Turning Points**: Contest where you recovered from a valley
- **Pre-Valley**: Your rating before the drop
- **Valley**: Your lowest rating in the valley
- **Post-Valley**: Your rating after recovery
- **Fall**: How much rating you lost
- **Rise**: How much rating you gained back
- **Comeback Ratio**: Overall ratio of successful recoveries

## Error Handling

The app includes robust error handling for:
- Invalid usernames
- Network connectivity issues
- API unavailability
- Insufficient contest data

## Contributing

Feel free to submit issues and enhancement requests!
