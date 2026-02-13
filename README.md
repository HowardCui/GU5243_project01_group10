# GU5243 Project01
### Collaborators：Haowen Cui(@HowardCui), Yuhan Guo(@FlamyFlame)
## Project Introduction
(project intro ....)

## Data Acquisition
This dataset is accessed through the Socrata Open Data API (SODA2). Since this API can return at most 50,000 records per request, we use $limit and $offset to implement the query. To obtain the complete dataset, we used a while loop and set appropriate delays to request data iteratively.

To improve development efficiency, I added a sample loading mode that allows us to load a partial dataset during testing. Additionally, I designed code that saves data locally to avoid repeated API calls while maintaining full reproducibility.

(...)
## Data Pre-preprocessing 
(...)
## Conclusion

---
