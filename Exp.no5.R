# ✅ STEP 1: Import Libraries
library(dplyr)
library(ggplot2)

# ✅ STEP 2: Create a Sample Dataset
dataset <- data.frame(
  Name = c("Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Alice"),
  Age = c(25, 30, 35, 40, NA, 30, 29, 25),
  Salary = c(50000, 60000, 55000, 70000, 62000, NA, 52000, 50000),
  Department = c("HR", "Finance", "IT", "HR", "Finance", "IT", NA, "HR"),
  stringsAsFactors = FALSE
)

# ✅ STEP 3: Explore Dataset
cat("Original Dataset:\n")
print(dataset)

cat("\nDataset Structure:\n")
str(dataset)

cat("\nSummary Statistics:\n")
summary(dataset)

# ✅ STEP 4: Data Cleaning
# Remove rows with missing values
clean_data <- na.omit(dataset)

# Remove duplicate rows
clean_data <- distinct(clean_data)

cat("\nCleaned Dataset:\n")
print(clean_data)

# ✅ STEP 5: Variable Filtering
filtered_columns <- clean_data %>% select(Name, Age, Salary)
cat("\nFiltered Columns (Name, Age, Salary):\n")
print(filtered_columns)

# ✅ STEP 6: Row Filtering
filtered_rows <- filtered_columns %>% filter(Age > 30)
cat("\nFiltered Rows (Age > 30):\n")
print(filtered_rows)

# ✅ STEP 7: Data Visualization (Age vs Salary)
ggplot(clean_data, aes(x = Age, y = Salary)) +
  geom_point(color = "blue", size = 3) +
  ggtitle("Age vs. Salary") +
  theme_minimal() +
  xlab("Age") +
  ylab("Salary")

