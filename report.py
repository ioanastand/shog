def show(processed):

    print()

    print(

        "Scanning image collection..."

    )

    print()

    for item in processed:

        image = item["image"]

        print(image.name)

        print(

            f"Resize: {item['resize'][0]}x{item['resize'][1]} → "

            f"{item['resize'][2]}x{item['resize'][3]}"

        )

        print(

            f"Format: {item['convert'][0]} → "

            f"{item['convert'][1]}"

        )

        print()
