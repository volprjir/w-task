from common.file_handler import process_file_content

from task1 import config, radius_math


def _should_exit(input: str):
    if input == "q":
        exit()


def main():
    # check if file as DB is already generated
    data = process_file_content(config.DATA_PATH)
    validation = {"postcode": False, "radius": False}

    while not validation["postcode"]:
        postcode = input("Please enter postcode:\n")
        _should_exit(postcode)
        if len(postcode) > 6:
            # not sure if the UK postcode could be longer - if I had more time, I'd study it more and used proper regex validation
            validation["postcode"] = True
        else:
            print(
                "You have entered invalid postcode. Try again or write q to end program"
            )

    while not validation["radius"]:
        try:
            # API limits to 1999
            raw_radius = input("Enter radius in decimal metres\n")
            _should_exit(raw_radius)
            radius = int(raw_radius)
            validation["radius"] = True
        except Exception as e:
            # dummy ignore validation
            print("Invalid value for radius")
            validation["radius"] = True

    stores_close_by_postcode = radius_math.get_close_stores(data, postcode, radius)

    if stores_close_by_postcode:
        print(f"The closest stores to {postcode}:")
        for store in stores_close_by_postcode:
            print(f"{store.name} - {store.postcode}")
    else:
        print(f"No stores found close to {postcode}")


if __name__ == "__main__":
    main()
