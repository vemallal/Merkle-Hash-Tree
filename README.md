# Merkle Hash Tree for File Integrity

## Overview
This project implements a Merkle Hash Tree using SHA-1 hashing. It computes a Top Hash from multiple files and demonstrates how modifying a file changes the Top Hash.

## How It Works
- Each file is hashed using SHA-1
- Hashes are combined pairwise
- Final Top Hash is generated

## Input
Multiple file pathnames (supports unlimited files)

## Output
- Hash of each file
- Top Hash

## Demonstration
After modifying a file, the Top Hash changes, proving data integrity.

## Example

Before modification:
Top Hash: 59535fc6b7915842b5aca85a5091120ed8cf7e30

After modification:
Top Hash: (different value)

## Conclusion
Merkle Trees ensure data integrity by detecting changes in files.
