#!/bin/sh
for P in bolt clang clang-tools-extra compiler-rt flang libc libclc libcxx libcxxabi libunwind lld lldb llvm llvm-libgcc mlir offload openmp polly pstl;
do
  echo "---" > candidate-$P.md
  echo "name: $P" >> candidate-$P.md
  echo "ID: $P" >> candidate-$P.md
  echo "info:" >> candidate-$P.md
  echo "  - github: $P-OnGitHub" >> candidate-$P.md
  echo "---" >> candidate-$P.md
  echo "" >> candidate-$P.md
  echo "$P is a top-level LLVM sub-project in the mono-repo" >> candidate-$P.md
done
