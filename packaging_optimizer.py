#!/usr/bin/env python3
# Packaging Optimizer for Pick & Pack Orders
# This program helps optimize packaging for orders by calculating volumes and selecting best boxes

# Product data - dimensions in inches, weight in pounds
products = {
    "KS001": {"name": "Square Plate (10\" Inch) - Pk of 25", "length": 10, "width": 10, "height": 4, "weight": 3.50},
    "KS002": {"name": "Square Plate (9\" Inch) - Pk of 50", "length": 9, "width": 9, "height": 8, "weight": 7.00},
    "KS003": {"name": "Round Plate (10\" Inch) - Pk of 25", "length": 10, "width": 10, "height": 4, "weight": 3.25},
    "KS004": {"name": "Round Plate (9\" Inch) - Pk of 50", "length": 9, "width": 9, "height": 8, "weight": 6.50},
    "KS005": {"name": "Round Plate (8\" Inch) - Pk of 50", "length": 8, "width": 8, "height": 8, "weight": 5.50},
    "KS008": {"name": "Rectangle Plate (11\"x7\" Inch) - Pk of 25", "length": 11, "width": 7, "height": 4, "weight": 4.00},
    "KS009": {"name": "Oval Tray (15\"x10\") - Pk of 10", "length": 15, "width": 10, "height": 2, "weight": 2.50},
    "KS010": {"name": "Oval Tray (18\"x12\") - Pk of 10", "length": 18, "width": 12, "height": 2, "weight": 3.50},
    "KS011": {"name": "Oval Tray (20\"x14\") - Pk of 10", "length": 20, "width": 14, "height": 2, "weight": 4.50},
    "KS012": {"name": "Round Mini Bowl (6\" Inch) - Pk of 50", "length": 6, "width": 6, "height": 6, "weight": 4.00},
    "KS013": {"name": "Round Mini Bowl (8\" Inch) - Pk of 25", "length": 8, "width": 8, "height": 6, "weight": 3.50},
    "KS014": {"name": "Round Mini Bowl (10\" Inch) - Pk of 25", "length": 10, "width": 10, "height": 6, "weight": 4.50},
    "KS015": {"name": "Oval Tray (22x12\" Inch) - Pk of 10", "length": 22, "width": 12, "height": 2, "weight": 4.40},
    "KS016": {"name": "Round Plate - 2 Partition (10\" Inch) - Pk of 25", "length": 10, "width": 10, "height": 4, "weight": 3.25},
    "KS017": {"name": "Round Plate - 3 Partition (10\" Inch) - Pk of 25", "length": 10, "width": 10, "height": 4, "weight": 3.38},
    "KS018": {"name": "Round Plate - 4 Partition (10\" Inch) - Pk of 25", "length": 10, "width": 10, "height": 4, "weight": 3.50},
    "KS019": {"name": "Round Plate - 6 Partition (10\" Inch) - Pk of 25", "length": 10, "width": 10, "height": 4, "weight": 3.75},
    "KS020": {"name": "Round Plate - 8 Partition (10\" Inch) - Pk of 25", "length": 10, "width": 10, "height": 4, "weight": 4.00},
}

# Master boxes available - dimensions in inches
master_boxes = [
    {"id": "MB-01", "length": 10, "width": 10, "height": 10, "volume": 1000},
    {"id": "MB-02", "length": 12, "width": 12, "height": 12, "volume": 1728},
    {"id": "MB-03", "length": 16, "width": 12, "height": 10, "volume": 1920},
    {"id": "MB-04", "length": 16, "width": 16, "height": 12, "volume": 3072},
    {"id": "MB-05", "length": 24, "width": 14, "height": 4, "volume": 1344},
    {"id": "MB-06", "length": 24, "width": 14, "height": 12, "volume": 4032},
]

# Order data
orders = [
    {"order_id": 1, "items": [{"sku": "KS001", "quantity": 1}, {"sku": "KS013", "quantity": 4}, {"sku": "KS005", "quantity": 4}]},
    {"order_id": 2, "items": [{"sku": "KS015", "quantity": 4}, {"sku": "KS020", "quantity": 2}]},
    {"order_id": 3, "items": [{"sku": "KS011", "quantity": 4}, {"sku": "KS010", "quantity": 2}, {"sku": "KS014", "quantity": 2}, {"sku": "KS003", "quantity": 2}]},
    {"order_id": 4, "items": [{"sku": "KS009", "quantity": 4}, {"sku": "KS012", "quantity": 2}, {"sku": "KS019", "quantity": 2}]},
    {"order_id": 5, "items": [{"sku": "KS002", "quantity": 1}, {"sku": "KS004", "quantity": 8}, {"sku": "KS016", "quantity": 2}, {"sku": "KS017", "quantity": 2}, {"sku": "KS012", "quantity": 2}, {"sku": "KS018", "quantity": 2}]},
]

