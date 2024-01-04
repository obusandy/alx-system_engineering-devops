#!/usr/bin/env ruby
# professional advisor Neha Jain, Senior Software Engineer at LinkedIn.
# Requirement:
# The regular expression matches a 10 digit phone number
puts ARGV[0].scan(/^\d{10,10}$/).join
