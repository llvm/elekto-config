---
name: Reid Kleckner
ID: rnk
info:
  - github: rnk
  - name: Reid Kleckner
---
I think having fast, high-quality build and test signals is one of the most important ingredients in building and evolving any software project, in particular, critical systems software like LLVM. I also think high quality infrastructure is essential for preventing maintainer burnout and enabling smooth contributions. A colleague explained it to me this way: Reviewing code and mentally proving it to be correct takes a huge amount of work, and then it gets committed, and we find problems, so we revert it, and we iterate and go back and forth. If we had community accessible, high-quality integration testing, contributors would be able to find and debug those problems themselves with lower latency, and maintainers could spend more time thinking about deeper design considerations. We have existing systems like llvm-test-suite, but I believe we can do more, and I hope the infra area team, whether I'm formally a lead or not, will prioritize improvements in integration testing next year.

I personally tend to assume the best of everyone and am always trying to work together and get along with people, but I have also learned that, no matter what decision we make in a project as large as ours, there will always be dissent. The important thing is understand everyone's needs and values, to not get stuck, to try to reach the best compromise for the project, and to iterate and adjust because running an open source project is an infinite game with no clear end.

I often cite Nikita's llvm-compile-time-tracker.com as an example of leading through infrastructure and metrics, and I think about what other kinds of metrics infrastructure projects we could do to guide the project to improve over time. I'm interested in the [Community Health Analytics in Open Source Software (CHAOSS) project[(https://chaoss.community/), and while it requires some care, I'm interested in this kind of project contribution analytics infrastructure.
