# Patch Grammar

```
{OPERATION}:{START-LINE},{NUMBER-OF-LINES},{END-LINE}${CODE1}<#>{CODE2}
```

## Terms

- BL: Buggy Line 
> This is the buggy line specified in fault_localization_rslt.

- TL: Target Line 
> This is the target line where patch is applied.


## Examples

1. Insert CODE before TL, which is 3 lines before BL.

```
insert-before:-3$CODE
```

2. Insert CODE after TL, which is 3 lines before BL.

```
insert-after:-3$CODE
```

3. Insert CODE after TL, which is BL in this case.

```
insert-after:0$CODE
```

4. Insert CODE before TL, which is 2 lines after BL.

```
insert-before:2$CODE
```

5. Insert CODE1 before TL1 (2 lines before BL) and CODE2 after TL2 (5 lines after BL).

```
insert-before-after:-2,5$CODE1<#>CODE2
```

6. Starting from TL, which is 2 lines before BL, delete 3 lines (including TL).

```
delete:-2,3
```

7. Starting from TL, which is BL in this case, delete 2 lines (including TL).

```
delete:0,2
```

8. Starting from TL, which is 2 lines before BL, replace the next 5 lines (including TL) with CODE.

```
replace:-2,5$CODE
```

9. Starting from TL, which is BL in this case, replace the line with CODE.

```
replace:0,1$CODE
```

10. Starting from TL, which is 1 line before BL, wrap the next 5 lines (including TL) with CODE (e.g., if (x == 0) { ).

```
wrap:-1,5$CODE
```

11. Starting from TL, which is 1 line before BL, move the next 3 lines (including TL) before ML, a line that is 20 lines after BL.

```
move-before:-1,3,20
```

12. Starting from TL, which is 1 line before BL, move the next 3 lines (including TL) after ML, a line that is 15 lines before BL.

```
move-after:-1,3,-15
```

## Simplified Grammar and its Equivalent Grammar

1. insert-before$CODE
```
Insert CODE before BL
Equivalent to insert-before:0$CODE
```

2. insert-after$CODE
```
Insert CODE after BL
Equivalent to insert-after:0$CODE
```

3. delete:M
```
Delete BL and its following M-1 lines (M lines in total)
Equivalent to delete:0,M
```

4. delete
```
Delete BL only
Equivalent to delete:0,1
```

5. replace:M$CODE
```
Replace BL and its following M-1 lines (M lines in total) with CODE
Equivalent to replace:0,M$CODE
```

6. replace$CODE
```
Replace BL with CODE
Equivalent to replace:0,1$CODE
```

7. wrap:M$CODE
```
Wrap BL and its following M-1 lines (M lines in total) with CODE
Equivalent to wrap:0,M$CODE
```

8. wrap$CODE
```
Wrap BL with CODE
Equivalent to wrap:0,1$CODE
```
