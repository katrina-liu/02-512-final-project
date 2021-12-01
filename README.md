# 02-512-final-project
## Project Structure
1. data: store all Hi-C matrices
2. src: store all implemented TAD boundary finding algorithm
3. test: store all implementation of finding testing measuring indices

## Nov. 30 Meeting Update:
### Three phase plan:
1. Hi-C data synthesis: simulate according to the two segmentation statistic model, link: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4147896/ 
    - Input: n (size of Hi-C data), K (number of domains)
    - Output: t (a list of two-element tuples representing boundaries, [(t0, t1),(t1,t2),....], easier for testing if they are uniform), C (2d list representing Hi-C data)
3. TAD boundary finding algorithms: Armatus, HiCSeg(if time allows)
    - Input:  n (size of Hi-C data), C (2d list representing Hi-C data)
    - Output: t (a list of two-element tuples representing boundaries)
5. Testing accuracy: two measuring indices:
    - Input: t1 (a list of two-element tuples representing boundaries), t2 (a list of two-element tuples representing boundaries)
    - Output: res (numerical value of the measuring index)
    1. Variation of information: link: https://almob.biomedcentral.com/articles/10.1186/1748-7188-9-14
    2. Jaccard Index: link: https://en.wikipedia.org/wiki/Jaccard_index 
6. (Optional) Investigate how to run SpectralTAD: both directly use their package and implementation 
### Responsibility:
- Shreya: 1
- Katrina: 2
- Linda: 3.1
- Amy: 3.2
- Leon: 4
### Presentation Slides:
- Topic: Comparing TAD Boundary Finding Algorithms
- Introduction:
  - TAD 
  - Hi-C data
  - Three algorithms: Armatus, HiCSeg, SpetralTAD
- Measurement:
  - Efficiency: Find Big-O bounds in Paper, time our tests.
  - VI and JI
- Further Impact 
