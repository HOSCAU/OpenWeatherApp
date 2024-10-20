# Real-Time Data Processing System for Weather Monitoring

## Overview

This project is a Real-Time Data Processing System designed to monitor weather data for major metro cities in India. It utilizes FastAPI for the backend, retrieves data from the OpenWeatherMap API, and implements rollups and aggregates for efficient data management. The system provides additional weather parameters, historical data support, forecasts, and sophisticated alert mechanisms.

## Features

- **Real-Time Data Retrieval:** Fetches current weather data from the OpenWeatherMap API.
- **Rollups and Aggregates:** Implements efficient data rollup and aggregation techniques.
- **Historical Data Support:** Stores and retrieves historical weather data.
- **Forecasting:** Provides weather forecasts based on retrieved data.
- **Alerts:** Sophisticated alert mechanisms based on specific weather conditions.

## Tech Stack

- **Backend:** FastAPI
- **Database:** sqlalchemy
- **API:** OpenWeatherMap API

## Getting Started

### Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.12.4 or higher

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/HOSCAU/Real-Time-Weather-Monitoring.git
   cd Real-Time-Weather-Monitoring