def calculate_order_volume(order):
    """Calculate total volume for an order"""
    total_volume = 0
    for item in order["items"]:
        sku = item["sku"]
        quantity = item["quantity"]
        if sku in products:
            product = products[sku]
            pack_volume = product["length"] * product["width"] * product["height"]
            total_volume += pack_volume * quantity
    return total_volume

def calculate_order_weight(order):
    """Calculate total weight for an order"""
    total_weight = 0
    for item in order["items"]:
        sku = item["sku"]
        quantity = item["quantity"]
        if sku in products:
            product = products[sku]
            total_weight += product["weight"] * quantity
    return total_weight

def find_best_boxes(order_volume):
    """Find the best box configuration for given volume"""
    # Sort boxes by volume (largest first)
    sorted_boxes = sorted(master_boxes, key=lambda x: x["volume"], reverse=True)
    
    # Try to fit in single box first
    for box in sorted_boxes:
        if order_volume <= box["volume"]:
            return [box]
    
    # If no single box fits, use multiple boxes
    selected_boxes = []
    remaining_volume = order_volume
    
    # Use largest boxes first to minimize count
    for box in sorted_boxes:
        while remaining_volume > 0 and remaining_volume >= box["volume"] * 0.8:  # 80% efficiency
            selected_boxes.append(box)
            remaining_volume -= box["volume"]
    
    # Add smallest box that fits remaining volume
    if remaining_volume > 0:
        for box in sorted_boxes:
            if remaining_volume <= box["volume"]:
                selected_boxes.append(box)
                break
    
    return selected_boxes

def analyze_order(order):
    """Analyze a single order and return results"""
    volume = calculate_order_volume(order)
    weight = calculate_order_weight(order)
    boxes = find_best_boxes(volume)
    
    # Calculate efficiency
    total_box_volume = sum(box["volume"] for box in boxes)
    efficiency = (volume / total_box_volume * 100) if total_box_volume > 0 else 0
    
    return {
        "order_id": order["order_id"],
        "volume": volume,
        "weight": weight,
        "boxes": boxes,
        "box_count": len(boxes),
        "total_box_volume": total_box_volume,
        "efficiency": efficiency
    }

def print_results(results):
    """Print the results in a nice format"""
    print("=" * 70)
    print("PACKAGING OPTIMIZATION RESULTS")
    print("=" * 70)
    print()
    
    for result in results:
        print(f"ORDER {result['order_id']}")
        print("-" * 35)
        print(f"Total Volume: {result['volume']:.0f} cubic inches")
        print(f"Total Weight: {result['weight']:.1f} lbs")
        print(f"Boxes Needed: {result['box_count']}")
        print(f"Box Volume: {result['total_box_volume']:.0f} cubic inches")
        print(f"Efficiency: {result['efficiency']:.1f}%")
        print()
        
        if result['boxes']:
            print("Recommended Boxes:")
            for i, box in enumerate(result['boxes'], 1):
                print(f"  Box {i}: {box['id']} ({box['length']}\" x {box['width']}\" x {box['height']}\")")
        else:
            print("No suitable boxes found!")
        
        print()
        print("=" * 70)
        print()

def main():
    """Main function"""
    print("Packaging Optimizer for Pick & Pack Orders")
    print("=" * 50)
    print()
    
    # Analyze all orders
    results = []
    for order in orders:
        result = analyze_order(order)
        results.append(result)
    
    # Print results
    print_results(results)
    
    # Print summary
    print("SUMMARY")
    print("-" * 20)
    total_boxes = sum(r['box_count'] for r in results)
    total_weight = sum(r['weight'] for r in results)
    avg_efficiency = sum(r['efficiency'] for r in results) / len(results)
    
    print(f"Total Orders: {len(results)}")
    print(f"Total Boxes: {total_boxes}")
    print(f"Total Weight: {total_weight:.1f} lbs")
    print(f"Avg Efficiency: {avg_efficiency:.1f}%")
    print()
    print("Done!")

if __name__ == "__main__":
    main() 