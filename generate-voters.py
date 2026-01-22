#!/usr/bin/env python3

import subprocess
import json
import sys

def QueryGroup(group):
  ghCommand = ['gh', 'api', '-H', 'Accept: application/vnd.github+json',
              '-H', 'X-GitHub-Api-Version: 2022-11-28', '--paginate',
              '/orgs/llvm/teams/%s/members' % group]
  status = subprocess.check_output(ghCommand)
  committers = json.loads(status)
  return committers

def QueryCommitters():
  return QueryGroup('llvm-committers')

def QueryTriagers():
  return QueryGroup('llvm-triagers')

def main():
  committers = [committer['login'] for committer in QueryCommitters()]
  committers.extend([committer['login'] for committer in QueryTriagers() if committer not in committers])
  print('%d committers identified' % len(committers))
  if len(sys.argv) > 1:
    with open(sys.argv[1], 'w') as file:
      file.write('eligible_voters:\n')
      for committer in committers:
        file.write('  - %s\n' % committer)

if __name__ == '__main__':
  main()
