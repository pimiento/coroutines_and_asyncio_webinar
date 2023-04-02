#!/usr/bin/env python3
import time
def grep(pattern, lines):
    pattern = pattern.lower()
    for line in lines:
        if pattern in line.lower():
            yield line
with open(
  "/usr/share/doc/python3.10/copyright"
) as fd:
  print(
    '\n'.join(grep(
        "http",
        grep("python", fd.readlines())
      )
    )
  )
