#!/usr/bin/env python3

import csv
import sys
import os
import subprocess
import json

TIMESTAMP = 'Timestamp'
NAME = 'Full Name'
EMAIL = 'Preferred email address'
TEAM_PROMPT = 'Which Area Team would you like to volunteer for?'
GITHUB = 'GitHub handle'
STATEMENT = 'Candidate Statement (Markdown formatting allowed)'

def QueryCommitters():
  ghCommand = ['gh', 'api', '-H', 'Accept: application/vnd.github+json',
              '-H', 'X-GitHub-Api-Version: 2022-11-28', '--paginate',
              '/orgs/llvm/teams/llvm-committers/members']
  status = subprocess.check_output(ghCommand)
  committers = json.loads(status)
  return committers

def main():
  committers = QueryCommitters()
  print('%d committers identified' % len(committers))
  if len(sys.argv) > 1:
    with open(sys.argv[1], 'w') as file:
      file.write('eligible_voters:\n')
      for committer in committers:
        file.write('  - %s\n' % committer['login'])

def main():
  election_dir = sys.argv[1]
  candidates = sys.argv[2]
  committers = [committer['login'] for committer in QueryCommitters()]
  nominees = {'LLVM':[], 'Clang':[], 'MLIR':[], 'Infrastructure':[]}
  with open(candidates, 'r') as file:
    data = csv.DictReader(file)
    for row in data:
      GitHub = row[GITHUB].removeprefix('https://github.com/')
      Status = ''
      if GitHub not in committers:
        Status = ' - **Ineligible**'
      for team in row[TEAM_PROMPT].split(','):
        candidate_md = os.path.join(election_dir, team.strip(), 'candidate-%s.md' % GitHub)
        nominees[team.strip()].append('* %s - %s%s' % (GitHub, row[NAME], Status))
        #if os.path.exists(candidate_md):
        #  continue
        with open(candidate_md, 'w') as candidate_file:
          candidate_file.write('---\n')
          candidate_file.write('name: %s\n' % row[NAME])
          candidate_file.write('ID: %s\n' % GitHub)
          candidate_file.write('info:\n')
          candidate_file.write('  - github: %s\n' % GitHub)
          candidate_file.write('  - name: %s\n' % row[NAME])
          candidate_file.write('---\n')
          candidate_file.write(row[STATEMENT])
          candidate_file.write('\n')
  for team in nominees:
    print('## %s' % team)
    for nominee in nominees[team]:
      print(nominee)

if __name__ == '__main__':
  main()
