import argparse
from utils.file_handler import save_data, load_data
from models.user import User

def main():
    parser = argparse.ArgumentParser(description="Project Management CLI")
    subparsers = parser.add_subparsers(dest="command")

    user_parser = subparsers.add_parser('add-user')
    user_parser.add_argument('--name', required=True)
    user_parser.add_argument('--email', required=True)

    args = parser.parse_args()
    data = load_data()

    if args.command == 'add-user':
        new_user = User(args.name, args.email)
        data['users'].append(new_user.to_dict())
        save_data(data)
        print(f"User {args.name} added successfully!")

if __name__ == "__main__":
    main()