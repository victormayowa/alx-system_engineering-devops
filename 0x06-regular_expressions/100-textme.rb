#!/usr/bin/env ruby

# Ensure there is exactly one argument provided
if ARGV.length != 1
  puts "Usage: #{$PROGRAM_NAME} <log_file>"
  exit 1
end

# Get the log file path from the script argument
log_file = ARGV[0]

# Read the log file content
log_content = File.read(log_file)

# Define the regular expression patterns for sender, receiver, and flags
sender_pattern = /\[from:(.*?)\]/
receiver_pattern = /\[to:(.*?)\]/
flags_pattern = /\[flags:(.*?)\]/

# Find the sender, receiver, and flags using regular expressions
sender = log_content.match(sender_pattern)&.captures&.first
receiver = log_content.match(receiver_pattern)&.captures&.first
flags = log_content.match(flags_pattern)&.captures&.first

# Output the result in the required format
puts "#{sender},#{receiver},#{flags}"
