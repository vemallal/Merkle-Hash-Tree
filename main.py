import hashlib

files = [f for f in os.listdir() if f.endswith(".txt")]

def hash_file(filename):
    with open(filename, "rb") as f:
        return hashlib.sha1(f.read()).hexdigest()

def build_merkle_tree(hashes):
    while len(hashes) > 1:
        new_hashes = []

        for i in range(0, len(hashes), 2):
            if i + 1 < len(hashes):
                combined = hashes[i] + hashes[i+1]
            else:
                combined = hashes[i]

            new_hash = hashlib.sha1(combined.encode()).hexdigest()
            new_hashes.append(new_hash)

        hashes = new_hashes

    return hashes[0]

files = ["file1.txt", "file2.txt", "file3.txt", "file4.txt"]

hashes = []
for file in files:
    file_hash = hash_file(file)
    print(file, "hash:", file_hash)
    hashes.append(file_hash)

top_hash = build_merkle_tree(hashes)

print("\nTop Hash:", top_hash)
