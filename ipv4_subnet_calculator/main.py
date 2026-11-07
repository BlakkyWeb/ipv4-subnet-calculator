from subnet_calculator import calculate_subnet


def main():
    print("=" * 40)
    print("IPv4 SUBNET CALCULATOR")
    print("=" * 40)

    ip_address = input("Enter IPv4 Address: ")
    prefix = input("Enter CDIR prefix: ")

    try:
        result = calculate_subnet(ip_address, prefix)

        print("\nNETWORK INFORMATION")
        print("-" * 40)

        for key, value in result.items():
            print(f"{key}: {value}")

        print("-" * 40)

    except ValueError as error:
        print(f"\nError: {error}")


if __name__ == "__main__":
    main()