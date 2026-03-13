## March 08  2026  
### Work done:
- Reviewed data cleaning pipeline
- Identified steps: load -> explore-> clean -> save

### Concepts:
- Missing values handling
- Duplicate detection

### Next Step:
- Rebuild cleaning function independently 

## March 09 2026

### Session Goal:
Review the data cleaning pipeline and understand dataset structure.

### Work Done:
- Reviewed dataset structure (rows vs columns)
- Studied dataset inspection commands
- Understood missing value handling using fillna()
- Reviewed duplicate detection
- Defined final scope of Project 1
- Planned basic EDA and visualization layer

### Key Learning:
Better understanding of NaN values and how pandas handles missing data.

### Next Step:
Add visual insights and finalize the project notebook structure.


## March 10 2026
Session Goal: Data cleaning Experiment

### Objective:
- Experimnet with different starategies for missing value handling.

### Work Done:
Tested two approach for missing value handling:
1. Replacing missing values using:
 ```
 df[col] = df[col].fillna("Not Available)
 ```

 2. Remove rows containing missing values using
 ```
df.dropna()
 ```

 ### Observation:
 - fillna() keeps all rows in the dataset while replacing missing values with a placeholder.

 - dropna() removes rows containing missing values, which reduces dataset size.

 ### Insight:  
 For this dataset, replacing missing values is often preferable because removing rows may lead to loss of useful data.

 ### Next Step:  
 Continue exploring the cleaning pipeline and inspect how other columns behave after cleaning.

## March 11 2026
### Session Goal:
 Review cleaning pipeline and start the EDA phase.

- Verified cleaned dataset integrity.
- Generated distribution analysis using value_counts().
- Created visualization for:  
   1. Content type distribution
   2. Release Year trend
   3. Country distribution.

- Improved chart readability with lael rotation and layout
 adjustments.
 - Saved charts to output directory.

 ### Key Insight  
 - Netflix content catlog is dominated by movies and heavily concentrated in recent years, with the United States as primary production country.

 ### Next Step:  
 - Generate rating and duration distribution visualization.


## March 12 2026
### Goal
Complete the remaining EDA work.

### Work done
- Generated rating distribution visualization.
- Generated duration distribution visualization.
- Completed the EDA visualization section for the dataset.

### Outcome
Exploratory Data Analysis(EDA) for the Netflix dataset is completed.

## March 13 2026
### Goal
Complete Project documentation and finalize the project.

### Work done
- Structured and wrote the project README.
- Added dataset description and project workflow.
- Embedded visual chart into README.
- Created engineering note.
- Finalized repository structure and documentation.

### Outcome
- Readme is complete.
- Project Documentation is finalized.

### Next Step
- Improve  README
- Add Engineering Note
- Finish project documentation.