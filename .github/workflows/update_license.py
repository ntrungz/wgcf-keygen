import toml
import sys

def update_license_key(file_path, new_key):
    # Load existing TOML file
    config = toml.load(file_path)

    # Update the license_key
    config['license_key'] = new_key

    # Save the updated TOML file
    with open(file_path, 'w') as f:
        toml.dump(config, f)

if __name__ == "__main__":
    file_path = 'wgcf-account.toml'
    new_key = sys.argv[1] if len(sys.argv) > 1 else ''
    if new_key:
        update_license_key(file_path, new_key)
    else:
        print("No WARP_KEY provided, skipping update.")
