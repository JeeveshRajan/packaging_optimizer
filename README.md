# Packaging Optimizer for Pick & Pack Orders

## Overview
This project provides an automated solution for optimizing packaging configurations for pick & pack orders. The system calculates order volumes, selects optimal box configurations, and minimizes shipping costs by using fewer, larger boxes.

## Features
- **Volume Calculation**: Automatically calculates total volume for each order based on product dimensions
- **Box Optimization**: Selects the most efficient box configuration to minimize shipping costs
- **Weight Calculation**: Determines total shipment weight for each order
- **Efficiency Analysis**: Provides packing efficiency metrics for each order

## Data Sources
The system uses three main data sources:
1. **SKU-Pack Sizes**: Product dimensions and weights
2. **Master Boxes**: Available packaging box dimensions
3. **Orders**: Customer order details with SKUs and quantities

## Installation
1. Ensure you have Python 3.7+ installed
2. Clone or download this repository
3. No additional dependencies required (uses only Python standard library)

## Usage
Run the main script:
```bash
python packaging_optimizer.py
```

## Output
The program provides detailed analysis for each order including:
- Total order volume (cubic inches)
- Total order weight (pounds)
- Recommended box configuration
- Number of boxes required
- Packing efficiency percentage

## Example Output
```
ORDER 1
----------------------------------------
Total Order Volume: 1,728.00 cubic inches
Total Order Weight: 45.50 lbs
Number of Boxes Required: 1
Total Box Volume: 1,728.00 cubic inches
Packing Efficiency: 100.0%

Recommended Box Configuration:
  Box 1: MB-02 (12" × 12" × 12")
    Volume: 1728 cubic inches
```

## Algorithm
The optimization algorithm:
1. Calculates total volume for each order
2. Attempts to fit the order in a single box (preferring larger boxes)
3. If single box is insufficient, uses multiple boxes with 80% efficiency threshold
4. Prioritizes fewer, larger boxes over multiple smaller ones

## File Structure
```
├── packaging_optimizer.py    # Main optimization script
├── requirements.txt          # Project dependencies
└── README.md                # This file
```

## Author
Jeevesh Rajan
27-07-25

