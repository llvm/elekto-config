#!/usr/bin/env python3

import subprocess
import json
import sys

def QueryCommitters():
  ghCommand = ['gh', 'api', '-H', 'Accept: application/vnd.github+json',
              '-H', 'X-GitHub-Api-Version: 2022-11-28', '--paginate',
              '/orgs/llvm/teams/llvm-committers/members']
  status = subprocess.check_output(ghCommand)
  committers = json.loads(status)
  return committers

def main():
  committers = [committer['login'] for committer in QueryCommitters()]
  print('%d committers identified' % len(committers))
  if len(sys.argv) > 1:
    with open(sys.argv[1], 'w') as file:
      file.write('eligible_voters:\n')
      for committer in committers:
        file.write('  - %s\n' % committer)
      if 'asl' not in committers:
        file.write('  - asl\n')

if __name__ == '__main__':
  main()
