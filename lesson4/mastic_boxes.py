TOTAL_MASTIC_WEIGHT: int = 185
SMALL_BOX_WEIGHT: int = 15
MIDDLE_BOX_WEIGHT: int = 17
LARGE_BOX_WEIGHT: int = 21

combinations_count: int = 0

for small_boxes in range(0, TOTAL_MASTIC_WEIGHT // SMALL_BOX_WEIGHT + 1):
    for middle_boxes in range(0, TOTAL_MASTIC_WEIGHT // MIDDLE_BOX_WEIGHT + 1):
        for large_boxes in range(0, TOTAL_MASTIC_WEIGHT // LARGE_BOX_WEIGHT + 1):
            if small_boxes * SMALL_BOX_WEIGHT +\
                    middle_boxes * MIDDLE_BOX_WEIGHT +\
                    large_boxes * LARGE_BOX_WEIGHT == TOTAL_MASTIC_WEIGHT:
                combinations_count += 1
                print(f"{small_boxes} * 15 + {middle_boxes} * 17 + {large_boxes} * 21 = {TOTAL_MASTIC_WEIGHT}")

print(f"{combinations_count} ways exist to collect {TOTAL_MASTIC_WEIGHT} kg of mastic.")
