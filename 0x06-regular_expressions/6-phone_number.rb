#!/usr/bin/env ruby

# Ensure there is exactly one argument provided
if ARGV.length != 1
  puts "Usage: #{$PROGRAM_NAME} <string>"
  exit 1
end

# Get the argument passed to the script
input_string = ARGV[0]

# Define the regular expression pattern to match a 10-digit phone number
pattern = /^\d{10}$/

# Perform the regular expression matching using Oniguruma library
result = Oniguruma::ORegexp.new(pattern).match(input_string)

# Output the matched part of the input string or an empty string if no match found
puts result ? result[0] : ''
