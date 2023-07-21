#!/usr/bin/env ruby

N = 100_000_000
start_time = Time.now

i, j = 0, 0

j += i while (i += 1) < N
puts(i, "Time required #{Time.now - start_time}s.")
