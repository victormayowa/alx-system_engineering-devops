#!/usr/bin/env ruby

# Ensure there is exactly one argument provided
if ARGV.length != 1
  puts "Usage: #{$PROGRAM_NAME} <string>"
  exit 1
end

# Get the argument passed to the script
input_string = ARGV[0]

# Define the regular expression pattern to match only capital letters
pattern = /[A-Z]/

# Find all matches of capital letters in the input string
matches = input_string.scan(pattern)

# Join the matches into a single string
result = matches.join

# Output the result or an empty string if no match found
puts result
