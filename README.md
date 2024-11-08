# LinkedIn Data ETL Project

Welcome to the **LinkedIn Data ETL Project**. This project demonstrates how to extract data from the **LinkedIn Data API**, transform it, and load it into **AWS DynamoDB**. The process involves extracting LinkedIn posts, transforming the data, and storing it in a DynamoDB table for further analysis.

## Project Overview

This ETL project works with the **LinkedIn Data API** to fetch LinkedIn posts for various users, extracts key metrics, transforms the data into a structured format, and then loads the transformed data into **AWS DynamoDB**.

### Key ETL Steps:
1. **Extract**: Fetch LinkedIn posts from user profiles using the LinkedIn Data API.
2. **Transform**: Clean, format, and structure the data.
3. **Load**: Store the transformed data in **AWS DynamoDB**.

---

## Features

- **Data Extraction**: Pulls LinkedIn posts and metrics like total reactions, comments, and author details.
- **Data Transformation**: Clean and structure the extracted data for easy querying and analysis.
- **Data Loading**: Loads the transformed data into **AWS DynamoDB**, ensuring fast, scalable storage and retrieval.

---

## Prerequisites

Ensure you have the following setup:

- **AWS Account**: You need an AWS account to set up DynamoDB.
- **Python 3.12+**
- **pip** for installing dependencies
- **AWS CLI** configured with credentials
- **DynamoDB Table**: Ensure you have created a DynamoDB table named `LinkedinPost`.

---

## Setup and Installation

### 1. Clone the GitHub Repository

Start by cloning the repository to your local machine:

```bash
git clone https://github.com/ehtisham784/ETL.git
cd ETL
