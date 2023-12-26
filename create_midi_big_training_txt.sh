#!/bin/bash

csv_dir="${1:-output_dir}"
out_file="${1:-input.txt}"

for file in ${csv_dir}/*.csv; do
  echo "" >> "${out_file}"
  cat "${file}" >> "${out_file}"
done

