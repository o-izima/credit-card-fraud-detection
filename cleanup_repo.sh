#!/bin/bash

set -e

echo "🔍 Checking repository size..."
git rev-list --objects --all | \
  git cat-file --batch-check='%(objecttype) %(objectname) %(objectsize) %(rest)' | \
  sort -k3 -n | tail -20

echo "🧹 Removing large files from history..."
git filter-repo --force --strip-blobs-bigger-than 50M

echo "🗂️ Enabling Git LFS..."
git lfs install
git lfs track "*.csv"
git lfs track "*.zip"
git lfs track "*.pkl"
git lfs track "*.json"

echo "📁 Cleaning working directory..."
git add .gitattributes
git add .
git commit -m "Cleanup large files and enable Git LFS" || true

echo "⬆️ Force pushing rewritten history..."
git push origin main --force

echo "🎉 Cleanup complete!"
