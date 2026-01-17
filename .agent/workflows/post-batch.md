---
description: Post-batch completion checklist for LeetCode solution enhancement
---
# Post-Batch Completion Workflow

After completing each batch of solution file enhancements, execute these steps in order:

## 1. Update Progress Files
// turbo
```powershell
# Count processed files
(Get-ChildItem -Path solutions\*.py -Recurse | Select-String -Pattern "# Pattern:").Length
```
- Update count in `patterns/PROGRESS.md`
- Update count in root `README.md` (Progress section)

## 2. Update Root README.md
- Update the **Progress** counter (e.g., "123 / 3056 files ✅")
- If new patterns discovered, add to **Pattern Index** table
- Update **Quick Reference** if new templates are added

## 3. Update Pattern Index
- Add any new patterns to the Pattern Index table in `README.md`
- Ensure all patterns have links to their guide files

## 4. Update Pattern Guide Files
For each pattern used in the batch:
- If pattern guide **doesn't exist**: Create new file in `patterns/[pattern-name].md`
- If pattern guide **exists**: Add new problems to the Problems table

Pattern guide template:
```markdown
# [Pattern Name] Pattern

## Core Concept
[Brief explanation]

## Template
[Code template]

## Problems
| Problem | Difficulty | Key Insight |
|---------|------------|-------------|
| [problem-name](../solutions/problem.py) | Easy/Medium/Hard | Insight ✅ |
```

## 5. Update patterns/README.md
- Ensure all pattern guides are listed
- Update any statistics or summaries

## 6. Git Workflow
// turbo-all
```powershell
git add .
```
```powershell
git commit -m "Add structured comments to [X] files (batch N): [patterns covered]. Total: [total] files"
```
```powershell
git push origin main
```

---

## Batch Summary Template

After each batch, record:
- **Batch number**: N
- **Files processed**: X  
- **New total**: Y / 3056
- **Patterns used**: [list]
- **New pattern guides created**: [if any]
- **Pattern guides updated**: [list]
