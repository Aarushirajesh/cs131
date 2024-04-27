input_file="Global YouTube Statistics.csv"
output_dir="Worsksheet5/United States"

mkdir -p "$output_dir"

echo "Reading data from: $input_file"

tail -n +2 "$input" | while IFS=, read -r country category details
do
    if [[ $country == "United States" ]]; then
       category_clean=$(echo "$category" | tr -d '[:space:]')
       echo "$country,$category,$details" >> "$output_dir/${category_clean}.txt"
    fi
done 


# in ws5.txt

echo "Music entries:" > ws5.txt
wc -l "${output_dir}/Music.txt" >> ws5.txt

echo "Entertainment entries:" >> ws5.txt
wc -l "${output_dir}/Entertainment.txt" >> ws5.txt

echo "Gaming entries:" >> ws5.txt
wc -l "${output_dir}/Gaming.txt" >> ws5.txt

echo "Comedy entries:" >> ws5.txt
wc -l "${output_dir}/Comedy.txt" >> ws5.txt
